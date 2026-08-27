---
id: LA-0009
title: "Matrices as organized coefficients and operators"
track: linear-algebra
level: L0
status: complete
curriculum_node: LA-N-0009
concepts_introduced: ["LA-C-0009"]
concepts_deepened: ["LA-C-0008", "LA-C-0007", "LA-C-0006"]
concepts_used: ["LA-C-0005", "LA-C-0004", "LA-C-0003", "LA-C-0002", "LA-C-0001"]
examples_added: ["LA-EX-029", "LA-EX-030", "LA-EX-031", "LA-EX-032"]
references_used: ["LA-REF-001", "LA-REF-002", "LA-REF-003", "LA-REF-004"]
last_reviewed: 2026-08-27
version_sensitive: false
review_after: null
---

# Matrices as organized coefficients and operators

## If you landed here directly

This lesson assumes `LA-0008`.

You should already know that a system of linear equations is a set of simultaneous constraints.

For example:

```math
\begin{aligned}
2x+y &= 5,\\
x-y &= 1.
\end{aligned}
```

contains repeated coefficient structure:

```text
row 1 coefficients: 2, 1
row 2 coefficients: 1, -1
```

Writing many large systems this way becomes cumbersome.

A matrix solves that organizational problem.

But a matrix is more than a coefficient table.

It can also represent a linear transformation or operator.

That dual role is the main subject of this lesson.

By the end, you should be able to:

- read matrix notation;
- identify rows, columns, entries, and shape;
- interpret `m × n`;
- organize a linear system into a coefficient matrix;
- distinguish a coefficient matrix from an augmented matrix;
- distinguish matrix-as-data from matrix-as-operator;
- explain why row meaning and column meaning differ;
- recognize square, tall, wide, zero, and identity matrices;
- understand why dimensions constrain valid operations;
- explain the input/output meaning of an `m × n` operator;
- prepare for matrix-vector multiplication as a column combination.

---

## The problem worth understanding

Consider:

```math
\begin{aligned}
2x_1 - x_2 + 3x_3 &= 7,\\
4x_1 + 5x_2 - 2x_3 &= 1,\\
-x_1 + 2x_2 + x_3 &= 0.
\end{aligned}
```

The coefficients form a rectangular pattern.

Instead of repeatedly writing variable names, collect the coefficients:

```math
A=
\begin{bmatrix}
2 & -1 & 3\\
4 & 5 & -2\\
-1 & 2 & 1
\end{bmatrix}.
```

This array is a **matrix**.

It organizes the coefficients.

But later the same object can act on a vector.

So:

```text
matrix
=
organized array
and, depending on interpretation,
linear operator representation
```

---

## What is a matrix?

A **matrix** is a rectangular array of entries arranged in rows and columns.

Example:

```math
A=
\begin{bmatrix}
2 & 5 & -1\\
0 & 3 & 4
\end{bmatrix}.
```

This matrix has:

- 2 rows;
- 3 columns;
- 6 entries.

Its shape is:

$$ 2\times3. $$

Read this as:

> two rows by three columns.

---

## Row first, column second

The convention is:

```text
m × n
=
m rows
n columns
```

Not the reverse.

For:

```math
A=
\begin{bmatrix}
a & b & c\\
d & e & f
\end{bmatrix},
```

the shape is:

$$ 2\times3. $$

This convention matters constantly.

---

## Matrix entries

An individual entry is often written:

$$ a_{ij}. $$

Here:

- `i` is the row index;
- `j` is the column index.

So:

$$ a_{23} $$

means:

> row 2, column 3.

For:

```math
A=
\begin{bmatrix}
4 & 1 & 9\\
7 & 3 & 5
\end{bmatrix},
```

we have:

$$ a_{23}=5. $$

---

## Indexing is semantic bookkeeping

Indices are not decorative subscripts.

They identify location.

In code-like language:

```text
a_23
→ row 2
→ column 3
```

Later, indices will help express:

- matrix-vector multiplication;
- matrix multiplication;
- sums;
- linear maps.

---

## Row

A **row** is a horizontal list of entries.

For:

```math
A=
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix},
```

row 1 is:

```text
[1, 2, 3]
```

row 2 is:

```text
[4, 5, 6]
```

