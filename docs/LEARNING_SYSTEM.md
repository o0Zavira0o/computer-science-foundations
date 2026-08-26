# Learning System Specification

**Status:** canonical
**Architecture:** V3.1
**Purpose:** define how this repository is taught, extended, audited, and handed between independent AI sessions.

---

## 1. Mission

This repository is a long-lived curriculum, not a transcript and not a finite tutorial series.

Its goal is to let a learner enter a subject with zero assumed subject-specific knowledge, make all outside prerequisites visible, and progress without an artificial ceiling toward:

- operational competence;
- formal understanding;
- implementation or problem-solving fluency;
- advanced undergraduate depth;
- graduate specialization;
- research literacy;
- current research questions and open problems.

An AI tutor has four roles at once:

1. **Teacher** — explain, challenge, diagnose, and adapt.
2. **Curriculum designer** — sequence dependencies and keep gaps visible.
3. **Editor** — protect accuracy, coherence, readability, and human voice.
4. **Librarian** — preserve structured evidence of what exists and what the learner has actually done.

The repository, not chat memory, is the durable continuity layer.

---

## 2. One source of truth

V3 separates canonical structured state from human-readable views.

Canonical JSON:

- `SYSTEM.json`
- `STATE.json`
- each `TRACK.json`
- each `CURRICULUM.json`
- each `COVERAGE.json`
- each `LEARNER_STATE.json`
- each `registry/concepts.json`
- each `registry/examples.json`
- each `registry/references.json`

Educational prose remains Markdown.

Generated Markdown views include:

- `STATE.md`
- `docs/TRACKS.md`
- `docs/CROSS_TRACK_INDEX.md`
- each `ROADMAP.md`
- each `PROGRESS.md`
- each `LEARNER.md`
- each `CONCEPTS.md`
- each `EXAMPLES.md`
- each `REFERENCES.md`
- each `CATALOG.md`
- each `CONTEXT.md`

When a view and canonical JSON disagree, the JSON wins and the view must be regenerated.

Run:

```bash
python scripts/csf.py sync
python scripts/csf.py audit
```

---

## 3. Session modes

### 3.1 Normal continuation mode

The default is targeted retrieval.

Read:

1. `AI_INSTRUCTIONS.md`
2. `SYSTEM.json`
3. this specification
4. `STATE.json` or `STATE.md`
5. target `CONTEXT.md`
6. target canonical graph/state/registries
7. only relevant lesson files

Relevant lessons normally include:

- direct prerequisite units;
- recently studied units;
- lessons that own a concept the proposed unit will deepen or use;
- lessons that contain a similar registered example;
- cross-track canonical explanations.

Do not recursively reread the whole track merely because it exists.

### 3.2 Audit mode

Recursive inspection is appropriate for:

- first curriculum reconnaissance;
- major coverage audits;
- suspected semantic duplication;
- migration;
- research-frontier refresh;
- long-paused tracks;
- repository-wide quality reviews.

### 3.3 Research-refresh mode

Research-frontier work additionally requires current web/literature verification and dated freshness state.

---

## 4. Depth ladder

### L0 — Absolute beginner / orientation

Assume no subject-specific vocabulary, notation, tools, or mental model.

Goals:

- map the field;
- establish language;
- build first mental models;
- become safely operational where tools are involved;
- expose prerequisites rather than hiding them.

L0 is an entry ramp, not the destination.

### L1 — Foundations

Goals:

- core objects, mechanisms, conventions;
- reliable basic problem solving;
- first nontrivial examples;
- debugging/error-analysis habits;
- enough vocabulary to read introductory references.

### L2 — Core undergraduate

Goals:

- canonical theories and tools;
- derivations/mechanisms where appropriate;
- broader problem classes;
- multiple representations;
- integration among earlier concepts;
- meaningful exercises and small projects.

### L3 — Advanced undergraduate / systems integration

Goals:

- edge cases;
- performance and complexity;
- internals;
- design tradeoffs;
- larger proofs, implementations, experiments, or systems studies;
- alternative methods;
- deeper failure analysis.

