# Publish and Audit Protocol

This file defines the mandatory publish gate for lesson/content changes.

It exists so a fresh AI session can reproduce the repository's validation process without relying on chat history or inventing one-off audit snippets.

The gates below are **complementary**. Passing one does not imply that the others passed.

## 1. Validation layers

A content change is not ready to merge merely because Markdown looks plausible or `csf.py audit` passes.

Use five layers:

1. **canonical integrity** — curriculum graph, registries, lesson metadata, references, coverage mappings, generated-view drift;
2. **test-suite integrity** — repository regression tests;
3. **render-source integrity** — known Markdown/MathJax source hazards;
4. **actual GitHub rendering** — equations, matrices, diagrams, and embedded images in the pushed branch;
5. **Git hygiene** — whitespace, staged diff, branch/base, clean final tree.

The actual GitHub Preview is a required manual gate when changed content contains mathematics, Mermaid, HTML/details interactions, or embedded images.

## 2. Source-of-truth order

When canonical state changes, the order is:

```text
edit/copy lesson and other source material
        ↓
APPLY_CANONICAL_UPDATES
        ↓
python scripts/csf.py sync
        ↓
audit / tests / render audit
        ↓
Git review
```

Never use this order:

```text
copy
↓
sync
↓
canonical update
```

Generated Markdown views are outputs. Do not manually repair a generated view while leaving its canonical source stale.

## 3. Preflight

From the repository root:

```bash
git status
git rev-parse --short HEAD
git log --oneline --decorate -3
```

Before a packaged change, confirm:

- expected base commit;
- expected branch;
- no unrelated working-tree changes.

Create a dedicated branch before applying the package.

## 4. Canonical update and synchronization

After copying `repo-root/` from a delivery package, run its `APPLY_CANONICAL_UPDATES.py` before synchronization.

Then:

```bash
python scripts/csf.py sync
python scripts/csf.py audit --strict
python -m unittest discover -s tests -v
```

`audit --strict` is the merge/push gate. Warnings are blocking.

Do not substitute plain `audit` for `audit --strict` at publication time.

## 5. Graph checks

For every track changed in the session, run:

```bash
python scripts/csf.py next <track-slug>
```

Check both:

- authoring candidates;
- learner next actions.

Publishing a lesson must move the curriculum graph as intended without falsely marking learner mastery.

## 6. Render-source audit

For changed lesson Markdown, run the repository tool explicitly:

```bash
python scripts/render_audit.py path/to/lesson-a.md path/to/lesson-b.md
```

After staging, it can also scan staged **lesson** Markdown (repository policy/docs are excluded from this shortcut because they may contain literal syntax examples):

```bash
python scripts/render_audit.py --staged
```

For repository-wide render migrations only:

```bash
python scripts/render_audit.py --all-lessons
```

The render audit checks source patterns that have caused real failures in this repository, including:

- forbidden legacy `\(...\)` / `\[...\]` delimiters;
- multiline `$$` source displays;
- row-sensitive LaTeX such as matrices or `aligned` forced into one-line dollar displays;
- malformed fenced `math` blocks;
- embedded-image source/license reminders.

A render-source PASS does **not** prove that GitHub rendered the page correctly.

## 7. Hybrid math rule

The repository uses a conservative hybrid:

```text
inline expression
    → $...$

simple standalone display
    → one-line $$ ... $$

matrix / aligned / cases / array / expression depending on LaTeX row separator \\
    → fenced ```math
