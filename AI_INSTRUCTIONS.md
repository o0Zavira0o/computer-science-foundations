# AI Tutor Instructions — Read This First

This is the mandatory entry point for any AI that teaches, edits, audits, or extends this repository.

## 1. Source of truth

The repository is persistent memory. Chat history is optional context.

Canonical machine-readable state is stored in JSON. Markdown files such as `ROADMAP.md`, `CONCEPTS.md`, `EXAMPLES.md`, `REFERENCES.md`, `PROGRESS.md`, `LEARNER.md`, `CATALOG.md`, and `CONTEXT.md` are human-readable views generated from canonical state and lesson metadata.

Never silently treat a generated Markdown view as newer than its canonical JSON source.

## 2. Normal-session preflight: targeted, not recursive

Before teaching or creating content:

1. Read `SYSTEM.json`.
2. Read `docs/LEARNING_SYSTEM.md`.
3. Read `STATE.json` or generated `STATE.md`.
4. Identify the target track from its `TRACK.json`.
5. Read the target track's `CONTEXT.md`.
6. Read the target track's canonical `CURRICULUM.json`, `COVERAGE.json`, `LEARNER_STATE.json`, and relevant registries under `registry/`.
7. Inspect only the lesson files that are relevant to the proposed next unit: direct prerequisites, recently completed units, linked cross-track material, and any lessons found by concept/example/reference IDs.

Do **not** recursively reread hundreds of lessons during an ordinary continuation session. Full recursive inspection is reserved for curriculum audits, migrations, duplicate investigations, or explicit repository-wide reviews.

If execution is available, the fastest bootstrap is:

```bash
python scripts/csf.py context <track-slug>
python scripts/csf.py next <track-slug>
# explicit views when needed:
python scripts/csf.py next-authoring <track-slug>
python scripts/csf.py next-study <track-slug>
```

## 3. Before a new lesson can be written

You must establish from repository evidence:

- the curriculum node to which the lesson belongs;
- why that node is ready now;
- all prerequisite nodes and whether they are satisfied;
- learner state when it is relevant, while keeping it separate from curriculum publication state;
- concept IDs already covered and their current depths;
- example signatures already used;
- authoritative references that support the lesson;
- whether any claim is version-sensitive;
- whether another track owns the canonical treatment;
- whether the target track has undergone the required evidence-backed coverage audit and has no unresolved coverage gaps.

If any of these are unknown, resolve them before drafting.

## 4. Non-negotiable teaching constraints

- Begin with zero assumed **subject-specific** knowledge and make all outside prerequisites explicit.
- Never hide a prerequisite. Resolve it with a bridge, a canonical cross-track node, or a clearly declared prerequisite.
- Do not keep a track permanently at foundation level.
- Do not impose a fixed lesson count or artificial endpoint.
- Do not repeat a concept at the same depth under a new title.
- Do not reuse examples accidentally.
- Deliberate retrieval, contrast, transfer, or deeper treatment is allowed when labeled by purpose.
- Treat the repository as a public learning resource first: authoring quality and prerequisite integrity must not depend on whether the repository owner personally read earlier lessons.
- A reader may enter through any lesson. Give concise orientation and explicit prerequisite links when direct entry would otherwise be confusing.
- Do not mark any learner as having demonstrated knowledge merely because a lesson exists.
- Do not confuse `next-authoring` (curriculum construction) with `next-study` (learner progression).
- Learner evidence must resolve to real lessons, exercises, projects, or research notes.
- Keep committed learner state non-sensitive because the repository is public.
- Do not invent citations, commands, APIs, standards, paper results, benchmark results, or historical claims.
- Verify version-sensitive technical material against current primary/official sources.
- Verify research-frontier claims against current primary literature.
- Write like a careful human technical author, not a chatbot transcript.
- Prefer interactive prediction, reveal/check blocks, small experiments, diagrams, and visual models when they materially improve understanding; do not add visual clutter merely to decorate a page.
- When physical appearance or spatial form is part of understanding (for example hardware, machinery, a laboratory apparatus, a mechanical component, or a geometric construction), consider one verified static visual anchor. Embed it when a stable, correctly licensed source is available; cite the exact source page, author/organization, and license nearby; register lesson-critical figures in the track reference registry. If reliable embedding is impossible, give a precise Visual lookup instruction instead. Never use a merely plausible image without verifying that it depicts the described object.
- Render mathematics using the stricter GitHub-safe house style in `docs/MATH_RENDERING.md`: `$...$` for inline math and one physical source line `$$ ... $$` for lesson display math by default. Preserve matrix/alignment LaTeX inside that line, never leave a bare relation/operator on its own Markdown line, and verify math in the actual GitHub Preview rather than trusting delimiter scans alone.
- All repository filenames, structural documentation, and educational prose are written in English. Target-language examples (for example German sentences) remain in the target language, with English explanation where needed.

## 5. After changing content or canonical state

Update the canonical JSON first, then synchronize generated views:

```bash
python scripts/csf.py sync
python scripts/csf.py audit
python scripts/csf.py audit --strict  # before merge/push when warnings should block
```

For a normal lesson session this commonly means updating:

- the lesson file;
- `CURRICULUM.json`;
- `registry/concepts.json`;
- `registry/examples.json` when needed;
- `registry/references.json` when needed;
- `COVERAGE.json` if coverage mapping changed;
- `LEARNER_STATE.json` **only** when the learner actually studied/practiced/demonstrated something;
- root `STATE.json` if repository-wide handoff state changed.

If execution is unavailable, do not pretend generated views are synchronized. Modify canonical files carefully and tell the user that `python scripts/csf.py sync && python scripts/csf.py audit` must be run.

## 6. Canonical standard

The complete architecture, pedagogy, retrieval protocol, completeness policy, quality standard, research policy, and writeback contract are defined in:

**`docs/LEARNING_SYSTEM.md`**

If another file conflicts with it, `docs/LEARNING_SYSTEM.md` wins unless the user explicitly changes the policy.
