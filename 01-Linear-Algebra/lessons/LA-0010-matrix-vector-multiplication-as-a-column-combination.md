---
id: LA-0010
title: "Matrix-vector multiplication as a column combination"
track: linear-algebra
level: L0
status: complete
curriculum_node: LA-N-0010
concepts_introduced: ["LA-C-0010"]
concepts_deepened: ["LA-C-0009", "LA-C-0005", "LA-C-0006", "LA-C-0008"]
concepts_used: ["LA-C-0004", "LA-C-0003", "LA-C-0002", "LA-C-0001"]
examples_added: ["LA-EX-033", "LA-EX-034", "LA-EX-035", "LA-EX-036"]
references_used: ["LA-REF-001", "LA-REF-002", "LA-REF-003", "LA-REF-004"]
last_reviewed: 2026-08-27
version_sensitive: false
review_after: null
---

# Matrix-vector multiplication as a column combination

## If you landed here directly

This lesson assumes:

- `LA-0005 — Linear combinations and weighted mixtures`;
- `LA-0009 — Matrices as organized coefficients and operators`.

You should already know:

- what a linear combination is;
- what matrix rows and columns are;
- what an `m × n` matrix shape means;
- why the columns of a matrix can be viewed as generators;
- why a matrix can represent a linear operator.

Now we make the operator active.

The central question is:

> what does `A x` actually mean?

The most important answer is not:

> multiply row by column.

The deeper answer is:

> use the coordinates of `x` as weights on the columns of `A`, then add the weighted columns.

By the end, you should be able to:

- compute `A x` from the column-combination viewpoint;
- explain why the dimensions must match;
- connect `A x = b` to span membership;
- switch between column-combination and row-output views;
- interpret matrix-vector multiplication as a linear map from input coordinates to output coordinates;
- explain why each column is the output produced by one coordinate-direction input;
- recognize sparse-input and sparse-matrix effects;
- distinguish a matrix-vector product from elementwise multiplication;
- understand how a neural decoder or linear measurement model can be written as matrix-vector multiplication.

---

## The problem worth understanding

Suppose:

```math
A=
\begin{bmatrix}
2 & -1 & 3\\
1 & 4 & 0
\end{bmatrix},
\qquad
\mathbf{x}=
\begin{bmatrix}
5\\
2\\
-1
\end{bmatrix}.
```

The matrix has three columns:

```math
\mathbf{a}_1=
\begin{bmatrix}
2\\
1
\end{bmatrix},
\qquad
\mathbf{a}_2=
\begin{bmatrix}
-1\\
4
\end{bmatrix},
\qquad
\mathbf{a}_3=
\begin{bmatrix}
3\\
0
\end{bmatrix}.
```

The input vector gives three weights:

```text
5
2
-1
```

So:

$$ A\mathbf{x}=5\mathbf{a}_1+2\mathbf{a}_2-\mathbf{a}_3. $$

That is the conceptual definition.

Everything else is bookkeeping.

---

## Matrix-vector multiplication

Let:

$$ A\in\mathbb{R}^{m\times n}. $$

Let:

$$ \mathbf{x}\in\mathbb{R}^{n}. $$

Write the columns of `A` as:

```math
A=
\begin{bmatrix}
| & | & & |\\
\mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n\\
| & | & & |
\end{bmatrix}.
```

Then:

$$ A\mathbf{x}=x_1\mathbf{a}_1+x_2\mathbf{a}_2+\cdots+x_n\mathbf{a}_n. $$

This is the column-combination view.

---

## Why the number of columns must match the input length

If `A` has `n` columns, we need one scalar weight for each column.

So `x` must supply exactly:

```text
n coordinates
```

If:

```text
A:
m × n
```

then:

```text
x:
n × 1
```

is compatible.

The output is:

```text
m × 1
```

because every column of `A` has `m` entries.

---

## Shape rule

Conceptually:

```text
(m × n) times (n × 1)
→
(m × 1)
```

The inner dimension:

```text
n
```

matches because there are `n` input weights and `n` matrix columns.

The surviving dimension:

```text
m
```

is the output coordinate count.

---

## Example LA-EX-033 — compute by columns

Let:

```math
A=
\begin{bmatrix}
2 & -1 & 3\\
1 & 4 & 0
\end{bmatrix},
\qquad
\mathbf{x}=
\begin{bmatrix}
5\\
2\\
-1
\end{bmatrix}.
```