Rows often correspond to:

- equations;
- observations;
- output coordinates;
- constraints;

depending on the model.

---

## Column

A **column** is a vertical list.

For the same matrix:

```math
A=
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix},
```

column 1 is:

```math
\begin{bmatrix}
1\\
4
\end{bmatrix}
```

column 2 is:

```math
\begin{bmatrix}
2\\
5
\end{bmatrix}
```

column 3 is:

```math
\begin{bmatrix}
3\\
6
\end{bmatrix}
```

Columns often correspond to:

- variables;
- features;
- generators;
- operator responses to coordinate directions.

Again, context determines meaning.

---

## Example LA-EX-029 — turn a system into a matrix

Start with:

```math
\begin{aligned}
2x_1 + 3x_2 &= 7,\\
-x_1 + 4x_2 &= 5.
\end{aligned}
```

Coefficient matrix:

```math
A=
\begin{bmatrix}
2 & 3\\
-1 & 4
\end{bmatrix}.
```

Unknown vector:

```math
\mathbf{x}=
\begin{bmatrix}
x_1\\
x_2
\end{bmatrix}.
```

Right-hand side:

```math
\mathbf{b}=
\begin{bmatrix}
7\\
5
\end{bmatrix}.
```

Later we will write:

$$ A\mathbf{x}=\mathbf{b}. $$

The matrix stores coefficient structure.

---

## Coefficient matrix

The **coefficient matrix** contains only coefficients multiplying unknowns.

For:

```math
\begin{aligned}
2x+y &= 7,\\
3x-4y &= 1,
\end{aligned}
```

the coefficient matrix is:

```math
\begin{bmatrix}
2 & 1\\
3 & -4
\end{bmatrix}.
```

The constants `7,1` are not part of the coefficient matrix.

---

## Augmented matrix

An **augmented matrix** appends the right-hand-side values:

```math
\left[
\begin{array}{cc|c}
2 & 1 & 7\\
3 & -4 & 1
\end{array}
\right].
```

The vertical bar is visual notation.

It separates:

```text
coefficients
|
right-hand side
```

This form becomes useful for elimination.

---

## The vertical bar is not another algebraic operation

The bar in an augmented matrix is organizational.

It does not mean:

- division;
- determinant;
- absolute value.

It marks the boundary between coefficient data and constants.

---

## Row meaning in a system

For a coefficient matrix from:

```math
\begin{aligned}
2x+y &= 7,\\
3x-4y &= 1,
\end{aligned}
```

row 1:

```text
[2, 1]
```

represents one constraint.

Row 2:

```text
[3, -4]
```

represents another.

So in the equation-system view:

```text
row
→ one linear equation
```

---

## Column meaning in a system

The same matrix:

```math
A=
\begin{bmatrix}
2 & 1\\
3 & -4
\end{bmatrix}
```

has columns:

```math
\mathbf{a}_1=
\begin{bmatrix}
2\\
3
\end{bmatrix},
\qquad
\mathbf{a}_2=
\begin{bmatrix}
1\\
-4
\end{bmatrix}.
```

Later:

$$ A\mathbf{x} $$

will mean:

$$ x_1\mathbf{a}_1+x_2\mathbf{a}_2. $$

So:

```text
row view
→ constraints

column view
→ generators
```

Same matrix.

Different interpretation.

---

## This duality is central

Linear algebra repeatedly switches between:

```text
rows:
what constraints must the input satisfy?

columns:
what output can combinations reach?
```

Do not memorize matrices only as rectangular number grids.

Learn to ask:

> what does each axis mean?

---

## Matrix shape carries structural information

Suppose:

$$ A\in\mathbb{R}^{m\times n}. $$

This means:

```text
m rows
n columns
```

If used as a linear operator, it naturally interacts with an `n`-coordinate input and produces an `m`-coordinate output.

Conceptually:

```text
n input coordinates
→ A
→ m output coordinates
```

The formal multiplication comes next.

---

## Why columns match input coordinates

An input vector with `n` coordinates has `n` scalar weights.

Those weights combine the `n` columns of `A`.

Therefore:

```text
number of columns
=
number of input coefficients
```

This is the deepest shape intuition for matrix-vector multiplication.

---

## Why rows match output coordinates

