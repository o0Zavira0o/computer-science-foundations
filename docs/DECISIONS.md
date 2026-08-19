# Architecture Decisions

This file records high-impact repository design choices. Keep entries concise; Git history preserves the detailed diff.

## 2026-08-19 — V3 hardening

**Decision:** separate canonical machine-readable state from generated Markdown views.

**Why:** Markdown-only ledgers are readable but difficult to validate reliably at scale.

## 2026-08-19 — Targeted retrieval

**Decision:** normal AI sessions read compact track context, canonical registries, and relevant prerequisite/recent lessons rather than recursively rereading the entire track.

**Why:** recursive rereading does not scale to hundreds or thousands of files.

## 2026-08-19 — Dynamic track discovery

**Decision:** curriculum tracks are discovered recursively from `TRACK.json`; organizational containers may group nested independent tracks without carrying curriculum state themselves.

**Why:** future subjects and grouped side studies should not require editing a hard-coded Python list or flattening the repository.

## 2026-08-19 — Curriculum graph

**Decision:** `CURRICULUM.json` is the canonical dependency graph. `ROADMAP.md` is generated.

**Why:** prerequisite edges need machine validation, cycle detection, and cross-track resolution.

## 2026-08-19 — Separate learner state

**Decision:** curriculum publication state and learner knowledge state are stored separately.

**Why:** "lesson exists" and "learner demonstrated it" are different facts.

## 2026-08-19 — Coverage baseline

**Decision:** each activated track maintains `COVERAGE.json` based on multiple external reference classes.

**Why:** anti-duplication alone cannot detect missing areas.

## 2026-08-19 — CI integrity

**Decision:** repository audits run locally and on GitHub Actions.

**Why:** structural drift should fail early rather than accumulate silently.

## 2026-08-19 — V3.1 pre-content gate

**Decision:** an audited coverage baseline must contain registered evidence sources, mapped coverage items, and no unresolved gaps before publication is allowed.

**Why:** a boolean `audited` flag without evidence can create false confidence.

## 2026-08-19 — Separate next-authoring and next-study

**Decision:** authoring readiness and learner readiness are different commands and state transitions.

**Why:** a published prerequisite satisfies curriculum construction, while learner progression requires learner evidence.

## 2026-08-19 — First-class evidence artifacts

**Decision:** exercises, projects, and research notes use validated stable IDs and metadata.

**Why:** active practice and research work must be traceable if they are used as evidence of learning.

## 2026-08-19 — Immutable CI action references

**Decision:** GitHub Actions used by curriculum integrity CI are pinned to reviewed full commit SHAs, with the human-readable release version recorded in comments.

**Why:** the CI gate is part of the repository trust boundary; mutable action tags are an unnecessary supply-chain risk.

## 2026-08-19 — Repository language

**Decision:** committed filenames, structural documentation, and educational prose are written in English.

**Why:** one consistent repository language improves reuse, public readability, cross-session AI continuity, and technical searchability. Language-learning tracks may still contain target-language material as study content.

## 2026-08-19 — Auxiliary Studies container

**Decision:** `09-Auxiliary-Studies/` is an organizational container, not a curriculum track. Advanced English, German Language, and Philosophy and Logic are nested independent tracks.

**Why:** each subject needs separate prerequisites, learner state, coverage audits, and long-term research progression while remaining visibly grouped.

## 2026-08-19 — Public-first authoring

**Decision:** curriculum authoring optimizes for public educational quality and prerequisite integrity rather than the repository owner's personal reading sequence. Learner state remains optional continuity metadata and is never evidence that every visitor has followed the same path.

**Why:** the repository is intended for many readers, including people who enter through random lessons or direct links.

## 2026-08-19 — Selective visual and interactive teaching

**Decision:** use interactive checks, Mermaid diagrams, and static figures selectively when they improve reasoning or spatial/causal understanding; do not impose a visual quota.

**Why:** interaction and visuals can make difficult structures easier to inspect, but decorative density can reduce clarity.

## 2026-08-19 — Dual licensing

**Decision:** educational/documentation material is released under CC BY-SA 4.0; repository software under `scripts/`, `tests/`, `.github/workflows/`, and `schemas/` is GPL-3.0-or-later. Attribution guidance and AI-assistance boundaries are recorded at repository root.

**Why:** the project should remain broadly reusable while requiring attribution and share-alike behavior for educational adaptations, and software should use a software-specific copyleft license rather than a Creative Commons license.
