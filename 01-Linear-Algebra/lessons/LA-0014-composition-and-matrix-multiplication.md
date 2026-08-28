---
id: LA-0014
title: "Composition and matrix multiplication"
track: linear-algebra
level: L0
status: complete
curriculum_node: LA-N-0014
concepts_introduced: ["LA-C-0014"]
concepts_deepened: ["LA-C-0009", "LA-C-0010", "LA-C-0013"]
concepts_used: ["LA-C-0002", "LA-C-0003", "LA-C-0004", "LA-C-0005"]
examples_added: ["LA-EX-050", "LA-EX-051", "LA-EX-052", "LA-EX-053", "LA-EX-054"]
references_used: ["LA-REF-001", "LA-REF-002", "LA-REF-003", "LA-REF-004"]
last_reviewed: 2026-08-28
version_sensitive: false
review_after: null
---
# Composition and matrix multiplication

## If you landed here directly

This lesson assumes two earlier foundations:

- `LA-0010 — Matrix-vector multiplication as a column combination`;
- `LA-0013 — Linear transformations in the plane`.

You should already be able to interpret:

$$ \mathbf{y}=A\mathbf{x} $$

as both:

```text
matrix acting on vector
```

and:

```text
linear transformation sending an input to an output
```

The new question is:

> what matrix represents doing one linear transformation and then another?

The answer is **matrix multiplication**.

The central mental model is:

```text
x
→ B
→ Bx
→ A
→ A(Bx)

same overall map as

x
→ AB
→ (AB)x
```

So:

$$ A(B\mathbf{x})=(AB)\mathbf{x}. $$

By the end, you should be able to:

- define composition of transformations in the correct order;
- interpret $AB$ as "first $B$, then $A$";
- compute a matrix product from rows and columns;
- compute a matrix product from transformed columns;
- explain why matrix multiplication is generally not commutative;
- explain why matrix multiplication is associative;
- check dimension compatibility before multiplying;
- connect composition to pipelines of coordinate transformations, graphics operations, decoders, and linear processing stages;
- distinguish matrix multiplication from entrywise multiplication;
- explain why the identity matrix acts like "do nothing" under composition.

---

# The problem worth understanding

Suppose $B$ shears the plane.

Then $A$ scales it.

You apply the shear first and the scaling second.

For every vector $\mathbf{x}$:

```text
x
→ shear B
→ Bx
→ scale A
→ A(Bx)
```

If we want one matrix $C$ that performs the same two-step action, we require:

$$ C\mathbf{x}=A(B\mathbf{x}) $$

for every input $\mathbf{x}$.

That matrix is:

$$ C=AB. $$

Matrix multiplication is therefore not an arbitrary table rule invented for matrices.

It is the algebra forced on us by composition of linear transformations.

---

# Part I — Composition means feeding one output into another input

Let:

$$ T:\mathbb{R}^2\to\mathbb{R}^2 $$

and:

$$ S:\mathbb{R}^2\to\mathbb{R}^2. $$

Their composition $T\circ S$ means:

```text
first apply S
then apply T
```

So:

$$ (T\circ S)(\mathbf{x})=T(S(\mathbf{x})). $$

The symbol order is easy to misread.

Remember:

```text
T ∘ S

read operationally from right to left:
first S, then T
```

---

# Part II — From transformation composition to matrices

Suppose $S$ is represented by matrix $B$:

$$ S(\mathbf{x})=B\mathbf{x}. $$

Suppose $T$ is represented by matrix $A$:

$$ T(\mathbf{y})=A\mathbf{y}. $$

Then:

$$ (T\circ S)(\mathbf{x})=A(B\mathbf{x}). $$

We define the matrix product $AB$ so that:

$$ A(B\mathbf{x})=(AB)\mathbf{x} $$

for every compatible vector $\mathbf{x}$.

This is the conceptual source of the multiplication rule.

---

# Part III — The product is built from what happens to basis directions

Let the columns of $B$ be $\mathbf{b}_1$ and $\mathbf{b}_2$:

```math
B=
\begin{bmatrix}
\vert & \vert \\
\mathbf{b}_1 & \mathbf{b}_2 \\
\vert & \vert
\end{bmatrix}.
```

From `LA-0010`, multiplying $B$ by a vector means forming a column combination.

From `LA-0013`, the columns tell us where the coordinate directions go.

Now apply $A$ after $B$.

The first coordinate direction goes:

```text
e1
→ B e1 = b1
→ A b1
```

The second goes:

```text
e2
→ B e2 = b2
→ A b2
```

Therefore the columns of $AB$ are:

```math
AB=
\begin{bmatrix}
\vert & \vert \\
A\mathbf{b}_1 & A\mathbf{b}_2 \\
\vert & \vert
\end{bmatrix}.
```

This is one of the most useful meanings of matrix multiplication:

> multiply $A$ by $B$ by applying $A$ to every column of $B$.

---

# Part IV — Row-by-column arithmetic

For two $2\times2$ matrices:

```math
A=
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix},
\qquad
B=
\begin{bmatrix}
e & f \\
g & h
\end{bmatrix}.
```

The product is:

```math
AB=
\begin{bmatrix}
ae+bg & af+bh \\
ce+dg & cf+dh
\end{bmatrix}.
```

Each entry is a row-column dot product.

For example, the upper-left entry is:

$$ ae+bg. $$

That comes from:

```text
row 1 of A
·
column 1 of B
```

The arithmetic rule is correct because it encodes composition.

Do not learn the arithmetic without the composition meaning.

---

# Part V — Why the inner dimensions must match

Suppose $B$ maps from $\mathbb{R}^n$ to $\mathbb{R}^p$.

Its matrix has shape:

$$ p\times n. $$

Suppose $A$ maps from $\mathbb{R}^p$ to $\mathbb{R}^m$.

Its matrix has shape:

$$ m\times p. $$

Then the pipeline is:

```text
R^n
→ B
→ R^p
→ A
→ R^m
```

So $AB$ is defined and has shape:

$$ m\times n. $$

The dimension pattern is:

$$ (m\times p)(p\times n)=(m\times n). $$

The inner dimensions must match because the output type of $B$ must fit the input type of $A$.

This is not merely a bookkeeping trick.

It is a compatibility condition for composition.

---

# Part VI — Example LA-EX-050: shear then scale

Let:

```math
B=
\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
```

be a horizontal shear.

Let:

```math
A=
\begin{bmatrix}
2 & 0 \\
0 & 3
\end{bmatrix}
```

scale horizontal components by 2 and vertical components by 3.

We want:

```text
first B
then A
```

so the overall matrix is $AB$.

Compute:

```math
AB=
\begin{bmatrix}
2 & 0 \\
0 & 3
\end{bmatrix}
\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
=
\begin{bmatrix}
2 & 2 \\
0 & 3
\end{bmatrix}.
```

For input:

```math
\mathbf{x}=
\begin{bmatrix}
1 \\
2
\end{bmatrix},
```

first shear:

```math
B\mathbf{x}=
\begin{bmatrix}
3 \\
2
\end{bmatrix}.
```

Then scale:

```math
A(B\mathbf{x})=
\begin{bmatrix}
6 \\
6
\end{bmatrix}.
```

Using the product directly:

```math
(AB)\mathbf{x}=
\begin{bmatrix}
2 & 2 \\
0 & 3
\end{bmatrix}
\begin{bmatrix}
1 \\
2
\end{bmatrix}
=
\begin{bmatrix}
6 \\
6
\end{bmatrix}.
```

The two-step pipeline and the one-product matrix agree.

---

# Part VII — Order matters

Now reverse the operations.

First scale by $A$, then shear by $B$.

The matrix is now:

$$ BA. $$

Compute:

```math
BA=
\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
2 & 0 \\
0 & 3
\end{bmatrix}
=
\begin{bmatrix}
2 & 3 \\
0 & 3
\end{bmatrix}.
```

Compare:

```math
AB=
\begin{bmatrix}
2 & 2 \\
0 & 3
\end{bmatrix},
\qquad
BA=
\begin{bmatrix}
2 & 3 \\
0 & 3
\end{bmatrix}.
```

They are not equal.

So in general:

$$ AB\neq BA. $$

Matrix multiplication is **not commutative**.

Geometrically, that makes sense:

```text
shear then scale
```

need not equal:

```text
scale then shear
```

---

# Part VIII — Why "AB means A then B" is wrong

A common mistake is reading matrix products from left to right as action order.

If a column vector is on the right:

$$ AB\mathbf{x}, $$

then $B$ touches $\mathbf{x}$ first.

So:

```text
ABx
=
A(Bx)

operation order:
B first
A second
```

A reliable habit is to keep the vector visible until the order is clear.

Instead of memorizing:

```text
AB = ?
```

