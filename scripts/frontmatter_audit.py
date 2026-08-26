#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TOP_LEVEL_FIELD_RE = re.compile(
    r"^([A-Za-z_][A-Za-z0-9_-]*):(?:[ \t]+)(.*)$"
)
SAFE_PREFIXES = ('"', "'", "[", "{", "|", ">")


def git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.stdout.strip()


def frontmatter_end(lines: list[str]):
    if not lines or lines[0].strip() != "---":
        return None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return index
    return "unterminated"


def unsafe_scalar_info(line: str):
    if not line or line[0].isspace():
        return None
    match = TOP_LEVEL_FIELD_RE.match(line)
    if not match:
        return None
    key, value = match.group(1), match.group(2).strip()
    if not value or value.startswith(SAFE_PREFIXES):
        return None
    if ": " in value:
        return key, value
    return None


def audit(path: Path) -> list[str]:
    lines = path.read_text().splitlines()
    end = frontmatter_end(lines)
    rel = path.relative_to(ROOT)

    if end is None:
        return []
    if end == "unterminated":
        return [f"{rel}: YAML frontmatter has no closing ---"]

    errors = []
    for index in range(1, end):
        line = lines[index]
        info = unsafe_scalar_info(line)
        if info is not None:
            key, value = info
            errors.append(
                f"{rel}:{index + 1}: unsafe unquoted YAML scalar "
                f"for {key!r}: {value!r}"
            )
        if "\t" in line:
            errors.append(
                f"{rel}:{index + 1}: tab in YAML frontmatter"
            )
    return errors


def all_markdown() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md")
        if ".git" not in p.parts
    )


def staged_markdown() -> list[Path]:
    output = git(
        "diff", "--cached", "--name-only", "--diff-filter=ACMR"
    )
    result = []
    for raw in output.splitlines():
        if raw.endswith(".md"):
            p = ROOT / raw
            if p.is_file():
                result.append(p)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--staged", action="store_true")
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()

    if args.staged and args.paths:
        parser.error("--staged cannot be combined with explicit paths")

    if args.staged:
        files = staged_markdown()
    elif args.paths:
        files = [
            (ROOT / raw).resolve()
            for raw in args.paths
            if (ROOT / raw).resolve().is_file()
            and (ROOT / raw).resolve().suffix == ".md"
        ]
    else:
        files = all_markdown()

    errors = []
    for path in files:
        errors.extend(audit(path))

    print(f"Frontmatter audit files: {len(files)}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\nPASS — Markdown YAML frontmatter checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