```

Do not force all mathematics into one delimiter style.

The decisive test for row-sensitive mathematics is whether the pushed GitHub Preview preserves the intended rows, alignment, symbols, fractions, subscripts, and superscripts.

## 8. Static-image rule

Static images are selective teaching evidence, not decoration.

When an image is materially useful:

- verify that it depicts the exact object/geometry described;
- prefer an authoritative source or traceable open-license repository;
- use a stable direct-media URL for embedding;
- place the exact source page, author/organization, and license near the image;
- register lesson-critical figures in the reference registry;
- use one accurate visual anchor rather than several decorative images.

If reliable embedding is not possible, provide a precise **Visual lookup** instruction.

## 9. Git review before commit

Stage:

```bash
git add -A
```

Then:

```bash
git diff --cached --check
git diff --cached --stat
git diff --cached --name-status
```

`git diff --cached --check` must produce no output.

Review important source diffs directly when the change is substantial.

Then commit.

## 10. Push branch before merge

Push the content branch first:

```bash
git push -u origin <branch>
```

Do **not** immediately merge math/visual changes to `main`.

Open the changed lesson files on the pushed GitHub branch and inspect the rendered page.

For math-heavy content verify:

- no raw LaTeX leakage;
- intended matrix rows;
- intended aligned derivation rows;
- fractions/subscripts/superscripts;
- no bare operators parsed as Markdown;
- no malformed code/math fences.

For visual content verify:

- the image loads;
- the image matches the surrounding explanation;
- caption/source/license are readable and correct;
- the visual is positioned where it actually helps understanding.

If GitHub Preview disagrees with local source assumptions, the Preview result wins as evidence of a rendering defect.

## 11. Fast-forward merge

Only after branch-level validation:

```bash
git switch main
git pull --ff-only origin main
git merge --ff-only <branch>
```

No merge commit is needed for this workflow.

## 12. Final validation on main

Run again:

```bash
python scripts/csf.py sync
python scripts/csf.py audit --strict
python -m unittest discover -s tests -v
```

Re-run relevant track graph checks and render-source checks.

Then:

```bash
git status --short
```

It must be empty.

Finally:

```bash
git push origin main
git status
git log --oneline --decorate --graph -6
```

The final state should have:

- `main` and `origin/main` on the same validated commit;
- a clean working tree;
- zero strict-audit errors;
- zero strict-audit warnings;
- all tests passing.

## 13. What each audit can and cannot prove

### `python scripts/csf.py audit --strict`

Can validate structured repository integrity.

It cannot prove:

- pedagogical quality;
- factual truth of every prose sentence;
- semantic non-duplication beyond machine-detectable cases;
- correct GitHub MathJax rendering;
- correctness of an external image.

### Unit tests

Can detect tooling regressions represented in the test suite.

They cannot prove lesson quality or rendering.

### `scripts/render_audit.py`

Can catch known source-level rendering hazards.

It cannot emulate GitHub's renderer perfectly.

### GitHub Preview

Can show the actual publication renderer.

It cannot prove that the mathematics or image is factually correct.

### Human/AI review

Must still verify:

- factual accuracy;
- causal/mechanistic explanation;
- correct source interpretation;
- correct image identity;
- appropriate lesson depth;
- exercise quality;
- conceptual duplication.

A publish decision requires all applicable layers, not one green command.

## YAML frontmatter integrity gate

GitHub parses lesson frontmatter as YAML before rendering the Markdown body.
A syntactically valid-looking line can therefore break the entire lesson
preview. In particular, a plain scalar containing a colon followed by a space
must be quoted.

Unsafe:

```yaml
title: DC circuits: sources, loads, resistance, KCL, and KVL
```

Safe:

```yaml
title: "DC circuits: sources, loads, resistance, KCL, and KVL"
```

Required checks:

```bash
python scripts/frontmatter_audit.py
python scripts/frontmatter_audit.py --staged
```

The full-repository check catches historical defects; the staged check is a
pre-commit gate. These checks complement, rather than replace,
`render_audit.py`, `csf.py audit --strict`, unit tests, and actual GitHub
Preview inspection.

## GitHub render-compatibility gate

Source-level Markdown can pass generic rendering checks and still fail on
GitHub-specific renderer restrictions.

Known hazards include:

- unsupported math macros such as `\operatorname{...}`;
- raw pipe characters inside Mermaid node labels such as
  `E[distribution P token | context]`.

Required checks:

```bash
python scripts/github_render_compat_audit.py
python scripts/github_render_compat_audit.py --staged
```

These checks complement:

```bash
python scripts/frontmatter_audit.py
python scripts/render_audit.py
python scripts/csf.py audit --strict
```

Actual pushed GitHub Preview inspection remains the final rendering gate.

Literal hazard examples written inside inline code or ordinary fenced code are documentation and are intentionally excluded from the compatibility scan; real math contexts and Mermaid diagrams remain checked.
