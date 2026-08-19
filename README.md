# Computer Science Foundations

**A self-directed, AI-assisted curriculum from first principles to research frontiers.**

This repository is designed as a durable learning system rather than a pile of notes or a fixed-length course. Each subject starts with zero assumed subject-specific knowledge, makes outside prerequisites explicit, develops through undergraduate and graduate depth, and stays open at the research frontier.

> **System version:** V3.1 — architecture frozen for normal content work
> **Active starts:** Linux Systems, German Language, and Large Language Models now have audited curriculum spines and their first published lessons. Learner mastery remains unclaimed until study evidence is recorded.

## Tracks

The track list is generated from machine-readable manifests:

**[`docs/TRACKS.md`](docs/TRACKS.md)**

Current tracks include Linear Algebra, Linux Systems, C++, Computer Architecture, Programming Parallel Processors, Complex Analysis, Computer Systems, and Large Language Models (LLMs). The `09-Auxiliary-Studies/` container groups independent tracks for Advanced English, German Language, and Philosophy and Logic. New top-level or nested tracks can be added without editing the audit script.

## First published learning paths

- **Linux Systems:** [`LNX-0001 — What a Linux system actually is`](02-Linux-Systems/lessons/LNX-0001-what-a-linux-system-actually-is.md)
- **German Language:** [`GER-0001 — Sounds, spelling, and your first German utterances`](09-Auxiliary-Studies/02-German-Language/lessons/GER-0001-sounds-spelling-and-your-first-german-utterances.md)
- **Large Language Models:** [`LLM-0001 — What a language model is`](08-Large-Language-Models/lessons/LLM-0001-what-a-language-model-is.md)

Each active track has an evidence-backed `RECONNAISSANCE.md`, an audited `COVERAGE.json`, and a dependency-ordered `CURRICULUM.json`. These spines are not fixed endpoints; they are the current auditable map.

## What makes this repository different

The repository separates four things that are often accidentally mixed together:

1. **Curriculum design** — what should be taught and in what dependency order.
2. **Published learning content** — the Markdown lessons, exercises, projects, and research notes.
3. **Learner state** — what the repository owner has actually read, practiced, demonstrated, or needs to review.
4. **Generated navigation** — roadmaps, catalogs, context packs, concept/example/reference ledgers, and progress views.

Canonical structured state is JSON; educational prose stays in clean Markdown.

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