write:

```text
ABx = A(Bx)
```

and read from the inside out.

---

# Part IX — Example LA-EX-051: build the product by columns

Let:

```math
A=
\begin{bmatrix}
1 & 2 \\
0 & 1
\end{bmatrix},
\qquad
B=
\begin{bmatrix}
3 & -1 \\
2 & 4
\end{bmatrix}.
```

The columns of $B$ are:

```math
\mathbf{b}_1=
\begin{bmatrix}
3 \\
2
\end{bmatrix},
\qquad
\mathbf{b}_2=
\begin{bmatrix}
-1 \\
4
\end{bmatrix}.
```

Apply $A$ to each column.

First:

```math
A\mathbf{b}_1=
\begin{bmatrix}
1 & 2 \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
3 \\
2
\end{bmatrix}
=
\begin{bmatrix}
7 \\
2
\end{bmatrix}.
```

Second:

```math
A\mathbf{b}_2=
\begin{bmatrix}
1 & 2 \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
-1 \\
4
\end{bmatrix}
=
\begin{bmatrix}
7 \\
4
\end{bmatrix}.
```

Therefore:

```math
AB=
\begin{bmatrix}
7 & 7 \\
2 & 4
\end{bmatrix}.
```

This method reveals the geometry hidden inside row-by-column arithmetic.

---

# Part X — The identity matrix means do nothing

In $\mathbb{R}^2$, the identity matrix is:

```math
I=
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}.
```

For every vector:

$$ I\mathbf{x}=\mathbf{x}. $$

So composing a transformation with the identity changes nothing.

For every compatible matrix $A$:

$$ AI=A $$

and:

$$ IA=A. $$

This mirrors the identity transformation:

```text
input
→ do nothing
→ same input
```

The identity matrix is the algebraic representation of that map.

---

# Part XI — Associativity: grouping can change, order cannot

With three compatible matrices $A$, $B$, and $C$:

$$ (AB)C=A(BC). $$

This is **associativity**.

It says the grouping of a fixed sequence does not change the final transformation.

The operation order remains:

```text
C first
B second
A third
```

whether we group as:

```text
(AB)C
```

or:

```text
A(BC)
```

Associativity does **not** say you may reorder the matrices.

In general:

$$ ABC\neq ACB. $$

Grouping and ordering are different questions.

---

# Example LA-EX-053 — a three-stage pipeline

Suppose:

```text
C = projection-like preprocessing
B = shear-like coordinate adjustment
A = output scaling
```

The overall map is:

$$ ABC. $$

You may compute:

$$ (AB)C $$

or:

$$ A(BC). $$

The result is the same because function composition is associative.

But if you swap $B$ and $C$, you have changed the physical pipeline.

That generally changes the result.

This distinction matters in software and scientific pipelines because parentheses can be optimized while semantic order must be preserved.

---

# Part XII — Matrix multiplication is not entrywise multiplication

For matrices of the same shape, someone might try:

```text
multiply upper-left by upper-left
multiply upper-right by upper-right
...
```

That is a different operation, often called elementwise or Hadamard multiplication.

It is **not** the standard matrix product representing composition.

For standard matrix multiplication, entries mix through row-column combinations.

Why?

Because the first transformation mixes coordinates, and the second transformation acts on those mixed outputs.

Composition creates sums of products.

---

# Part XIII — Why matrix multiplication looks asymmetric

Addition of matrices is entrywise and symmetric in structure.

Matrix multiplication is different because it represents directional composition:

```text
input space
→ intermediate space
→ output space
```

The intermediate space appears as the matching inner dimension.

That is why:

$$ (m\times p)(p\times n) $$

works, while:

$$ (m\times p)(q\times n) $$

with $p\neq q$ does not.

The asymmetry comes from chaining maps, not from arbitrary notation.

---

# Part XIV — Example LA-EX-054: rectangular composition

Consider:

$$ B:\mathbb{R}^2\to\mathbb{R}^3 $$

and:

$$ A:\mathbb{R}^3\to\mathbb{R}^2. $$

Then $B$ has shape $3\times2$ and $A$ has shape $2\times3$.

Let:

```math
B=
\begin{bmatrix}
1 & 0 \\
0 & 1 \\
1 & 1
\end{bmatrix},
\qquad
A=
\begin{bmatrix}
1 & 2 & 0 \\
0 & 1 & 1
\end{bmatrix}.
```

The product $AB$ is defined:

```math
AB=
\begin{bmatrix}
1 & 2 & 0 \\
0 & 1 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 \\
0 & 1 \\
1 & 1
\end{bmatrix}
=
\begin{bmatrix}
1 & 2 \\
1 & 2
\end{bmatrix}.
```

Its shape is $2\times2$ because the whole pipeline maps:

```text
R^2
→ R^3
→ R^2
```

The intermediate dimension disappears from the final input-output type, but it is essential for the multiplication to be defined.

---

# Part XV — Composition viewed through columns

Suppose:

```math
B=
\begin{bmatrix}
\vert & \vert & & \vert \\
\mathbf{b}_1 & \mathbf{b}_2 & \cdots & \mathbf{b}_n \\
\vert & \vert & & \vert
\end{bmatrix}.
```

Then:

```math
AB=
\begin{bmatrix}
\vert & \vert & & \vert \\
A\mathbf{b}_1 & A\mathbf{b}_2 & \cdots & A\mathbf{b}_n \\
\vert & \vert & & \vert
\end{bmatrix}.
```

This is a general statement.

It says:

> left multiplication by $A$ transforms every column of $B$ by $A$.

This connects matrix multiplication directly to `LA-0010`.

---

# Part XVI — Composition viewed through rows

There is a complementary viewpoint.

Each row of $AB$ can be seen as a combination of rows of $B$, with weights supplied by a row of $A$.

At L0, the column viewpoint is usually more geometrically intuitive because columns already represent transformed coordinate directions.

But remembering that a product has both row and column interpretations will matter later in linear algebra and numerical computing.

---

# Part XVII — Example LA-EX-052: graphics-style transformation pipeline

Imagine a simple 2D graphics pipeline with vectors measured from the origin.

First rotate by $90^\circ$:

```math
R=
\begin{bmatrix}
0 & -1 \\
1 & 0
\end{bmatrix}.
```

Then stretch horizontally by a factor of 2:

```math
S=
\begin{bmatrix}
2 & 0 \\
0 & 1
\end{bmatrix}.
```

The overall matrix is:

$$ SR. $$

Compute:

```math
SR=
\begin{bmatrix}
2 & 0 \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
0 & -1 \\
1 & 0
\end{bmatrix}
=
\begin{bmatrix}
0 & -2 \\
1 & 0
\end{bmatrix}.
```

Now reverse the pipeline:

$$ RS. $$

```math
RS=
\begin{bmatrix}
0 & -1 \\
1 & 0
\end{bmatrix}
\begin{bmatrix}
2 & 0 \\
0 & 1
\end{bmatrix}
=
\begin{bmatrix}
0 & -1 \\
2 & 0
\end{bmatrix}.
```

The results differ.

This is a concrete visual reason matrix order matters.

---

# Part XVIII — Repeated transformations

If the same square matrix $A$ is applied twice:

$$ A(A\mathbf{x})=A^2\mathbf{x}. $$

Applied three times:

$$ A(A(A\mathbf{x}))=A^3\mathbf{x}. $$

The exponent means repeated matrix multiplication, not entrywise exponentiation.

For example, if $R$ rotates by $90^\circ$, then $R^2$ rotates by $180^\circ$.

Using:

```math
R=
\begin{bmatrix}
0 & -1 \\
1 & 0
\end{bmatrix},
```

we obtain:

```math
R^2=
\begin{bmatrix}
-1 & 0 \\
0 & -1
\end{bmatrix}.
```

That is exactly the $180^\circ$ rotation matrix.

Composition makes matrix powers meaningful.

---

# Part XIX — What zero in a product can mean

It is possible for two nonzero matrices to multiply to the zero matrix.

That may feel strange if your intuition comes only from real-number multiplication.

For example:

```math
A=
\begin{bmatrix}
1 & 0 \\
0 & 0
\end{bmatrix},
\qquad
B=
\begin{bmatrix}
0 & 0 \\
0 & 1
\end{bmatrix}.
```

Then:

```math
AB=
\begin{bmatrix}
0 & 0 \\
0 & 0
\end{bmatrix}.
```

Geometrically, $B$ sends every input onto the vertical axis, while $A$ keeps only the horizontal component.

So after $B$, $A$ erases everything.

This is another reminder that matrices represent maps, not ordinary scalar numbers.

---

# Part XX — Multiplication and information loss

Suppose $B$ is a projection that loses one direction.