### L4 — Graduate / specialization

Goals:

- specialist formalism;
- advanced subareas;
- advanced standards/literature;
- reproduction of established results where feasible;
- research-grade methodology;
- neighboring-discipline connections.

### L5 — Research literacy

Goals:

- read papers critically;
- reconstruct assumptions;
- identify baselines and contributions;
- evaluate evidence;
- distinguish demonstrated results from speculation;
- reproduce or benchmark when feasible;
- understand limitations and conflicting work.

### L6 — Research frontier

Goals:

- current primary literature;
- active debates;
- recent techniques;
- open problems;
- reproducible exploration;
- original research questions.

**L6 is open-ended and must be refreshed over time.**

---

## 5. Prerequisite closure

"Starts from zero" does not mean pretending neighboring knowledge is unnecessary.

It means no prerequisite may remain hidden.

An outside prerequisite must be resolved as one of:

- **bridge** — taught inside the track before it is needed;
- **canonical cross-track dependency** — linked to an existing curriculum node elsewhere;
- **declared external prerequisite** — stated explicitly with rationale.

A reader must never discover halfway through a lesson that an unstated course in calculus, C++, shell usage, probability, or architecture was assumed.

Prerequisite closure is checked during roadmap reconnaissance and coverage audit.

---

## 6. Curriculum graph

`CURRICULUM.json` is canonical.

A curriculum node represents a teachable dependency unit. It may later correspond to one lesson or, if justified, a tightly connected learning unit.

Each node records:

- `id`
- `title`
- `level`
- `status`
- `prerequisites`
- `outcomes`
- `target_concepts`
- optional `branch`
- optional `lesson_id`

Allowed node statuses:

- `planned`
- `ready`
- `drafting`
- `published`
- `deprecated`

The audit:

- rejects duplicate node IDs;
- resolves cross-track prerequisites;
- rejects self-dependencies;
- rejects dependency cycles;
- verifies published node ↔ lesson consistency.

Do not store `unlocks`; derive them from reverse prerequisite edges.

Lesson count is an implementation detail. Do not create filler to hit a round number, and do not stop because a round number was reached.

---

## 7. Curriculum reconnaissance and completeness

No finite roadmap proves that an evolving discipline is complete.

`COVERAGE.json` therefore stores a coverage baseline.

### 7.1 Baseline construction

Before the first published lesson of an activated track, compare the proposed roadmap against multiple relevant classes such as:

- respected university sequences;
- canonical textbooks;
- official documentation;
- standards/specifications;
- language/hardware specifications;
- seminal papers;
- strong surveys/reviews;
- current primary research where frontier coverage matters.

No single textbook, certification, or university course defines an entire field.

### 7.2 Coverage items

Each important external expectation becomes a coverage item mapped to curriculum nodes.

Allowed states:

- `planned`
- `covered`
- `gap`
- `deferred`

A `deferred` item requires rationale.

### 7.3 Audit questions

Ask:

1. Which canonical areas are absent?
2. Which concepts exist only at shallow depth?
3. Which prerequisites are hidden or unresolved?
4. Which capabilities have theory but no practice?
5. Which tools are taught without mechanisms?
6. Which mechanisms lack measurement/evidence?
7. Which advanced topics lack research bridges?
8. Which references are stale?
9. Which concepts are duplicated?
10. Which examples are overused?
11. Which cross-track ownership decisions are unclear?
12. Which claims lack adequate support?
13. Which branches of the field were silently ignored?

Record gaps instead of hiding them.

---

## 8. Concept registry

Canonical file: `registry/concepts.json`.

Each concept should have a stable ID, human name, aliases where useful, current curriculum depth, and ownership information. `current_depth` is derived from published curriculum-node targets and must agree with that derivation; it is `null` before the concept has published coverage.

Recommended ID style:

`<TRACK>-<AREA>-<NUMBER>`

Coverage depth:

- **D0 — Named**
- **D1 — Intuitive**
- **D2 — Operational**
- **D3 — Mechanistic/Formal**
- **D4 — Advanced**
- **D5 — Research**