Then:

```math
A\mathbf{x}
=
5
\begin{bmatrix}
2\\
1
\end{bmatrix}
+
2
\begin{bmatrix}
-1\\
4
\end{bmatrix}
-
\begin{bmatrix}
3\\
0
\end{bmatrix}.
```

Compute:

```math
A\mathbf{x}
=
\begin{bmatrix}
10\\
5
\end{bmatrix}
+
\begin{bmatrix}
-2\\
8
\end{bmatrix}
+
\begin{bmatrix}
-3\\
0
\end{bmatrix}
=
\begin{bmatrix}
5\\
13
\end{bmatrix}.
```

The result lives in `R^2`.

That matches the two rows of `A`.

---

## The input coordinates are weights

This is the key mental model:

```text
x1
weights column 1

x2
weights column 2

...

xn
weights column n
```

Then the weighted columns are added.

So:

```text
input coordinates
→ weighting coefficients
→ output vector
```

---

## Matrix-vector multiplication is a linear combination

This is not a new kind of arithmetic object.

It reuses the operation from `LA-0005`.

The new feature is organization.

The matrix packages the vectors to be combined.

The input vector packages the weights.

So:

```text
matrix
+
input vector
→ organized linear combination
```

---

## Connection to span

Because:

$$ A\mathbf{x}=x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n, $$

every possible output `A x` lies in the span of the columns.

Therefore:

```text
all outputs A x
=
all linear combinations of columns of A
```

This becomes the **column space** later.

---

## System consistency becomes reachability

Consider:

$$ A\mathbf{x}=\mathbf{b}. $$

This asks:

> can the columns of `A` combine to produce `b`?

So:

```text
A x = b has a solution
⇔
b lies in span(columns of A)
```

This unifies systems and span.

---

## Example LA-EX-034 — solve a system as a column-combination question

Suppose:

```math
A=
\begin{bmatrix}
1 & 3\\
2 & -1
\end{bmatrix},
\qquad
\mathbf{b}=
\begin{bmatrix}
7\\
3
\end{bmatrix}.
```

Then:

$$ A\mathbf{x}=\mathbf{b} $$

means:

```math
x_1
\begin{bmatrix}
1\\
2
\end{bmatrix}
+
x_2
\begin{bmatrix}
3\\
-1
\end{bmatrix}
=
\begin{bmatrix}
7\\
3
\end{bmatrix}.
```

Coordinate-wise:

```math
\begin{aligned}
x_1+3x_2 &= 7,\\
2x_1-x_2 &= 3.
\end{aligned}
```

Same problem.

Three views:

```text
system of equations
column combination
matrix equation
```

---

## The row view is also valid

The column view explains the structure.

The row view explains each output coordinate.

For:

```math
A=
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix},
```

and:

```math
\mathbf{x}=
\begin{bmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{bmatrix},
```

the first output coordinate is:

$$ y_1=a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n. $$

The second is:

$$ y_2=a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n. $$

And so on.

---

## Row view versus column view

Same product:

$$ \mathbf{y}=A\mathbf{x}. $$

### Column view

```text
combine columns using x as weights
```

### Row view

```text
each row computes one output coordinate
```

Both are correct.

The column view is often more conceptually powerful at this stage.

---

## Why "row times column" is incomplete teaching

The phrase:

```text
row times column
```

helps compute entries.

But it can hide:

- why dimensions match;
- why output lies in the column span;
- why matrix columns are operator responses;
- how systems connect to span.

So use the row recipe as an arithmetic view.

Do not let it replace the column-combination model.

---

## Operator interpretation

Suppose:

$$ A\in\mathbb{R}^{m\times n}. $$

Then `A` represents a linear rule:

```text
R^n → R^m
```

in the chosen coordinates.

Input:

```text
n coordinates
```

Output:

```text
m coordinates
```

---

## Each column is the response to one coordinate direction

Let:

```math
\mathbf{e}_1=
\begin{bmatrix}
1\\
0\\
\vdots\\
0
\end{bmatrix}.
```

Then:

$$ A\mathbf{e}_1=\mathbf{a}_1. $$

Similarly:

$$ A\mathbf{e}_2=\mathbf{a}_2. $$

So column `j` is the output generated by input direction `e_j`.

This is a major idea.

---

## Why columns determine the operator