No matrix applied afterward can reconstruct information that is no longer present in $B\mathbf{x}$ without additional assumptions or outside information.

So if:

```text
x
→ B
→ compressed / projected state
→ A
→ output
```

then the properties of the overall product $AB$ depend strongly on what $B$ destroys before $A$ ever sees the vector.

This prepares for later ideas about invertibility, null spaces, rank, and information loss.

We do not formalize those topics yet.

---

# Part XXI — Matrix multiplication as a reusable abstraction

A real pipeline may contain many stages:

```text
raw coordinates
→ calibration
→ rotation
→ scaling
→ projection
→ output coordinates
```

If every stage is linear and represented by a matrix, the entire pipeline can be represented by one matrix product.

That gives two advantages.

## Conceptual compression

A multi-stage system becomes one linear map.

## Computational opportunity

If the individual matrices are fixed, their product may be precomputed once and reused.

The best computational strategy depends on matrix sizes, sparsity, numerical issues, and whether stages change over time.

Those are later numerical-linear-algebra questions.

---

# Part XXII — Common failure modes

## Failure mode 1 — reversing the order

Mistake:

```text
first B, then A
→ write BA
```

Correct:

```text
first B, then A
→ A(Bx)
→ ABx
→ product AB
```

---

## Failure mode 2 — assuming commutativity

Mistake:

$$ AB=BA. $$

In general this is false.

Check the transformation order.

---

## Failure mode 3 — multiplying entries position by position

That is not standard matrix multiplication.

Standard multiplication uses row-column combinations because it represents composition.

---

## Failure mode 4 — ignoring dimensions

Before computing entries, check:

```text
columns of left matrix
=
rows of right matrix
```

Or more conceptually:

```text
output dimension of right map
=
input dimension of left map
```

---

## Failure mode 5 — confusing associativity with commutativity

Associativity:

$$ (AB)C=A(BC). $$

Commutativity would be:

$$ AB=BA. $$

The first is true for compatible matrices.

The second is generally false.

---

## Failure mode 6 — forgetting the vector

When order feels confusing, reattach an input:

$$ AB\mathbf{x}=A(B\mathbf{x}). $$

The vector exposes the operation order immediately.

---

## Failure mode 7 — treating a product as mysterious arithmetic

If an entry formula seems arbitrary, return to columns:

```text
column j of AB
=
A(column j of B)
```

The arithmetic will follow.

---

# Part XXIII — Worked example with a reflection and projection

Let reflection across the $x$-axis be:

```math
F=
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}.
```

Let projection onto the line $y=x$ be:

```math
P=\frac{1}{2}
\begin{bmatrix}
1 & 1 \\
1 & 1
\end{bmatrix}.
```

First reflect, then project:

$$ PF. $$

```math
PF=\frac{1}{2}
\begin{bmatrix}
1 & -1 \\
1 & -1
\end{bmatrix}.
```

First project, then reflect:

$$ FP. $$

```math
FP=\frac{1}{2}
\begin{bmatrix}
1 & 1 \\
-1 & -1
\end{bmatrix}.
```

Again:

$$ PF\neq FP. $$

The difference is geometric, not merely symbolic.

---

# Part XXIV — Worked example from a decoder pipeline

Suppose a feature vector is:

```math
\mathbf{x}=
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}.
```

A first linear stage mixes the features:

```math
B=
\begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}.
```

A second stage scales the two intermediate outputs:

```math
A=
\begin{bmatrix}
2 & 0 \\
0 & \tfrac{1}{2}
\end{bmatrix}.
```

The final output is:

$$ \mathbf{y}=A(B\mathbf{x})=(AB)\mathbf{x}. $$

The product is:

```math
AB=
\begin{bmatrix}
2 & 2 \\
\tfrac{1}{2} & -\tfrac{1}{2}
\end{bmatrix}.
```

So the two-stage linear decoder can be represented by one matrix.

This does not mean every real neural decoder is linear.

It means linear stages compose through matrix multiplication.

---

# Part XXV — Active work

## Exercise 1 — order

A system first rotates by matrix $R$ and then scales by matrix $S$.

Which product represents the overall map?

Explain using an input vector rather than memory alone.

---

## Exercise 2 — compute

Let:

```math
A=
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix},
\qquad
B=
\begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}.
```

Compute $AB$ and $BA$.

Are they equal?

---

## Exercise 3 — columns

For the same $A$ and $B$, compute $AB$ by applying $A$ to each column of $B$.

