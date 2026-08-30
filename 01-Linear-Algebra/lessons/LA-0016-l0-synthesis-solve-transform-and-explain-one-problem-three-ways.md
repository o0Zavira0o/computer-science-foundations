---
id: LA-0016
title: "L0 synthesis: solve, transform, and explain one problem three ways"
track: linear-algebra
level: L0
status: complete
curriculum_node: LA-N-0016
concepts_introduced: ["LA-C-0016"]
concepts_deepened: ["LA-C-0008", "LA-C-0010", "LA-C-0011", "LA-C-0012", "LA-C-0013", "LA-C-0014", "LA-C-0015"]
concepts_used: ["LA-C-0004", "LA-C-0005", "LA-C-0006", "LA-C-0007", "LA-C-0009"]
examples_added: ["LA-EX-060", "LA-EX-061", "LA-EX-062", "LA-EX-063", "LA-EX-064"]
references_used: ["LA-REF-001", "LA-REF-002", "LA-REF-003", "LA-REF-004"]
last_reviewed: 2026-08-28
version_sensitive: false
review_after: null
---
# L0 synthesis: solve, transform, and explain one problem three ways

## If you landed here directly

This is a synthesis lesson.

It assumes the L0 foundations through `LA-0015 — Invertibility as reversible linear action`.

No major new computational technique is the point.

Instead, we will force several ideas that may have felt separate to describe the **same mathematical object**.

The central problem is:

$$ A\mathbf{x}=\mathbf{b}. $$

You will learn to read that expression in three mutually reinforcing ways:

```text
1. system view
   simultaneous linear constraints

2. column-combination view
   choose weights on the columns of A to build b

3. transformation view
   find an input x that A sends to output b
```

The central mental model is:

```text
same matrix equation
→ different question lenses
→ same mathematical answer
→ stronger explanation and error checking
```

By the end, you should be able to:

- translate one problem among scalar equations, matrix equation, column combination, and transformation language;
- solve a small system by elimination and verify the same solution by matrix multiplication;
- explain unique, inconsistent, and infinitely-many-solution cases in all three views;
- connect pivots and free variables to reachability and information preservation;
- use invertibility to explain why a square transformation has one preimage for every target;
- distinguish a computation from an explanation;
- choose the most useful representation for a question;
- detect contradictions between representations as evidence of an error;
- explain one applied linear model without mistaking mathematical coefficients for physical mechanisms;
- finish L0 with a coherent map rather than a list of isolated procedures.

---

# Part I — The one problem we will keep translating

Consider:

```math
A=
\begin{bmatrix}
2 & 1 \\
1 & 1
\end{bmatrix},
\qquad
\mathbf{x}=
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix},
\qquad
\mathbf{b}=
\begin{bmatrix}
5 \\
3
\end{bmatrix}.
```

We want to solve:

$$ A\mathbf{x}=\mathbf{b}. $$

At first glance, this can look like a compact piece of matrix notation.

But it contains several stories at once.

---

# Part II — View 1: a system of simultaneous constraints

Expand the matrix equation row by row:

```math
\begin{aligned}
2x_1+x_2&=5,\\
x_1+x_2&=3.
\end{aligned}
```

Each equation is a constraint.

The solution must satisfy both at once.

Subtract the second equation from the first:

$$ x_1=2. $$

Then:

$$ x_2=1. $$

So:

```math
\mathbf{x}=
\begin{bmatrix}
2 \\
1
\end{bmatrix}.
```

The system view emphasizes:

```text
constraints
→ elimination
→ solution set
```

---

# Part III — View 2: a column combination

Write the columns of $A$ as:

```math
\mathbf{a}_1=
\begin{bmatrix}
2 \\
1
\end{bmatrix},
\qquad
\mathbf{a}_2=
\begin{bmatrix}
1 \\
1
\end{bmatrix}.
```

Then:

$$ A\mathbf{x}=x_1\mathbf{a}_1+x_2\mathbf{a}_2. $$

Our equation asks:

> what weights on the two columns build the target $\mathbf{b}$?

Substitute the solution:

```math
2
\begin{bmatrix}
2 \\
1
\end{bmatrix}
+
1
\begin{bmatrix}
1 \\
1
\end{bmatrix}
=
\begin{bmatrix}
5 \\
3
\end{bmatrix}.
```

The column view emphasizes:

```text
generators
→ weights
→ reachability of target
```

---

# Part IV — View 3: a transformation and its preimage

Interpret $A$ as a linear transformation.

```text
input x
→ A
→ output b
```

Now the question is:

> which input does the transformation send to the target output $\mathbf{b}$?

We found:

```math
A
\begin{bmatrix}
2 \\
1
\end{bmatrix}
=
\begin{bmatrix}
5 \\
3
\end{bmatrix}.
```

Because this $A$ is invertible, every target in $\mathbb{R}^2$ has exactly one input.

The transformation view emphasizes:

```text
input-output action
→ information preservation
→ reversibility / preimage
```

---

# Part V — Worked example 1: one answer, three explanations

The problem above is `LA-EX-060`.

The answer $\mathbf{x}=[2,1]^T$ can be justified three ways:

| View | Meaning of the answer |
|---|---|
| System | the one point satisfying both equations |
| Columns | the unique weights that build the target from the columns |
| Transformation | the unique input mapped to the target output |

These statements are not analogies layered on top of unrelated algebra.

They are equivalent readings of the same matrix equation.

---

# Part VI — Why elimination is more than a recipe

Elimination acts on the system representation.

It changes equations while preserving the solution set.

But because the system and matrix equation encode the same problem, elimination is also revealing structure about the transformation.

When elimination produces a pivot in every variable column of an appropriate square system, no input direction is left free.

When it exposes a free variable, there is a family of inputs satisfying the homogeneous relation.

So a row-operation calculation can answer an input-output question.

That is synthesis.

---

# Part VII — Pivots connect equations to geometry

Recall:

```text
pivot variable
→ constrained by leading structure

free variable
→ parameter remains
```

For a consistent system, each free variable contributes a degree of freedom to the solution family.

In transformation language, a free direction can describe input changes that do not affect the output in the homogeneous problem.

In column language, nonunique coefficients mean the same target can be built in more than one way.

One structural fact appears in three dialects.

---

# Part VIII — A singular matrix: unreachable target

Consider:

```math
B=
\begin{bmatrix}
1 & 2 \\
2 & 4
\end{bmatrix},
\qquad
\mathbf{c}=
\begin{bmatrix}
1 \\
0
\end{bmatrix}.
```

Solve:

$$ B\mathbf{x}=\mathbf{c}. $$

The scalar system is:

```math
\begin{aligned}
x_1+2x_2&=1,\\
2x_1+4x_2&=0.
\end{aligned}
```

Doubling the first left-hand side gives the second left-hand side, but the right-hand sides disagree.

Elimination produces a contradiction.

Therefore there is no solution.

---

# Part IX — The same no-solution case in column language

The columns of $B$ are:

```math
\mathbf{b}_1=
\begin{bmatrix}
1 \\
2
\end{bmatrix},
\qquad
\mathbf{b}_2=
\begin{bmatrix}
2 \\
4
\end{bmatrix}=2\mathbf{b}_1.
```

They span only a line.

The target:

```math
\mathbf{c}=
\begin{bmatrix}
1 \\
0
\end{bmatrix}
```

is not on that line.

So it is unreachable as a column combination.

---

# Part X — The same no-solution case in transformation language

The transformation $B$ collapses the plane onto a line.

Its output set is not all of $\mathbb{R}^2$.

The target $\mathbf{c}$ lies outside the output set.

Therefore it has no preimage.

This is `LA-EX-061`.

Three statements are equivalent here:

```text
system inconsistent
=
target outside column span
=
target outside transformation output
```

---

# Part XI — A singular matrix: reachable target with many solutions

Keep the same matrix $B$, but choose:

```math
\mathbf{d}=
\begin{bmatrix}
3 \\
6
\end{bmatrix}.
```

Now:

$$ B\mathbf{x}=\mathbf{d}. $$

The system reduces to one independent equation:

$$ x_1+2x_2=3. $$

Let:

$$ x_2=t. $$

Then:

$$ x_1=3-2t. $$

So there are infinitely many solutions.

---

# Part XII — Many solutions in the other two views

## Column view

The target lies on the line spanned by the columns.

But the columns are redundant.

So the target can be expressed with infinitely many coefficient pairs.

## Transformation view

The transformation collapses a whole input direction.

Different inputs can map to the same output.

Thus a reachable output can have many preimages.

This is `LA-EX-062`.

The synthesis is:

```text
free variable
=
nonunique column coefficients
=
multiple preimages
```

---

# Part XIII — Invertibility unifies the unique-solution case

For a square matrix $A$, invertibility means there is a transformation that undoes $A$.

If $A^{-1}$ exists, then:

$$ A\mathbf{x}=\mathbf{b} $$

implies:

$$ \mathbf{x}=A^{-1}\mathbf{b}. $$

But the deeper statement is not the formula.

It is:

```text
for every target b
there exists exactly one input x
```

System language:

```text
one solution for every right-hand side
```

Column language:

```text
columns reach every target with unique weights
```

Transformation language:

```text
output preserves enough information to recover the input
```

---

# Part XIV — Verification is representation switching

Suppose elimination gives a proposed $\mathbf{x}$.

A strong check is not to repeat the same elimination.

Instead compute:

$$ A\mathbf{x}. $$

If the product equals $\mathbf{b}$, the candidate satisfies the original matrix equation.

You can also substitute into the scalar equations.

Switching representations gives independent opportunities to catch mistakes.

This is a general technical habit:

> verify a result using a different view when possible.

---

# Part XV — Worked example 4: composition and reversal

Suppose a point is first scaled and then sheared.

Let:

```math
S=
\begin{bmatrix}
2 & 0 \\
0 & 1
\end{bmatrix},
\qquad
H=
\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}.
```

The forward pipeline is:

$$ \mathbf{x}\mapsto HS\mathbf{x}. $$

To recover the original input, undo the shear first and the scaling second:

$$ \mathbf{x}=S^{-1}H^{-1}\mathbf{y}. $$

Therefore:

$$ (HS)^{-1}=S^{-1}H^{-1}. $$

This is `LA-EX-063`.

The order reversal is obvious in action language even if the symbolic formula is easy to forget.

---

# Part XVI — Matrix multiplication is composition, not decoration

`LA-0014` showed that $AB$ means:

```text
first B
then A
```

The synthesis lesson adds:

```text
composition changes the operator
but the resulting matrix can still be read as

- a system coefficient matrix,
- a set of columns,
- a transformation.
```

Matrix multiplication therefore connects pipeline structure to the same three views.

---

# Part XVII — Shape tells you which questions are legal

If $A$ is $m\times n$, then:

```text
input dimension = n
output dimension = m
```

The system $A\mathbf{x}=\mathbf{b}$ therefore requires:

```text
x in R^n
b in R^m
```

The columns of $A$ live in $\mathbb{R}^m$ because they are possible output directions.

This one shape rule aligns all three views.

A dimension mismatch is not merely a syntax problem.

It means the proposed input-output story is incoherent.

---

# Part XVIII — Rectangular systems fit the synthesis too

The ordinary two-sided inverse is a square-matrix concept, but the three-view synthesis is not restricted to square matrices.

For a rectangular matrix, you can still ask:

- is the system consistent?
- is the target in the column span?
- how many preimages does the transformation have?

What changes is the invertibility story.