Each output coordinate is determined by one row's coefficient pattern.

Therefore:

```text
number of rows
=
number of output coordinates
```

So:

```text
A is m × n
→ n-dimensional coordinate input
→ m-dimensional coordinate output
```

when `A` is interpreted as an operator.

---

## Example LA-EX-030 — shape as input/output contract

Let:

```math
A=
\begin{bmatrix}
1 & 2 & 0\\
-1 & 4 & 3
\end{bmatrix}.
```

Shape:

$$ 2\times3. $$

Interpretation as operator:

```text
input:
3 coordinates

output:
2 coordinates
```

A 4-coordinate input does not match the three columns.

A 3-coordinate input does.

Shape is therefore an **interface contract**.

---

## Matrix as data

A matrix can simply organize a rectangular dataset.

Example:

```math
X=
\begin{bmatrix}
170 & 65 & 28\\
182 & 80 & 34\\
160 & 55 & 22
\end{bmatrix}.
```

Depending on convention:

```text
rows:
people

columns:
height, weight, age
```

This matrix is being used as a data table.

It is not automatically a linear transformation.

---

## Matrix as operator

Another matrix may represent a rule mapping one vector to another.

Example conceptual use:

```text
input state
→ matrix operator
→ output state
```

The entries now encode how input coordinates contribute to output coordinates.

Same mathematical object.

Different semantics.

---

## Matrix-as-data and matrix-as-operator must not be conflated

Suppose a 1000 × 64 matrix stores:

```text
1000 observations
64 features
```

That does not automatically mean the experiment applies a linear map:

```text
R64 → R1000
```

Mathematically multiplication is possible in some contexts.

But the scientific interpretation can be completely different.

Always ask:

> is this matrix a dataset, coefficient table, or operator?

---

## Matrix as coefficient table

In a linear system:

```text
rows
→ equations

columns
→ unknown variables
```

This is a third common semantic role.

So one rectangular array can be interpreted as:

- data;
- coefficients;
- operator.

Context is part of the mathematical model.

---

## Row vector

A matrix with one row is a **row vector**.

Example:

```math
\begin{bmatrix}
2 & 5 & -1
\end{bmatrix}.
```

Shape:

$$ 1\times3. $$

It can represent:

- one observation;
- one constraint;
- one linear functional's coefficients.

---

## Column vector

A matrix with one column is a **column vector**.

Example:

```math
\begin{bmatrix}
2\\
5\\
-1
\end{bmatrix}.
```

Shape:

$$ 3\times1. $$

Throughout this course, vectors are usually represented as column vectors unless stated otherwise.

---

## Scalar as 1 × 1 matrix?

A scalar can be represented as:

```math
\begin{bmatrix}
5
\end{bmatrix}.
```

But conceptually a scalar and a matrix are different object types in many contexts.

Do not collapse distinctions just because one representation is possible.

---

## Square matrix

A **square matrix** has equal row and column counts.

Examples:

```text
2 × 2
3 × 3
100 × 100
```

Square matrices are especially important because they can represent maps from a coordinate space back to the same coordinate dimension.

---

## Tall matrix

A **tall matrix** has:

```text
more rows than columns
```

Example:

$$ 5\times2. $$

In a system interpretation:

```text
more equations than unknowns
```

This often appears in overdetermined models.

But equation count alone does not determine consistency.

---

## Wide matrix

A **wide matrix** has:

```text
more columns than rows
```

Example:

$$ 2\times5. $$

In a system:

```text
more unknowns than equations
```

This often leaves degrees of freedom if the system is consistent.

Again, rank and dependence matter later.

---

## Shape does not determine rank

A 10 × 10 matrix can still contain highly redundant rows or columns.

A large square matrix is not automatically:

- invertible;
- full rank;
- informative.

Shape gives limits.

Structure determines actual rank.

---

## Zero matrix

A **zero matrix** contains only zeros.

Example:

```math
0_{2\times3}=
\begin{bmatrix}
0 & 0 & 0\\
0 & 0 & 0
\end{bmatrix}.
```

Shape matters even for zero matrices.

A `2 × 3` zero matrix and a `3 × 2` zero matrix are different shaped objects.

---

## Identity matrix

