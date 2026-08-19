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

Use a display block for an equation that deserves its own visual line:

```markdown
$$
T(au+bv)=aT(u)+bT(v).
$$
```

Keep a blank line before and after the block. Do not put prose on the delimiter lines.

### Long, multiline, or alignment-heavy mathematics

For long derivations, aligned equations, or source that becomes hard to read inside dollar delimiters, use GitHub's fenced `math` block:

````markdown
```math
A=
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
```
````

Both display styles are supported by GitHub. Prefer `$$...$$` for ordinary standalone equations and fenced `math` when multiline structure materially improves source readability.

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
2. Confirm every standalone equation uses `$$...$$` or a fenced `math` block.
3. Confirm no mathematical expression is accidentally inside an ordinary code block.
4. Confirm notation is introduced before it is heavily used.
5. Confirm matrices, fractions, subscripts, superscripts, and symbols are readable in GitHub preview.
6. Prefer a small diagram or table only when it adds structure that the equation alone does not communicate.

## Compatibility target

The canonical rendering target is GitHub Markdown. GitHub documents LaTeX-formatted mathematics in Markdown using MathJax, with `$...$` (or dollar-backtick syntax) for inline expressions and `$$...$$` or fenced `math` blocks for display expressions.

Official reference: <https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions>
