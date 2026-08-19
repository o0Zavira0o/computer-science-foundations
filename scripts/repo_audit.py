#!/usr/bin/env python3
"""Lightweight structural audit for the curriculum repository.

Standard-library only. It validates track scaffolds and detects duplicate
published lesson IDs. It intentionally does not try to judge educational
quality; that is governed by docs/LEARNING_SYSTEM.md.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

TRACKS = [
    "01-Linear-Algebra",
    "02-Linux-Systems",
    "03-CPP",
    "04-Computer-Architecture",
    "05-Programming-Parallel-Processors",
    "06-Complex-Analysis",
    "07-Computer-Systems",
]

REQUIRED_ROOT = [
    "README.md",
    "AI_INSTRUCTIONS.md",
    "STATE.md",
    "AGENTS.md",
    "docs/LEARNING_SYSTEM.md",
    "docs/CROSS_TRACK_INDEX.md",
]

REQUIRED_TRACK_FILES = [
    "README.md",
    "ROADMAP.md",
    "PROGRESS.md",
    "CONCEPTS.md",
    "EXAMPLES.md",
    "REFERENCES.md",
]

REQUIRED_TRACK_DIRS = [
    "lessons",
    "exercises",
    "projects",
    "research",
]


def frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return text[4:end]


def scalar(fm: str, key: str) -> str | None:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", fm)
    if not m:
        return None
    return m.group(1).strip().strip("'\"")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_ROOT:
        if not (ROOT / rel).exists():
            errors.append(f"Missing required root file: {rel}")

    for track in TRACKS:
        tp = ROOT / track
        if not tp.is_dir():
            errors.append(f"Missing track directory: {track}")
            continue

        for name in REQUIRED_TRACK_FILES:
            if not (tp / name).is_file():
                errors.append(f"{track}: missing {name}")

        for name in REQUIRED_TRACK_DIRS:
            if not (tp / name).is_dir():
                errors.append(f"{track}: missing directory {name}/")

    lesson_ids: dict[str, Path] = {}
    for track in TRACKS:
        lesson_dir = ROOT / track / "lessons"
        if not lesson_dir.exists():
            continue

        for path in sorted(lesson_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            fm = frontmatter(text)
            if fm is None:
                errors.append(f"{path.relative_to(ROOT)}: missing YAML front matter")
                continue

            for key in ("id", "title", "track", "level", "status", "last_reviewed"):
                if scalar(fm, key) is None:
                    errors.append(
                        f"{path.relative_to(ROOT)}: missing front-matter field '{key}'"
                    )

            lid = scalar(fm, "id")
            if lid:
                if lid in lesson_ids:
                    errors.append(
                        f"Duplicate lesson id {lid}: "
                        f"{lesson_ids[lid].relative_to(ROOT)} and {path.relative_to(ROOT)}"
                    )
                else:
                    lesson_ids[lid] = path

            status = scalar(fm, "status")
            if status not in {"draft", "complete", "needs-review", "deprecated", None}:
                warnings.append(
                    f"{path.relative_to(ROOT)}: unusual status '{status}'"
                )

    print("Curriculum repository audit")
    print("=" * 28)
    print(f"Root: {ROOT}")
    print(f"Tracks checked: {len(TRACKS)}")
    print(f"Lesson IDs found: {len(lesson_ids)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if warnings:
        print("\nWarnings:")
        for item in warnings:
            print(f"  - {item}")

    if errors:
        print("\nErrors:")
        for item in errors:
            print(f"  - {item}")
        return 1

    print("\nPASS — structural checks succeeded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
