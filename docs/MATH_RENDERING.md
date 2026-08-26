# Mathematical Rendering Standard

This repository is rendered primarily on GitHub. Mathematical notation in Markdown must therefore use syntax that GitHub renders with MathJax rather than LaTeX delimiters that may remain visible as raw source.

## Canonical house style

### Inline mathematics

Use single-dollar delimiters for short expressions that belong inside a sentence:

```markdown
A vector $x \in \mathbb{R}^n$ has $n$ real coordinates.
```

Rendered intent: the mathematical expressions flow with the surrounding prose.

If an inline expression contains characters that conflict with Markdown parsing, use GitHub's dollar-backtick form:

```markdown
$`\sqrt{3x-1} + (1+x)^2`$
```

Use that form only when it solves a real parsing problem; ordinary `$...$` is easier to read in source.

### Display mathematics

Use a display block for an equation that deserves its own visual line.

For a **simple standalone expression that does not require LaTeX row separators or an alignment/matrix environment**, use a self-contained one-line display:

```markdown
$$ T(au+bv)=aT(u)+bT(v). $$
```

Keep a blank line before and after that display line.

### Matrices, aligned derivations, and row-sensitive mathematics

When the expression contains a matrix, an aligned derivation, `cases`, `array`, or any structure that depends on LaTeX row separators such as `\\`, use GitHub's fenced `math` form:

````markdown
```math
A=
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
```
````

For a compact aligned derivation:

````markdown
```math
\begin{aligned}
a(u+v)
&= au+av \\
&= \text{next justified step}
\end{aligned}
```
````

This split is deliberate. GitHub supports both `$$...$$` and fenced `math`, but repository experience shows that forcing row-sensitive LaTeX into a one-line dollar display can allow Markdown/rendering layers to interfere with `\\`. Preserve row-sensitive mathematics inside a fenced `math` block instead.

Never leave a bare relation or operator such as `=`, `-`, `+`, `\neq`, or `\rightarrow` on its own ordinary Markdown line outside a math container.

### Renderer-validation rule

A source/delimiter scan is necessary but not sufficient. For math-heavy lessons:

1. verify simple display equations are self-contained `$$ ... $$` lines;
2. verify matrix/alignment-sensitive displays use fenced `math`;
3. verify no one-line `$$ ... $$` expression contains a LaTeX row separator `\\`;
4. push the branch before merging;
5. inspect the **actual GitHub Preview** and confirm matrices have the intended rows and aligned derivations have the intended line breaks.

If the raw source contains `\\` but the rendered Preview visually collapses rows, treat that as a rendering failure even if every automated delimiter check passes.

## Delimiters that must not be used

Do **not** use backslash-parenthesis delimiters for inline math or backslash-bracket delimiters for display math in repository Markdown. They are common in LaTeX/MathJax environments, but they are not the repository's GitHub-safe Markdown convention and can appear as raw source instead of rendered mathematics.

## Notation versus code

Mathematics and code are different semantic objects.

- Use math delimiters for variables, equations, sets, vectors, matrices, sums, probabilities, and mathematical relations.
- Use backticks or fenced code blocks for literal shell commands, program text, filenames, flags, identifiers, and data that readers should copy exactly.
- Do not wrap a mathematical formula in an ordinary code fence merely to preserve spacing; use a math block.

For example:

```markdown
The vector $x \in \mathbb{R}^3$ is mathematical notation.

Run `python scripts/csf.py audit --strict` is a literal command.
```

## Tables, lists, headings, and details blocks

Inline math may appear inside table cells, list items, headings, and `<details>` content when the expression is short. For a substantial equation inside any of these structures, prefer a separate display block with surrounding blank lines.

Avoid dense formulas in Markdown tables when a standalone equation plus explanatory prose would be easier to read on narrow screens.

## Typography and readability

- Use `\mathbb{R}`, `\mathbb{C}`, subscripts, superscripts, fractions, matrices, and named operators through LaTeX syntax inside math mode.
- Prefer semantic notation such as `\lVert x \rVert` for norms rather than improvised ASCII when the mathematical object matters.
- Explain new notation in prose immediately before or after first use.
- Keep equations short enough to read on GitHub when possible; split a long derivation into meaningful steps rather than one very wide line.
- A formula should not replace explanation. State what the objects mean, what the relation claims, and why the reader should care.

## Authoring checklist

Before publishing a lesson, exercise, project, or research note containing mathematics:

1. Confirm every inline expression uses GitHub-supported inline math syntax.
2. Confirm simple lesson displays use self-contained one-line `$$ ... $$`, while matrices/aligned/row-sensitive expressions use fenced `math`.
3. Confirm no mathematical expression is accidentally inside an ordinary code block.
4. Confirm notation is introduced before it is heavily used.
5. Confirm matrices, fractions, subscripts, superscripts, and symbols are readable in the **actual GitHub Preview**, not only in a delimiter/source scan.
6. Confirm no one-line `$$ ... $$` display contains a LaTeX row separator `\\`.
7. Confirm no display block leaves a bare relation/operator on an ordinary Markdown line.
8. Prefer a small diagram or table only when it adds structure that the equation alone does not communicate.

## Compatibility target

The canonical rendering target is GitHub Markdown. GitHub documents LaTeX-formatted mathematics in Markdown using MathJax, with `$...$` (or dollar-backtick syntax) for inline expressions and `$$...$$` or fenced `math` blocks for display expressions. This repository deliberately uses a conservative hybrid subset: simple display expressions use one-line `$$ ... $$`; matrices, aligned derivations, and other row-sensitive expressions use fenced `math`; both are followed by visual inspection in the actual GitHub Preview.

Official reference: <https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions>