Any input can be written:

$$ \mathbf{x}=x_1\mathbf{e}_1+\cdots+x_n\mathbf{e}_n. $$

Linearity gives:

```math
A\mathbf{x}
=
x_1A\mathbf{e}_1+\cdots+x_nA\mathbf{e}_n.
```

But:

$$ A\mathbf{e}_j=\mathbf{a}_j. $$

Therefore:

$$ A\mathbf{x}=x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n. $$

So once you know all columns, you know the operator's action on every input.

---

## Linear means combinations pass through predictably

Matrix-vector multiplication satisfies:

$$ A(\mathbf{u}+\mathbf{v})=A\mathbf{u}+A\mathbf{v}. $$

And:

$$ A(c\mathbf{u})=cA\mathbf{u}. $$

Therefore:

$$ A(c_1\mathbf{u}+c_2\mathbf{v})=c_1A\mathbf{u}+c_2A\mathbf{v}. $$

This is linearity.

---

## Why this matters

If a transformation is linear, knowing its effect on basis directions is enough.

You do not need to store a separate output rule for every possible input.

The columns store the essential coordinate information.

---

## Example: coordinate scaling

Let:

```math
A=
\begin{bmatrix}
2 & 0\\
0 & 3
\end{bmatrix}.
```

Then:

```math
A
\begin{bmatrix}
x\\
y
\end{bmatrix}
=
x
\begin{bmatrix}
2\\
0
\end{bmatrix}
+
y
\begin{bmatrix}
0\\
3
\end{bmatrix}
=
\begin{bmatrix}
2x\\
3y
\end{bmatrix}.
```

So:

```text
x-coordinate scaled by 2
y-coordinate scaled by 3
```

---

## Identity matrix

For:

```math
I=
\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix},
```

we have:

```math
I
\begin{bmatrix}
x\\
y
\end{bmatrix}
=
x
\begin{bmatrix}
1\\
0
\end{bmatrix}
+
y
\begin{bmatrix}
0\\
1
\end{bmatrix}
=
\begin{bmatrix}
x\\
y
\end{bmatrix}.
```

Identity leaves the input unchanged.

---

## Zero matrix

For a zero matrix:

```math
0=
\begin{bmatrix}
0 & 0\\
0 & 0
\end{bmatrix},
```

every column is zero.

Therefore every input combination gives:

```math
0\mathbf{x}=
\begin{bmatrix}
0\\
0
\end{bmatrix}.
```

The operator erases all input directions.

---

## Sparse input

Suppose:

```math
\mathbf{x}=
\begin{bmatrix}
0\\
5\\
0\\
-2
\end{bmatrix}.
```

Then only columns 2 and 4 contribute.

So:

$$ A\mathbf{x}=5\mathbf{a}_2-2\mathbf{a}_4. $$

Sparse inputs can make interpretation especially simple.

---

## Sparse matrix

If many matrix entries are zero, each output coordinate may depend on only a subset of inputs.

This can represent limited coupling.

Example:

```math
A=
\begin{bmatrix}
2 & 0 & 0\\
0 & 3 & 0\\
1 & 0 & 4
\end{bmatrix}.
```

Output 1 depends only on input 1.

Output 2 depends only on input 2.

Output 3 depends on inputs 1 and 3.

---

## Sparse does not mean weak

A sparse matrix can contain large nonzero coefficients.

Sparse means:

```text
many zeros
```

not:

```text
small influence
```

---

## Dense does not mean more expressive in every sense

A dense matrix has many nonzero entries.

But:

- columns can still be dependent;
- rank can still be low;
- information can still be lost.

Density and rank are different ideas.

---

## Weight interpretation

In an engineered linear model, entry:

$$ a_{ij} $$

can be interpreted as:

> contribution of input coordinate `j` to output coordinate `i`.

This is useful in:

- decoders;
- regressions;
- linear filters.

But interpretation depends on scaling and feature definitions.

---

## Example LA-EX-035 — neural decoder

Suppose neural features are:

```math
\mathbf{r}=
\begin{bmatrix}
r_1\\
r_2\\
r_3\\
r_4
\end{bmatrix}.
```

A decoder produces two outputs:

```math
\hat{\mathbf{y}}
=
W\mathbf{r},
```

with:

```math
W=
\begin{bmatrix}
0.5 & -0.2 & 0.1 & 0.3\\
-0.1 & 0.4 & 0.6 & 0.2
\end{bmatrix}.
```

