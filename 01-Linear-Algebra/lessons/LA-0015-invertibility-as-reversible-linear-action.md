---
id: LA-0015
title: "Invertibility as reversible linear action"
track: linear-algebra
level: L0
status: complete
curriculum_node: LA-N-0015
concepts_introduced: ["LA-C-0015"]
concepts_deepened: ["LA-C-0011", "LA-C-0012", "LA-C-0014"]
concepts_used: ["LA-C-0004", "LA-C-0005", "LA-C-0009", "LA-C-0010", "LA-C-0013"]
examples_added: ["LA-EX-055", "LA-EX-056", "LA-EX-057", "LA-EX-058", "LA-EX-059"]
references_used: ["LA-REF-001", "LA-REF-002", "LA-REF-003", "LA-REF-004"]
last_reviewed: 2026-08-28
version_sensitive: false
review_after: null
---
# Invertibility as reversible linear action

## If you landed here directly

This lesson assumes two earlier foundations:

- `LA-0011 — Elimination: changing equations without changing solutions`;
- `LA-0014 — Composition and matrix multiplication`.

You should already be able to:

- use row operations to solve a linear system;
- recognize when elimination leaves pivots or free variables;
- interpret a matrix as a linear transformation;
- interpret $AB$ as "first $B$, then $A$";
- use the identity matrix as the transformation that does nothing.

The new question is:

> when can a linear action be undone exactly?

The answer is **invertibility**.

The central mental model is:

```text
input x
→ transformation A
→ output y
→ inverse A⁻¹
→ original x
```

For a square matrix $A$, an inverse matrix $A^{-1}$ satisfies both:

$$ A^{-1}A=I $$

and:

$$ AA^{-1}=I. $$

By the end, you should be able to:

- explain invertibility as reversible action;
- connect an inverse transformation to a two-sided inverse matrix;
- explain why information loss makes inversion impossible;
- recognize simple invertible and non-invertible planar transformations;
- relate invertibility of a square matrix to unique solvability of $A\mathbf{x}=\mathbf{b}$ for every $\mathbf{b}$;
- connect invertibility to pivots and free variables using elimination;
- explain why square shape is necessary for an ordinary two-sided matrix inverse but is not sufficient;
- compute inverses of simple scaling, reflection, rotation, and shear transformations by reasoning about the action;
- explain why $(AB)^{-1}=B^{-1}A^{-1}$ when both inverses exist;
- distinguish matrix inversion from entrywise reciprocals and from transposition;
- explain why solving a system by explicitly forming an inverse is conceptually useful but is not always the preferred computational method.

---

# Part I — The problem worth understanding

Suppose a transformation stretches every horizontal coordinate by a factor of two while leaving vertical coordinates unchanged.

If:

```math
A=
\begin{bmatrix}
2 & 0 \\
0 & 1
\end{bmatrix},
```

then:

```math
A
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
2x \\
y
\end{bmatrix}.
```

Can we recover the original vector from the output?

Yes.

Halve the first coordinate:

```math
A^{-1}=
\begin{bmatrix}
\tfrac12 & 0 \\
0 & 1
\end{bmatrix}.
```

Then:

$$ A^{-1}(A\mathbf{x})=\mathbf{x}. $$

Nothing was erased.

The transformation changed the representation, but the original input remained recoverable.

That is the intuitive heart of invertibility.

---

# Part II — Reversible means one output remembers one input

If a transformation is invertible, distinct inputs cannot collapse to the same output.

Why?

Suppose:

$$ A\mathbf{x}_1=A\mathbf{x}_2. $$

If $A^{-1}$ exists, apply it to both sides:

$$ A^{-1}A\mathbf{x}_1=A^{-1}A\mathbf{x}_2. $$

Therefore:

$$ \mathbf{x}_1=\mathbf{x}_2. $$

So an invertible transformation does not merge two distinct inputs into one indistinguishable output.

This is the information-preservation viewpoint.

---

# Part III — The identity transformation is the target of undoing

The identity matrix leaves every vector unchanged.

In two dimensions:

```math
I=
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}.
```

For every vector $\mathbf{x}$:

$$ I\mathbf{x}=\mathbf{x}. $$

An inverse is therefore a transformation that composes with the original transformation to produce identity.

That is why:

$$ A^{-1}A=I $$

means:

```text
first A
then A⁻¹
=
do nothing overall
```

