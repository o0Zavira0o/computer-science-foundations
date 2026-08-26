# Fusion Energy

Track ID: `fusion-energy`
Code: `FUS`
Status: active

This independent Auxiliary Studies track develops fusion-energy literacy from zero subject-specific knowledge through plasma and nuclear foundations, confinement physics, reactor engineering, whole-plant energy accounting, computational methods, and research-frontier work.

The track is deliberately broader than “how a tokamak works.” A fusion reaction, a high-gain plasma or target, an integrated reactor, and a net-electric power plant are different system boundaries. The curriculum keeps those boundaries explicit from lesson one.

## Start reading

- First published lesson: [`FUS-0001 — What fusion energy is actually trying to achieve`](lessons/FUS-0001-what-fusion-energy-is-actually-trying-to-achieve.md)
- `CONTEXT.md` — compact AI/reader handoff generated from canonical state
- `ROADMAP.md` — dependency-ordered curriculum roadmap
- `PROGRESS.md` — curriculum publication state
- `CATALOG.md` — published lesson catalog
- `CONCEPTS.md` — generated concept registry view
- `EXAMPLES.md` — generated example registry view
- `REFERENCES.md` — generated evidence/reference registry view
- [`RECONNAISSANCE.md`](RECONNAISSANCE.md) — curriculum-baseline rationale

## Canonical machine state

- `TRACK.json`
- `CURRICULUM.json`
- `COVERAGE.json`
- `LEARNER_STATE.json`
- `registry/concepts.json`
- `registry/examples.json`
- `registry/references.json`
- `research/FRONTIER.json`

Published curriculum content is not automatically learner knowledge; `LEARNER_STATE.json` remains independent.

From the repository root:

```bash
python scripts/csf.py context fusion-energy
python scripts/csf.py next fusion-energy
```