The **identity matrix** has ones on the main diagonal and zeros elsewhere.

For two dimensions:

```math
I_2=
\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}.
```

For three dimensions:

```math
I_3=
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}.
```

As an operator, identity leaves coordinates unchanged.

Formal multiplication comes later.

---

## Identity matrix is square

An identity matrix must have the same number of rows and columns because it maps each coordinate direction back to itself.

So notation like:

```text
I_3
```

means:

```text
3 × 3 identity
```

---

## Main diagonal

For a square matrix:

```math
A=
\begin{bmatrix}
a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33}
\end{bmatrix},
```

the main diagonal is:

```text
a11
a22
a33
```

The diagonal becomes important for:

- identity matrices;
- diagonal matrices;
- eigenvalue algorithms;
- numerical methods.

---

## Diagonal matrix

A **diagonal matrix** is square and has zeros off the main diagonal.

Example:

```math
D=
\begin{bmatrix}
2 & 0 & 0\\
0 & -1 & 0\\
0 & 0 & 4
\end{bmatrix}.
```

Such a matrix will later represent independent coordinate-wise scaling.

Do not overdevelop that interpretation yet.

---

## Matrix equality

Two matrices are equal only if:

1. they have the same shape;
2. corresponding entries are equal.

So:

```math
\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix}
```

is not equal to:

```math
\begin{bmatrix}
1 & 3\\
2 & 4
\end{bmatrix}.
```

The second array has rearranged entries.

---

## Order matters

Rows and columns have semantic order.

If columns represent:

```text
height
weight
age
```

then swapping columns changes the data interpretation.

If matrix columns represent variables:

```text
x1
x2
x3
```

then swapping columns without also changing variable order changes the represented system.

---

## Permuting representation can preserve meaning only with coordinated relabeling

Suppose you reorder variables from:

```text
x1, x2, x3
```

to:

```text
x3, x1, x2.
```

The coefficient columns must be reordered consistently.

Representation changes.

Underlying system can remain the same.

This is an early example of representation versus object.

---

## Example LA-EX-031 — data matrix versus operator matrix

Consider the same numeric array:

```math
M=
\begin{bmatrix}
1 & 0\\
0 & 2\\
3 & 1
\end{bmatrix}.
```

### Interpretation A — data

Rows are three observations.

Columns are two features.

### Interpretation B — operator

`M` maps a two-coordinate input into a three-coordinate output.

Same numbers.

Different meaning.

Therefore:

> matrix semantics are not contained in entries alone.

The model contract matters.

---

## Matrix labels matter

It is useful to annotate dimensions:

```text
X:
samples × features

A:
equations × variables

W:
outputs × inputs
```

These labels prevent shape mistakes.

In engineering code, many bugs are semantic dimension errors rather than arithmetic errors.

---

## Dimension checking

Suppose:

```text
A:
5 × 3

x:
3 × 1
```

Then the input coordinate count matches the number of columns.

But:

```text
y:
4 × 1
```

cannot be substituted as the same input type.

Dimensional consistency is the matrix analogue of unit checking.

---

## Shape is not physical units

Two vectors can both have shape:

```text
3 × 1
```

but represent:

```text
meters
```

versus:

```text
volts
```

Matrix shape checks algebraic compatibility.

It does not guarantee physical or semantic compatibility.

---

## Matrix notation compresses systems

Without matrices:

```math
\begin{aligned}
a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n &= b_1,\\
a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n &= b_2,\\
&\vdots\\
a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n &= b_m.
\end{aligned}
```

With matrices:

$$ A\mathbf{x}=\mathbf{b}. $$

This compression is not cosmetic.

It exposes structure.

---

## Matrix notation makes scale manageable

A system with:

```text
1000 equations
500 unknowns
```

is impossible to reason about line-by-line manually.

Matrix notation allows:

- algorithms;
- structural properties;
- numerical implementation.

Matrices are a language for scalable linear structure.

---

## Coefficient layout is systematic

For:

$$ A=[a_{ij}], $$

entry:

$$ a_{ij} $$

means:

> coefficient of variable `j` in equation `i`.

This convention explains why:

```text
rows = equations
columns = variables
```

for system matrices.

---

## Operator layout is systematic too

For an operator matrix:

```text
rows = output coordinates
columns = input coordinates
```

Entry:

$$ a_{ij} $$

describes how input coordinate `j` contributes to output coordinate `i`.

This interpretation becomes exact in the next lesson.

---

## One entry is a local coupling coefficient

Suppose:

$$ a_{23}=4. $$

Under operator interpretation:

```text
input coordinate 3
contributes coefficient 4
to output coordinate 2
```

This local contribution view helps understand large matrices.

---

## Sparse matrix

A matrix is **sparse** when many entries are zero.

Example:

```math
A=
\begin{bmatrix}
2 & 0 & 0 & 0\\
0 & 3 & 0 & 0\\
0 & 0 & 0 & 5
\end{bmatrix}.
```

Sparse structure can indicate limited coupling.

It also matters computationally.

---

## Dense matrix

A matrix is **dense** when many entries are nonzero.

Dense does not mean:

- more important;
- more invertible;
- more informative.

It only describes entry pattern.

---

## Sparsity can encode network structure

Suppose rows and columns represent nodes.

A zero entry can indicate:

```text
no direct modeled coupling
```

A nonzero entry can indicate:

```text
direct modeled influence
```

This links matrices to graph-like network models.

But numerical value and physical meaning remain model specific.

---

## Example LA-EX-032 — neural population weight matrix

Suppose a simplified decoder has:

```text
4 neural features
2 output variables
```

A weight matrix might have shape:

$$ 2\times4. $$

Example:

```math
W=
\begin{bmatrix}
0.3 & -0.2 & 0.7 & 0.1\\
-0.4 & 0.5 & 0.2 & 0.6
\end{bmatrix}.
```

Interpretation:

```text
4 input neural features
→ 2 decoded output coordinates
```

The matrix does not say:

- the biological system is linear;
- each weight is a synaptic strength;
- the decoder is causal.

It is an engineered linear operator model.

---

## Matrices can represent images too

A grayscale image can be stored as a matrix:

```text
rows:
pixel height

columns:
pixel width

entry:
brightness
```

This is matrix-as-data.

The same mathematics can manipulate it.

But the meaning of rows and columns is spatial, not equation-based.

---

## Matrices can represent adjacency

A graph can use an adjacency matrix.

Entry:

```text
A_ij
```

can indicate whether node `j` connects to node `i`, depending on convention.

This is matrix-as-relationship data/operator structure.

Conventions must be stated.

---

## Convention choice matters

Some fields use:

```text
rows = samples
columns = features
```

Others may transpose the convention.

Neither is universally correct.

The requirement is consistency.

Always inspect documentation.

---

## Transpose preview

The **transpose** swaps rows and columns.

If:

$$ A $$

is:

$$ m\times n, $$

then:

$$ A^T $$

is:

$$ n\times m. $$

Example:

```math
A=
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix},
```

then:

```math
A^T=
\begin{bmatrix}
1 & 4\\
2 & 5\\
3 & 6
\end{bmatrix}.
```

The transpose changes orientation.

Its deeper geometric meaning comes later.

---

## Transpose is not simply cosmetic

If rows are samples and columns are features, transposing gives:

```text
features × samples
```

The numbers are the same but roles switch.

A downstream algorithm may expect one orientation.

So transpose changes interface semantics.

---

## Matrix addition preview

Matrices of the same shape can be added entrywise.

Example:

```math
A=
\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix},
\qquad
B=
\begin{bmatrix}
5 & 6\\
7 & 8
\end{bmatrix}.
```

Then:

```math
A+B=
\begin{bmatrix}
6 & 8\\
10 & 12
\end{bmatrix}.
```

Different shapes cannot be added directly in ordinary matrix algebra.

---

## Scalar multiplication preview

A matrix can be multiplied by a scalar entrywise.

```math
2
\begin{bmatrix}
1 & -1\\
3 & 4
\end{bmatrix}
=
\begin{bmatrix}
2 & -2\\
6 & 8
\end{bmatrix}.
```

This parallels vector scalar multiplication.

---

## Matrix multiplication is not entrywise multiplication

Later matrix multiplication will represent composition.

Do not assume:

```text
AB
```

means multiply corresponding entries.

Entrywise multiplication exists in some contexts but is a different operation.

