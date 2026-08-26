#!/usr/bin/env python3
"""
Repository-local Markdown/render source audit.

This tool does not replace `python scripts/csf.py audit --strict` and it cannot
replace inspection of the actual GitHub Preview. It catches source patterns that
have repeatedly caused rendering failures in this repository.

Typical use before commit:

    python scripts/render_audit.py \
      02-Linux-Systems/lessons/LNX-0010-standard-streams-redirection-and-pipelines.md \
      09-Auxiliary-Studies/03-Philosophy-and-Logic/lessons/PHL-0003-premises-conclusions-and-argument-indicators.md

After staging:

    python scripts/render_audit.py --staged
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

LEGACY_DELIMITERS = (r"\(", r"\)", r"\[", r"\]")
ROW_SENSITIVE = (
    r"\begin{bmatrix}",
    r"\begin{pmatrix}",
    r"\begin{Bmatrix}",
    r"\begin{vmatrix}",
    r"\begin{Vmatrix}",
    r"\begin{matrix}",
    r"\begin{aligned}",
    r"\begin{alignedat}",
    r"\begin{array}",
    r"\begin{cases}",
    r"\begin{gathered}",
)


def git_root() -> Path:
    p = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return Path(p.stdout.strip())


def staged_markdown(root: Path) -> list[Path]:
    p = subprocess.run(
        [
            "git",
            "diff",
            "--cached",
            "--name-only",
            "--diff-filter=ACMR",
            "--",
            "*.md",
        ],
        cwd=root,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    paths = [root / x for x in p.stdout.splitlines() if x.strip()]
    # Staged mode is intentionally lesson-scoped. Repository documentation may
    # contain literal examples of forbidden delimiters or fenced syntax while
    # explaining the house rules; those are not lesson-render defects.
    return [p for p in paths if "lessons" in p.parts]


def lesson_markdown(root: Path) -> list[Path]:
    return sorted(root.glob("**/lessons/*.md"))


def resolve_paths(root: Path, raw: list[str]) -> list[Path]:
    out: list[Path] = []
    for item in raw:
        p = Path(item)
        if not p.is_absolute():
            p = root / p
        if p.is_dir():
            out.extend(sorted(p.rglob("*.md")))
        else:
            out.append(p)
    return out


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def scan_file(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    notices: list[str] = []

    if not path.exists():
        return [f"{path}: file does not exist"], notices

    text = path.read_text(errors="replace")
    lines = text.splitlines()

    # Repository convention forbids legacy backslash delimiters.
    for token in LEGACY_DELIMITERS:
        pos = text.find(token)
        if pos >= 0:
            errors.append(
                f"{path}:{line_number(text, pos)}: legacy math delimiter {token!r}"
            )

    # Multiline dollar-display blocks are forbidden by the conservative profile.
    multiline = re.compile(r"(?ms)^\s*\$\$\s*$.*?^\s*\$\$\s*$")
    for match in multiline.finditer(text):
        errors.append(
            f"{path}:{line_number(text, match.start())}: multiline $$ display; "
            "use one-line $$ for simple displays or fenced math for row-sensitive math"
        )

    # One-line dollar displays must not contain row-sensitive structures.
    for n, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("$$") and s.endswith("$$") and len(s) > 4:
            expr = s[2:-2]
            if "\\\\" in expr or any(token in expr for token in ROW_SENSITIVE):
                errors.append(
                    f"{path}:{n}: row-sensitive LaTeX inside one-line $$ display; "
                    "use fenced ```math"
                )

    # Parse math fences and reject unclosed/nested malformed blocks.
    i = 0
    while i < len(lines):
        if lines[i].strip() == "```math":
            start = i + 1
            i += 1
            while i < len(lines) and lines[i].strip() != "```":
                if lines[i].strip() == "```math":
                    errors.append(f"{path}:{i+1}: nested math fence")
                i += 1
            if i >= len(lines):
                errors.append(f"{path}:{start}: unclosed fenced math block")
                break
        i += 1

    # Static visual anchors require nearby source/license discipline.
    image_lines = [
        n for n, line in enumerate(lines, 1)
        if re.search(r"!\[[^\]]*\]\([^)]+\)", line)
    ]
    for n in image_lines:
        nearby = "\n".join(lines[n:min(len(lines), n + 5)])
        if "Source:" not in nearby:
            notices.append(
                f"{path}:{n}: embedded image found; verify nearby caption contains exact Source:"
            )
        if not re.search(
            r"\b(CC BY|CC0|public domain|Public domain|license|License)\b",
            nearby,
        ):
            notices.append(
                f"{path}:{n}: embedded image found; verify author/organization and license"
            )

    return errors, notices


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", help="Markdown files or directories to audit")
    ap.add_argument(
        "--staged",
        action="store_true",
        help="Audit staged lesson Markdown files instead of positional paths",
    )
    ap.add_argument(
        "--all-lessons",
        action="store_true",
        help="Audit every lesson Markdown file (use for migrations/repository review)",
    )
    args = ap.parse_args()

    root = git_root()

    modes = int(args.staged) + int(args.all_lessons) + int(bool(args.paths))
    if modes != 1:
        ap.error("choose exactly one of: positional paths, --staged, --all-lessons")

    if args.staged:
        paths = staged_markdown(root)
    elif args.all_lessons:
        paths = lesson_markdown(root)
    else:
        paths = resolve_paths(root, args.paths)

    if not paths:
        print("Render audit: no Markdown files selected.")
        return 0

    all_errors: list[str] = []
    all_notices: list[str] = []

    for path in sorted(dict.fromkeys(paths)):
        errors, notices = scan_file(path)
        all_errors.extend(errors)
        all_notices.extend(notices)

    print(f"Render audit files: {len(set(paths))}")
    print(f"Errors: {len(all_errors)}")
    print(f"Notices: {len(all_notices)}")

    if all_errors:
        print("\nERRORS")
        for item in all_errors:
            print(f"- {item}")

    if all_notices:
        print("\nNOTICES (manual verification)")
        for item in all_notices:
            print(f"- {item}")

    if all_errors:
        print("\nFAIL — fix source-level rendering hazards before commit.")
        return 1

    print("\nPASS — source-level render checks passed.")
    print(
        "MANDATORY NEXT GATE for rendered/visual changes: push the branch and inspect "
        "the actual GitHub Preview before merging."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
