from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
import io
from contextlib import redirect_stdout
from contextlib import contextmanager
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("csf_tool", REPO / "scripts" / "csf.py")
assert SPEC and SPEC.loader
csf = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(csf)


@contextmanager
def isolated_repo():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "repo"
        shutil.copytree(REPO, root, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
        old = csf.ROOT
        csf.ROOT = root
        try:
            yield root
        finally:
            csf.ROOT = old


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, obj):
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")


class CurriculumToolTests(unittest.TestCase):
    def test_repository_baseline_is_clean(self):
        audit = csf.audit_repository(check_generated=True)
        self.assertEqual(audit.errors, [])
        self.assertEqual(audit.warnings, [])

    def test_fake_empty_coverage_audit_is_rejected(self):
        with isolated_repo() as root:
            tp = root / "02-Linux-Systems"
            cov = load(tp / "COVERAGE.json")
            cov["baseline"] = {"status": "audited", "last_audited": "2026-08-19", "sources": []}
            cov["items"] = []
            dump(tp / "COVERAGE.json", cov)
            cur = load(tp / "CURRICULUM.json")
            cur["audit_status"] = "audited"
            cur["last_coverage_audit"] = "2026-08-19"
            dump(tp / "CURRICULUM.json", cur)
            audit = csf.audit_repository(check_generated=False)
            joined = "\n".join(audit.errors)
            self.assertIn("at least 3 distinct registered sources", joined)
            self.assertIn("audited baseline requires non-empty coverage items", joined)
            self.assertIn("audited curriculum requires at least one curriculum node", joined)

    def test_dependency_cycle_is_rejected_iteratively(self):
        with isolated_repo() as root:
            tp = root / "02-Linux-Systems"
            cur = load(tp / "CURRICULUM.json")
            cur["nodes"] = [
                {"id":"LNX-N-0001","title":"A","level":"L0","status":"planned","prerequisites":["LNX-N-0002"],"outcomes":["a"],"target_concepts":[]},
                {"id":"LNX-N-0002","title":"B","level":"L0","status":"planned","prerequisites":["LNX-N-0001"],"outcomes":["b"],"target_concepts":[]},
            ]
            dump(tp / "CURRICULUM.json", cur)
            audit = csf.audit_repository(check_generated=False)
            self.assertTrue(any("dependency cycle detected" in e for e in audit.errors))

    def test_new_track_is_discovered_without_code_edit(self):
        with isolated_repo():
            before = len(csf.discover_tracks())
            with redirect_stdout(io.StringIO()):
                rc = csf.cmd_new_track("Operating Systems", "operating-systems", "OS", None)
            self.assertEqual(rc, 0)
            audit = csf.audit_repository(check_generated=True)
            self.assertEqual(audit.errors, [])
            self.assertEqual(len(csf.discover_tracks()), before + 1)

    def test_nested_track_is_discovered_and_validated(self):
        with isolated_repo() as root:
            before = len(csf.discover_tracks())
            with redirect_stdout(io.StringIO()):
                rc = csf.cmd_new_track(
                    "History of Science", "history-of-science", "HSCI", None,
                    parent="09-Auxiliary-Studies"
                )
            self.assertEqual(rc, 0)
            hit = csf.track_by_slug(csf.discover_tracks(), "history-of-science")
            self.assertIsNotNone(hit)
            assert hit is not None
            path, _ = hit
            self.assertEqual(path.parent.name, "09-Auxiliary-Studies")
            audit = csf.audit_repository(check_generated=True)
            self.assertEqual(audit.errors, [])
            self.assertEqual(len(csf.discover_tracks()), before + 1)

    def test_invalid_review_queue_target_is_rejected(self):
        with isolated_repo() as root:
            tp = root / "02-Linux-Systems"
            learner = load(tp / "LEARNER_STATE.json")
            learner["review_queue"] = [
                {"target_type":"concept","target_id":"LNX-NOT-REAL-999","due":"2026-08-20","reason":"test"}
            ]
            dump(tp / "LEARNER_STATE.json", learner)
            audit = csf.audit_repository(check_generated=False)
            self.assertTrue(any("unknown concept" in e for e in audit.errors))


    def test_strict_mode_blocks_warnings(self):
        audit = csf.Audit()
        audit.warn("stale")
        with redirect_stdout(io.StringIO()):
            self.assertEqual(csf.print_audit(audit, strict=True), 1)

    def test_concept_depth_cannot_claim_unpublished_coverage(self):
        with isolated_repo() as root:
            tp = root / "02-Linux-Systems"
            concepts = load(tp / "registry/concepts.json")
            concepts["concepts"] = [
                {"id":"LNX-ORI-001","name":"Orientation","aliases":[],"current_depth":"D3"}
            ]
            dump(tp / "registry/concepts.json", concepts)
            audit = csf.audit_repository(check_generated=False)
            self.assertTrue(any("published curriculum implies None" in e for e in audit.errors))

    def test_invalid_track_slug_is_rejected(self):
        with isolated_repo():
            rc = csf.cmd_new_track("Bad Track", "../bad", "BAD", 8)
            self.assertEqual(rc, 2)


if __name__ == "__main__":
    unittest.main()