A rectangular map generally cannot have an ordinary two-sided inverse between spaces of different dimensions.

Later linear algebra develops richer one-sided and generalized inverse ideas.

We do not need them yet.

---

# Part XIX — Applied synthesis: a two-sensor mixing model

Suppose two latent source amplitudes $s_1,s_2$ produce two sensor outputs:

```math
\begin{bmatrix}
y_1 \\
y_2
\end{bmatrix}
=
\begin{bmatrix}
2 & 1 \\
1 & 1
\end{bmatrix}
\begin{bmatrix}
s_1 \\
s_2
\end{bmatrix}.
```

If measured output is:

```math
\begin{bmatrix}
5 \\
3
\end{bmatrix},
```

then mathematically this is the same core example.

The solution is:

```math
\begin{bmatrix}
s_1 \\
s_2
\end{bmatrix}
=
\begin{bmatrix}
2 \\
1
\end{bmatrix}.
```

---

# Part XX — Applied example through three views

This is `LA-EX-064`.

## System view

Each sensor output gives one linear constraint on the source amplitudes.

## Column view

Each column is the modeled sensor signature of one unit of one source.

The unknown source amplitudes are the weights needed to reconstruct the observed sensor vector.

## Transformation view

The matrix maps a source-state vector to a sensor-output vector.

If the matrix is invertible, the idealized model allows unique recovery of the source state from the sensor output.

But be careful:

> mathematical invertibility of a model does not prove the physical model is correct or noise-free.

---

# Part XXI — Mathematics versus model semantics

A matrix can be invertible and still be a poor scientific model.

Reasons include:

- the real system is nonlinear;
- coefficients drift over time;
- measurement noise is large;
- important variables are missing;
- units were mixed incorrectly;
- the matrix was estimated badly;
- the physical process is not actually reversible.

Linear algebra tells you consequences **inside the stated model**.

It does not automatically validate the model's scientific assumptions.

This distinction is essential for engineering use.

---

# Part XXII — Choosing the most useful view

Use the **system view** when the question emphasizes:

- constraints;
- elimination;
- consistency;
- explicit unknown values.

Use the **column view** when the question emphasizes:

- reachability;
- mixtures;
- generators;
- coefficient uniqueness.

Use the **transformation view** when the question emphasizes:

- input-output behavior;
- composition;
- reversibility;
- geometric action.

Good linear algebra means switching views rather than forcing every question into one procedure.

---

# Part XXIII — A representation translation protocol

Given $A\mathbf{x}=\mathbf{b}$, practice this sequence:

1. **Shape check** — identify input and output dimensions.
2. **Scalar expansion** — write the row equations.
3. **Column expansion** — write $x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n=\mathbf{b}$.
4. **Transformation statement** — say what input is mapped to what output.
5. **Solve** — use elimination or another justified method.
6. **Classify** — unique, none, or infinitely many.
7. **Explain in all views** — translate the classification.
8. **Verify** — multiply $A\mathbf{x}$ for any proposed solution.
9. **State model assumptions** — if the matrix represents a real system.

This protocol is more valuable than memorizing disconnected matrix tricks.

---

# Part XXIV — Common failure modes

## Failure mode 1: solving without knowing what the equation means

A correct arithmetic answer with no interpretation is fragile knowledge.

## Failure mode 2: treating rows and columns as interchangeable

Rows encode output equations; columns encode input-coordinate contributions.

They support different but compatible views.

## Failure mode 3: saying "no inverse" means "no solutions"

A singular system can have no solution or infinitely many solutions depending on the target.

## Failure mode 4: saying "free variable" means arbitrary output

A free variable means there is freedom among inputs that satisfy the constraints.

The output target remains fixed in $A\mathbf{x}=\mathbf{b}$.

## Failure mode 5: believing every target is reachable

Reachability depends on the column span / transformation output.

## Failure mode 6: applying $A^{-1}$ when an inverse has not been established

