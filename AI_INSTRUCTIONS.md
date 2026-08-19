# AI Tutor Instructions — Read This First

This file is the mandatory entry point for any AI that teaches, edits, audits, or extends this repository.

## Rule 0: never rely on chat history as the source of truth

The repository is the persistent memory. Chat history is optional context.

Before creating educational content, you MUST:

1. Read `docs/LEARNING_SYSTEM.md`.
2. Read `STATE.md`.
3. Read the target track's `README.md`, `ROADMAP.md`, `PROGRESS.md`, `CONCEPTS.md`, `EXAMPLES.md`, and `REFERENCES.md`.
4. Recursively inspect the target track's existing lessons, exercises, projects, and research notes.
5. Read `docs/CROSS_TRACK_INDEX.md` when the proposed material may overlap another track.
6. Identify what has already been taught, at what depth, with which examples, and what the roadmap says should come next.
7. Only then propose or create new material.

If you do not have filesystem/repository access, do **not** pretend that you inspected it. Tell the user that repository access or the relevant files are required before continuity-sensitive work can be trusted.

## Non-negotiable constraints

- Every track begins at absolute zero assumed domain knowledge.
- No track has a fixed lesson count or artificial stopping point.
- Every track must remain extendable through graduate study and current research.
- Do not repeat a concept at the same depth just to fill a lesson.
- Do not reuse an example when a different example can test the same idea, unless deliberate comparison is pedagogically necessary.
- Repetition for **deeper treatment**, **retrieval practice**, **contrast**, or **cross-domain transfer** is allowed, but it must be labeled as such.
- Never call a track "complete" simply because its current roadmap is exhausted. Run a coverage audit first.
- Never invent citations, commands, APIs, standards, paper results, or historical claims.
- For version-sensitive software and research-frontier material, verify current primary sources before writing.
- Prefer primary/official sources for technical facts and original papers for research claims.
- Educational prose must sound like a careful human author, not a generic chatbot transcript.

## Before writing a lesson

You must be able to answer, from repository evidence:

- What is the learner assumed to know?
- What exact concepts are already covered?
- What is the intended new depth?
- Why is this the next useful lesson?
- Which concept IDs will be introduced or deepened?
- Which examples have already been used?
- What prerequisites and cross-track links exist?
- What authoritative references support the material?

If any answer is unknown, resolve it before drafting.

## After writing a lesson

Update, at minimum:

- the track `PROGRESS.md`;
- the track `CONCEPTS.md`;
- the track `EXAMPLES.md` if examples were added;
- the track `REFERENCES.md` if sources were added;
- the track `ROADMAP.md` if sequencing or scope changed;
- root `STATE.md`;
- root `README.md` only when its high-level status/progress information changes.

Run `python scripts/repo_audit.py` if execution is available.

## Canonical standard

Everything else — curriculum depth, lesson structure, writing style, exercises, research progression, gap audits, metadata, naming, and handoff rules — is defined in:

**`docs/LEARNING_SYSTEM.md`**

If another file conflicts with it, `docs/LEARNING_SYSTEM.md` wins unless the user explicitly changes the policy.