and:

$$ AA^{-1}=I $$

means the reverse composition also cancels.

For the ordinary square-matrix inverse, both directions matter.

---

# Part IV — Worked example LA-EX-055: a shear that can be undone

Consider a horizontal shear:

```math
S=
\begin{bmatrix}
1 & 3 \\
0 & 1
\end{bmatrix}.
```

It acts as:

```math
\begin{bmatrix}
x \\
y
\end{bmatrix}
\mapsto
\begin{bmatrix}
x+3y \\
y
\end{bmatrix}.
```

To undo it, subtract $3y$ from the first coordinate:

```math
S^{-1}=
\begin{bmatrix}
1 & -3 \\
0 & 1
\end{bmatrix}.
```

Check the product:

```math
S^{-1}S
=
\begin{bmatrix}
1 & -3 \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 3 \\
0 & 1
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}.
```

And in the other order:

```math
SS^{-1}
=
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}.
```

The shear deforms geometry but loses no information.

---

# Part V — Reversible geometric transformations

Several transformations from `LA-0013` are naturally invertible.

## Nonzero scaling

Scaling by a nonzero factor can be undone by scaling by its reciprocal.

For example:

```math
A=
\begin{bmatrix}
4 & 0 \\
0 & \tfrac12
\end{bmatrix}
```

has inverse:

```math
A^{-1}=
\begin{bmatrix}
\tfrac14 & 0 \\
0 & 2
\end{bmatrix}.
```

---

## Reflection

Reflect across the $x$-axis twice and you return to the original vector.

So for:

```math
R=
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix},
```

we have:

$$ R^{-1}=R. $$

---

## Rotation

Rotate by an angle $\theta$.

The inverse rotates by $-\theta$.

The geometry itself tells us the inverse action.

---

## Shear

A shear can be undone by an opposite shear, as in LA-EX-055.

---

# Part VI — Non-invertible means information was collapsed or lost

Now consider projection onto the $x$-axis:

```math
P=
\begin{bmatrix}
1 & 0 \\
0 & 0
\end{bmatrix}.
```

It maps:

```math
\begin{bmatrix}
x \\
y
\end{bmatrix}
\mapsto
\begin{bmatrix}
x \\
0
\end{bmatrix}.
```

Every input with the same $x$-coordinate becomes the same output.

For example:

```math
P
\begin{bmatrix}
2 \\
1
\end{bmatrix}
=
P
\begin{bmatrix}
2 \\
9
\end{bmatrix}
=
\begin{bmatrix}
2 \\
0
\end{bmatrix}.
```

Once the output is only $(2,0)$, no inverse can know whether the original second coordinate was $1$, $9$, or something else.

The information is gone.

---

# Part VII — Worked example LA-EX-056: projection cannot be reversed

Assume, for contradiction, that the projection matrix $P$ had an inverse $P^{-1}$.

We just found two different vectors $\mathbf{u}$ and $\mathbf{v}$ with:

$$ P\mathbf{u}=P\mathbf{v}. $$

Applying $P^{-1}$ would imply:

$$ \mathbf{u}=\mathbf{v}. $$

But they are visibly different.

Contradiction.

The failure is not a missing trick for computing the inverse.

There is **no inverse** because the forward transformation erased a distinction.

---

# Part VIII — Zero scaling is also irreversible

Consider:

```math
Z=
\begin{bmatrix}
1 & 0 \\
0 & 0
\end{bmatrix}.
```

This is the same projection structure as above.

The second coordinate is multiplied by zero.

Multiplication by zero cannot be undone by multiplying by a finite reciprocal.

This gives an important rule:

```text
nonzero scaling
can be reversible

zero scaling
collapses a direction
and is not reversible
```

---

# Part IX — Invertibility and solving Ax=b

Now return to systems of equations.

Suppose:

$$ A\mathbf{x}=\mathbf{b}. $$

If $A^{-1}$ exists, apply it to both sides:

$$ A^{-1}A\mathbf{x}=A^{-1}\mathbf{b}. $$

So:

$$ \mathbf{x}=A^{-1}\mathbf{b}. $$

This gives two important consequences.

For every allowed output vector $\mathbf{b}$:

1. a solution exists;
2. that solution is unique.

That is the equation-solving interpretation of invertibility.

---

# Part X — Why uniqueness follows immediately