If a concept already exists at D2, restating D2 under a different title is duplication. Advancing it to D3 may be necessary.

The audit can detect exact ID/title/alias collisions. Semantic near-duplicates still require AI/human judgment during audits.

---

## 9. Example registry

Canonical file: `registry/examples.json`.

Register substantial worked examples, labs, proof examples, debugging scenarios, and recurring toy domains.

Before adding one, ask:

- has the exact example appeared?
- has this shape/domain been overused?
- would a different example expose another aspect?
- is deliberate reuse valuable for comparison or retrieval?

Prefer diversity across:

- minimal and realistic;
- normal and failure cases;
- synthetic and real-world;
- forward and reverse reasoning;
- hand-worked and tool-assisted;
- correctness, performance, and debugging;
- proofs and counterexamples where relevant.

Intentional reuse must declare a pedagogical purpose.

---

## 10. Reference registry and freshness

Canonical file: `registry/references.json`.

Lesson front matter uses stable reference IDs.

Prefer:

- canonical textbooks for established foundations;
- official documentation and standards for technical behavior;
- primary/original papers for research claims;
- high-quality surveys for synthesis.

Never fabricate bibliographic details.

### Version-sensitive material

If behavior depends on a current version, record the version/review date and set an explicit `review_after` when appropriate.

A source becoming old does not automatically make it invalid. Freshness warnings apply only to entries that declare themselves time-sensitive.

---

## 11. Learner state is not curriculum state

Canonical file: `LEARNER_STATE.json`.

A published lesson means the repository contains the material. It says nothing by itself about whether the learner knows it.

Recommended learner states:

- `unseen`
- `read`
- `practiced`
- `demonstrated`

A review can also be due after prior demonstration.

Learner state may record:

- last engagement date;
- confidence;
- evidence IDs;
- review due date;
- demonstrated concept depth.

Evidence IDs resolve to real lessons, exercises, projects, or research notes. Review-queue targets and dates are validated. Because learner state is committed to a public repository in the default owner profile, it must contain learning metadata only—never private notes, credentials, health data, or other sensitive personal information. A fork may replace the owner profile with its own.

Do not mark `demonstrated` merely because the learner says "I think I understand" or because the lesson exists.

Evidence should fit the subject: explanation, derivation, proof, prediction, debugging, implementation, benchmark, design justification, project, or research critique.

---

## 12. Learning-science defaults

Operational rationale is documented in `docs/LEARNING_SCIENCE.md`.

Default practices:

- retrieval rather than rereading alone;
- spaced review rather than massed repetition;
- worked examples for early unfamiliar skills, then fading;
- self-explanation prompts;
- selective interleaving after multiple methods are known;
- evidence-based mastery rather than familiarity.

Do not apply these mechanically when the discipline or learner state makes another approach more appropriate.

---

## 12.5 Public readership and non-linear entry

This repository is a public curriculum, not a private transcript of one learner's journey. Learner state is useful continuity metadata, but it must **not** become the editorial gate for curriculum authoring or lesson quality.

Assume that many readers will arrive from search, a direct link, or a random browse. A strong lesson therefore:

- identifies genuine prerequisites without forcing readers through irrelevant history;
- gives a short orientation when a direct-entry reader would otherwise be lost;
- links backward to canonical prerequisites rather than re-teaching them at the same depth;
- remains useful even when `LEARNER_STATE.json` belongs to somebody else or is empty;
- uses progressive disclosure so a casual reader can get the core model while a committed learner can continue into mechanism and active work.

### Visual and interactive material

Use visuals because they resolve a real explanatory bottleneck, not because every page needs artwork. Match the visual to the job:

1. use an equation or compact table when symbolic/comparative structure is clearest there;
2. use Mermaid for relationships, flows, state transitions, dependency structure, and system boundaries;
3. use a carefully chosen static image when the learner needs to know **what a physical object, component, apparatus, geometry, interface, or spatial construction actually looks like**.

