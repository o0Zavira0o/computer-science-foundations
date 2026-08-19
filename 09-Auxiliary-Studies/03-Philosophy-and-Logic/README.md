# Philosophy and Logic

**Track ID:** `philosophy-and-logic`
**Code:** `PHL`
**Status:** active

This track has an evidence-backed reconnaissance baseline, an audited dependency graph, and published learning content. The curriculum spine is extensible rather than a fixed endpoint.

## Start reading

- **First published lesson:** [PHL-0001 — What philosophy and logic are actually doing](lessons/PHL-0001-what-philosophy-and-logic-are-actually-doing.md)
- [`CONTEXT.md`](CONTEXT.md) — compact AI/reader handoff
- [`ROADMAP.md`](ROADMAP.md) — dependency-ordered curriculum roadmap
- [`PROGRESS.md`](PROGRESS.md) — publication state
- [`CATALOG.md`](CATALOG.md) — published lesson catalog
- [`CONCEPTS.md`](CONCEPTS.md) — concept registry view
- [`EXAMPLES.md`](EXAMPLES.md) — example registry view
- [`REFERENCES.md`](REFERENCES.md) — evidence/reference registry view
- [`RECONNAISSANCE.md`](RECONNAISSANCE.md) — curriculum-baseline rationale

## Public reading model

Readers may enter through any lesson, not only from lesson 0001. Each lesson therefore states genuine prerequisites and provides enough local orientation for direct entry without re-teaching earlier material at the same depth.

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

From the repository root:

```bash
python scripts/csf.py context philosophy-and-logic
python scripts/csf.py next philosophy-and-logic
```