Then:

```text
4 neural features
→ 2 decoded coordinates
```

Column `j` tells how feature `r_j` contributes to both outputs.

This is an engineered linear model.

It does not mean each column is one biological synapse.

---

## Decoder columns

Suppose:

```math
\mathbf{w}_3=
\begin{bmatrix}
0.1\\
0.6
\end{bmatrix}.
```

This is column 3.

If only feature 3 were active with value 1:

```math
\mathbf{r}=
\begin{bmatrix}
0\\
0\\
1\\
0
\end{bmatrix},
```

then:

$$ W\mathbf{r}=\mathbf{w}_3. $$

This makes column meaning concrete.

---

## Sensor mixing model

Suppose hidden sources are:

```math
\mathbf{s}=
\begin{bmatrix}
s_1\\
s_2\\
s_3
\end{bmatrix}.
```

Sensors observe:

$$ \mathbf{y}=A\mathbf{s}. $$

Then columns of `A` describe how each source appears across sensors.

This is a common linear-mixture model.

---

## One source active

If only source 2 is active:

```math
\mathbf{s}=
\begin{bmatrix}
0\\
c\\
0
\end{bmatrix},
```

then:

$$ \mathbf{y}=c\mathbf{a}_2. $$

The measured sensor pattern is a scaled copy of column 2.

This interpretation appears in source-separation problems.

---

## Multiple sources active

If several sources are active:

$$ \mathbf{y}=s_1\mathbf{a}_1+s_2\mathbf{a}_2+s_3\mathbf{a}_3. $$

The sensor vector is a mixture of source signatures.

This is exactly a column combination.

---

## Linear mixing is a model assumption

Real sensors may have:

- nonlinearities;
- saturation;
- time filtering;
- noise.

So:

$$ \mathbf{y}=A\mathbf{s} $$

is an approximation under assumptions.

Linear algebra gives the model structure.

It does not guarantee the physical world is perfectly linear.

---

## Example LA-EX-036 — two sources and three sensors

Let:

```math
A=
\begin{bmatrix}
1 & 0.2\\
0.5 & 1\\
-0.2 & 0.7
\end{bmatrix},
\qquad
\mathbf{s}=
\begin{bmatrix}
2\\
3
\end{bmatrix}.
```

Then:

```math
\mathbf{y}
=
2
\begin{bmatrix}
1\\
0.5\\
-0.2
\end{bmatrix}
+
3
\begin{bmatrix}
0.2\\
1\\
0.7
\end{bmatrix}.
```

So:

```math
\mathbf{y}
=
\begin{bmatrix}
2\\
1\\
-0.4
\end{bmatrix}
+
\begin{bmatrix}
0.6\\
3\\
2.1
\end{bmatrix}
=
\begin{bmatrix}
2.6\\
4\\
1.7
\end{bmatrix}.
```

Three sensor outputs arise from two source weights.

---

## Tall matrix interpretation

If:

$$ A\in\mathbb{R}^{5\times2}, $$

then two input coordinates produce five output coordinates.

There are two columns.

Each column is a 5-coordinate output pattern.

Input `x` chooses a weighted mixture of those two patterns.

---

## Wide matrix interpretation

If:

$$ A\in\mathbb{R}^{2\times5}, $$

then five input coordinates produce two output coordinates.

There are five columns in `R^2`.

The output is a combination of five 2D generators.

Many input combinations can potentially lead to the same output if the columns are redundant.

---

## Square matrix interpretation

If:

$$ A\in\mathbb{R}^{n\times n}, $$

input and output coordinate counts match.

But that does not imply:

- invertibility;
- no information loss;
- unique input recovery.

Column dependence still matters.

---

## Recovering x from A x

Forward problem:

$$ \mathbf{x}\rightarrow A\mathbf{x}. $$

Inverse question:

> given `A` and output `b`, can we recover `x`?

That depends on:

- whether `b` is reachable;
- whether multiple `x` values produce the same output;
- invertibility/rank structure.

Later lessons formalize this.

---

## Null directions preview

If a nonzero vector `x` satisfies:

$$ A\mathbf{x}=\mathbf{0}, $$

then the input direction is erased by the matrix.

That is a **null-space** idea.

We will study it later.

---

## Same output from different inputs

If:

$$ A\mathbf{x}_1=A\mathbf{x}_2, $$

then:

$$ A(\mathbf{x}_1-\mathbf{x}_2)=\mathbf{0}. $$

So differences between inputs can disappear if they lie in a null direction.

This is information loss.

---

## Column dependence creates nonunique weights

Suppose:

$$ \mathbf{a}_3=\mathbf{a}_1+\mathbf{a}_2. $$

Then:

```text
1*a3
```

produces the same output as:

```text
1*a1 + 1*a2
```

So different input coordinates can yield the same output.

This foreshadows linear dependence.

---

## Input coordinates depend on representation

The entries of `x` are coordinates in a chosen basis or feature convention.

Change the basis.

The matrix and coordinates change together.

The abstract linear map may remain the same.

That deeper distinction comes later.

---

## Matrix-vector product versus elementwise product

Suppose:

```math
A=
\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix},
\qquad
\mathbf{x}=
\begin{bmatrix}
5\\
6
\end{bmatrix}.
```

Standard matrix-vector product:

```math
A\mathbf{x}
=
\begin{bmatrix}
1(5)+2(6)\\
3(5)+4(6)
\end{bmatrix}
=
\begin{bmatrix}
17\\
39
\end{bmatrix}.
```

This is not:

```text
multiply matching entries only
```

There is no ordinary elementwise matrix-vector operation with the same meaning.

---

## Broadcasting is a software feature, not matrix algebra

Some numerical libraries automatically "broadcast" arrays.

For example, a vector can be added to each matrix row.

That is useful.

But broadcasting rules are programming conventions.

They are not the definition of matrix-vector multiplication.

---

## Shape mismatch should be interpreted

Suppose:

```text
A:
3 × 4

x:
5 × 1
```

The product is invalid under standard matrix multiplication.

Why?

There are:

```text
4 columns
```

but:

```text
5 input weights
```

The semantic interface is inconsistent.

---

## Padding is not a mathematical fix by default

Do not silently append zeros just to make dimensions match.

Padding changes the modeled input space.

If padding is justified, state why.

---

## Transpose changes the mapping direction

If:

$$ A\in\mathbb{R}^{m\times n}, $$

then:

$$ A^T\in\mathbb{R}^{n\times m}. $$

So:

```text
A:
R^n → R^m

A^T:
R^m → R^n
```

in coordinate-shape terms.

The transpose is not the inverse in general.

---

## A transpose is not an undo operation

Even when dimensions reverse, generally:

$$ A^TA\neq I. $$

So do not infer:

```text
transpose
=
reverse transformation
```

The inverse concept comes later.

---

## Row output as weighted sum of inputs

Take row `i`:

```text
[a_i1, a_i2, ..., a_in]
```

Then output coordinate `i` is:

$$ y_i=\sum_{j=1}^n a_{ij}x_j. $$

So each output is a weighted sum of inputs.

This is the row perspective.

---

## Column output as weighted sum of response patterns

Take columns:

```text
a1, a2, ..., an
```

Then:

$$ \mathbf{y}=\sum_{j=1}^n x_j\mathbf{a}_j. $$

So the whole output vector is a weighted sum of column response patterns.

This is the column perspective.

---

## Same algebra, different questions

Row view answers:

> how is output coordinate `i` computed?

Column view answers:

> how does input coordinate `j` contribute to the whole output pattern?

Both are valuable in interpretation.

---

## Feature attribution caution

In a linear model, large matrix entry magnitude can indicate a strong coefficient.

But coefficient magnitude can depend on:

- feature scaling;
- correlated inputs;
- units.

So a large weight is not automatically the most scientifically important feature.

---

## Standardization changes coefficient meaning

If one feature is measured in:

```text
volts
```

and another in:

```text
microvolts
```

their coefficients may differ greatly because of units.

Scaling inputs changes numerical weights.

Matrix interpretation must preserve units.

---

## Units in matrix-vector multiplication

Suppose:

```text
x:
sensor voltages

A:
decoder coefficients
```

Then each row's weighted sum must produce the correct output unit.

Dimensional analysis still matters.

Shape alone is not enough.

---

## Affine models preview

Many practical models use:

$$ \mathbf{y}=A\mathbf{x}+\mathbf{b}. $$

The `A x` part is linear.

The added offset `b` makes the full map affine rather than purely linear.

This distinction matters later.

---

## Bias in neural networks