Static images are selective teaching evidence, not decoration. Before embedding one:
- verify that the pictured object or geometry is actually the thing described in the surrounding prose;
- prefer an authoritative primary source or a traceable open-license repository such as Wikimedia Commons;
- use a stable direct-media URL for the embedded image and place the exact source-page URL, author/organization, and license in the nearby caption;
- register a lesson-critical external figure in the track reference registry and include its reference ID in lesson metadata;
- do not substitute a generic stock image when a precise technical figure is required;
- do not add several images where one accurate visual anchor is enough.

If a correct figure is genuinely necessary but cannot be embedded reliably, include an explicit **Visual lookup** instruction with an exact source page or a precise search phrase and tell the learner what feature to inspect. Embedding the verified figure is preferred when licensing and link stability allow it.

Interactive Markdown patterns such as `<details>` may reveal hints, checks, counterexamples, or optional derivations after the reader has had a chance to predict. Core prerequisites and essential explanations must remain visible without interaction.

A page can be excellent with no static image. A page with many decorative images can be worse than one precise, correctly sourced visual anchor.
### Mathematical notation and GitHub rendering

Mathematical notation is part of the teaching interface, not merely source text. Repository Markdown must use GitHub-supported math syntax so formulas render rather than leak LaTeX into the page.

House style:

- inline mathematics: `$...$`;
- simple standalone display mathematics: one physical source line using `$$ ... $$`, with blank lines around it;
- matrices, aligned derivations, `cases`, `array`, and any expression that depends on LaTeX row separators `\\`: fenced `math` blocks;
- never force row-sensitive LaTeX into one-line dollar display merely to satisfy a source-format preference;
- never leave a bare relation/operator such as `=`, `-`, `+`, `\neq`, or `\rightarrow` on an ordinary Markdown line outside a math container;
- backslash-parenthesis and backslash-bracket math delimiters are not used in repository Markdown;
- ordinary code fences are reserved for literal code/commands, not mathematical display.

A delimiter/source scan is necessary but not sufficient. Before publishing math-heavy content, push the candidate branch and visually inspect the **actual GitHub Preview**. Verify equations, matrix rows, aligned derivations, subscripts, superscripts, fractions, and symbols. In particular, a raw-source `\\` that collapses in Preview is a rendering failure and must be corrected before merge.

New notation must still be explained in prose. Rendering an expression beautifully does not make it pedagogically self-explanatory. For examples, edge cases, tables, and detailed compatibility guidance, see [`MATH_RENDERING.md`](MATH_RENDERING.md).

## 13. Anatomy of a strong lesson

Not every lesson needs identical headings, but a substantial lesson should accomplish this arc.

### 13.1 Motivation before machinery

Open with a real problem, phenomenon, contradiction, use case, or question.

Avoid empty hooks such as "X is very important in today's world."

### 13.2 Mental model

Give the learner something coherent to reason with before a wall of terminology.

Possible forms:

- invariant;
- data flow;
- state machine;
- geometric model;
- dependency structure;
- physical analogy with boundaries;
- diagram;
- small formal model.

### 13.3 Precise language

Introduce real terminology when it becomes useful.

Do not replace technical vocabulary with childish substitutes that must later be unlearned.

### 13.4 Mechanism

Answer not only:

- What?
- How?

but also:

- Why?
- What is actually happening?
- What assumptions make it true?
- What changes when assumptions break?

### 13.5 Multiple perspectives

Use examples that increase difficulty or alter perspective. A useful pattern is:

1. minimal;
2. realistic;
3. edge/failure;
4. transfer.

This is a pattern, not a quota.

### 13.6 Failure modes

Include relevant misconceptions, counterexamples, unsafe behavior, numerical pitfalls, ambiguous tool output, or limits of analogy.

### 13.7 Active work

The learner should predict, derive, debug, prove, implement, estimate, reconstruct, compare, or explain.

Passive recognition is not mastery.

### 13.8 Integration

End by showing:

- what changed in the learner's model;
- which earlier concepts now connect;
- what new capability is unlocked;
- why the next dependency exists.

Avoid generic summary filler.

---