Invertibility is a property to justify, not a symbol to assume.

## Failure mode 7: confusing a model coefficient with a causal physical pathway

A matrix entry expresses a relation within a model.

It does not automatically identify mechanism.

## Failure mode 8: redoing the same arithmetic as "verification"

Prefer an independent representation check.

---

# Part XXV — Active exercise set

## Exercise A — Three-view translation

For:

```math
A=
\begin{bmatrix}
1 & 3 \\
2 & 4
\end{bmatrix},
\qquad
\mathbf{b}=
\begin{bmatrix}
7 \\
10
\end{bmatrix},
```

write:

- the scalar system;
- the column combination;
- the transformation/preimage question.

Then solve and verify.

## Exercise B — Unreachable target

Construct a $2\times2$ matrix with parallel columns and a target outside their span.

Explain inconsistency in all three views.

## Exercise C — Many preimages

Use the same singular matrix but choose a target in its column span.

Parameterize the solution set and explain why the coefficients are not unique.

## Exercise D — Composition

Choose two simple invertible planar transformations.

Describe the forward order and the inverse order before multiplying matrices.

## Exercise E — Modeling language

Write a two-input, two-output linear engineering model.

State what each row, each column, the input vector, and the output vector mean.

Then name one physical assumption the matrix equation does not validate by itself.

---

# Part XXVI — Retrieval practice

Without looking back, answer:

1. What are the three main readings of $A\mathbf{x}=\mathbf{b}$ used in this lesson?
2. What do rows emphasize?
3. What do columns emphasize?
4. What does a free variable mean in transformation language?
5. What does inconsistency mean in column-span language?
6. What does invertibility say about preimages of every target?
7. Why can a singular system still have solutions?
8. Why is multiplying $A\mathbf{x}$ a good verification step?
9. Why does $(AB)^{-1}$ reverse order?
10. What does matrix shape say about input and output dimensions?
11. Why does mathematical invertibility not prove a physical model is accurate?
12. When might the transformation view be more useful than the row-equation view?

---

# Part XXVII — The L0 concept map

The first stage of this track now fits together as:

```text
vectors
→ addition and scaling
→ linear combinations
→ span and reachability
→ linear equations as constraints
→ systems and solution sets
→ matrices
→ matrix-vector multiplication
→ elimination
→ pivots and free variables
→ linear transformations
→ composition / matrix multiplication
→ invertibility
→ synthesis across representations
```

This is not merely a sequence of chapters.

Each idea answers a different question about the same family of linear structures.

---

# Part XXVIII — What you should carry forward

Do not carry forward only formulas.

Carry these habits:

```text
ask what the objects mean
check dimensions
translate representations
solve structurally
classify the solution set
verify in another view
separate mathematics from model assumptions
```

Those habits scale to vector spaces, subspaces, bases, rank, null spaces, eigenvectors, least squares, numerical methods, and modern high-dimensional applications.

---

# Compact summary

The equation $A\mathbf{x}=\mathbf{b}$ can be read as a system of simultaneous constraints, as a request to build a target from matrix columns, or as an input-output transformation problem.

Elimination, pivots, free variables, span, transformation geometry, composition, and invertibility are therefore not isolated topics. They are different windows onto the same structure.

A unique solution means one input satisfies the constraints, one set of column weights builds the target, and one preimage maps to the output. No solution means the target is inconsistent with the constraints and lies outside the transformation output. Infinitely many solutions mean the target is reachable but some input freedom is invisible at the output.

The most important L0 skill is now representation control:

> choose a useful view, translate correctly, solve, and verify the same result from another view.

---

# References used in this lesson

- `LA-REF-001` — existing audited linear-algebra reference baseline.
- `LA-REF-002` — existing audited linear-algebra reference baseline.
- `LA-REF-003` — existing audited linear-algebra reference baseline.
- `LA-REF-004` — existing audited linear-algebra reference baseline.