Suppose two solutions existed:

$$ A\mathbf{x}_1=\mathbf{b} $$

and:

$$ A\mathbf{x}_2=\mathbf{b}. $$

Then:

$$ A\mathbf{x}_1=A\mathbf{x}_2. $$

Invertibility forces:

$$ \mathbf{x}_1=\mathbf{x}_2. $$

So an invertible matrix cannot give two different inputs for the same right-hand side.

---

# Part XI — Elimination reveals the same story

`LA-0011` and `LA-0012` described pivots and free variables.

For a square matrix, the beginner-level invertibility picture is:

```text
pivot in every variable column
and
no inconsistent row for any right-hand side
and
no free variables
```

When all square-matrix directions are pivot directions, solving $A\mathbf{x}=\mathbf{b}$ gives one value for every unknown.

When a free variable remains, multiple inputs can produce the same output difference structure.

When a required output direction cannot be reached, some $\mathbf{b}$ has no solution.

Invertibility is therefore the transformation-language version of complete unique solvability.

---

# Part XII — A square matrix is necessary but not sufficient

An ordinary two-sided inverse matrix must reverse a map from a coordinate space back to the same-size coordinate space.

That requires a square matrix.

But square shape alone does not guarantee invertibility.

For example:

```math
A=
\begin{bmatrix}
1 & 2 \\
2 & 4
\end{bmatrix}.
```

The second row is twice the first.

Elimination gives:

```math
\begin{bmatrix}
1 & 2 \\
0 & 0
\end{bmatrix}.
```

There is no pivot in the second variable column.

A free variable remains in the homogeneous problem.

So the matrix is square but not invertible.

---

# Part XIII — Worked example LA-EX-057: square but singular

Apply the matrix:

```math
A=
\begin{bmatrix}
1 & 2 \\
2 & 4
\end{bmatrix}
```

to the vector:

```math
\mathbf{v}=
\begin{bmatrix}
-2 \\
1
\end{bmatrix}.
```

We get:

```math
A\mathbf{v}
=
\begin{bmatrix}
0 \\
0
\end{bmatrix}.
```

But $\mathbf{v}$ is not the zero vector.

So at least two distinct inputs map to zero:

```text
zero vector
and
v
```

The map has collapsed a direction.

No two-sided inverse can exist.

This is the same geometric idea as projection, expressed through the columns and equations.

---

# Part XIV — Columns and recoverability

Recall from `LA-0010`:

```math
A\mathbf{x}
=x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n.
```

If the columns contain a redundancy that allows a nonzero coefficient vector to produce zero, then some input information disappears.

In the previous example:

```text
column 2 = 2 × column 1
```

so different coefficient pairs can create the same output.

Invertibility therefore requires more than having the right matrix shape.

The columns must encode each input coordinate without redundant collapse.

The formal language of linear independence will appear soon in L1.

---

# Part XV — Computing an inverse by solving for what undoes A

At this stage, do not treat inverse computation as a new magical formula.

The meaning comes first.

To find $A^{-1}$, ask:

```text
What transformation sends each output basis direction
back to the input basis direction that produced it?
```

Equivalently, the columns of $A^{-1}$ solve:

```math
A\mathbf{x}_1=\mathbf{e}_1,
\qquad
A\mathbf{x}_2=\mathbf{e}_2,
\quad \ldots
```

This connects inversion directly to solving systems.

---

# Part XVI — Augmented-matrix method

For a square matrix, one standard computational procedure is to row-reduce:

```math
\left[
\begin{array}{c|c}
A & I
\end{array}
\right].
```

If elimination transforms the left block into $I$, the right block becomes $A^{-1}$:

```math
\left[
\begin{array}{c|c}
A & I
\end{array}
\right]
\longrightarrow
\left[
\begin{array}{c|c}
I & A^{-1}
\end{array}
\right].
```

This is not an unrelated trick.

We are simultaneously solving:

```text
A x1 = e1
A x2 = e2
...
```

for all basis outputs.

---

# Part XVII — Worked example LA-EX-058: solving via inverse and elimination

Take:

```math
A=
\begin{bmatrix}
1 & 1 \\
0 & 2
\end{bmatrix},
\qquad
\mathbf{b}=
\begin{bmatrix}
5 \\
6
\end{bmatrix}.
```

From the triangular system:

```math
\begin{aligned}
x+y &= 5,\\
2y &= 6,
\end{aligned}
```

we get:

$$ y=3, $$

then:

$$ x=2. $$

Now reason about the inverse action.

The transformation is:

```text
(x,y)
→
(x+y, 2y)
```

To undo output $(u,v)$:

```text
y = v/2
x = u - v/2
```

so:

```math
A^{-1}=
\begin{bmatrix}
1 & -\tfrac12 \\
0 & \tfrac12
\end{bmatrix}.
```

Then:

```math
A^{-1}\mathbf{b}
=
\begin{bmatrix}
2 \\
3
\end{bmatrix}.
```

Both viewpoints give the same unique solution.

The inverse packages the solution rule for **every** right-hand side, not only this one.

---

# Part XVIII — Why we do not always solve systems by forming A⁻¹

The identity:

$$ \mathbf{x}=A^{-1}\mathbf{b} $$

is conceptually important.

But for actual computation, explicitly building the inverse is often unnecessary.

If you only need one solution $\mathbf{x}$, elimination or a suitable factorization can solve:

$$ A\mathbf{x}=\mathbf{b} $$

directly.

So distinguish:

```text
mathematical existence of A⁻¹
```

from:

```text
best numerical procedure for a particular problem
```

Later numerical-linear-algebra lessons will make this distinction precise.

---

# Part XIX — Inverse of a composition

Suppose:

```text
x
→ B
→ Bx
→ A
→ ABx
```

To undo the pipeline, what must happen first?

You must undo the **last** operation first.

So:

```text
AB pipeline:
first B, then A

undo:
first A⁻¹, then B⁻¹
```

The matrix for that undoing is:

$$ (AB)^{-1}=B^{-1}A^{-1}. $$

The order reverses.

---

# Part XX — Why the inverse order reverses

Check by composition:

```math
(B^{-1}A^{-1})(AB)
=
B^{-1}(A^{-1}A)B
=
B^{-1}IB
=I.
```

And:

```math
(AB)(B^{-1}A^{-1})
=
A(BB^{-1})A^{-1}
=AIA^{-1}
=I.
```

This is the same logic as taking off clothing layers:

```text
put on shirt
then jacket

undo:
remove jacket
then shirt
```

Composition order matters in both directions.

---

# Part XXI — Worked example LA-EX-059: undo a graphics pipeline

Let $B$ scale the $x$-coordinate by two:

```math
B=
\begin{bmatrix}
2 & 0 \\
0 & 1
\end{bmatrix}.
```

Let $A$ shear horizontally:

```math
A=
\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}.
```

The forward pipeline is:

```text
first B
then A
=
AB
```

The inverse pieces are:

```math
B^{-1}=
\begin{bmatrix}
\tfrac12 & 0 \\
0 & 1
\end{bmatrix}
```

and:

```math
A^{-1}=
\begin{bmatrix}
1 & -1 \\
0 & 1
\end{bmatrix}.
```

To recover the input from the final output, apply:

$$ B^{-1}A^{-1}. $$

That means:

```text
undo A first
then undo B
```

The order reversal is not a memorized symbol rule.

It follows from the pipeline.

---

# Part XXII — Inverse is not entrywise reciprocal

Suppose:

```math
A=
\begin{bmatrix}
1 & 1 \\
0 & 2
\end{bmatrix}.
```

The inverse from LA-EX-058 is:

```math
A^{-1}=
\begin{bmatrix}
1 & -\tfrac12 \\
0 & \tfrac12
\end{bmatrix}.
```

We did not take the reciprocal of every entry.

In fact, the zero entry would make that impossible.

Matrix inversion is about **composition**, not elementwise arithmetic.

---

# Part XXIII — Inverse is not transpose in general

The transpose $A^T$ swaps rows and columns.

That operation has a different definition.

For special transformations such as rotations and reflections represented by orthogonal matrices, the transpose happens to equal the inverse.

But in general:

$$ A^{-1}\ne A^T. $$

Do not infer invertibility from the existence of a transpose.

Every matrix has a transpose.

Not every square matrix has an inverse.

---

# Part XXIV — Rectangular matrices and the two-sided inverse

Consider a matrix that maps $\mathbb{R}^2$ into $\mathbb{R}^3$.

Its shape is $3\times2$.

A matrix in the reverse direction could have shape $2\times3$.

Could the two products both be identity matrices of their respective spaces?