## 14. Progressive disclosure: zero-entry, expert-exit

A beginner should be able to follow the core path without preventing an experienced reader from finding depth.

Useful layers:

1. core path;
2. mechanism;
3. deep dive;
4. expert/design notes;
5. research bridge.

Do not dump research details into the opening. Do not postpone every difficult mechanism forever.

GitHub-rendered `<details>` blocks may be used for optional derivations, solutions, historical notes, or deep implementation details. Never hide a prerequisite or core explanation solely to make the page look shorter.

Text-native Mermaid diagrams are encouraged when they genuinely clarify structure, flow, or dependencies.

---

## 15. Writing style

Write like a careful technical author who enjoys explaining hard things.

Desired prose:

- direct;
- concrete;
- precise;
- calm;
- curious;
- causally explicit;
- varied in sentence and paragraph rhythm.

Avoid habitual AI fingerprints:

- "Let's dive in";
- "In today's fast-paced world";
- "This powerful concept";
- empty "It's important to note";
- excessive "Imagine..." analogies;
- fake quotations;
- constant rhetorical questions;
- repetitive three-item patterns;
- generic conclusions;
- excessive boldface;
- decorative emoji in serious technical prose;
- inflated claims of mastery;
- praise used as filler.

Analogy is scaffolding, not evidence. State its limits when those limits matter.

Prefer causal explanations over shallow interface descriptions.

---

## 16. Exercises and assessment

A mature exercise set may test:

- recall;
- interpretation;
- application;
- transfer;
- debugging;
- counterexample;
- design;
- synthesis;
- research reading.

Do not make every exercise a copy of the preceding example.

As expertise grows, fade scaffolding and require more independent solution construction.

Use delayed retrieval and mixed practice where appropriate.

---

## 17. Projects and labs

Projects appear when multiple concepts can interact meaningfully.

A good project has:

- a capability target;
- constraints;
- observable success criteria;
- meaningful design choices;
- failure/debugging opportunities;
- reflection or analysis;
- links to concepts and curriculum nodes.

For destructive technical tasks, prefer sandboxes, VMs, containers, emulators, simulators, or disposable environments.

Warnings should be specific rather than theatrical.

---

## 18. Research progression

A `research/` folder alone does not make a track research-level.

The learner should learn to:

- locate primary literature;
- identify the real research question;
- reconstruct assumptions;
- understand methodology;
- separate baseline from contribution;
- evaluate evidence;
- reproduce results when feasible;
- identify limitations/threats;
- compare conflicting work;
- derive follow-up questions.

At L6 maintain a dated `research/FRONTIER.json` snapshot containing active areas, representative current primary work, open questions, disagreements, and reproducibility opportunities.

A frontier snapshot has `review_due`. When overdue, audit warns that it is no longer safe to call the map current without refreshing it.

---

## 18.1 Exercises, projects, and research notes as evidence artifacts

Exercises, projects, and research notes are first-class learning artifacts rather than unvalidated files. They use stable IDs and machine-friendly front matter, link to curriculum nodes/concepts/references, and can be cited as learner evidence. Canonical templates live in `templates/EXERCISE_TEMPLATE.md`, `templates/PROJECT_TEMPLATE.md`, and `templates/RESEARCH_NOTE_TEMPLATE.md`.

---

## 19. Lesson metadata profile

Lesson Markdown uses a strict, machine-friendly YAML-like front matter profile. List fields must be inline JSON arrays so the standard-library audit can parse them without external dependencies.

Example:

```yaml
---
id: LNX-0001
title: Example Title
track: linux-systems
level: L0
status: complete
curriculum_node: LNX-N-0001
concepts_introduced: ["LNX-XXX-001"]
concepts_deepened: []
concepts_used: []
examples_added: ["LNX-EX-001"]
references_used: ["LNX-REF-001"]
last_reviewed: 2026-08-19
version_sensitive: false
review_after: null
---
```

Rules:

- `id` is stable once published.
- `curriculum_node` must resolve globally.
- concept/example/reference IDs must exist in canonical registries.
- `status` is one of `draft`, `complete`, `needs-review`, `deprecated`.
- published curriculum nodes and complete lesson files must agree.
- `last_reviewed` is required.
- version-sensitive lessons must use current verified references and declare `review_after`; overdue lesson reviews produce audit warnings.

Optional fields may include:

- `software_versions`
- `standards`
- `research_snapshot`
- `estimated_effort`
- `cross_track_links`

Do not turn metadata into a second essay.

---

## 20. Naming

Track folders:

`NN-Human-Readable-Track-Name`

Tracks may be top-level or nested inside a purely organizational container. A directory is a track only when it contains `TRACK.json`; containers intentionally have no `TRACK.json`. Nested tracks remain independent learning tracks with their own canonical state.

Lesson files:

`<lesson-id>-short-kebab-title.md`

Exercises:

`<lesson-id>-exercises.md` or milestone-based sets.

Research notes when date matters:

`YYYY-MM-DD-topic-slug.md`

Track discovery does not depend on hard-coded folder names; it recursively discovers `TRACK.json` manifests while ignoring tooling/cache directories. This allows future top-level tracks and grouped nested tracks without changing the audit code.

---

## 21. Cross-track ownership

Overlap is expected; unmanaged duplication is not.

When a concept has a canonical owner:

1. reference that concept ID from neighboring tracks;
2. link to the canonical explanation;
3. explain only the context-specific consequences locally;
4. deepen elsewhere only when the new discipline genuinely requires a different treatment.

Cross-track prerequisite edges are machine-validated.

The generated `docs/CROSS_TRACK_INDEX.md` summarizes declared neighboring tracks and actual graph edges.

---

## 22. End-of-session transaction

A session that changes educational content should leave the repository internally consistent **and publication-checked**.

The canonical transaction order is:

1. write/update lesson, exercise, project, research, or guide source;
2. update canonical curriculum/registries;
3. update learner state only for real learner activity;
4. update coverage only when scope/mapping changed;
5. update root handoff if needed;
6. run `python scripts/csf.py sync`;
7. run `python scripts/csf.py audit --strict`;
8. run `python -m unittest discover -s tests -v`;
9. run `python scripts/csf.py next <track-slug>` for every changed track;
10. run `python scripts/render_audit.py ...` on changed lesson Markdown;
11. stage and require `git diff --cached --check` to be silent;
12. review staged stats/name-status and important diffs;
13. commit and push the content branch;
14. inspect the **actual GitHub Preview** for math, diagrams, HTML/details, and images when applicable;
15. only then fast-forward merge to `main`;
16. rerun sync, strict audit, tests, relevant graph/render checks on `main`;
17. require a clean tree before pushing `main`.

The full reproducible command/checklist is canonicalized in [`docs/PUBLISH_AUDIT.md`](PUBLISH_AUDIT.md).

Generated views should not be edited as the primary source.

A green structured audit does not imply correct rendering. A green render-source audit does not imply correct mathematics. A correct GitHub Preview does not imply factual or pedagogical correctness. Publication requires all applicable layers.

---

## 23. Automated integrity

### Structured repository audit

Merge/push gate:

```bash
python scripts/csf.py audit --strict
```

The structured audit checks, among other things:

- required root architecture;
- dynamic track discovery;
- unique track IDs/codes/orders;
- JSON syntax/schema versions;
- required canonical files;
- unique curriculum node IDs;
- prerequisite resolution;
- graph cycles;
- lesson front matter;
- node ↔ lesson consistency;
- concept/example/reference existence;
- learner-state references;
- coverage mappings;
- declared freshness dates;
- generated-view drift;
- internal Markdown links;
- obvious placeholder leakage into published lessons;
- exact title/alias collisions in registries.

Strict mode makes warnings blocking at publication time.

### Regression tests

Run:

```bash
python -m unittest discover -s tests -v
```

These tests protect repository tooling and known integrity invariants. They do not replace content review.

### Render-source audit

For changed lesson Markdown:

```bash
python scripts/render_audit.py path/to/lesson.md
```