Confirm that you obtain the same result as row-column multiplication.

---

## Exercise 4 — dimensions

Decide whether each product is defined.

1. $(3\times2)(2\times4)$
2. $(3\times2)(3\times4)$
3. $(1\times5)(5\times1)$
4. $(5\times1)(1\times5)$

For every defined product, give the output shape.

---

## Exercise 5 — composition story

Create two simple planar linear transformations.

For each:

- write its matrix;
- describe its geometric action;
- compute both possible orders;
- explain why the products agree or differ.

---

# Part XXVI — Retrieval practice

Answer without looking back.

1. What does composition $T\circ S$ mean operationally?
2. In $AB\mathbf{x}$, which matrix acts first?
3. Why is matrix multiplication the natural algebra of linear-transformation composition?
4. What are the columns of $AB$ in terms of the columns of $B$?
5. How is an entry of $AB$ computed using rows and columns?
6. What dimension condition must hold for $AB$?
7. If $A$ is $m\times p$ and $B$ is $p\times n$, what shape is $AB$?
8. Why is matrix multiplication generally not commutative?
9. What does associativity mean?
10. Why does associativity not permit reordering matrices?
11. What does the identity matrix represent geometrically?
12. Why is entrywise multiplication not the same as standard matrix multiplication?
13. What does $A^3$ mean for a square matrix?
14. How can nonzero matrices multiply to the zero matrix?
15. Why can information lost by an early projection not generally be restored by a later matrix?
16. How can a fixed multi-stage linear pipeline be compressed into one matrix?
17. What is the safest way to recover operation order if you forget it?
18. How does matrix multiplication connect `LA-0010` and `LA-0013`?

---

# Part XXVII — Connection backward: LA-0009

`LA-0009` introduced matrices as organized coefficients and operators.

At that stage, one matrix could represent one transformation.

This lesson answers the next systems question:

```text
if one matrix is one operator,
what represents two operators in sequence?
```

The answer is the matrix product.

---

# Part XXVIII — Connection backward: LA-0010

`LA-0010` gave the column-combination viewpoint:

```math
A\mathbf{x}
=
x_1\mathbf{a}_1+x_2\mathbf{a}_2+\cdots+x_n\mathbf{a}_n.
```

Now use that idea one level higher.

If $B$ has columns $\mathbf{b}_j$, then the columns of $AB$ are $A\mathbf{b}_j$.

So matrix multiplication is built from repeated matrix-vector multiplication.

This is a major conceptual bridge.

---

# Part XXIX — Connection backward: LA-0013

`LA-0013` made matrices geometric.

You saw scaling, reflection, projection, rotation, and shear.

This lesson composes them.

The question changes from:

```text
What does this transformation do?
```

into:

```text
What does this sequence of transformations do?
```

Matrix multiplication is the answer.

---

# Part XXX — Connection to neural engineering

A neural system may contain several linear stages:

```text
features x
→ spatial filter B
→ filtered features
→ decoder A
→ command y
```

If both stages are linear:

$$ \mathbf{y}=A(B\mathbf{x})=(AB)\mathbf{x}. $$

That means the two fixed linear stages can be interpreted as one composed linear map.

The NNE tradeoff lesson adds a systems warning:

- combining matrices may simplify computation;
- it does not remove bandwidth limits;
- it does not remove noise;
- it does not remove biological drift;
- it does not make a closed-loop system automatically stable or safe.

Mathematical composition and engineering validity are different questions.

---

# Part XXXI — What this unlocks

You should now be able to inspect a product and ask:

```text
What spaces do these matrices map between?
Which transformation happens first?
Are the dimensions compatible?
What do the product columns mean?
What does the product do geometrically?
Would reversing the order change the result?
Can I simplify a multi-stage linear pipeline into one matrix?
Has an earlier stage already lost information?
```

This prepares the way for later topics in the curriculum where composition interacts with invertibility, systems of equations, subspaces, rank, and numerical computation.

---

# References

- **LA-REF-001** — MIT OpenCourseWare, `18.06 Linear Algebra`.
- **LA-REF-002** — MIT OpenCourseWare, `18.06SC Linear Algebra`.
- **LA-REF-003** — Sheldon Axler, *Linear Algebra Done Right*, 4th ed.
- **LA-REF-004** — Stephen Boyd and Lieven Vandenberghe, *Introduction to Applied Linear Algebra — Vectors, Matrices, and Least Squares*.