Not in the ordinary finite-dimensional two-sided sense when the dimensions differ.

One direction would have to embed a lower-dimensional space into a higher-dimensional one; the other would have to recover every point of the higher-dimensional space from only the embedded subset.

Later lessons distinguish **left inverses**, **right inverses**, and the pseudoinverse.

For now:

> "invertible matrix" means an ordinary square matrix with a two-sided inverse unless stated otherwise.

---

# Part XXV — Invertible does not mean unchanged geometry

A transformation can dramatically alter:

- lengths;
- angles;
- areas;
- orientation;
- coordinate appearance;

and still be invertible.

Invertibility asks only whether the action can be undone uniquely.

A strong shear is invertible.

A severe nonzero stretch is invertible.

A reflection is invertible.

A projection can look visually mild but is not invertible because it destroys a dimension of information.

So:

```text
invertibility
is about recoverability
not visual similarity
```

---

# Part XXVI — Invertible does not mean numerically easy

A matrix can be mathematically invertible while being difficult to work with accurately in finite-precision computation.

For example, if two transformation directions are almost collapsed onto each other, tiny measurement or rounding errors can be greatly amplified when undoing the transformation.

That topic belongs to later lessons on:

- norms;
- condition numbers;
- forward and backward error;
- numerical stability.

For now, keep the distinction:

```text
inverse exists
≠
inverse is numerically benign
```

---

# Part XXVII — A practical beginner checklist

Given a square matrix or linear transformation, ask:

```text
1. Does the map visibly collapse a direction?
2. Can two different inputs produce the same output?
3. Does elimination produce a pivot for every variable?
4. Are there free variables?
5. Can every right-hand side be reached uniquely?
6. Can I describe an explicit undoing transformation?
7. Does composing the proposed inverse on both sides give identity?
```

These are not seven unrelated tests.

They are different views of one structural fact.

---

# Part XXVIII — Common failure modes

## Failure mode 1 — "Square means invertible"

False.

Square shape makes a two-sided inverse possible, not guaranteed.

---

## Failure mode 2 — "Every nonzero matrix is invertible"

False.

A matrix can have many nonzero entries and still collapse a direction.

---

## Failure mode 3 — "A⁻¹ means reciprocal of each entry"

False.

The inverse is defined through matrix multiplication and composition.

---

## Failure mode 4 — "A⁻¹ always equals Aᵀ"

False.

That equality occurs only for special matrices.

---

## Failure mode 5 — "If Ax=b has one solution for one b, A is invertible"

Not enough.

For square $A$, invertibility means unique solvability for **every** right-hand side.

---

## Failure mode 6 — "If I can solve Ax=b, I should compute A⁻¹"

Not necessarily.

Direct solution methods can be preferable.

---

## Failure mode 7 — "The inverse of AB is A⁻¹B⁻¹"

Usually wrong order.

The correct order is:

$$ (AB)^{-1}=B^{-1}A^{-1}. $$

---

## Failure mode 8 — "Projection should be invertible because I can draw the original object"

A drawing may use outside information.

The projected output itself does not contain the erased coordinate.

---

# Part XXIX — Active work

## Exercise 1 — Classify by geometry

For each transformation, decide whether it is invertible and state the inverse action if it exists:

1. rotate by $30^\circ$;
2. reflect across the $x$-axis;
3. project onto the $x$-axis;
4. scale both coordinates by $5$;
5. scale the $x$-coordinate by $0$ and the $y$-coordinate by $2$.

---

## Exercise 2 — Verify a proposed inverse

Let:

```math
A=
\begin{bmatrix}
1 & 4 \\
0 & 1
\end{bmatrix}.
```

Propose a matrix that undoes the shear.

Multiply in both orders and verify that you obtain identity.

---

## Exercise 3 — Elimination test

For:

```math
A=
\begin{bmatrix}
1 & 2 \\
3 & 6
\end{bmatrix},
```

perform one elimination step.

Explain the result in all three languages:

```text
pivots/free variables
transformation/recoverability
unique solvability
```

---

## Exercise 4 — Pipeline inverse

Suppose $C=AB$.

Write the order in which an input experiences $A$ and $B$.

Then write the order in which the output must experience $A^{-1}$ and $B^{-1}$ to recover the input.

---

## Exercise 5 — System solve

Use either elimination or inverse reasoning to solve:

