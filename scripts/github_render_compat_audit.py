#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OPERATOR_RE = re.compile(r"\\operatorname\s*\{([^{}]+)\}")
PHANTOM_RE = re.compile(r"\\phantom\s*\{")
BRACKET_LABEL_RE = re.compile(r"\[([^\]\n]*)\]")


def git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.stdout.rstrip("\n")


def strip_inline_code(line: str) -> str:
    out = []
    i = 0
    n = len(line)

    while i < n:
        if line[i] != "`":
            out.append(line[i])
            i += 1
            continue

        j = i
        while j < n and line[j] == "`":
            j += 1

        ticks = line[i:j]
        close = line.find(ticks, j)

        if close == -1:
            out.append(line[i:])
            break

        i = close + len(ticks)

    return "".join(out)


def fence_info(stripped: str):
    for marker in ("```", "~~~"):
        if stripped.startswith(marker):
            rest = stripped[len(marker):].strip()
            lang = rest.split()[0].lower() if rest else ""
            return marker, lang
    return None


def audit_text(
    text: str,
    display_name: str,
) -> list[str]:
    lines = text.splitlines()
    errors = []

    fence_marker = None
    fence_lang = ""

    for line_no, line in enumerate(lines, 1):
        stripped = line.strip()

        if fence_marker is None:
            info = fence_info(stripped)

            if info is not None:
                fence_marker, fence_lang = info
                continue

            visible = strip_inline_code(line)

            for match in OPERATOR_RE.finditer(visible):
                errors.append(
                    f"{display_name}:{line_no}: unsupported GitHub "
                    f"math macro {match.group(0)!r}; "
                    r"use a supported alternative such as \mathrm{...}"
                )

            for _ in PHANTOM_RE.finditer(visible):
                errors.append(
                    f"{display_name}:{line_no}: unsupported GitHub "
                    r"math macro '\phantom{...}'; "
                    "remove layout-only phantom spacing"
                )

            continue

        if stripped.startswith(fence_marker):
            fence_marker = None
            fence_lang = ""
            continue

        if fence_lang == "math":
            for match in OPERATOR_RE.finditer(line):
                errors.append(
                    f"{display_name}:{line_no}: unsupported GitHub "
                    f"math macro {match.group(0)!r} inside fenced math"
                )

            for _ in PHANTOM_RE.finditer(line):
                errors.append(
                    f"{display_name}:{line_no}: unsupported GitHub "
                    r"math macro '\phantom{...}' inside fenced math"
                )

        elif fence_lang == "mermaid":
            for match in BRACKET_LABEL_RE.finditer(line):
                label = match.group(1).strip()

                if "|" not in label:
                    continue

                quoted = (
                    len(label) >= 2
                    and (
                        (
                            label.startswith('"')
                            and label.endswith('"')
                        )
                        or (
                            label.startswith("'")
                            and label.endswith("'")
                        )
                    )
                )

                if not quoted:
                    errors.append(
                        f"{display_name}:{line_no}: raw pipe inside "
                        "unquoted Mermaid node label"
                    )

    return errors


def audit(path: Path) -> list[str]:
    return audit_text(
        path.read_text(),
        str(path.relative_to(ROOT)),
    )


def self_test() -> None:
    cases = [
        (
            "safe inline literal",
            r"Example literals: `\operatorname{...}` and `\phantom{x}`",
            0,
        ),
        (
            "safe normal fenced code",
            "```text\n"
            r"\operatorname{count}(x)"
            "\n"
            r"\phantom{x}"
            "\n```\n",
            0,
        ),
        (
            "bad display math",
            r"$$ \operatorname{count}(x)=1 $$" + "\n",
            1,
        ),
        (
            "bad display phantom",
            r"$$ \phantom{x} y = 1 $$" + "\n",
            1,
        ),
        (
            "bad fenced math",
            "```math\n"
            r"\operatorname{count}(x)=1"
            "\n```\n",
            1,
        ),
        (
            "bad fenced phantom",
            "```math\n"
            r"\phantom{x}y=1"
            "\n```\n",
            1,
        ),
        (
            "bad Mermaid",
            "```mermaid\n"
            "flowchart TD\n"
            "A[P token | context]\n"
            "```\n",
            1,
        ),
        (
            "safe Mermaid",
            "```mermaid\n"
            "flowchart TD\n"
            'A["P(token given context)"]\n'
            "```\n",
            0,
        ),
    ]

    for name, text, expected in cases:
        actual = len(
            audit_text(
                text,
                f"<self-test:{name}>",
            )
        )

        if actual != expected:
            raise RuntimeError(
                f"self-test failed for {name!r}: "
                f"expected {expected}, got {actual}"
            )


def all_markdown() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md")
        if ".git" not in p.parts
    )


def staged_markdown() -> list[Path]:
    output = git(
        "diff",
        "--cached",
        "--name-only",
        "--diff-filter=ACMR",
    )

    files = []

    for raw in output.splitlines():
        if not raw.endswith(".md"):
            continue

        path = ROOT / raw

        if path.is_file():
            files.append(path)

    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--staged",
        action="store_true",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
    )
    parser.add_argument(
        "paths",
        nargs="*",
    )
    args = parser.parse_args()

    if args.staged and args.paths:
        parser.error(
            "--staged cannot be combined with explicit paths"
        )

    try:
        self_test()
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 2

    if args.self_test:
        print(
            "GitHub render-compat auditor self-test: PASS"
        )
        return 0

    if args.staged:
        files = staged_markdown()
    elif args.paths:
        files = []

        for raw in args.paths:
            path = (ROOT / raw).resolve()

            if path.is_file() and path.suffix == ".md":
                files.append(path)
    else:
        files = all_markdown()

    errors = []

    for path in files:
        errors.extend(
            audit(path)
        )

    print(
        "GitHub render-compat auditor self-test: PASS"
    )
    print(
        f"GitHub render-compat audit files: {len(files)}"
    )
    print(
        f"Errors: {len(errors)}"
    )

    if errors:
        print("\nErrors:")

        for error in errors:
            print(f"  - {error}")

        return 1

    print(
        "\nPASS — GitHub render-compat checks passed."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
