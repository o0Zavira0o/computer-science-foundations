# Computer Science Foundations

**A self-directed, AI-assisted curriculum from first principles to research frontiers.**

This repository is designed as a durable learning system rather than a pile of notes or a fixed-length course. Each subject starts with zero assumed subject-specific knowledge, makes outside prerequisites explicit, develops through undergraduate and graduate depth, and stays open at the research frontier.

> **System version:** V3.1 — architecture frozen for normal content work
> **Active starts:** Linear Algebra, Linux Systems, German Language, Large Language Models, Philosophy and Logic, Fusion Energy, and Electrical Engineering — Power Engineering have audited curriculum spines and published lessons. Learner mastery remains separate from publication state.

## Tracks

The track list is generated from machine-readable manifests:

**[`docs/TRACKS.md`](docs/TRACKS.md)**

The generated index is the authoritative human-readable track inventory. Active published tracks currently include Linear Algebra, Linux Systems, Large Language Models, German Language, Philosophy and Logic, Fusion Energy, and Electrical Engineering — Power Engineering. Scaffolded tracks remain visible in the generated index without being misrepresented as already published.

## Published learning paths and current publication snapshot

Publication state is not learner mastery. The table below is a repository handoff snapshot after this content transaction; generated `CATALOG.md` and `PROGRESS.md` files remain the detailed per-track views.

| Track | Start here | Published through |
|---|---|---|
| Linear Algebra | [`LA-0001`](01-Linear-Algebra/lessons/LA-0001-what-linear-algebra-is-actually-studying.md) | [`LA-0004 — Vector addition and scalar multiplication`](01-Linear-Algebra/lessons/LA-0004-vector-addition-and-scalar-multiplication.md) |
| Linux Systems | [`LNX-0001`](02-Linux-Systems/lessons/LNX-0001-what-a-linux-system-actually-is.md) | [`LNX-0010 — Standard streams, redirection, and pipelines`](02-Linux-Systems/lessons/LNX-0010-standard-streams-redirection-and-pipelines.md) |
| German Language | [`GER-0001`](09-Auxiliary-Studies/02-German-Language/lessons/GER-0001-sounds-spelling-and-your-first-german-utterances.md) | `GER-0001` |
| Large Language Models | [`LLM-0001`](08-Large-Language-Models/lessons/LLM-0001-what-a-language-model-is.md) | [`LLM-0005 — Vectors and dot products as similarity and scoring`](08-Large-Language-Models/lessons/LLM-0005-vectors-and-dot-products-as-similarity-and-scoring.md) |
| Philosophy and Logic | [`PHL-0001`](09-Auxiliary-Studies/03-Philosophy-and-Logic/lessons/PHL-0001-what-philosophy-and-logic-are-actually-doing.md) | [`PHL-0004 — Truth, validity, and soundness`](09-Auxiliary-Studies/03-Philosophy-and-Logic/lessons/PHL-0004-truth-validity-and-soundness.md) |
| Fusion Energy | [`FUS-0001`](09-Auxiliary-Studies/04-Fusion-Energy/lessons/FUS-0001-what-fusion-energy-is-actually-trying-to-achieve.md) | [`FUS-0004 — Coulomb repulsion, collision energy, and quantum tunneling`](09-Auxiliary-Studies/04-Fusion-Energy/lessons/FUS-0004-coulomb-repulsion-collision-energy-and-quantum-tunneling.md) |
| Electrical Engineering — Power Engineering | [`PWR-0001`](09-Auxiliary-Studies/05-Electrical-Engineering-Power-Engineering/lessons/PWR-0001-what-electrical-power-engineering-is-actually-studying.md) | [`PWR-0004 — Reference directions, signs, and passive-versus-active power`](09-Auxiliary-Studies/05-Electrical-Engineering-Power-Engineering/lessons/PWR-0004-reference-directions-signs-and-passive-versus-active-power.md) |
| Neurotechnology & Neural Engineering | [`NNE-0001`](09-Auxiliary-Studies/06-Neurotechnology-Neural-Engineering/lessons/NNE-0001-what-neurotechnology-and-neural-engineering-are-actually-studying.md) | [`NNE-0001 — What neurotechnology and neural engineering are actually studying`](09-Auxiliary-Studies/06-Neurotechnology-Neural-Engineering/lessons/NNE-0001-what-neurotechnology-and-neural-engineering-are-actually-studying.md) |

For exact current authoring and learner next actions, run `python scripts/csf.py next <track-slug>`. Each active track has an evidence-backed `RECONNAISSANCE.md`, audited `COVERAGE.json`, dependency-ordered `CURRICULUM.json`, and generated progress/catalog/context views.

## What makes this repository different

The repository separates four things that are often accidentally mixed together:

1. **Curriculum design** — what should be taught and in what dependency order.
2. **Published learning content** — the Markdown lessons, exercises, projects, and research notes.
3. **Learner state** — what the repository owner has actually read, practiced, demonstrated, or needs to review.
4. **Generated navigation** — roadmaps, catalogs, context packs, concept/example/reference ledgers, and progress views.

Canonical structured state is JSON; educational prose stays in clean Markdown.


## Public reading model

The repository is designed for non-linear public reading as well as sequential study. A visitor may arrive at any lesson from search or a direct link; lessons therefore expose genuine prerequisites, give concise local orientation, and avoid depending on the repository owner's personal learner state. Visuals and interactive checks are used selectively when they improve understanding.

## Starting a new AI session

If the AI can access this repository, the minimal instruction is:

> **Read `AI_INSTRUCTIONS.md`, inspect the target track using the V3 targeted-retrieval protocol, and continue the track I name.**

A normal session should not reread every lesson. The repository maintains compact context and registries so an AI can retrieve only what matters.

If command execution is available:

```bash
python scripts/csf.py context <track-slug>
python scripts/csf.py next <track-slug>
# or explicitly:
python scripts/csf.py next-authoring <track-slug>
python scripts/csf.py next-study <track-slug>
```

## Integrity checks

Run locally:

```bash
python scripts/csf.py sync
python scripts/csf.py audit
python scripts/csf.py audit --strict   # merge/CI gate
python -m unittest discover -s tests -v
# after architecture changes only:
python scripts/stress_test.py
```

The same audit runs automatically on GitHub through GitHub Actions.

The audit checks more than file existence: dynamic track discovery, unique IDs, curriculum dependencies, graph cycles, lesson-to-node consistency, concept/example/reference references, learner-state references, coverage prerequisites, generated-view drift, internal Markdown links, and staleness warnings for explicitly time-sensitive material.

## Depth model

`L0 Absolute beginner → L1 Foundations → L2 Core undergraduate → L3 Advanced undergraduate → L4 Graduate → L5 Research literacy → L6 Research frontier`

L6 is deliberately open-ended. A track is never permanently declared complete because a numbered list ended.

## Key documents

- [`AI_INSTRUCTIONS.md`](AI_INSTRUCTIONS.md) — mandatory AI entry point.
- [`docs/LEARNING_SYSTEM.md`](docs/LEARNING_SYSTEM.md) — canonical teaching and architecture standard.
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — source-of-truth map and data flow.
- [`docs/LEARNING_SCIENCE.md`](docs/LEARNING_SCIENCE.md) — rationale for retrieval, spacing, worked examples, self-explanation, and interleaving.
- [`docs/MATH_RENDERING.md`](docs/MATH_RENDERING.md) — GitHub-safe mathematical notation and equation rendering standard.
- [`STATE.md`](STATE.md) — generated repository handoff view.
- [`docs/TRACKS.md`](docs/TRACKS.md) — generated track index.
- [`docs/CROSS_TRACK_INDEX.md`](docs/CROSS_TRACK_INDEX.md) — generated cross-track relationship index.
- [`docs/FILE_PACKAGE_WORKFLOW.md`](docs/FILE_PACKAGE_WORKFLOW.md) — exact ZIP-to-repository placement workflow for future AI-delivered files.

## Design principles

- Start from zero without staying shallow.
- Make prerequisite closure explicit.
- Explain mechanisms, not only procedures.
- Prefer coherent mental models over disconnected facts.
- Use varied examples, counterexamples, exercises, experiments, proofs, and projects where appropriate.
- Distinguish curriculum publication from learner mastery.
- Revisit concepts only for a declared pedagogical reason.
- Keep claims traceable to authoritative sources.
- Treat current research and fast-changing technology as time-sensitive.
- Write for humans: precise, concrete, readable, and worth continuing.
- Keep repository filenames, structural documentation, and educational content in English; conversational guidance outside the repository may use the user's preferred language.
- Keep gaps, uncertainty, and stale material visible rather than hiding them.

## Learner-state privacy

The default `LEARNER_STATE.json` files describe the repository owner's learning progression and are committed for cross-session continuity. Because this repository is public, they must contain only non-sensitive learning metadata. People following the curriculum should fork the repository or maintain their own learner profile/state rather than treating the owner's progress as their own.

## License and attribution

Educational material and documentation are licensed under **CC BY-SA 4.0**. Repository software under `scripts/`, `tests/`, `.github/workflows/`, and `schemas/` is licensed under **GPL-3.0-or-later**. See [`LICENSE`](LICENSE), [`ATTRIBUTION.md`](ATTRIBUTION.md), and [`NOTICE.md`](NOTICE.md).

The requested project credit is **Computer Science Foundations — o0Zavira0o**, with a link back to this repository and an indication of changes when material is adapted.
