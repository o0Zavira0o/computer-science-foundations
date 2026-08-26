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

Use a display block for an equation that deserves its own visual line. The repository's **strict compatibility profile** keeps the opening delimiter, expression, and closing delimiter on one physical source line:

```markdown
$$ T(au+bv)=aT(u)+bT(v). $$
```

Keep a blank line before and after the display line. This form is intentionally stricter than the full range of syntax GitHub documents because it is robust across GitHub preview, alternate Markdown viewers, and text extraction.

### Matrices, derivations, and aligned mathematics

Keep the outer `$$ ... $$` display on one physical source line even when the LaTeX itself contains matrix row separators or an alignment environment:

```markdown
$$ A=\begin{bmatrix}1 & 2 \\ 3 & 4\end{bmatrix}. $$

$$ \begin{aligned} f(x) &= a(x+y) \\ &= ax+ay. \end{aligned} $$
```

GitHub officially supports fenced `math` blocks, but repository lessons use the stricter one-line display profile unless an expression has been manually verified in the actual GitHub Preview and cannot reasonably be expressed this way. Never put a bare relation or operator such as `=`, `-`, `+`, `\neq`, or `\rightarrow` on its own physical Markdown line inside a display expression.

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
2. Confirm every lesson display equation uses a self-contained one-line `$$ ... $$` source form by default.
3. Confirm no mathematical expression is accidentally inside an ordinary code block.
4. Confirm notation is introduced before it is heavily used.
5. Confirm matrices, fractions, subscripts, superscripts, and symbols are readable in the **actual GitHub Preview**, not only in a delimiter/source scan.
6. Confirm no display block leaves a bare relation/operator on its own physical Markdown line.
7. Prefer a small diagram or table only when it adds structure that the equation alone does not communicate.

## Compatibility target

The canonical rendering target is GitHub Markdown. GitHub documents LaTeX-formatted mathematics in Markdown using MathJax, with `$...$` (or dollar-backtick syntax) for inline expressions and `$$...$$` or fenced `math` blocks for display expressions. This repository deliberately adopts a stricter lesson-authoring subset: one physical source line per `$$ ... $$` display by default, followed by visual inspection in the actual GitHub Preview.

Official reference: <https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions>
