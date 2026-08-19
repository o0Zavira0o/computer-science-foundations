#!/usr/bin/env python3
"""Manual scale regression for CSF architecture changes.

Builds a temporary 3,000-node curriculum chain, verifies it without recursion,
then injects a cycle and verifies that the audit rejects it. Nothing is written
to the real repository.
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("csf_tool", REPO / "scripts" / "csf.py")
assert SPEC and SPEC.loader
csf = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(csf)

with tempfile.TemporaryDirectory() as td:
    root = Path(td) / "repo"
    shutil.copytree(REPO, root, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
    old_root = csf.ROOT
    csf.ROOT = root
    try:
        tp = root / "02-Linux-Systems"
        manifest = json.loads((tp / "TRACK.json").read_text())
        manifest["status"] = "active"
        (tp / "TRACK.json").write_text(json.dumps(manifest, indent=2) + "\n")

        cur = json.loads((tp / "CURRICULUM.json").read_text())
        cur["nodes"] = []
        for i in range(1, 3001):
            nid = f"LNX-N-{i:04d}"
            cur["nodes"].append({
                "id": nid,
                "title": f"Synthetic node {i}",
                "level": "L0",
                "status": "planned",
                "prerequisites": [] if i == 1 else [f"LNX-N-{i-1:04d}"],
                "outcomes": [f"Synthetic outcome {i}"],
                "target_concepts": [],
            })
        (tp / "CURRICULUM.json").write_text(json.dumps(cur, indent=2) + "\n")

        t0 = time.perf_counter()
        csf.sync()
        sync_s = time.perf_counter() - t0
        t1 = time.perf_counter()
        audit = csf.audit_repository(check_generated=True)
        audit_s = time.perf_counter() - t1
        if audit.errors:
            raise SystemExit("Scale audit failed:\n" + "\n".join(audit.errors))

        cur["nodes"][0]["prerequisites"] = ["LNX-N-3000"]
        (tp / "CURRICULUM.json").write_text(json.dumps(cur, indent=2) + "\n")
        cycle_audit = csf.audit_repository(check_generated=False)
        if not any("dependency cycle detected" in e for e in cycle_audit.errors):
            raise SystemExit("Cycle regression: audit failed to detect injected cycle")

        print(f"PASS — 3,000-node scale audit: sync={sync_s:.3f}s audit={audit_s:.3f}s; injected cycle detected")
    finally:
        csf.ROOT = old_root