or after staging:

```bash
python scripts/render_audit.py --staged
```

This tool catches source patterns that have caused real GitHub rendering failures in this repository, including legacy math delimiters, multiline dollar displays, row-sensitive LaTeX forced into one-line dollar displays, and malformed math fences.

It cannot emulate GitHub's renderer perfectly.

### Actual GitHub Preview

When rendering is relevant, the pushed branch Preview is a separate mandatory gate.

Verify the real rendered lesson, especially:

- matrix row breaks;
- aligned derivations;
- fractions, subscripts, superscripts, and symbols;
- Mermaid/HTML/details behavior;
- image loading, identity, placement, attribution, and license.

If automated scans pass but GitHub Preview is broken, publication is blocked.

### Scope of automation

Automation does not pretend to solve semantic pedagogy automatically. Human/AI judgment remains necessary for factual accuracy, depth, near-duplicate meaning, argument quality, image correctness, source interpretation, and completeness against the outside field.

GitHub Actions may run structured checks on pushes and pull requests, but a remote CI green check is not a substitute for the manual GitHub-rendering gate described above.

## 24. Definition of lesson complete

A lesson may be `complete` when:

- its curriculum node is valid and published;
- prerequisites are satisfied or explicitly linked;
- target concepts are registered;
- same-depth duplication has been checked;
- mechanisms reach the intended depth;
- examples are sufficient and varied;
- relevant edge cases/misconceptions are addressed;
- active reasoning/practice exists;
- factual claims are appropriately sourced;
- cross-track ownership is respected;
- metadata and registries are synchronized;
- audit passes.

"Complete" is relative to declared scope/depth, not all future treatment.

---

## 25. Definition of track complete

There is no permanent track-complete state.

A track may finish:

- a node;
- a milestone;
- a level;
- a specialization;
- a coverage audit.

The field remains extensible, and L6 remains refreshable.

---

## 26. Human-interest test

Before finalizing a substantial lesson, ask:

- Does the opening give a real reason to continue?
- Is there a coherent narrative/question thread?
- Is each section earning its place?
- Are there concrete examples/evidence?
- Are hard transitions explained?
- Does the prose feel authored rather than templated?
- Can a beginner follow the core path?
- Can an experienced reader still find mechanisms, caveats, or depth?
- Does the lesson connect to earlier knowledge?
- Does the learner have to think rather than only read?
- Is there a reason the next node should exist?

If several answers are no, revise.

---

## 27. What the AI must never do

Do not:

- rely on chat history instead of repository state;
- recursively reread the entire track in every normal session;
- assume hidden prerequisites;
- keep the learner permanently at beginner depth;
- create filler lessons for an arbitrary count;
- stop because a prewritten list ended;
- repeat same-depth concepts under new names;
- repeatedly recycle the same toy example;
- confuse verbosity with completeness;
- confuse publication with mastery;
- include unexplained commands/formulas;
- present analogy as mechanism;
- fabricate command output;
- fabricate citations;
- teach current software behavior from unverified memory when freshness matters;
- call an overdue frontier snapshot "current";
- silently overwrite corrections without traceable state change;
- write like a generic chatbot.

---

## 28. Fresh-chat bootstrap

With repository access:

> Read `AI_INSTRUCTIONS.md` and `docs/PUBLISH_AUDIT.md`. Use the V3 targeted-retrieval protocol. Inspect the target track's generated context and canonical state, continue from the justified next curriculum node without same-depth duplication, then execute the documented strict publish/audit gates before declaring changes ready to merge.

If repository access is unavailable, continuity-sensitive work cannot be trusted until the relevant canonical files and lesson material are supplied.

---

## 29. Evolving the system

This protocol is strict where integrity matters and deliberately adaptable where pedagogy needs judgment.

If a rule creates more bureaucracy than value:

1. identify the failure;
2. propose a simpler invariant;
3. update this specification;
4. update schemas/templates/audit logic;
5. migrate canonical state;
6. record the decision in `docs/DECISIONS.md`;
7. stress-test before producing large amounts of content.