This distinction becomes essential.

---

## Matrix-vector multiplication is next

The next canonical lesson is:

`LA-N-0010 — Matrix-vector multiplication as a column combination`.

There we will explain:

$$ A\mathbf{x} $$

as:

```text
scale each column of A
by the matching coordinate of x
then add
```

That interpretation will unify:

- matrices;
- span;
- systems;
- operators.

---

## Why matrix-vector multiplication should not start with a recipe

A common teaching mistake is:

> row times column.

That recipe computes entries.

But it hides structure.

The deeper meaning is:

```text
input coefficients
→ combine columns
→ output vector
```

We postpone the arithmetic recipe until the concept is clear.

---

## Basis-direction preview

Suppose an operator acts on coordinate directions.

Its columns can later be interpreted as outputs produced by basis-direction inputs.

This is why columns completely determine a linear operator.

The formal statement comes later.

---

## Matrix as operator representation

A matrix is not the abstract operator itself in the deepest sense.

It is a coordinate representation of an operator once coordinate systems are chosen.

At L0 we will often speak loosely:

> matrix acts on vector.

Later we will distinguish:

```text
linear map
from
matrix representation
```

---

## Representation depends on basis

The same abstract linear map can have different matrices in different bases.

That advanced idea matters later.

For now:

> matrix entries depend on coordinate choices.

Do not confuse coordinates with the underlying geometric action.

---

## Operator versus relation

A general matrix can participate in equations without being interpreted as an invertible function.

For:

$$ A\mathbf{x}=\mathbf{b}, $$

there may be:

- no solution;
- one solution;
- many solutions.

Matrix notation alone does not guarantee reversibility.

---

## Square does not imply invertible

Even:

```math
A=
\begin{bmatrix}
1 & 2\\
2 & 4
\end{bmatrix}
```

is square.

But its columns are redundant.

So it will not be invertible.

Invertibility comes later.

---

## Tall does not imply inconsistent

A tall coefficient matrix means:

```text
more equations than unknowns
```

But equations can agree.

Consistency depends on values and rank.

---

## Wide does not imply every target reachable

A wide matrix has many input coordinates.

But columns can still fail to span the whole output space.

Again, shape sets possibilities.

It does not determine span.

---

## Matrix shape and span

The columns of an:

$$ m\times n $$

matrix live in:

$$ \mathbb{R}^m. $$

Their span is therefore a subset of:

$$ \mathbb{R}^m. $$

This will become the column space.

You already know the span concept.

Matrix notation packages the generators.

---

## Row vectors live in a different coordinate dimension

Rows of an:

$$ m\times n $$

matrix have `n` entries.

So they live in:

$$ \mathbb{R}^n. $$

Columns have `m` entries.

So they live in:

$$ \mathbb{R}^m. $$

This difference becomes important for row space and column space.

---

## Do not mix row-space and column-space ambient dimensions

For:

$$ A\in\mathbb{R}^{3\times5}, $$

rows have 5 coordinates.

Columns have 3 coordinates.

Therefore:

```text
row vectors live in R5
column vectors live in R3
```

They cannot be casually treated as the same type of vector.

---

## Matrix as a collection of columns

We can write conceptually:

```math
A=
\begin{bmatrix}
| & | & & |\\
\mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n\\
| & | & & |
\end{bmatrix}.
```

This emphasizes the column view.

Each column is a vector in `R^m`.

This notation will dominate `LA-0010`.

---

## Matrix as a stack of rows

We can also think:

```text
row_1
row_2
...
row_m
```

This emphasizes constraints and output coordinates.

Both decompositions are legitimate.

---

## Matrix storage in code

In programming libraries, matrices are often stored as 2D arrays.

But details vary:

- row-major memory;
- column-major memory;
- dense;
- sparse;
- GPU tensor layouts.

Mathematical row/column meaning is distinct from physical memory layout.

---

## Tensor versus matrix

A matrix has two axes.

A higher-order tensor/array can have more axes.

Example neural data:

```text
trials × time × channels
```

is naturally three-dimensional.

Flattening it into a matrix changes organization.

Later machine-learning workflows will use tensors extensively.

---

## Flattening changes semantics

Suppose:

```text
trials × time × neurons
```

is flattened to:

```text
samples × features.
```

This can be mathematically convenient.

But time and neuron axes are no longer explicit.

Representation choices matter.

---

## Matrix dimensions as type signatures

A useful habit is to annotate:

```text
A : R^n → R^m
```

when `A` is an `m × n` operator.

This tells you:

- expected input type;
- output type.

It is similar to a function signature in programming.

---

## Semantic type is stronger than dimension

Two variables may both live in:

$$ \mathbb{R}^3 $$

but represent:

- position;
- velocity.

A matrix mapping position to force is not interchangeable with one mapping velocity to force.

Dimensions match.

Semantics may not.

---

## Common failure mode: 3 × 5 means three columns and five rows

No.

Rows first:

```text
3 rows
5 columns
```

---

## Common failure mode: a matrix is just a big vector

No.

Rows and columns create two-axis structure.

That structure carries meaning.

---

## Common failure mode: matrix entries explain the matrix by themselves

No.

You need row/column semantics.

---

## Common failure mode: every matrix is an operator

A matrix can be data, coefficients, or operator representation.

Context decides.

---

## Common failure mode: every data matrix should be interpreted as a map

No.

A samples-by-features table is not automatically a physical transformation.

---

## Common failure mode: square matrix is automatically invertible

No.

Columns or rows may be dependent.

---

## Common failure mode: tall matrix means no solution

No.

An overdetermined system can be consistent.

---

## Common failure mode: wide matrix means infinite solutions for every target

No.

Some targets may be unreachable.

---

## Common failure mode: matrix multiplication is entrywise

No.

Standard matrix multiplication is a structured composition operation.

---

## Common failure mode: augmented matrix bar means another operation

No.

It is notation separating coefficients from constants.

---

## Common failure mode: transpose changes only formatting

It swaps row and column roles.

This can change interface semantics.

---

## Common failure mode: shape checking guarantees a physically meaningful model

No.

Shape is algebraic compatibility.

Units and semantics still matter.

---

## Active work

### Exercise 1 — identify shape

For:

```math
A=
\begin{bmatrix}
1 & 2 & 3 & 4\\
5 & 6 & 7 & 8\\
9 & 10 & 11 & 12
\end{bmatrix},
```

state:

- number of rows;
- number of columns;
- shape;
- `a_23`.

### Exercise 2 — system to coefficient matrix

Convert:

```math
\begin{aligned}
x+2y-z &= 4,\\
3x-y+5z &= 7.
\end{aligned}
```

into:

- coefficient matrix;
- unknown vector;
- right-hand-side vector;
- augmented matrix.

### Exercise 3 — row versus column semantics

For the matrix from Exercise 2:

- describe row 1;
- describe column 1;
- explain why those meanings differ.

### Exercise 4 — operator shape

A decoder maps:

```text
12 neural features
→ 3 output variables
```

What matrix shape should its linear weight operator have under column-vector convention?

Explain.

### Exercise 5 — data versus operator

A matrix has shape:

```text
500 × 64
```

Give:

- one data-table interpretation;
- one operator interpretation.

Explain why they are not the same scientific claim.

### Exercise 6 — classify matrix shapes

Classify:

```text
3 × 3
8 × 2
2 × 8
1 × 5
5 × 1
```

as:

- square;
- tall;
- wide;
- row vector;
- column vector.

### Exercise 7 — transpose

Transpose:

```math
A=
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix}.
```

State the new shape.

### Exercise 8 — semantic dimension checking

Suppose:

```text
W:
2 outputs × 4 neural features

r:
4 neural features × 1
```

Explain why shape matches.

Then explain why replacing `r` with a 4-coordinate temperature vector can still be semantically wrong even though dimensions match.

---

## Retrieval check

Without looking back:

1. What is a matrix?
2. What does `m × n` mean?
3. Which index comes first in `a_ij`?
4. What does `a_23` mean?
5. What is a row?
6. What is a column?
7. What is a coefficient matrix?
8. What is an augmented matrix?
9. What does the vertical bar mean?
10. How do rows correspond to equations?
11. How do columns correspond to variables?
12. What is the column-generator view?
13. What is the row-constraint view?
14. What is a row vector?
15. What is a column vector?
16. What is a square matrix?
17. What is a tall matrix?
18. What is a wide matrix?
19. What is a zero matrix?
20. What is an identity matrix?
21. Why is identity square?
22. What is the main diagonal?
23. What is a diagonal matrix?
24. When are two matrices equal?
25. Why does entry order matter?
26. What is matrix-as-data?
27. What is matrix-as-operator?
28. Why are those interpretations different?
29. What does an `m × n` operator expect as input?
30. What output dimension does it produce?
31. Why does the number of columns match input coordinates?
32. Why does the number of rows match output coordinates?
33. What is transpose?
34. How does transpose change shape?
35. Can different shaped matrices be added directly?
36. Why is standard matrix multiplication not entrywise multiplication?
37. Why does square not imply invertible?
38. Why does tall not imply inconsistent?
39. Why does wide not imply every target reachable?
40. Where do column vectors of an `m × n` matrix live?
41. Where do row vectors live?
42. What is sparsity?
43. Why can sparsity encode coupling structure?
44. Why is shape like an interface contract?
45. Why is semantic type stronger than shape alone?

---

## Connection backward: LA-0008

`LA-0008` gave:

```text
many equations
→ simultaneous constraints
```

This lesson packages their coefficients:

```text
system
→ coefficient matrix
→ compact representation
```

The system did not change.

Only the representation became more structured.

---

## Connection backward: LA-0006

`LA-0006` gave span.

The columns of a matrix are generators.

Soon:

```text
all possible A x
=
all linear combinations of columns
=
column span
```

Matrix notation therefore packages span problems.

---

## Connection forward: LA-0010

The next canonical lesson is:

`LA-N-0010 — Matrix-vector multiplication as a column combination`.

That lesson will make precise:

```math
A\mathbf{x}
=
x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n.
```

This is the bridge from:

```text
matrix as organized array
```

to:

```text
matrix as active linear operator
```

---

## Connection forward: LA-0011

Elimination will operate on matrix rows.

The augmented matrix will let us transform systems compactly while preserving solution sets.

So:

```text
rows
→ constraints
→ row operations
```

becomes algorithmic.

---

## Connection forward: linear transformations

Later a matrix will represent transformations such as:

- scaling;
- reflection;
- rotation;
- shear;
- projection.

At that point we will distinguish abstract map from coordinate matrix more carefully.

---

## Connection to LLMs

Modern neural networks use large matrices for linear layers.

A weight matrix shape encodes:

```text
input feature dimension
→ output feature dimension
```

For example:

```text
4096 input features
→ 11008 hidden features
```

requires an appropriately shaped linear operator under the chosen convention.

The exact software storage convention may vary.

The mathematical input/output contract does not.

---

## Connection to neural engineering

Neural data are often matrices:

```text
time × channels
trials × features
neurons × time
```

Decoders also use matrices:

```text
neural feature vector
→ weight matrix
→ behavioral estimate
```

The same word "matrix" can therefore refer to:

- measured dataset;
- model coefficients;
- linear operator.

Correct interpretation requires labels.

---

## Connection to software engineering

A matrix dimension mismatch is similar to a type mismatch.

Good practice:

```text
write shapes
write units
write semantics
```

before implementing numerical code.

This habit prevents many silent research bugs.

---

## What this unlocks

You should now be able to read:

```math
A=
\begin{bmatrix}
a_{11} & \cdots & a_{1n}\\
\vdots & \ddots & \vdots\\
a_{m1} & \cdots & a_{mn}
\end{bmatrix}
```

and immediately ask:

```text
what do rows mean?
what do columns mean?
what is the shape?
is this data, coefficients, or an operator?
what is the input dimension?
what is the output dimension?
```

That is enough to begin matrix-vector multiplication without treating it as a memorized arithmetic trick.

---

## References

- **LA-REF-001** — MIT OpenCourseWare, `18.06 Linear Algebra`.
- **LA-REF-002** — MIT OpenCourseWare, `18.06SC Linear Algebra`.
- **LA-REF-003** — Sheldon Axler, *Linear Algebra Done Right*, 4th ed.
- **LA-REF-004** — Stephen Boyd and Lieven Vandenberghe, *Introduction to Applied Linear Algebra — Vectors, Matrices, and Least Squares*.
