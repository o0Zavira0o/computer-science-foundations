#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from collections import Counter, defaultdict, deque
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

LEVELS = {"L0", "L1", "L2", "L3", "L4", "L5", "L6"}
NODE_STATUSES = {"planned", "ready", "drafting", "published", "deprecated"}
LESSON_STATUSES = {"draft", "complete", "needs-review", "deprecated"}
LEARNER_STATES = {"unseen", "read", "practiced", "demonstrated"}
COVERAGE_STATUSES = {"planned", "covered", "gap", "deferred"}
DEPTHS = {"D0", "D1", "D2", "D3", "D4", "D5"}
DEPTH_RANK = {f"D{i}": i for i in range(6)}
TRACK_STATUSES = {"scaffolded", "active", "paused", "needs-audit"}
BASELINE_STATUSES = {"not-audited", "audited", "needs-audit"}
REFERENCE_TYPES = {
    "textbook", "official-documentation", "standard-specification",
    "university-course", "primary-paper", "survey-review",
    "technical-report", "dataset", "other",
}
ARTIFACT_STATUSES = {"draft", "complete", "needs-review", "deprecated"}
TRACK_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TRACK_CODE_RE = re.compile(r"^[A-Z][A-Z0-9]{1,7}$")

REQUIRED_ROOT = [
    "SYSTEM.json",
    "STATE.json",
    "README.md",
    "AI_INSTRUCTIONS.md",
    "AGENTS.md",
    "docs/LEARNING_SYSTEM.md",
    "docs/ARCHITECTURE.md",
    "docs/LEARNING_SCIENCE.md",
    "docs/DECISIONS.md",
]

REQUIRED_TRACK_CANONICAL = [
    "TRACK.json",
    "CURRICULUM.json",
    "COVERAGE.json",
    "LEARNER_STATE.json",
    "registry/concepts.json",
    "registry/examples.json",
    "registry/references.json",
    "research/FRONTIER.json",
]

REQUIRED_TRACK_DIRS = ["lessons", "exercises", "projects", "research", "registry"]

GENERATED_TRACK_VIEWS = [
    "ROADMAP.md",
    "PROGRESS.md",
    "LEARNER.md",
    "CONCEPTS.md",
    "EXAMPLES.md",
    "REFERENCES.md",
    "CATALOG.md",
    "CONTEXT.md",
]

PLACEHOLDER_PATTERNS = [
    "replace me",
    "to be built after curriculum reconnaissance",
    "todo",
]


class Audit:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)



def parse_iso_date(value: Any, label: str, audit: Audit, *, allow_none: bool = True) -> date | None:
    if value is None and allow_none:
        return None
    if not isinstance(value, str):
        audit.error(f"{label}: expected ISO date string YYYY-MM-DD")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        audit.error(f"{label}: invalid ISO date {value!r}")
        return None


def md_cell(value: Any) -> str:
    text = str(value if value is not None else "—")
    return text.replace("\n", " ").replace("|", r"\|").strip() or "—"


def expected_id_prefix(code: str) -> str:
    return f"{code}-"


def load_json(path: Path, audit: Audit | None = None) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        if audit:
            audit.error(f"Missing JSON file: {path.relative_to(ROOT)}")
        return None
    except json.JSONDecodeError as exc:
        if audit:
            audit.error(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None
    if not isinstance(value, dict):
        if audit:
            audit.error(f"{path.relative_to(ROOT)}: top-level JSON must be an object")
        return None
    return value


def schema_pointer(from_file: Path, schema_name: str) -> str:
    target = ROOT / "schemas" / schema_name
    return os.path.relpath(target, start=from_file.parent).replace(os.sep, "/")


def discover_tracks(audit: Audit | None = None) -> list[tuple[Path, dict[str, Any]]]:
    """Discover tracks recursively.

    A directory becomes a track only by containing TRACK.json. This allows
    organizational containers such as 09-Auxiliary-Studies/ without turning
    the container itself into a curriculum track.
    """
    found: list[tuple[Path, dict[str, Any]]] = []
    for manifest in sorted(ROOT.rglob("TRACK.json")):
        try:
            rel = manifest.relative_to(ROOT)
        except ValueError:
            continue
        if any(part.startswith(".") for part in rel.parts):
            continue
        # Never discover tracks inside tooling/cache directories.
        if rel.parts and rel.parts[0] in {"schemas", "templates", "tests", "scripts"}:
            continue
        data = load_json(manifest, audit)
        if data is not None:
            found.append((manifest.parent, data))
    found.sort(key=lambda x: (x[1].get("order", 10**9), x[0].relative_to(ROOT).as_posix()))
    return found


def parse_frontmatter(path: Path, audit: Audit | None = None) -> tuple[dict[str, Any], str] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        if audit:
            audit.error(f"{path.relative_to(ROOT)}: missing front matter")
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        if audit:
            audit.error(f"{path.relative_to(ROOT)}: unterminated front matter")
        return None

    block = text[4:end]
    body = text[end + 5 :]
    data: dict[str, Any] = {}
    for lineno, line in enumerate(block.splitlines(), start=2):
        if not line.strip():
            continue
        if ":" not in line:
            if audit:
                audit.error(
                    f"{path.relative_to(ROOT)}:{lineno}: front-matter fields must be one-line key: value pairs"
                )
            continue
        key, raw = line.split(":", 1)
        key = key.strip()
        raw = raw.strip()
        if not key:
            if audit:
                audit.error(f"{path.relative_to(ROOT)}:{lineno}: empty front-matter key")
            continue

        if raw.startswith("[") or raw.startswith("{"):
            try:
                value = json.loads(raw)
            except json.JSONDecodeError:
                if audit:
                    audit.error(
                        f"{path.relative_to(ROOT)}:{lineno}: list/object front-matter values must be valid inline JSON"
                    )
                value = raw
        elif raw in {"true", "false"}:
            value = raw == "true"
        elif raw in {"null", "~"}:
            value = None
        else:
            value = raw.strip("'\"")
        data[key] = value
    return data, body


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.casefold()).strip()


def fmt_list(items: list[Any]) -> str:
    return ", ".join(md_cell(x) for x in items) if items else "—"


def track_by_slug(tracks: list[tuple[Path, dict[str, Any]]], slug: str) -> tuple[Path, dict[str, Any]] | None:
    for path, manifest in tracks:
        if manifest.get("id") == slug or path.name == slug:
            return path, manifest
    return None


def lesson_records(track_path: Path) -> list[tuple[Path, dict[str, Any], str]]:
    records: list[tuple[Path, dict[str, Any], str]] = []
    for path in sorted((track_path / "lessons").rglob("*.md")):
        parsed = parse_frontmatter(path, None)
        if parsed:
            fm, body = parsed
            records.append((path, fm, body))
    return records


def render_root_state(state: dict[str, Any]) -> str:
    decisions = "\n".join(f"- {x}" for x in state.get("persistent_decisions", [])) or "- None recorded."
    return f"""<!-- GENERATED by scripts/csf.py sync. Edit STATE.json, not this file. -->

# Repository State

- **Schema:** {state.get('schema_version', '—')}
- **Last updated:** {state.get('last_updated') or '—'}
- **Repository phase:** {state.get('repository_phase') or '—'}
- **Active track:** {state.get('active_track') or 'none'}
- **Last completed lesson:** {state.get('last_completed_lesson') or 'none'}
- **Next planned item:** {state.get('next_planned_item') or 'none'}
- **Legacy Linux policy:** {state.get('legacy_linux_policy') or '—'}

## Persistent decisions

{decisions}
"""


def render_tracks(tracks: list[tuple[Path, dict[str, Any]]]) -> str:
    rows = []
    for path, m in tracks:
        rel = path.relative_to(ROOT)
        rel_posix = rel.as_posix()
        if len(rel.parts) > 1:
            group = re.sub(r"^\d+-", "", rel.parts[0]).replace("-", " ")
        else:
            group = "Core"
        rows.append(
            f"| {m.get('order','—')} | {md_cell(m.get('title','—'))} | {md_cell(group)} | `{m.get('id','—')}` | "
            f"{m.get('status','—')} | [`{rel_posix}/README.md`](../{rel_posix}/README.md) |"
        )
    return """<!-- GENERATED by scripts/csf.py sync. Edit TRACK.json manifests, not this file. -->

# Tracks

| # | Track | Group | ID | Status | Entry point |
|---|---|---|---|---|---|
""" + "\n".join(rows) + "\n"


def render_cross_track(tracks: list[tuple[Path, dict[str, Any]]]) -> str:
    slug_to_title = {m["id"]: m.get("title", m["id"]) for _, m in tracks if "id" in m}
    rows: list[str] = []
    for _, m in tracks:
        for n in m.get("neighbor_tracks", []):
            rows.append(f"| {md_cell(m.get('title'))} | {md_cell(slug_to_title.get(n, n))} | declared neighbor |")
    # actual graph edges
    node_owner: dict[str, str] = {}
    curricula: dict[str, dict[str, Any]] = {}
    for path, m in tracks:
        cur = load_json(path / "CURRICULUM.json") or {}
        curricula[m["id"]] = cur
        for node in cur.get("nodes", []):
            if isinstance(node, dict) and isinstance(node.get("id"), str):
                node_owner[node["id"]] = m["id"]
    for owner, cur in curricula.items():
        for node in cur.get("nodes", []):
            if not isinstance(node, dict):
                continue
            for pre in node.get("prerequisites", []):
                other = node_owner.get(pre)
                if other and other != owner:
                    rows.append(
                        f"| {slug_to_title.get(owner, owner)} | {slug_to_title.get(other, other)} | "
                        f"`{node.get('id')}` requires `{pre}` |"
                    )
    unique = list(dict.fromkeys(rows))
    body = "\n".join(unique) if unique else "| — | — | No cross-track relationships registered yet |"
    return """<!-- GENERATED by scripts/csf.py sync. Edit TRACK.json/CURRICULUM.json, not this file. -->

# Cross-Track Index

| Track | Related track | Relationship |
|---|---|---|
""" + body + "\n"