A linear layer is often written:

$$ \mathbf{y}=W\mathbf{x}+\mathbf{b}. $$

Software may call this a "linear layer."

Mathematically, if `b` is nonzero, the complete mapping is affine.

The matrix multiplication remains the central linear part.

---

## Batch processing preview

Suppose many input vectors are processed at once.

They can be stacked into a matrix.

Then matrix-matrix multiplication applies the same operator to many inputs efficiently.

That comes later.

---

## Why column convention matters

Throughout this course, input vectors are usually columns.

So:

```text
A x
```

means matrix on the left, vector on the right.

Some software or fields use row-vector conventions.

The formulas then transpose.

Conventions are not truths.

Consistency is essential.

---

## Common failure mode: multiply every entry of A by every entry of x

No.

Each coordinate of `x` scales one column.

---

## Common failure mode: row-times-column is the only meaning

It is a valid computational view, but the column-combination interpretation exposes deeper structure.

---

## Common failure mode: inner dimensions match because of a memorized rule

The deeper reason:

```text
one weight per column
```

---

## Common failure mode: A x can leave the column span

Impossible.

`A x` is literally a linear combination of columns.

---

## Common failure mode: A x = b always has a solution

Only if `b` lies in the column span.

---

## Common failure mode: square A means x can always be recovered

No.

A square matrix can still collapse directions.

---

## Common failure mode: transpose reverses A

No.

Transpose changes row/column orientation but is not generally an inverse.

---

## Common failure mode: matrix-vector multiplication proves the physical system is linear

No.

It is a model or mathematical operation.

Physical validity depends on assumptions.

---

## Common failure mode: a decoder weight is a synaptic weight

No.

Engineered model coefficients and biological synaptic strengths are different objects.

---

## Common failure mode: large coefficient means causal importance

No.

Scaling and input correlation can affect coefficients.

---

## Common failure mode: software broadcasting is matrix algebra

No.

Broadcasting is a library convention.

---

## Active work

### Exercise 1 — column combination

Given:

```math
A=
\begin{bmatrix}
1 & 2\\
3 & -1\\
0 & 4
\end{bmatrix},
\qquad
\mathbf{x}=
\begin{bmatrix}
5\\
-2
\end{bmatrix},
```

compute `A x` using columns only.

### Exercise 2 — shape reasoning

For each pair, decide whether the product is valid:

```text
(3 × 4)(4 × 1)
(3 × 4)(3 × 1)
(2 × 5)(5 × 1)
(5 × 2)(2 × 1)
```

Explain using:

> one input weight per matrix column.

### Exercise 3 — row and column views

For:

```math
A=
\begin{bmatrix}
1 & -1\\
2 & 3
\end{bmatrix},
\qquad
\mathbf{x}=
\begin{bmatrix}
4\\
5
\end{bmatrix},
```

compute the output:

- once by column combination;
- once by rows.

Verify the same result.

### Exercise 4 — span membership

Given:

```math
A=
\begin{bmatrix}
1 & 0\\
0 & 1\\
1 & 1
\end{bmatrix},
```

ask whether:

```math
\mathbf{b}=
\begin{bmatrix}
2\\
3\\
5
\end{bmatrix}
```

can equal `A x`.

Translate the question into a column-span statement.

### Exercise 5 — basis directions

For a 3 × 2 matrix `A`, compute conceptually:

```text
A e1
A e2
```

What do these outputs tell you about the columns?

### Exercise 6 — sparse input

If:

```math
\mathbf{x}=
\begin{bmatrix}
0\\
0\\
7\\
0
\end{bmatrix},
```

what is `A x` in terms of matrix columns?

### Exercise 7 — neural decoder

A matrix:

```text
2 × 8
```

maps eight neural features to two outputs.

Explain:

- what one column means;
- what one row means;
- what one entry means.

### Exercise 8 — model limitation

Give one physical system where:

```text
y ≈ A x
```

could be useful locally but fail globally because of nonlinearity or saturation.

---

## Retrieval check

Without looking back:

1. What is the column-combination definition of `A x`?
2. If `A` is `m × n`, how many entries must `x` have?
3. What dimension is `A x`?
4. Why must the inner dimension match?
5. What role does `x_j` play?
6. What role does column `a_j` play?
7. Why is `A x` always in the column span?
8. What does `A x = b` ask geometrically?
9. When is `A x = b` consistent?
10. What is the row view of `A x`?
11. What is the column view?
12. Why are both equivalent?
13. What is `A e_j`?
14. Why do columns determine a linear operator?
15. What does linearity mean for sums?
16. What does linearity mean for scalar multiples?
17. What does identity do?
18. What does the zero matrix do?
19. What happens with a sparse input?
20. What can a sparse matrix encode?
21. Does sparse mean weak?
22. Does dense mean full rank?
23. What does a tall matrix do to coordinate counts?
24. What does a wide matrix do?
25. Why can different inputs produce the same output?
26. What is a null-direction preview?
27. Why can column dependence create nonunique weights?
28. What is the difference between matrix-vector and elementwise multiplication?
29. What is broadcasting?
30. Why is a shape mismatch conceptually meaningful?
31. Why is padding not automatically valid?
32. What does transpose do to dimensions?
33. Why is transpose not inverse?
34. How does one row compute one output coordinate?
35. How does one column describe one input coordinate's whole output pattern?
36. What is a linear mixing model?
37. What do columns mean in a source-mixing matrix?
38. What does a neural decoder matrix represent?
39. Why is a decoder weight not a synaptic weight?
40. Why can coefficient magnitude mislead?
41. Why do units matter?
42. What is an affine model?
43. What role does `A x` play inside `A x + b`?
44. Why does column-vector convention matter?
45. What conceptual topic comes next after matrix-vector multiplication?

---

## Connection backward: LA-0009

`LA-0009` introduced:

```text
matrix as organized columns
```

and:

```text
m × n
→ n-coordinate input
→ m-coordinate output
```

This lesson makes that interface operational:

```text
input coordinates
→ scale columns
→ add
→ output vector
```

---

## Connection backward: LA-0005

`LA-0005` introduced linear combinations.

This lesson simply packages them:

```text
generators
→ matrix columns

weights
→ input vector

weighted mixture
→ A x
```

So matrix-vector multiplication is not conceptually separate from linear combination.

---

## Connection backward: LA-0008

A system:

$$ A\mathbf{x}=\mathbf{b} $$

now has two simultaneous interpretations:

```text
row view:
x satisfies every equation

column view:
columns of A combine to reach b
```

This is a major unification.

---

## Connection forward: LA-N-0011

One ready branch after this lesson is elimination.

Elimination changes rows while preserving the system solution set.

This uses the row view.

---

## Connection forward: LA-N-0013

Another branch studies plane transformations.

That uses the operator view:

```text
input vector
→ A
→ transformed vector
```

The columns will show where basis directions move.

---

## Connection forward: column space

Later:

```text
column space
=
all possible A x
```

The concept is already visible here.

We postpone the formal subspace language until the prerequisites are ready.

---

## Connection to neural engineering

A linear neural decoder can be written:

$$ \hat{\mathbf{y}}=W\mathbf{r}. $$

Here:

```text
r:
neural feature vector

W:
decoder matrix

y-hat:
estimated behavior / control output
```

The product is a weighted combination of decoder columns.

This gives a clean mathematical language for multi-channel neural features.

---

## Connection to neural signal mixing

An electrode array can be approximated by:

$$ \mathbf{y}=A\mathbf{s}+\boldsymbol{\varepsilon}. $$

Here:

- `s` represents source amplitudes;
- columns of `A` represent source signatures across sensors;
- `ε` represents noise/model mismatch.

This connects directly to the measurement ideas in `NNE-0008`.

---

## What this unlocks

You should now be able to look at:

$$ A\mathbf{x} $$

and immediately think:

```text
one scalar input coordinate
per matrix column

scale each column
add the results

output lives in the column span
```

You should also be able to switch to:

```text
one matrix row
→ one weighted output coordinate
```

without losing the deeper column-combination meaning.

That is the conceptual foundation needed for elimination, transformations, column space, and matrix composition.

---

## References

- **LA-REF-001** — MIT OpenCourseWare, `18.06 Linear Algebra`.
- **LA-REF-002** — MIT OpenCourseWare, `18.06SC Linear Algebra`.
- **LA-REF-003** — Sheldon Axler, *Linear Algebra Done Right*, 4th ed.
- **LA-REF-004** — Stephen Boyd and Lieven Vandenberghe, *Introduction to Applied Linear Algebra — Vectors, Matrices, and Least Squares*.