```math
\begin{bmatrix}
2 & 0 \\
1 & 1
\end{bmatrix}
\mathbf{x}
=
\begin{bmatrix}
8 \\
7
\end{bmatrix}.
```

Then describe the inverse transformation in words.

---

## Exercise 6 — Information loss

Give two distinct vectors that projection onto the line $y=0$ maps to the same output.

Explain why that single example is enough to prove the projection is not invertible.

---

# Part XXX — Retrieval practice

Answer without looking back.

1. What does it mean for a linear transformation to be invertible?
2. Why do we require both $A^{-1}A=I$ and $AA^{-1}=I$ for an ordinary two-sided inverse?
3. Why can an invertible map not send two distinct inputs to the same output?
4. Why is projection not invertible?
5. Why is nonzero scaling invertible?
6. How does invertibility connect to $A\mathbf{x}=\mathbf{b}$?
7. What does elimination look like for an invertible square matrix?
8. Why is square shape not enough?
9. Why is $A^{-1}$ not an entrywise reciprocal?
10. Why does the inverse of a product reverse order?
11. Why might you solve $A\mathbf{x}=\mathbf{b}$ without explicitly forming $A^{-1}$?
12. What is the difference between mathematical invertibility and numerical stability?
13. Why does a rectangular matrix not have an ordinary two-sided inverse when the dimensions differ?
14. What geometric transformations from `LA-0013` are obviously reversible?
15. What does information loss have to do with invertibility?

---

# Part XXXI — Connection backward: LA-0011

`LA-0011` taught elimination as solution-preserving transformation of equations.

This lesson turns elimination into a structural diagnostic.

For a square matrix:

```text
full pivot structure
→ no free variables
→ one solution for every right-hand side
→ reversible action
```

The row-operation story and the transformation story describe the same matrix from different viewpoints.

---

# Part XXXII — Connection backward: LA-0012

`LA-0012` made pivots and free variables geometric.

A free variable means some direction of input is not uniquely determined by the constraints.

Invertibility asks for the opposite situation:

```text
no hidden input direction
no ambiguity
unique recovery
```

This is why `LA-N-0012` and `LA-N-0015` jointly unlock the L0 synthesis lesson.

---

# Part XXXIII — Connection backward: LA-0014

`LA-0014` made matrix multiplication into composition.

That is exactly the language needed to define an inverse:

```text
A followed by A⁻¹
=
identity
```

and to understand:

$$ (AB)^{-1}=B^{-1}A^{-1}. $$

Invertibility is therefore not an isolated matrix operation.

It is a property of transformations under composition.

---

# Part XXXIV — Connection to neural engineering

The paired neural-engineering lesson opens the electrode-tissue interface and asks how a physical signal is transformed before it reaches data.

Invertibility gives a useful systems distinction.

If a known linear stage merely distorts a signal without collapsing relevant information, an inverse or approximate correction may be possible.

If a measurement stage maps multiple physically different states to the same observation, no inverse can identify which state occurred without additional information or assumptions.

So:

```text
reversible distortion
and
irreversible information loss
```

are fundamentally different measurement problems.

---

# Part XXXV — What this unlocks

You should now be able to move among three equivalent beginner-level viewpoints:

```text
TRANSFORMATION VIEW
Can the action be undone uniquely?

SYSTEM VIEW
Does Ax=b have exactly one solution for every b?

ELIMINATION VIEW
Does the square system have complete pivot structure and no free variables?
```

The next canonical lesson is:

`LA-N-0016 — L0 synthesis: solve, transform, and explain one problem three ways`.

That lesson deliberately combines the equation, vector, and transformation viewpoints before the curriculum moves into L1 vector-space abstraction.

Publishing this lesson also satisfies one prerequisite of the later determinant lesson `LA-N-0032`, where invertibility will acquire a geometric volume-scaling test after dimension has been developed.

---

# References

- **LA-REF-001** — MIT OpenCourseWare, `18.06 Linear Algebra`.
- **LA-REF-002** — MIT OpenCourseWare, `18.06SC Linear Algebra`.
- **LA-REF-003** — Sheldon Axler, *Linear Algebra Done Right*, 4th ed.
- **LA-REF-004** — Stephen Boyd and Lieven Vandenberghe, *Introduction to Applied Linear Algebra — Vectors, Matrices, and Least Squares*.
