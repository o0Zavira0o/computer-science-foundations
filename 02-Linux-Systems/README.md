# Linux Systems

**Track ID:** `linux-systems`  
**Code:** `LNX`  
**Status:** scaffolded

This track contains no V3 lesson content yet. Its scope and detailed curriculum must be established by evidence-backed reconnaissance before lesson 0001.

## Human navigation

- [`CONTEXT.md`](CONTEXT.md) — fastest handoff for an AI or returning reader
- [`ROADMAP.md`](ROADMAP.md) — generated dependency roadmap
- [`PROGRESS.md`](PROGRESS.md) — generated curriculum publication progress
- [`LEARNER.md`](LEARNER.md) — generated learner progress
- [`CATALOG.md`](CATALOG.md) — generated lesson catalog
- [`CONCEPTS.md`](CONCEPTS.md) — generated concept ledger
- [`EXAMPLES.md`](EXAMPLES.md) — generated example ledger
- [`REFERENCES.md`](REFERENCES.md) — generated reference ledger

## Canonical machine state

- `TRACK.json`
- `CURRICULUM.json`
- `COVERAGE.json`
- `LEARNER_STATE.json`
- `registry/concepts.json`
- `registry/examples.json`
- `registry/references.json`

## Content directories

- `lessons/`
- `exercises/`
- `projects/`
- `research/`

## Before the first lesson

The track must first undergo curriculum reconnaissance and a coverage audit. The roadmap must not be filled from a single textbook/course or from model memory alone.

Run:

```bash
python scripts/csf.py context linux-systems
python scripts/csf.py next linux-systems
```

from the repository root.