def render_roadmap(track_path: Path, manifest: dict[str, Any]) -> str:
    cur = load_json(track_path / "CURRICULUM.json") or {}
    nodes = [n for n in cur.get("nodes", []) if isinstance(n, dict)]
    lines = [
        "<!-- GENERATED by scripts/csf.py sync. Edit CURRICULUM.json, not this file. -->",
        "",
        f"# {manifest.get('title')} Roadmap",
        "",
        f"- **Audit status:** {cur.get('audit_status', '—')}",
        f"- **Last coverage audit:** {cur.get('last_coverage_audit') or 'not yet performed'}",
        f"- **Nodes:** {len(nodes)}",
        "",
        "This is a human-readable view of the dependency graph. `CURRICULUM.json` is canonical.",
        "",
    ]
    for level in ["L0","L1","L2","L3","L4","L5","L6"]:
        lines += [f"## {level}", ""]
        subset = [n for n in nodes if n.get("level") == level]
        if not subset:
            lines += ["_No nodes registered yet._", ""]
            continue
        lines += [
            "| Node | Title | Status | Prerequisites | Lesson |",
            "|---|---|---|---|---|",
        ]
        for n in subset:
            lines.append(
                f"| `{n.get('id','—')}` | {md_cell(n.get('title','—'))} | {n.get('status','—')} | "
                f"{fmt_list(n.get('prerequisites', []))} | {n.get('lesson_id') or '—'} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_progress(track_path: Path, manifest: dict[str, Any]) -> str:
    cur = load_json(track_path / "CURRICULUM.json") or {}
    nodes = [n for n in cur.get("nodes", []) if isinstance(n, dict)]
    counts = Counter(n.get("status", "unknown") for n in nodes)
    level_counts = Counter(n.get("level", "unknown") for n in nodes if n.get("status") == "published")
    return f"""<!-- GENERATED by scripts/csf.py sync. Curriculum publication state only; learner state is in LEARNER.md. -->

# {manifest.get('title')} Curriculum Progress

- **Track status:** {manifest.get('status', '—')}
- **Curriculum audit:** {cur.get('audit_status', '—')}
- **Total nodes:** {len(nodes)}
- **Planned:** {counts.get('planned',0)}
- **Ready:** {counts.get('ready',0)}
- **Drafting:** {counts.get('drafting',0)}
- **Published:** {counts.get('published',0)}
- **Deprecated:** {counts.get('deprecated',0)}

## Published by level

| Level | Count |
|---|---:|
""" + "\n".join(f"| {level} | {level_counts.get(level,0)} |" for level in ["L0","L1","L2","L3","L4","L5","L6"]) + "\n"


def render_learner(track_path: Path, manifest: dict[str, Any]) -> str:
    st = load_json(track_path / "LEARNER_STATE.json") or {}
    lessons = st.get("lessons", {}) if isinstance(st.get("lessons"), dict) else {}
    counts = Counter()
    for value in lessons.values():
        if isinstance(value, dict):
            counts[value.get("state", "unseen")] += 1
    reviews = st.get("review_queue", [])
    due_count = 0
    if isinstance(reviews, list):
        for item in reviews:
            if isinstance(item, dict) and isinstance(item.get("due"), str):
                try:
                    if date.fromisoformat(item["due"]) <= date.today():
                        due_count += 1
                except ValueError:
                    pass
    return f"""<!-- GENERATED by scripts/csf.py sync. Edit LEARNER_STATE.json, not this file. -->

# {manifest.get('title')} Learner State

- **Profile:** {st.get('profile_id') or '—'}
- **Last updated:** {st.get('last_updated') or 'never'}
- **Read:** {counts.get('read',0)}
- **Practiced:** {counts.get('practiced',0)}
- **Demonstrated:** {counts.get('demonstrated',0)}
- **Review queue:** {len(reviews) if isinstance(reviews,list) else 0}
- **Due now:** {due_count}

A published lesson is not automatically learner knowledge. `LEARNER_STATE.json` is canonical. Keep committed learner metadata non-sensitive because this repository is public.
"""


def render_concepts(track_path: Path, manifest: dict[str, Any]) -> str:
    data = load_json(track_path / "registry/concepts.json") or {}
    concepts = [x for x in data.get("concepts", []) if isinstance(x, dict)]
    lines = [
        "<!-- GENERATED by scripts/csf.py sync. Edit registry/concepts.json, not this file. -->",
        "",
        f"# {manifest.get('title')} Concept Registry",
        "",
        "| Concept ID | Name | Current depth | Aliases |",
        "|---|---|---|---|",
    ]
    if not concepts:
        lines.append("| — | — | — | No concepts registered yet |")
    else:
        for c in concepts:
            lines.append(
                f"| `{c.get('id','—')}` | {md_cell(c.get('name','—'))} | {c.get('current_depth') or '—'} | "
                f"{fmt_list(c.get('aliases', []))} |"
            )
    return "\n".join(lines) + "\n"


def render_examples(track_path: Path, manifest: dict[str, Any]) -> str:
    data = load_json(track_path / "registry/examples.json") or {}
    examples = [x for x in data.get("examples", []) if isinstance(x, dict)]
    lines = [
        "<!-- GENERATED by scripts/csf.py sync. Edit registry/examples.json, not this file. -->",
        "",
        f"# {manifest.get('title')} Example Registry",
        "",
        "| Example ID | Signature | Domain | First lesson | Reuse purpose |",
        "|---|---|---|---|---|",
    ]
    if not examples:
        lines.append("| — | — | — | — | No examples registered yet |")
    else:
        for e in examples:
            lines.append(
                f"| `{e.get('id','—')}` | {md_cell(e.get('signature','—'))} | {md_cell(e.get('domain','—'))} | "
                f"{e.get('first_lesson') or '—'} | {e.get('reuse_purpose') or '—'} |"
            )
    return "\n".join(lines) + "\n"


def render_references(track_path: Path, manifest: dict[str, Any]) -> str:
    data = load_json(track_path / "registry/references.json") or {}
    refs = [x for x in data.get("references", []) if isinstance(x, dict)]
    lines = [
        "<!-- GENERATED by scripts/csf.py sync. Edit registry/references.json, not this file. -->",
        "",
        f"# {manifest.get('title')} Reference Registry",
        "",
        "| Reference ID | Title | Type | Authority | Reviewed | Review after |",
        "|---|---|---|---|---|---|",
    ]
    if not refs:
        lines.append("| — | — | — | — | — | No references registered yet |")
    else:
        for r in refs:
            lines.append(
                f"| `{r.get('id','—')}` | {md_cell(r.get('title','—'))} | {r.get('type','—')} | "
                f"{md_cell(r.get('authority','—'))} | {r.get('reviewed_at') or '—'} | {r.get('review_after') or '—'} |"
            )
    return "\n".join(lines) + "\n"


def render_catalog(track_path: Path, manifest: dict[str, Any]) -> str:
    recs = lesson_records(track_path)
    lines = [
        "<!-- GENERATED by scripts/csf.py sync. Derived from lesson front matter. -->",
        "",
        f"# {manifest.get('title')} Lesson Catalog",
        "",
        "| Lesson | Title | Level | Status | Curriculum node | Last reviewed |",
        "|---|---|---|---|---|---|",
    ]
    if not recs:
        lines.append("| — | — | — | — | — | No lessons published yet |")
    else:
        for path, fm, _ in recs:
            lines.append(
                f"| [`{fm.get('id','—')}`]({path.relative_to(track_path).as_posix()}) | {md_cell(fm.get('title','—'))} | "
                f"{fm.get('level','—')} | {fm.get('status','—')} | `{fm.get('curriculum_node','—')}` | "
                f"{fm.get('last_reviewed','—')} |"
            )
    return "\n".join(lines) + "\n"


def ready_nodes(track_path: Path, all_node_status: dict[str, str]) -> list[dict[str, Any]]:
    cur = load_json(track_path / "CURRICULUM.json") or {}
    nodes = [n for n in cur.get("nodes", []) if isinstance(n, dict)]
    candidates: list[dict[str, Any]] = []
    for n in nodes:
        if n.get("status") not in {"planned", "ready"}:
            continue
        prerequisites = n.get("prerequisites", [])
        if isinstance(prerequisites, list) and all(all_node_status.get(p) == "published" for p in prerequisites):
            candidates.append(n)
    return candidates


def build_global_node_to_lesson(tracks: list[tuple[Path, dict[str, Any]]]) -> dict[str, str]:
    out: dict[str, str] = {}
    for path, _ in tracks:
        cur = load_json(path / "CURRICULUM.json") or {}
        for n in cur.get("nodes", []):
            if isinstance(n, dict) and isinstance(n.get("id"), str) and isinstance(n.get("lesson_id"), str):
                out[n["id"]] = n["lesson_id"]
    return out


def build_global_learner_lesson_state(tracks: list[tuple[Path, dict[str, Any]]]) -> dict[str, str]:
    out: dict[str, str] = {}
    for path, _ in tracks:
        learner = load_json(path / "LEARNER_STATE.json") or {}
        lessons = learner.get("lessons", {}) if isinstance(learner.get("lessons"), dict) else {}
        for lid, st in lessons.items():
            if isinstance(st, dict) and isinstance(st.get("state"), str):
                out[lid] = st["state"]
    return out


def study_candidates(track_path: Path, tracks: list[tuple[Path, dict[str, Any]]]) -> tuple[list[str], list[str], list[str]]:
    learner = load_json(track_path / "LEARNER_STATE.json") or {}
    local_states = learner.get("lessons", {}) if isinstance(learner.get("lessons"), dict) else {}
    node_to_lesson = build_global_node_to_lesson(tracks)
    global_states = build_global_learner_lesson_state(tracks)
    due_reviews: list[str] = []
    for item in learner.get("review_queue", []) if isinstance(learner.get("review_queue"), list) else []:
        if not isinstance(item, dict):
            continue
        due = item.get("due")
        try:
            if isinstance(due, str) and date.fromisoformat(due) <= date.today():
                due_reviews.append(f"{item.get('target_type')}:{item.get('target_id')} — {item.get('reason','review due')}")
        except ValueError:
            pass
    practice: list[str] = []
    for lid, st in local_states.items():
        if isinstance(st, dict) and st.get("state") == "read":
            practice.append(lid)
    new_lessons: list[str] = []
    cur = load_json(track_path / "CURRICULUM.json") or {}
    for node in cur.get("nodes", []) if isinstance(cur.get("nodes"), list) else []:
        if not isinstance(node, dict) or node.get("status") != "published":
            continue
        lid = node.get("lesson_id")
        if not isinstance(lid, str):
            continue
        local = local_states.get(lid, {})
        if isinstance(local, dict) and local.get("state") in {"read", "practiced", "demonstrated"}:
            continue
        prereq_ok = True
        for pre in node.get("prerequisites", []) if isinstance(node.get("prerequisites"), list) else []:
            pre_lesson = node_to_lesson.get(pre)
            if pre_lesson and global_states.get(pre_lesson) not in {"practiced", "demonstrated"}:
                prereq_ok = False
                break
        if prereq_ok:
            new_lessons.append(f"{lid} — {node.get('title')} [{node.get('level')}]")
    return due_reviews, practice, new_lessons


def build_global_node_status(tracks: list[tuple[Path, dict[str, Any]]]) -> dict[str, str]:
    out: dict[str, str] = {}
    for path, _ in tracks:
        cur = load_json(path / "CURRICULUM.json") or {}
        for n in cur.get("nodes", []):
            if isinstance(n, dict) and isinstance(n.get("id"), str):
                out[n["id"]] = n.get("status", "unknown")
    return out


def render_context(track_path: Path, manifest: dict[str, Any], tracks: list[tuple[Path, dict[str, Any]]]) -> str:
    cur = load_json(track_path / "CURRICULUM.json") or {}
    cov = load_json(track_path / "COVERAGE.json") or {}
    learner = load_json(track_path / "LEARNER_STATE.json") or {}
    concepts = load_json(track_path / "registry/concepts.json") or {}
    examples = load_json(track_path / "registry/examples.json") or {}
    refs = load_json(track_path / "registry/references.json") or {}
    all_status = build_global_node_status(tracks)
    baseline = cov.get("baseline", {}) if isinstance(cov.get("baseline"), dict) else {}
    authoring_unlocked = cur.get("audit_status") == "audited" and baseline.get("status") == "audited"
    ready = ready_nodes(track_path, all_status) if authoring_unlocked else []
    if not authoring_unlocked:
        ready_lines = "- BLOCKED — curriculum/coverage reconnaissance is not audited yet."
    else:
        ready_lines = "\n".join(
            f"- `{n.get('id')}` — {n.get('title')} ({n.get('level')}, {n.get('status')})"
            for n in ready[:20]
        ) or "- None. Resolve prerequisites or extend the audited curriculum."
    due_reviews, practice_candidates, study_new = study_candidates(track_path, tracks)
    study_lines = []
    if due_reviews:
        study_lines.append("**Due review**")
        study_lines.extend(f"- {x}" for x in due_reviews[:10])
    if practice_candidates:
        study_lines.append("**Practice before advancing**")
        study_lines.extend(f"- `{x}`" for x in practice_candidates[:10])
    if study_new:
        study_lines.append("**New lessons with practiced/demonstrated prerequisites**")
        study_lines.extend(f"- {x}" for x in study_new[:10])
    if not study_lines:
        study_lines = ["- None yet."]
    study_text = "\n".join(study_lines)
    lessons = lesson_records(track_path)
    recent = lessons[-8:]
    recent_lines = "\n".join(
        f"- `{fm.get('id')}` — {fm.get('title')} ({fm.get('level')}, {fm.get('status')})"
        for _, fm, _ in recent
    ) or "- None."
    return f"""<!-- GENERATED by scripts/csf.py sync. Fast handoff view; canonical JSON remains authoritative. -->

# {manifest.get('title')} — AI Context

## Identity

- **Track:** {manifest.get('title')}
- **ID:** `{manifest.get('id')}`
- **Code:** `{manifest.get('code')}`
- **Track status:** {manifest.get('status')}
- **Entry model:** {manifest.get('entry_model')}
- **Focus:** {manifest.get('scope',{}).get('focus','—') if isinstance(manifest.get('scope'),dict) else '—'}

## Curriculum state

- **Audit status:** {cur.get('audit_status','—')}
- **Nodes:** {len(cur.get('nodes',[])) if isinstance(cur.get('nodes'),list) else 0}
- **Coverage baseline:** {baseline.get('status','—')}
- **Coverage items:** {len(cov.get('items',[])) if isinstance(cov.get('items'),list) else 0}
- **Published lessons:** {len([1 for _,fm,_ in lessons if fm.get('status') == 'complete'])}

## Registry sizes

- **Concepts:** {len(concepts.get('concepts',[])) if isinstance(concepts.get('concepts'),list) else 0}
- **Examples:** {len(examples.get('examples',[])) if isinstance(examples.get('examples'),list) else 0}
- **References:** {len(refs.get('references',[])) if isinstance(refs.get('references'),list) else 0}

## Learner state

- **Tracked lessons:** {len(learner.get('lessons',{})) if isinstance(learner.get('lessons'),dict) else 0}
- **Review queue:** {len(learner.get('review_queue',[])) if isinstance(learner.get('review_queue'),list) else 0}
- **Last updated:** {learner.get('last_updated') or 'never'}

## Authoring candidates

{ready_lines}

## Learner next actions

{study_text}

## Recent lessons

{recent_lines}

## Normal-session retrieval rule

Do not recursively reread the whole track. Inspect the canonical JSON above, then open only the direct prerequisite/recent/cross-track lessons and any lessons found by relevant concept/example/reference IDs.

For full coverage or semantic-duplication audits, explicitly switch to audit mode.
"""


def generated_track_views(track_path: Path, manifest: dict[str, Any], tracks: list[tuple[Path, dict[str, Any]]]) -> dict[str, str]:
    return {
        "ROADMAP.md": render_roadmap(track_path, manifest),
        "PROGRESS.md": render_progress(track_path, manifest),
        "LEARNER.md": render_learner(track_path, manifest),
        "CONCEPTS.md": render_concepts(track_path, manifest),
        "EXAMPLES.md": render_examples(track_path, manifest),
        "REFERENCES.md": render_references(track_path, manifest),
        "CATALOG.md": render_catalog(track_path, manifest),
        "CONTEXT.md": render_context(track_path, manifest, tracks),
    }


def sync(slug: str | None = None) -> None:
    tracks = discover_tracks()
    state = load_json(ROOT / "STATE.json") or {}
    (ROOT / "STATE.md").write_text(render_root_state(state), encoding="utf-8")
    (ROOT / "docs/TRACKS.md").write_text(render_tracks(tracks), encoding="utf-8")
    (ROOT / "docs/CROSS_TRACK_INDEX.md").write_text(render_cross_track(tracks), encoding="utf-8")

    for path, manifest in tracks:
        if slug and manifest.get("id") != slug and path.name != slug:
            continue
        for name, content in generated_track_views(path, manifest, tracks).items():
            (path / name).write_text(content, encoding="utf-8")


def audit_repository(check_generated: bool = True) -> Audit:
    a = Audit()
    today = date.today()

    for rel in REQUIRED_ROOT:
        if not (ROOT / rel).is_file():
            a.error(f"Missing required root file: {rel}")

    system = load_json(ROOT / "SYSTEM.json", a)
    state = load_json(ROOT / "STATE.json", a)
    if system is not None:
        if system.get("$schema") != "schemas/system.schema.json":
            a.error("SYSTEM.json: $schema must be 'schemas/system.schema.json'")
        if system.get("schema_version") != 1:
            a.error("SYSTEM.json: unsupported schema_version")
        if system.get("system_version") != "3.1":
            a.warn(f"SYSTEM.json: expected system_version 3.1, found {system.get('system_version')!r}")
    if state is not None:
        if state.get("$schema") != "schemas/state.schema.json":
            a.error("STATE.json: $schema must be 'schemas/state.schema.json'")
        if state.get("schema_version") != 2:
            a.error("STATE.json: unsupported schema_version")
        parse_iso_date(state.get("last_updated"), "STATE.json last_updated", a, allow_none=False)

    tracks = discover_tracks(a)
    if not tracks:
        a.error("No TRACK.json manifests discovered")
        return a

    slugs: dict[str, Path] = {}
    codes: dict[str, Path] = {}
    orders: dict[int, Path] = {}
    manifests: dict[str, dict[str, Any]] = {}

    for tp, m in tracks:
        rel = tp.relative_to(ROOT)
        for key in ("schema_version", "id", "code", "title", "folder", "order", "status", "entry_model", "scope", "entry_prerequisites", "neighbor_tracks"):
            if key not in m:
                a.error(f"{rel}/TRACK.json: missing key {key!r}")
        expected_track_schema = schema_pointer(tp / "TRACK.json", "track.schema.json")
        if m.get("$schema") != expected_track_schema:
            a.error(f"{rel}/TRACK.json: invalid $schema pointer; expected {expected_track_schema!r}")
        if m.get("schema_version") != 1:
            a.error(f"{rel}/TRACK.json: unsupported schema_version")
        slug = m.get("id")
        code = m.get("code")
        order = m.get("order")
        if isinstance(slug, str) and not TRACK_ID_RE.fullmatch(slug):
            a.error(f"{rel}/TRACK.json: invalid id format {slug!r}; use lowercase kebab-case")
        if isinstance(code, str) and not TRACK_CODE_RE.fullmatch(code):
            a.error(f"{rel}/TRACK.json: invalid code format {code!r}")
        if m.get("status") not in TRACK_STATUSES:
            a.error(f"{rel}/TRACK.json: invalid status {m.get('status')!r}")
        scope = m.get("scope")
        if not isinstance(scope, dict):
            a.error(f"{rel}/TRACK.json: scope must be object")
        else:
            if not isinstance(scope.get("focus"), str):
                a.error(f"{rel}/TRACK.json: scope.focus must be string")
            for field in ("includes", "delegates"):
                if not isinstance(scope.get(field), list):
                    a.error(f"{rel}/TRACK.json: scope.{field} must be array")
        if not isinstance(m.get("entry_prerequisites"), list):
            a.error(f"{rel}/TRACK.json: entry_prerequisites must be array")
        if not isinstance(m.get("neighbor_tracks"), list):
            a.error(f"{rel}/TRACK.json: neighbor_tracks must be array")
        if not isinstance(slug, str) or not slug:
            a.error(f"{rel}/TRACK.json: id must be non-empty string")
            continue
        manifests[slug] = m
        if slug in slugs:
            a.error(f"Duplicate track id {slug}: {slugs[slug]} and {rel}")
        slugs[slug] = rel
        if isinstance(code, str):
            if code in codes:
                a.error(f"Duplicate track code {code}: {codes[code]} and {rel}")
            codes[code] = rel
        else:
            a.error(f"{rel}/TRACK.json: code must be string")
        if isinstance(order, int):
            if order in orders:
                a.error(f"Duplicate track order {order}: {orders[order]} and {rel}")
            orders[order] = rel
        else:
            a.error(f"{rel}/TRACK.json: order must be integer")
        if m.get("folder") != tp.name:
            a.error(f"{rel}/TRACK.json: folder must equal actual folder name {tp.name!r}")
        if m.get("entry_model") != "zero-subject-specific-knowledge":
            a.warn(f"{rel}/TRACK.json: unusual entry_model {m.get('entry_model')!r}")
        for neighbor in m.get("neighbor_tracks", []) if isinstance(m.get("neighbor_tracks"), list) else []:
            if neighbor == slug:
                a.error(f"{rel}/TRACK.json: track cannot be its own neighbor")

        for req in REQUIRED_TRACK_CANONICAL:
            if not (tp / req).is_file():
                a.error(f"{rel}: missing canonical file {req}")
        for req in REQUIRED_TRACK_DIRS:
            if not (tp / req).is_dir():
                a.error(f"{rel}: missing directory {req}/")

    # Validate neighbors after all slugs known.
    for tp, m in tracks:
        for neighbor in m.get("neighbor_tracks", []) if isinstance(m.get("neighbor_tracks"), list) else []:
            if neighbor not in slugs:
                a.error(f"{tp.name}/TRACK.json: unknown neighbor track {neighbor!r}")

    # Canonical registries and curricula.
    global_nodes: dict[str, tuple[str, dict[str, Any]]] = {}
    global_concepts: dict[str, tuple[str, dict[str, Any]]] = {}
    global_examples: dict[str, tuple[str, dict[str, Any]]] = {}
    global_refs: dict[str, tuple[str, dict[str, Any]]] = {}
    curricula: dict[str, dict[str, Any]] = {}
    coverages: dict[str, dict[str, Any]] = {}
    learners: dict[str, dict[str, Any]] = {}

    for tp, m in tracks:
        slug = m["id"]
        rel = tp.relative_to(ROOT)

        cur = load_json(tp / "CURRICULUM.json", a) or {}
        cov = load_json(tp / "COVERAGE.json", a) or {}
        lea = load_json(tp / "LEARNER_STATE.json", a) or {}
        con = load_json(tp / "registry/concepts.json", a) or {}
        exa = load_json(tp / "registry/examples.json", a) or {}
        ref = load_json(tp / "registry/references.json", a) or {}
        frontier = load_json(tp / "research/FRONTIER.json", a) or {}

        curricula[slug] = cur
        coverages[slug] = cov
        learners[slug] = lea

        schema_ptrs = {
            "CURRICULUM.json": schema_pointer(tp / "CURRICULUM.json", "curriculum.schema.json"),
            "COVERAGE.json": schema_pointer(tp / "COVERAGE.json", "coverage.schema.json"),
            "LEARNER_STATE.json": schema_pointer(tp / "LEARNER_STATE.json", "learner-state.schema.json"),
            "registry/concepts.json": schema_pointer(tp / "registry/concepts.json", "concept-registry.schema.json"),
            "registry/examples.json": schema_pointer(tp / "registry/examples.json", "example-registry.schema.json"),
            "registry/references.json": schema_pointer(tp / "registry/references.json", "reference-registry.schema.json"),
        }
        for obj, name in [(cur,"CURRICULUM.json"),(cov,"COVERAGE.json"),(lea,"LEARNER_STATE.json"),(con,"registry/concepts.json"),(exa,"registry/examples.json"),(ref,"registry/references.json")]:
            if obj and obj.get("$schema") != schema_ptrs[name]:
                a.error(f"{rel}/{name}: invalid $schema pointer")
            if obj and obj.get("schema_version") != 1:
                a.error(f"{rel}/{name}: unsupported schema_version")
            if obj and obj.get("track") != slug:
                a.error(f"{rel}/{name}: track must equal {slug!r}")

        if cur.get("audit_status") not in {"not-audited","audited","needs-audit"}:
            a.error(f"{rel}/CURRICULUM.json: invalid audit_status {cur.get('audit_status')!r}")

        nodes = cur.get("nodes", [])
        if not isinstance(nodes, list):
            a.error(f"{rel}/CURRICULUM.json: nodes must be array")
            nodes = []
        for n in nodes:
            if not isinstance(n, dict):
                a.error(f"{rel}/CURRICULUM.json: every node must be object")
                continue
            for key in ("id","title","level","status","prerequisites","outcomes","target_concepts"):
                if key not in n:
                    a.error(f"{rel}/CURRICULUM.json: node missing {key!r}: {n}")
            nid = n.get("id")
            if not isinstance(nid, str) or not nid:
                a.error(f"{rel}/CURRICULUM.json: node id must be non-empty string")
                continue
            if not re.fullmatch(rf"{re.escape(m['code'])}-N-[0-9]{{4,}}", nid):
                a.error(f"{rel}/CURRICULUM.json: invalid node ID {nid!r}; expected {m['code']}-N-NNNN")
            if not isinstance(n.get("title"), str) or not n.get("title", "").strip():
                a.error(f"{rel}/CURRICULUM.json: {nid} title must be non-empty string")
            if nid in global_nodes:
                a.error(f"Duplicate curriculum node ID {nid}")
            global_nodes[nid] = (slug, n)
            if n.get("level") not in LEVELS:
                a.error(f"{rel}/CURRICULUM.json: {nid} invalid level {n.get('level')!r}")
            if n.get("status") not in NODE_STATUSES:
                a.error(f"{rel}/CURRICULUM.json: {nid} invalid status {n.get('status')!r}")
            if not isinstance(n.get("prerequisites"), list):
                a.error(f"{rel}/CURRICULUM.json: {nid} prerequisites must be array")
            elif any(not isinstance(x, str) for x in n.get("prerequisites", [])):
                a.error(f"{rel}/CURRICULUM.json: {nid} prerequisites must contain only node IDs")
            if not isinstance(n.get("outcomes"), list):
                a.error(f"{rel}/CURRICULUM.json: {nid} outcomes must be array")
            elif any(not isinstance(x, str) or not x.strip() for x in n.get("outcomes", [])):
                a.error(f"{rel}/CURRICULUM.json: {nid} outcomes must contain non-empty strings")
            if not isinstance(n.get("target_concepts"), list):
                a.error(f"{rel}/CURRICULUM.json: {nid} target_concepts must be array")

        concepts = con.get("concepts", [])
        if not isinstance(concepts, list):
            a.error(f"{rel}/registry/concepts.json: concepts must be array")
            concepts = []
        local_names: dict[str, str] = {}
        alias_owner: dict[str, str] = {}
        for c in concepts:
            if not isinstance(c, dict):
                a.error(f"{rel}/registry/concepts.json: concept entries must be objects")
                continue
            cid = c.get("id")
            name = c.get("name")
            if not isinstance(cid, str) or not cid:
                a.error(f"{rel}/registry/concepts.json: concept missing id")
                continue
            if not cid.startswith(expected_id_prefix(m["code"])):
                a.error(f"{rel}/registry/concepts.json: concept {cid} must use track code prefix {m['code']}-")
            if not isinstance(name, str) or not name.strip():
                a.error(f"{rel}/registry/concepts.json: {cid} name must be non-empty string")
            if cid in global_concepts:
                a.error(f"Duplicate concept ID {cid}")
            global_concepts[cid] = (slug, c)
            if c.get("current_depth") is not None and c.get("current_depth") not in DEPTHS:
                a.error(f"{rel}/registry/concepts.json: {cid} invalid current_depth {c.get('current_depth')!r}")
            if isinstance(name, str):
                nn = norm(name)
                if nn and nn in local_names:
                    a.warn(f"{rel}/registry/concepts.json: near-exact duplicate concept titles: {local_names[nn]} and {cid}")
                local_names[nn] = cid
            aliases = c.get("aliases", [])
            if not isinstance(aliases, list):
                a.error(f"{rel}/registry/concepts.json: {cid} aliases must be array")
                aliases = []
            for alias in aliases:
                if not isinstance(alias, str):
                    a.error(f"{rel}/registry/concepts.json: {cid} alias must be string")
                    continue
                na = norm(alias)
                if na in alias_owner and alias_owner[na] != cid:
                    a.warn(f"{rel}/registry/concepts.json: alias {alias!r} shared by {alias_owner[na]} and {cid}")
                alias_owner[na] = cid

        examples = exa.get("examples", [])
        if not isinstance(examples, list):
            a.error(f"{rel}/registry/examples.json: examples must be array")
            examples = []
        local_sigs: dict[str, str] = {}
        for e in examples:
            if not isinstance(e, dict):
                a.error(f"{rel}/registry/examples.json: example entries must be objects")
                continue
            eid = e.get("id")
            sig = e.get("signature")
            if not isinstance(eid, str) or not eid:
                a.error(f"{rel}/registry/examples.json: example missing id")
                continue
            if not re.fullmatch(rf"{re.escape(m['code'])}-EX-[0-9]{{3,}}", eid):
                a.error(f"{rel}/registry/examples.json: invalid example ID {eid!r}; expected {m['code']}-EX-NNN")
            if not isinstance(sig, str) or not sig.strip():
                a.error(f"{rel}/registry/examples.json: {eid} signature must be non-empty string")
            if not isinstance(e.get("domain"), str) or not e.get("domain", "").strip():
                a.error(f"{rel}/registry/examples.json: {eid} domain must be non-empty string")
            if eid in global_examples:
                a.error(f"Duplicate example ID {eid}")
            global_examples[eid] = (slug, e)
            if isinstance(sig, str):
                ns = norm(sig)
                if ns and ns in local_sigs:
                    a.warn(f"{rel}/registry/examples.json: duplicate example signature: {local_sigs[ns]} and {eid}")
                local_sigs[ns] = eid

        refs = ref.get("references", [])
        if not isinstance(refs, list):
            a.error(f"{rel}/registry/references.json: references must be array")
            refs = []
        for r in refs:
            if not isinstance(r, dict):
                a.error(f"{rel}/registry/references.json: reference entries must be objects")
                continue
            rid = r.get("id")
            if not isinstance(rid, str) or not rid:
                a.error(f"{rel}/registry/references.json: reference missing id")
                continue
            if not re.fullmatch(rf"{re.escape(m['code'])}-REF-[0-9]{{3,}}", rid):
                a.error(f"{rel}/registry/references.json: invalid reference ID {rid!r}; expected {m['code']}-REF-NNN")
            for field in ("title", "authority", "locator"):
                if not isinstance(r.get(field), str) or not r.get(field, "").strip():
                    a.error(f"{rel}/registry/references.json: {rid} {field} must be non-empty string")
            if r.get("type") not in REFERENCE_TYPES:
                a.error(f"{rel}/registry/references.json: {rid} invalid type {r.get('type')!r}")
            parse_iso_date(r.get("reviewed_at"), f"{rel}/registry/references.json: {rid} reviewed_at", a, allow_none=False)
            if rid in global_refs:
                a.error(f"Duplicate reference ID {rid}")
            global_refs[rid] = (slug, r)
            review_after = r.get("review_after")
            if review_after is not None:
                due = parse_iso_date(review_after, f"{rel}/registry/references.json: {rid} review_after", a, allow_none=True)
                if due and due < today:
                    a.warn(f"{rel}/registry/references.json: {rid} declared stale; review_after={review_after}")

        if frontier:
            expected_frontier_schema = schema_pointer(tp / "research/FRONTIER.json", "frontier.schema.json")
            if frontier.get("$schema") != expected_frontier_schema:
                a.error(f"{rel}/research/FRONTIER.json: invalid $schema pointer; expected {expected_frontier_schema!r}")
            if frontier.get("schema_version") != 1:
                a.error(f"{rel}/research/FRONTIER.json: unsupported schema_version")
            if frontier.get("track") != slug:
                a.error(f"{rel}/research/FRONTIER.json: track mismatch")
            frontier_status = frontier.get("status")
            if frontier_status not in {"inactive", "active", "needs-refresh"}:
                a.error(f"{rel}/research/FRONTIER.json: invalid status {frontier_status!r}")
            if not isinstance(frontier.get("areas"), list) or not isinstance(frontier.get("open_questions"), list):
                a.error(f"{rel}/research/FRONTIER.json: areas/open_questions must be arrays")
            snapshot = frontier.get("snapshot_date")
            review_due = frontier.get("review_due")
            if frontier_status == "active":
                parse_iso_date(snapshot, f"{rel}/research/FRONTIER.json snapshot_date", a, allow_none=False)
                if not review_due:
                    a.error(f"{rel}/research/FRONTIER.json: active frontier requires review_due")
            elif snapshot is not None:
                parse_iso_date(snapshot, f"{rel}/research/FRONTIER.json snapshot_date", a, allow_none=True)
            if review_due:
                due = parse_iso_date(review_due, f"{rel}/research/FRONTIER.json review_due", a, allow_none=True)
                if due and due < today:
                    a.warn(f"{rel}/research/FRONTIER.json: frontier snapshot is overdue for refresh ({review_due})")

    # Resolve graph and target concepts after registries loaded.
    adjacency: dict[str, list[str]] = defaultdict(list)
    for nid, (slug, n) in global_nodes.items():
        for pre in n.get("prerequisites", []) if isinstance(n.get("prerequisites"), list) else []:
            if pre == nid:
                a.error(f"Curriculum node {nid} depends on itself")
            if pre not in global_nodes:
                a.error(f"Curriculum node {nid} has unresolved prerequisite {pre}")
            else:
                adjacency[nid].append(pre)
        for target in n.get("target_concepts", []) if isinstance(n.get("target_concepts"), list) else []:
            if not isinstance(target, dict):
                a.error(f"Curriculum node {nid}: target_concepts entries must be objects")
                continue
            cid = target.get("id")
            depth = target.get("target_depth")
            if cid not in global_concepts:
                a.error(f"Curriculum node {nid}: unknown target concept {cid}")
            elif global_concepts[cid][0] != slug:
                a.error(f"Curriculum node {nid}: cannot target concept {cid} owned by track {global_concepts[cid][0]!r}; use a cross-track prerequisite and local concepts_used instead")
            if depth not in DEPTHS:
                a.error(f"Curriculum node {nid}: invalid target depth {depth!r} for {cid}")

    # Kahn topological pass: iterative, so very deep curricula do not hit Python recursion limits.
    indegree: dict[str, int] = {nid: 0 for nid in global_nodes}
    dependents: dict[str, list[str]] = defaultdict(list)
    for nid, prereqs in adjacency.items():
        for pre in prereqs:
            if pre in global_nodes:
                indegree[nid] += 1
                dependents[pre].append(nid)
    q = deque([nid for nid, deg in indegree.items() if deg == 0])
    visited = 0
    while q:
        current = q.popleft()
        visited += 1
        for dep in dependents.get(current, []):
            indegree[dep] -= 1
            if indegree[dep] == 0:
                q.append(dep)
    if visited != len(global_nodes):
        cyclic = sorted(nid for nid, deg in indegree.items() if deg > 0)
        preview = ", ".join(cyclic[:12])
        suffix = " ..." if len(cyclic) > 12 else ""
        a.error(f"Curriculum dependency cycle detected among: {preview}{suffix}")

    # Coverage validation.
    for tp, m in tracks:
        slug = m["id"]
        rel = tp.relative_to(ROOT)
        cov = coverages.get(slug, {})
        cur = curricula.get(slug, {})
        baseline = cov.get("baseline", {})
        if not isinstance(baseline, dict):
            a.error(f"{rel}/COVERAGE.json: baseline must be object")
            baseline = {}
        baseline_status = baseline.get("status")
        if baseline_status not in BASELINE_STATUSES:
            a.error(f"{rel}/COVERAGE.json: invalid baseline status {baseline_status!r}")
        baseline_sources = baseline.get("sources", [])
        if not isinstance(baseline_sources, list):
            a.error(f"{rel}/COVERAGE.json: baseline.sources must be array of reference IDs")
            baseline_sources = []
        elif any(not isinstance(x, str) for x in baseline_sources):
            a.error(f"{rel}/COVERAGE.json: baseline.sources must contain only reference IDs")
        for rid in baseline_sources:
            if rid not in global_refs:
                a.error(f"{rel}/COVERAGE.json: baseline source references unknown ID {rid!r}")
        if baseline_status == "audited":
            parse_iso_date(baseline.get("last_audited"), f"{rel}/COVERAGE.json baseline.last_audited", a, allow_none=False)
            if len(set(baseline_sources)) < 3:
                a.error(f"{rel}/COVERAGE.json: audited baseline requires at least 3 distinct registered sources")
            source_types = {global_refs[rid][1].get("type") for rid in baseline_sources if rid in global_refs}
            if len(source_types) < 2:
                a.error(f"{rel}/COVERAGE.json: audited baseline requires at least 2 source classes")
        if cur.get("last_coverage_audit") is not None:
            parse_iso_date(cur.get("last_coverage_audit"), f"{rel}/CURRICULUM.json last_coverage_audit", a, allow_none=True)
        items = cov.get("items", [])
        if not isinstance(items, list):
            a.error(f"{rel}/COVERAGE.json: items must be array")
            items = []
        coverage_ids: set[str] = set()
        for item in items:
            if not isinstance(item, dict):
                a.error(f"{rel}/COVERAGE.json: coverage item must be object")
                continue
            iid = item.get("id")
            if not isinstance(iid, str) or not iid:
                a.error(f"{rel}/COVERAGE.json: coverage item missing id")
            elif iid in coverage_ids:
                a.error(f"{rel}/COVERAGE.json: duplicate coverage item {iid}")
            else:
                coverage_ids.add(iid)
            if not isinstance(item.get("title"), str) or not item.get("title", "").strip():
                a.error(f"{rel}/COVERAGE.json: {iid} title must be non-empty string")
            if item.get("status") not in COVERAGE_STATUSES:
                a.error(f"{rel}/COVERAGE.json: {iid} invalid status {item.get('status')!r}")
            source_refs = item.get("source_refs", [])
            if not isinstance(source_refs, list):
                a.error(f"{rel}/COVERAGE.json: {iid} source_refs must be array")
                source_refs = []
            for rid in source_refs:
                if rid not in global_refs:
                    a.error(f"{rel}/COVERAGE.json: {iid} references unknown source {rid!r}")
            if baseline_status == "audited" and not source_refs:
                a.error(f"{rel}/COVERAGE.json: audited coverage item {iid} requires source_refs")
            mapped = item.get("mapped_nodes", [])
            if not isinstance(mapped, list):
                a.error(f"{rel}/COVERAGE.json: {iid} mapped_nodes must be array")
                mapped = []
            for nid in mapped:
                if nid not in global_nodes:
                    a.error(f"{rel}/COVERAGE.json: {iid} maps to unknown node {nid}")
            if item.get("status") in {"planned", "covered"} and not mapped:
                a.error(f"{rel}/COVERAGE.json: {iid} status {item.get('status')} requires mapped_nodes")
            if item.get("status") == "deferred" and not item.get("rationale"):
                a.error(f"{rel}/COVERAGE.json: deferred item {iid} requires rationale")

        if baseline_status == "audited" and not items:
            a.error(f"{rel}/COVERAGE.json: audited baseline requires non-empty coverage items")
        published = any(isinstance(n, dict) and n.get("status") == "published" for n in cur.get("nodes", []) if isinstance(cur.get("nodes"), list))
        has_gap = any(isinstance(item, dict) and item.get("status") == "gap" for item in items)
        if published and baseline.get("status") != "audited":
            a.error(f"{rel}: published curriculum exists before coverage baseline is audited")
        if published and has_gap:
            a.error(f"{rel}: published curriculum is blocked while coverage contains unresolved gap items")
        if cur.get("audit_status") == "audited" and baseline.get("status") != "audited":
            a.error(f"{rel}: curriculum says audited but coverage baseline does not")
        if cur.get("audit_status") == "audited" and has_gap:
            a.error(f"{rel}: curriculum cannot be audited while coverage contains unresolved gaps")
        if cur.get("audit_status") == "audited" and not cur.get("nodes"):
            a.error(f"{rel}: audited curriculum requires at least one curriculum node")
        if m.get("status") == "scaffolded" and (cur.get("audit_status") == "audited" or bool(cur.get("nodes"))):
            a.error(f"{rel}/TRACK.json: scaffolded track cannot contain an audited/non-empty curriculum; set track status to active or paused")

    # Lessons.
    lesson_ids: dict[str, tuple[str, Path, dict[str, Any]]] = {}
    node_to_lesson: dict[str, str] = {}
    required_fm = [
        "id","title","track","level","status","curriculum_node",
        "concepts_introduced","concepts_deepened","concepts_used",
        "examples_added","references_used","last_reviewed","version_sensitive","review_after"
    ]
    for tp, m in tracks:
        slug = m["id"]
        rel = tp.relative_to(ROOT)
        for path in sorted((tp / "lessons").rglob("*.md")):
            parsed = parse_frontmatter(path, a)
            if not parsed:
                continue
            fm, body = parsed
            for key in required_fm:
                if key not in fm:
                    a.error(f"{path.relative_to(ROOT)}: missing front-matter field {key!r}")
            lid = fm.get("id")
            if not isinstance(lid, str) or not lid:
                a.error(f"{path.relative_to(ROOT)}: invalid lesson id")
                continue
            if not re.fullmatch(rf"{re.escape(m['code'])}-[0-9]{{4,}}", lid):
                a.error(f"{path.relative_to(ROOT)}: invalid lesson ID {lid!r}; expected {m['code']}-NNNN")
            if not path.name.startswith(f"{lid}-"):
                a.error(f"{path.relative_to(ROOT)}: filename must start with lesson ID {lid}-")
            if lid in lesson_ids:
                a.error(f"Duplicate lesson ID {lid}")
            lesson_ids[lid] = (slug, path, fm)
            if fm.get("track") != slug:
                a.error(f"{path.relative_to(ROOT)}: track must equal {slug!r}")
            if fm.get("level") not in LEVELS:
                a.error(f"{path.relative_to(ROOT)}: invalid level {fm.get('level')!r}")
            if fm.get("status") not in LESSON_STATUSES:
                a.error(f"{path.relative_to(ROOT)}: invalid status {fm.get('status')!r}")
            nid = fm.get("curriculum_node")
            if nid not in global_nodes:
                a.error(f"{path.relative_to(ROOT)}: unknown curriculum_node {nid!r}")
            else:
                owner, node = global_nodes[nid]
                if owner != slug:
                    a.error(f"{path.relative_to(ROOT)}: lesson cannot publish node owned by track {owner!r}")
                if nid in node_to_lesson and node_to_lesson[nid] != lid:
                    a.error(f"Curriculum node {nid} is linked to multiple lessons")
                node_to_lesson[nid] = lid
                if fm.get("status") == "complete" and node.get("status") != "published":
                    a.error(f"{path.relative_to(ROOT)}: complete lesson requires published node {nid}")
                if node.get("lesson_id") not in {None, lid}:
                    a.error(f"{path.relative_to(ROOT)}: node {nid} lesson_id is {node.get('lesson_id')!r}, expected {lid!r}")
                if node.get("level") != fm.get("level"):
                    a.error(f"{path.relative_to(ROOT)}: lesson level must match curriculum node {nid}")

            for field, registry in [
                ("concepts_introduced", global_concepts),
                ("concepts_deepened", global_concepts),
                ("concepts_used", global_concepts),
                ("examples_added", global_examples),
                ("references_used", global_refs),
            ]:
                value = fm.get(field)
                if not isinstance(value, list):
                    a.error(f"{path.relative_to(ROOT)}: {field} must be inline JSON array")
                    continue
                for rid in value:
                    if rid not in registry:
                        a.error(f"{path.relative_to(ROOT)}: {field} references unknown ID {rid!r}")

            intro = set(fm.get("concepts_introduced", [])) if isinstance(fm.get("concepts_introduced"), list) else set()
            deep = set(fm.get("concepts_deepened", [])) if isinstance(fm.get("concepts_deepened"), list) else set()
            if intro & deep:
                a.error(f"{path.relative_to(ROOT)}: same concept cannot be both introduced and deepened in one lesson: {sorted(intro & deep)}")
            parse_iso_date(fm.get("last_reviewed"), f"{path.relative_to(ROOT)} last_reviewed", a, allow_none=False)
            if not isinstance(fm.get("version_sensitive"), bool):
                a.error(f"{path.relative_to(ROOT)}: version_sensitive must be true/false")
            review_after = fm.get("review_after")
            if fm.get("version_sensitive") is True and review_after is None:
                a.error(f"{path.relative_to(ROOT)}: version-sensitive lesson requires review_after")
            if review_after is not None:
                due = parse_iso_date(review_after, f"{path.relative_to(ROOT)} review_after", a, allow_none=True)
                if due and due < today:
                    a.warn(f"{path.relative_to(ROOT)}: lesson freshness review is overdue ({review_after})")

            if fm.get("status") == "complete":
                lower_body = body.casefold()
                for placeholder in PLACEHOLDER_PATTERNS:
                    if placeholder in lower_body:
                        a.error(f"{path.relative_to(ROOT)}: published lesson contains placeholder text {placeholder!r}")

    # Every published node must point back to a complete lesson.
    for nid, (owner, node) in global_nodes.items():
        if node.get("status") == "published":
            lid = node.get("lesson_id")
            if not lid:
                a.error(f"Published curriculum node {nid} has no lesson_id")
            elif lid not in lesson_ids:
                a.error(f"Published curriculum node {nid} references missing lesson {lid}")
            elif lesson_ids[lid][2].get("status") != "complete":
                a.error(f"Published curriculum node {nid} references non-complete lesson {lid}")

    # Exercises, projects, and research notes are first-class evidence artifacts.
    artifact_ids: dict[str, tuple[str, Path, str]] = {}
    artifact_specs = [
        ("exercises", "EXR", {"id","title","track","level","status","curriculum_nodes","concepts_used","references_used","last_reviewed"}),
        ("projects", "PRJ", {"id","title","track","level","status","curriculum_nodes","concepts_used","references_used","last_reviewed"}),
        ("research", "R", {"id","title","track","status","curriculum_nodes","concepts_used","references_used","research_snapshot","last_reviewed"}),
    ]
    for tp, m in tracks:
        slug = m["id"]
        code = m["code"]
        for dirname, kind, required in artifact_specs:
            for path in sorted((tp / dirname).rglob("*.md")):
                parsed = parse_frontmatter(path, a)
                if not parsed:
                    continue
                fm, _ = parsed
                for key in required:
                    if key not in fm:
                        a.error(f"{path.relative_to(ROOT)}: missing front-matter field {key!r}")
                aid = fm.get("id")
                if not isinstance(aid, str) or not aid:
                    a.error(f"{path.relative_to(ROOT)}: invalid artifact id")
                    continue
                if kind == "R":
                    pattern = rf"{re.escape(code)}-R-[0-9]{{8}}-[0-9]{{3,}}"
                else:
                    pattern = rf"{re.escape(code)}-{kind}-[0-9]{{4,}}"
                if not re.fullmatch(pattern, aid):
                    a.error(f"{path.relative_to(ROOT)}: invalid {kind} artifact ID {aid!r}")
                if aid in artifact_ids or aid in lesson_ids:
                    a.error(f"Duplicate learning artifact ID {aid}")
                artifact_ids[aid] = (slug, path, kind)
                if fm.get("track") != slug:
                    a.error(f"{path.relative_to(ROOT)}: track must equal {slug!r}")
                if fm.get("status") not in ARTIFACT_STATUSES:
                    a.error(f"{path.relative_to(ROOT)}: invalid status {fm.get('status')!r}")
                if kind != "R" and fm.get("level") not in LEVELS:
                    a.error(f"{path.relative_to(ROOT)}: invalid level {fm.get('level')!r}")
                parse_iso_date(fm.get("last_reviewed"), f"{path.relative_to(ROOT)} last_reviewed", a, allow_none=False)
                if kind == "R":
                    parse_iso_date(fm.get("research_snapshot"), f"{path.relative_to(ROOT)} research_snapshot", a, allow_none=False)
                for field, registry in (("curriculum_nodes", global_nodes), ("concepts_used", global_concepts), ("references_used", global_refs)):
                    values = fm.get(field)
                    if not isinstance(values, list):
                        a.error(f"{path.relative_to(ROOT)}: {field} must be inline JSON array")
                        continue
                    for value in values:
                        if value not in registry:
                            a.error(f"{path.relative_to(ROOT)}: {field} references unknown ID {value!r}")

    # Concept current_depth is derived from published curriculum targets.
    derived_depth: dict[str, str | None] = {cid: None for cid in global_concepts}
    for nid, (_, node) in global_nodes.items():
        if node.get("status") != "published":
            continue
        for target in node.get("target_concepts", []) if isinstance(node.get("target_concepts"), list) else []:
            if not isinstance(target, dict):
                continue
            cid = target.get("id")
            depth = target.get("target_depth")
            if cid in derived_depth and depth in DEPTH_RANK:
                prior = derived_depth[cid]
                if prior is None or DEPTH_RANK[depth] > DEPTH_RANK[prior]:
                    derived_depth[cid] = depth
    for cid, (owner, concept) in global_concepts.items():
        actual = concept.get("current_depth")
        expected = derived_depth.get(cid)
        if actual != expected:
            a.error(f"Concept {cid} current_depth={actual!r} but published curriculum implies {expected!r}")
    for nid, (_, node) in global_nodes.items():
        if node.get("status") in {"planned", "ready", "drafting"}:
            for target in node.get("target_concepts", []) if isinstance(node.get("target_concepts"), list) else []:
                if not isinstance(target, dict):
                    continue
                cid = target.get("id")
                depth = target.get("target_depth")
                current = derived_depth.get(cid)
                if current in DEPTH_RANK and depth in DEPTH_RANK and DEPTH_RANK[depth] <= DEPTH_RANK[current]:
                    a.warn(f"Curriculum node {nid} targets {cid} at {depth}, not deeper than current published depth {current}; review for same-depth duplication")

    # Learner state must reference real lessons/concepts/evidence artifacts.
    evidence_ids = set(artifact_ids) | set(lesson_ids)
    for tp, m in tracks:
        slug = m["id"]
        rel = tp.relative_to(ROOT)
        lea = learners.get(slug, {})
        if not isinstance(lea.get("profile_id"), str) or not lea.get("profile_id", "").strip():
            a.error(f"{rel}/LEARNER_STATE.json: profile_id must be non-empty string")
        if lea.get("last_updated") is not None:
            parse_iso_date(lea.get("last_updated"), f"{rel}/LEARNER_STATE.json last_updated", a, allow_none=True)
        lesson_state = lea.get("lessons", {})
        if not isinstance(lesson_state, dict):
            a.error(f"{rel}/LEARNER_STATE.json: lessons must be object")
            lesson_state = {}
        for lid, st in lesson_state.items():
            if lid not in lesson_ids:
                a.error(f"{rel}/LEARNER_STATE.json: unknown lesson {lid}")
                continue
            if lesson_ids[lid][0] != slug:
                a.error(f"{rel}/LEARNER_STATE.json: lesson {lid} belongs to another track")
            if not isinstance(st, dict):
                a.error(f"{rel}/LEARNER_STATE.json: state for {lid} must be object")
                continue
            if st.get("state") not in LEARNER_STATES:
                a.error(f"{rel}/LEARNER_STATE.json: {lid} invalid state {st.get('state')!r}")
            for date_field in ("last_engaged", "review_due"):
                if st.get(date_field) is not None:
                    parse_iso_date(st.get(date_field), f"{rel}/LEARNER_STATE.json {lid} {date_field}", a, allow_none=True)
            confidence = st.get("confidence")
            if confidence is not None and (not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or not 0 <= confidence <= 1):
                a.error(f"{rel}/LEARNER_STATE.json: {lid} confidence must be between 0 and 1")
            evidence = st.get("evidence", [])
            if not isinstance(evidence, list):
                a.error(f"{rel}/LEARNER_STATE.json: {lid} evidence must be array")
            else:
                for eid in evidence:
                    if eid not in evidence_ids:
                        a.error(f"{rel}/LEARNER_STATE.json: {lid} evidence references unknown artifact {eid!r}")
        concept_state = lea.get("concepts", {})
        if not isinstance(concept_state, dict):
            a.error(f"{rel}/LEARNER_STATE.json: concepts must be object")
            concept_state = {}
        for cid, st in concept_state.items():
            if cid not in global_concepts:
                a.error(f"{rel}/LEARNER_STATE.json: unknown concept {cid}")
                continue
            if global_concepts[cid][0] != slug:
                a.error(f"{rel}/LEARNER_STATE.json: concept {cid} belongs to another track")
            if not isinstance(st, dict):
                a.error(f"{rel}/LEARNER_STATE.json: concept state for {cid} must be object")
                continue
            depth = st.get("demonstrated_depth")
            if depth is not None and depth not in DEPTHS:
                a.error(f"{rel}/LEARNER_STATE.json: {cid} invalid demonstrated_depth {depth!r}")
            curriculum_depth = derived_depth.get(cid)
            if depth in DEPTH_RANK and curriculum_depth in DEPTH_RANK and DEPTH_RANK[depth] > DEPTH_RANK[curriculum_depth]:
                a.error(f"{rel}/LEARNER_STATE.json: {cid} demonstrated_depth {depth} exceeds published curriculum depth {curriculum_depth}")
            confidence = st.get("confidence")
            if confidence is not None and (not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or not 0 <= confidence <= 1):
                a.error(f"{rel}/LEARNER_STATE.json: {cid} confidence must be between 0 and 1")
            for date_field in ("last_engaged", "review_due"):
                if st.get(date_field) is not None:
                    parse_iso_date(st.get(date_field), f"{rel}/LEARNER_STATE.json {cid} {date_field}", a, allow_none=True)
            evidence = st.get("evidence", [])
            if not isinstance(evidence, list):
                a.error(f"{rel}/LEARNER_STATE.json: {cid} evidence must be array")
            else:
                for eid in evidence:
                    if eid not in evidence_ids:
                        a.error(f"{rel}/LEARNER_STATE.json: {cid} evidence references unknown artifact {eid!r}")
        review_queue = lea.get("review_queue", [])
        if not isinstance(review_queue, list):
            a.error(f"{rel}/LEARNER_STATE.json: review_queue must be array")
            review_queue = []
        for i, item in enumerate(review_queue):
            if not isinstance(item, dict):
                a.error(f"{rel}/LEARNER_STATE.json: review_queue[{i}] must be object")
                continue
            target_type = item.get("target_type")
            target_id = item.get("target_id")
            if target_type not in {"lesson", "concept"}:
                a.error(f"{rel}/LEARNER_STATE.json: review_queue[{i}] invalid target_type {target_type!r}")
            if target_type == "lesson" and target_id not in lesson_ids:
                a.error(f"{rel}/LEARNER_STATE.json: review_queue[{i}] unknown lesson {target_id!r}")
            if target_type == "concept" and target_id not in global_concepts:
                a.error(f"{rel}/LEARNER_STATE.json: review_queue[{i}] unknown concept {target_id!r}")
            parse_iso_date(item.get("due"), f"{rel}/LEARNER_STATE.json review_queue[{i}] due", a, allow_none=False)
            if not isinstance(item.get("reason"), str) or not item.get("reason", "").strip():
                a.error(f"{rel}/LEARNER_STATE.json: review_queue[{i}] reason must be non-empty string")

    # Internal Markdown links (relative files only).
    link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            target = target.strip()
            if not target or target.startswith(("http://","https://","#","mailto:")):
                continue
            target = target.split("#",1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                a.warn(f"{path.relative_to(ROOT)}: relative link escapes repository: {target}")
                continue
            if not resolved.exists():
                a.error(f"{path.relative_to(ROOT)}: broken internal link: {target}")

    # Generated view drift.
    if check_generated:
        expected_root = {
            "STATE.md": render_root_state(state or {}),
            "docs/TRACKS.md": render_tracks(tracks),
            "docs/CROSS_TRACK_INDEX.md": render_cross_track(tracks),
        }
        for rel, content in expected_root.items():
            p = ROOT / rel
            if not p.is_file():
                a.error(f"Missing generated view: {rel}")
            elif p.read_text(encoding="utf-8") != content:
                a.error(f"Generated view is stale: {rel} (run `python scripts/csf.py sync`)")
        for tp, m in tracks:
            for name, content in generated_track_views(tp, m, tracks).items():
                p = tp / name
                if not p.is_file():
                    a.error(f"Missing generated view: {p.relative_to(ROOT)}")
                elif p.read_text(encoding="utf-8") != content:
                    a.error(f"Generated view is stale: {p.relative_to(ROOT)} (run `python scripts/csf.py sync`)")

    return a


def print_audit(a: Audit, *, strict: bool = False) -> int:
    print("CSF V3.1 curriculum audit")
    print("=" * 24)
    tracks = discover_tracks()
    print(f"Root: {ROOT}")
    print(f"Tracks discovered: {len(tracks)}")
    print(f"Errors: {len(a.errors)}")
    print(f"Warnings: {len(a.warnings)}")
    if a.warnings:
        print("\nWarnings:")
        for x in a.warnings:
            print(f"  - {x}")
    if a.errors:
        print("\nErrors:")
        for x in a.errors:
            print(f"  - {x}")
        return 1
    if strict and a.warnings:
        print("\nFAIL (strict mode) — warnings must be resolved before merge.")
        return 1
    print("\nPASS — canonical state, graph integrity, references, links, and generated views are consistent.")
    return 0


def cmd_context(slug: str) -> int:
    tracks = discover_tracks()
    hit = track_by_slug(tracks, slug)
    if not hit:
        print(f"Unknown track: {slug}", file=sys.stderr)
        return 2
    path, manifest = hit
    print(render_context(path, manifest, tracks), end="")
    return 0


def cmd_next_authoring(slug: str) -> int:
    tracks = discover_tracks()
    hit = track_by_slug(tracks, slug)
    if not hit:
        print(f"Unknown track: {slug}", file=sys.stderr)
        return 2
    path, manifest = hit
    cur = load_json(path / "CURRICULUM.json") or {}
    cov = load_json(path / "COVERAGE.json") or {}
    baseline = cov.get("baseline", {}) if isinstance(cov.get("baseline"), dict) else {}
    if cur.get("audit_status") != "audited" or baseline.get("status") != "audited":
        print(f"{manifest.get('title')}: authoring is blocked; curriculum/coverage is not audited.")
        print("Perform curriculum reconnaissance before publishing lesson 0001.")
        return 0
    if any(isinstance(item, dict) and item.get("status") == "gap" for item in cov.get("items", []) if isinstance(cov.get("items"), list)):
        print(f"{manifest.get('title')}: authoring is blocked by unresolved coverage gaps.")
        return 0
    status = build_global_node_status(tracks)
    candidates = ready_nodes(path, status)
    if not candidates:
        print(f"{manifest.get('title')}: no authoring-ready curriculum node.")
        return 0
    print(f"{manifest.get('title')} authoring candidates:")
    for n in candidates:
        print(f"- {n.get('id')}: {n.get('title')} [{n.get('level')}]")
    return 0


def cmd_next_study(slug: str) -> int:
    tracks = discover_tracks()
    hit = track_by_slug(tracks, slug)
    if not hit:
        print(f"Unknown track: {slug}", file=sys.stderr)
        return 2
    path, manifest = hit
    due, practice, new = study_candidates(path, tracks)
    print(f"{manifest.get('title')} learner next actions:")
    if due:
        print("Due review:")
        for item in due[:20]:
            print(f"- {item}")
    if practice:
        print("Practice before advancing:")
        for lid in practice[:20]:
            print(f"- {lid}")
    if new:
        print("New lessons with practiced/demonstrated prerequisites:")
        for item in new[:20]:
            print(f"- {item}")
    if not (due or practice or new):
        print("- No study action is ready yet.")
    return 0


def cmd_next(slug: str) -> int:
    rc = cmd_next_authoring(slug)
    if rc != 0:
        return rc
    print()
    return cmd_next_study(slug)


def slugify_title(title: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", title).strip("-")
    return s or "Track"


def cmd_new_track(title: str, slug: str, code: str, order: int | None, parent: str | None = None) -> int:
    if not TRACK_ID_RE.fullmatch(slug):
        print("Track slug must be lowercase kebab-case.", file=sys.stderr)
        return 2
    if not TRACK_CODE_RE.fullmatch(code):
        print("Track code must be 2-8 uppercase alphanumeric characters, starting with a letter.", file=sys.stderr)
        return 2
    tracks = discover_tracks()
    existing_slugs = {m.get("id") for _,m in tracks}
    existing_codes = {m.get("code") for _,m in tracks}
    if slug in existing_slugs:
        print(f"Track id already exists: {slug}", file=sys.stderr)
        return 2
    if code in existing_codes:
        print(f"Track code already exists: {code}", file=sys.stderr)
        return 2
    if order is None:
        order = max([m.get("order",0) for _,m in tracks if isinstance(m.get("order"),int)] or [0]) + 1
    if any(m.get("order") == order for _,m in tracks):
        print(f"Track order already exists: {order}", file=sys.stderr)
        return 2

    if parent:
        parent_rel = Path(parent)
        if parent_rel.is_absolute() or ".." in parent_rel.parts:
            print("Parent must be a safe repository-relative directory.", file=sys.stderr)
            return 2
        parent_path = ROOT / parent_rel
        parent_path.mkdir(parents=True, exist_ok=True)
        prefixes = []
        for child in parent_path.iterdir():
            if child.is_dir():
                m = re.match(r"^(\d+)-", child.name)
                if m:
                    prefixes.append(int(m.group(1)))
        local_prefix = max(prefixes or [0]) + 1
        folder = f"{local_prefix:02d}-{slugify_title(title)}"
        tp = parent_path / folder
    else:
        folder = f"{order:02d}-{slugify_title(title)}"
        tp = ROOT / folder

    if tp.exists():
        print(f"Folder already exists: {tp.relative_to(ROOT)}", file=sys.stderr)
        return 2

    for d in ["lessons","exercises","projects","research","registry"]:
        (tp / d).mkdir(parents=True, exist_ok=True)
    for d in ["lessons","exercises","projects"]:
        (tp / d / ".gitkeep").write_text("", encoding="utf-8")

    def dump(name: str, obj: dict[str, Any]) -> None:
        target = tp / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")

    dump("TRACK.json", {
        "$schema":schema_pointer(tp / "TRACK.json", "track.schema.json"),
        "schema_version":1,"id":slug,"code":code,"title":title,"folder":folder,"order":order,
        "status":"scaffolded","entry_model":"zero-subject-specific-knowledge",
        "scope":{"focus":"","includes":[],"delegates":[]},"entry_prerequisites":[],"neighbor_tracks":[]
    })
    dump("CURRICULUM.json", {"$schema":schema_pointer(tp / "CURRICULUM.json", "curriculum.schema.json"),"schema_version":1,"track":slug,"audit_status":"not-audited","last_coverage_audit":None,"nodes":[]})
    dump("COVERAGE.json", {"$schema":schema_pointer(tp / "COVERAGE.json", "coverage.schema.json"),"schema_version":1,"track":slug,"baseline":{"status":"not-audited","last_audited":None,"sources":[]},"items":[],"unresolved_questions":[]})
    dump("LEARNER_STATE.json", {"$schema":schema_pointer(tp / "LEARNER_STATE.json", "learner-state.schema.json"),"schema_version":1,"track":slug,"profile_id":"owner","last_updated":None,"lessons":{},"concepts":{},"review_queue":[]})
    dump("registry/concepts.json", {"$schema":schema_pointer(tp / "registry/concepts.json", "concept-registry.schema.json"),"schema_version":1,"track":slug,"concepts":[]})
    dump("registry/examples.json", {"$schema":schema_pointer(tp / "registry/examples.json", "example-registry.schema.json"),"schema_version":1,"track":slug,"examples":[]})
    dump("registry/references.json", {"$schema":schema_pointer(tp / "registry/references.json", "reference-registry.schema.json"),"schema_version":1,"track":slug,"references":[]})
    dump("research/FRONTIER.json", {"$schema":schema_pointer(tp / "research/FRONTIER.json", "frontier.schema.json"),"schema_version":1,"track":slug,"status":"inactive","snapshot_date":None,"review_due":None,"areas":[],"open_questions":[],"notes":""})
    (tp / "README.md").write_text(f"# {title}\n\nTrack scaffold created. Perform curriculum reconnaissance before lesson 0001.\n", encoding="utf-8")
    sync()
    print(f"Created {tp.relative_to(ROOT)}")
    print("Next: define TRACK.json scope, perform coverage reconnaissance, then run audit.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Computer Science Foundations V3.1 repository tool")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("sync", help="regenerate Markdown views from canonical state")

    ap = sub.add_parser("audit", help="validate repository integrity")
    ap.add_argument("--no-generated-check", action="store_true")
    ap.add_argument("--strict", action="store_true", help="treat warnings as CI-blocking failures")

    cp = sub.add_parser("context", help="print a compact AI context pack")
    cp.add_argument("track")

    np = sub.add_parser("next", help="show both authoring and learner next actions")
    np.add_argument("track")

    nap = sub.add_parser("next-authoring", help="show curriculum nodes ready to be authored")
    nap.add_argument("track")

    nsp = sub.add_parser("next-study", help="show learner review/practice/new-study actions")
    nsp.add_argument("track")

    nt = sub.add_parser("new-track", help="scaffold a future track without editing audit code")
    nt.add_argument("--title", required=True)
    nt.add_argument("--slug", required=True)
    nt.add_argument("--code", required=True)
    nt.add_argument("--order", type=int)
    nt.add_argument("--parent", help="optional repository-relative container directory for a nested track")

    args = parser.parse_args(argv)
    if args.command == "sync":
        sync()
        print("Generated views synchronized.")
        return 0
    if args.command == "audit":
        return print_audit(audit_repository(check_generated=not args.no_generated_check), strict=args.strict)
    if args.command == "context":
        return cmd_context(args.track)
    if args.command == "next":
        return cmd_next(args.track)
    if args.command == "next-authoring":
        return cmd_next_authoring(args.track)
    if args.command == "next-study":
        return cmd_next_study(args.track)
    if args.command == "new-track":
        return cmd_new_track(args.title, args.slug, args.code, args.order, args.parent)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
