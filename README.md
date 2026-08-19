# Computer Science Foundations

**A self-directed, AI-assisted curriculum from first principles to research frontiers.**

This repository is not a pile of notes and it is not a fixed-length course. It is a living learning system: every subject begins with zero assumed knowledge, develops through undergraduate and graduate depth, and remains open at the research frontier.

> **Current state:** curriculum foundation rebuilt; lesson content intentionally reset.

## Tracks

| # | Track | Status | Entry point |
|---|---|---|---|
| 01 | Linear Algebra | Scaffolded | [`01-Linear-Algebra/README.md`](01-Linear-Algebra/README.md) |
| 02 | Linux Systems | Reset / Scaffolded | [`02-Linux-Systems/README.md`](02-Linux-Systems/README.md) |
| 03 | C++ | Scaffolded | [`03-CPP/README.md`](03-CPP/README.md) |
| 04 | Computer Architecture | Scaffolded | [`04-Computer-Architecture/README.md`](04-Computer-Architecture/README.md) |
| 05 | Programming Parallel Processors | Scaffolded | [`05-Programming-Parallel-Processors/README.md`](05-Programming-Parallel-Processors/README.md) |
| 06 | Complex Analysis | Scaffolded | [`06-Complex-Analysis/README.md`](06-Complex-Analysis/README.md) |
| 07 | Computer Systems | Scaffolded | [`07-Computer-Systems/README.md`](07-Computer-Systems/README.md) |

## How this repository works

The repository has two layers:

1. **Learning content** inside each subject track.
2. **A learning protocol** that tells any AI tutor how to inspect existing work, avoid repetition, plan the next material, write lessons, audit gaps, and preserve continuity between unrelated chat sessions.

The canonical protocol is:

- [`AI_INSTRUCTIONS.md`](AI_INSTRUCTIONS.md) — short mandatory entry point for an AI tutor.
- [`docs/LEARNING_SYSTEM.md`](docs/LEARNING_SYSTEM.md) — the complete teaching, curriculum, continuity, and quality standard.
- [`STATE.md`](STATE.md) — repository-wide handoff state.
- [`docs/CROSS_TRACK_INDEX.md`](docs/CROSS_TRACK_INDEX.md) — prevents unnecessary duplication between overlapping subjects.
- [`templates/`](templates/) — canonical templates for lessons, roadmaps, progress ledgers, and research notes.

## Starting a new AI session

If the AI has access to this repository, the minimal instruction is:

> **Read `AI_INSTRUCTIONS.md`, inspect the repository as required there, and continue the track I name.**

Do not ask the AI to "just teach the next lesson" without the repository preflight. Continuity is a repository responsibility, not a chat-history responsibility.

## Depth model

Every track is expected to remain capable of progressing through:

`L0 Absolute beginner → L1 Foundations → L2 Core undergraduate → L3 Advanced undergraduate → L4 Graduate → L5 Research literacy → L6 Research frontier`

The research frontier is deliberately **open-ended**. A track is never declared permanently complete merely because it has accumulated many lessons.

## Design principles

- Start from zero without staying shallow.
- Explain mechanisms, not only procedures.
- Prefer coherent mental models over disconnected facts.
- Use varied examples, exercises, experiments, proofs, and projects where appropriate.
- Revisit concepts only when depth increases or a new context genuinely requires it.
- Keep claims traceable to canonical documentation, standards, textbooks, or primary research.
- Treat current research and fast-changing technical material as time-sensitive.
- Write for humans: precise, concrete, curious, and readable.
- Make progress visible and gaps auditable.

## Repository status

The previous Linux lesson sequence has intentionally not been carried into this scaffold. The next Linux curriculum should be rebuilt according to the same protocol as every other track, beginning from first principles and preserving a path all the way to systems research.

See [`STATE.md`](STATE.md) for the current handoff state.
