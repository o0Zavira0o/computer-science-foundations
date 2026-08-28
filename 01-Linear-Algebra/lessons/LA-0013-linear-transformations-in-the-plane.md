---
id: LA-0013
title: "Linear transformations in the plane"
track: linear-algebra
level: L0
status: complete
curriculum_node: LA-N-0013
concepts_introduced: ["LA-C-0013"]
concepts_deepened: ["LA-C-0004", "LA-C-0009", "LA-C-0010"]
concepts_used: ["LA-C-0002", "LA-C-0003", "LA-C-0005"]
examples_added: ["LA-EX-045", "LA-EX-046", "LA-EX-047", "LA-EX-048", "LA-EX-049"]
references_used: ["LA-REF-001", "LA-REF-002", "LA-REF-003", "LA-REF-004"]
last_reviewed: 2026-08-28
version_sensitive: false
review_after: null
---
# Linear transformations in the plane

## If you landed here directly

This lesson assumes two earlier foundations:

- `LA-0004 — Vector addition and scalar multiplication`;
- `LA-0009 — Matrices as organized coefficients and operators`.

You should already know that vectors in $\mathbb{R}^2$ can be added and scaled, and that a matrix can represent an operator that maps an input vector to an output vector.

The new question is:

> what kinds of geometric actions preserve the linear structure of vectors?

The central mental model is:

```text
input vector
→ linear transformation
→ output vector

while preserving:
addition
and
scalar multiplication
```

In symbols, a transformation $T$ is linear when it respects:

$$ T(\mathbf{u}+\mathbf{v})=T(\mathbf{u})+T(\mathbf{v}) $$

and:

$$ T(c\mathbf{v})=cT(\mathbf{v}). $$

At L0 we will test these ideas with geometry in the plane.

By the end, you should be able to:

- interpret a transformation as a rule that sends every input vector to an output vector;
- distinguish a linear transformation from a general geometric transformation;
- explain why every linear transformation sends the origin to the origin;
- recognize uniform and nonuniform scaling, reflection, projection, rotation, and shear as linear transformations when centered at the origin;
- recognize translation as a standard example of a transformation that is not linear;
- use the images of the coordinate directions to predict the action of a linear transformation;
- connect a $2\times2$ matrix to a transformation of the plane;
- explain what information projection loses and why that matters for reversibility later;
- prepare for composition and matrix multiplication.

---

# The problem worth understanding

Consider three geometric rules.

Rule A doubles every vector:

```text
(x,y) → (2x,2y)
```

Rule B rotates every vector by $90^\circ$ around the origin.

Rule C shifts every point one unit to the right:

```text
(x,y) → (x+1,y)
```

All three transform the plane.

But only the first two are linear transformations.

Why?

The answer is not merely that A and B can be written with matrices.

The deeper reason is that they preserve vector addition and scalar multiplication.

Translation does not.

---

# Part I — Transformation means input-to-output rule

A **transformation** is a rule that maps an input vector to an output vector.

We write:

$$ T:\mathbb{R}^2\to\mathbb{R}^2. $$

This means:

```text
input: 2-component real vector
output: 2-component real vector
```

For example:

$$ T(x,y)=(2x,y). $$

The input $(3,-1)$ becomes:

$$ T(3,-1)=(6,-1). $$

---

# Part II — Linear means structure-preserving

A linear transformation must preserve the two vector operations introduced in `LA-0004`.

## Addition preservation

For any vectors $\mathbf{u}$ and $\mathbf{v}$:

$$ T(\mathbf{u}+\mathbf{v})=T(\mathbf{u})+T(\mathbf{v}). $$

Meaning:

```text
add first, then transform
=
transform first, then add
```

---

## Scalar preservation

For any scalar $c$:

$$ T(c\mathbf{v})=cT(\mathbf{v}). $$

Meaning:

```text
scale first, then transform
=
transform first, then scale
```

These are not arbitrary rules.

They say the transformation respects linear combinations.

---

# Part III — One compact linear-combination test

If both properties hold, then:

$$ T(a\mathbf{u}+b\mathbf{v})=aT(\mathbf{u})+bT(\mathbf{v}). $$

This is the most useful mental model:

> a linear transformation can be moved through a linear combination.

That is why knowing what the transformation does to a few generating directions can determine what it does to every combination of those directions.

---

# Part IV — The origin test

Set $c=0$ in the scalar rule:

$$ T(0\mathbf{v})=0T(\mathbf{v}). $$

Therefore:

$$ T(\mathbf{0})=\mathbf{0}. $$

So every linear transformation sends the origin to the origin.

This gives a fast failure test:

> if a transformation moves the origin somewhere else, it is not linear.

The origin test is necessary, but not by itself sufficient.

A strange nonlinear rule could still happen to fix the origin.

---

# Part V — Example LA-EX-045: translation fails linearity

Consider:

$$ T(x,y)=(x+1,y). $$

Apply it to the origin:

$$ T(0,0)=(1,0). $$

But a linear transformation must satisfy:

$$ T(0,0)=(0,0). $$

Therefore translation by $(1,0)$ is not linear.

This is a useful boundary:

```text
rotation around origin → can be linear
translation away from origin → not linear
```

Later mathematics extends linear transformations to **affine** transformations, which can include translations.

That is not our topic yet.

---

# Part VI — Matrix as transformation

A $2\times2$ matrix:

```math
A=
\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}
```

acts on:

```math
\mathbf{x}=
\begin{bmatrix}
x\\y
\end{bmatrix}
```

through:

$$ T(\mathbf{x})=A\mathbf{x}. $$

The output is:

```math
A\mathbf{x}
=
\begin{bmatrix}
a & b\\c & d
\end{bmatrix}
\begin{bmatrix}x\\y\end{bmatrix}
=
\begin{bmatrix}
ax+by\\
cx+dy
\end{bmatrix}.
```

Matrix-vector multiplication therefore defines a linear rule.

---

# Part VII — The columns tell the geometric story

Let the standard coordinate directions be:

```math
\mathbf{e}_1=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\mathbf{e}_2=
\begin{bmatrix}0\\1\end{bmatrix}.
```

Any vector is:

$$ \mathbf{x}=x\mathbf{e}_1+y\mathbf{e}_2. $$

Linearity gives:

$$ T(\mathbf{x})=xT(\mathbf{e}_1)+yT(\mathbf{e}_2). $$

If:

```math
A=
\begin{bmatrix}
a & b\\c & d
\end{bmatrix},
```

then:

```math
T(\mathbf{e}_1)=
\begin{bmatrix}a\\c\end{bmatrix},
\qquad
T(\mathbf{e}_2)=
\begin{bmatrix}b\\d\end{bmatrix}.
```

Those are exactly the columns of $A$.

So:

> the columns tell us where the coordinate directions go.

This turns matrix entries into geometry.

---

# Part VIII — Example LA-EX-046: nonuniform scaling

Consider:

```math
A=
\begin{bmatrix}
2 & 0\\
0 & 1/2
\end{bmatrix}.
```

Then:

```math
A\mathbf{e}_1=
\begin{bmatrix}2\\0\end{bmatrix},
\qquad
A\mathbf{e}_2=
\begin{bmatrix}0\\1/2\end{bmatrix}.
```

So horizontal components double while vertical components are halved.

A unit square becomes a rectangle.

For:

```math
\mathbf{x}=\begin{bmatrix}3\\4\end{bmatrix},
```

we get:

```math
A\mathbf{x}=\begin{bmatrix}6\\2\end{bmatrix}.
```

This is linear even though the two directions are scaled differently.

Linearity does not mean "same scaling in every direction."

---

# Part IX — Uniform scaling

If:

```math
A=
\begin{bmatrix}
s&0\\0&s
\end{bmatrix},
```

then:

$$ A\mathbf{x}=s\mathbf{x}. $$

Every vector is scaled by the same scalar $s$.

Special cases:

```text
s > 1     expansion
0 < s < 1 contraction
s = 1     identity
s = 0     collapse to origin
s < 0     scaling plus reversal through origin
```

Even $s=0$ is linear.

It loses all directional information, but it still preserves addition and scalar multiplication.

---

# Part X — Reflection

Reflection across the $x$-axis sends:

$$ (x,y)\mapsto(x,-y). $$

Its matrix is:

```math
R_x=
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}.
```

The coordinate directions become:

```math
R_x\mathbf{e}_1=\mathbf{e}_1,
\qquad
R_x\mathbf{e}_2=-\mathbf{e}_2.
```

So the horizontal direction is preserved and the vertical direction reverses.

The origin stays fixed.

---

# Part XI — Example LA-EX-047: reflection versus projection

Reflection across the $x$-axis:

$$ (x,y)\mapsto(x,-y). $$

Projection onto the $x$-axis:

$$ (x,y)\mapsto(x,0). $$

Projection matrix:

```math
P_x=
\begin{bmatrix}
1&0\\
0&0
\end{bmatrix}.
```

Compare what happens to:

```math
\mathbf{v}=\begin{bmatrix}2\\3\end{bmatrix}.
```

Reflection gives:

```math
R_x\mathbf{v}=\begin{bmatrix}2\\-3\end{bmatrix}.
```

Projection gives:

```math
P_x\mathbf{v}=\begin{bmatrix}2\\0\end{bmatrix}.
```

Both are linear.

But projection destroys the original $y$ component.

Many different inputs:

```text
(2,3)
(2,-1)
(2,100)
```

all project to:

```text
(2,0)
```

This previews a later idea:

> some linear transformations lose information and therefore cannot be reversed uniquely.

---

# Part XII — Rotation around the origin

A counterclockwise rotation by angle $\theta$ has matrix:

```math
R_\theta=
\begin{bmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{bmatrix}.
```

You do not need to memorize this immediately.

Instead understand what it means:

```text
column 1 = rotated e1
column 2 = rotated e2
```

Because every vector is a linear combination of $\mathbf{e}_1$ and $\mathbf{e}_2$, those two rotated directions determine the rotation of every vector.

---

# Part XIII — Example LA-EX-048: 90-degree rotation

For $\theta=90^\circ$:

```math
R=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}.
```

Then:

```math
R\mathbf{e}_1=
\begin{bmatrix}0\\1\end{bmatrix}=\mathbf{e}_2,
```

and:

```math
R\mathbf{e}_2=
\begin{bmatrix}-1\\0\end{bmatrix}=-\mathbf{e}_1.
```

For:

```math
\mathbf{v}=\begin{bmatrix}2\\1\end{bmatrix},
```

we get:

```math
R\mathbf{v}=
\begin{bmatrix}-1\\2\end{bmatrix}.
```

The vector rotates $90^\circ$ counterclockwise about the origin.

---

# Part XIV — Rotation about another point is different

Suppose we rotate around the point $(1,0)$ rather than around the origin.

The origin generally moves.

Therefore that full transformation is not linear in the original coordinates.

It can be described by:

```text
translate center to origin
→ rotate
→ translate back
```

But translations are not linear.

This is another example of why the chosen origin matters.

---

# Part XV — Shear

A horizontal shear can be written:

$$ (x,y)\mapsto(x+ky,y). $$

Its matrix is:

```math
S=
\begin{bmatrix}
1&k\\
0&1
\end{bmatrix}.
```

The coordinate directions become:

```math
S\mathbf{e}_1=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
S\mathbf{e}_2=
\begin{bmatrix}k\\1\end{bmatrix}.
```

A square becomes a parallelogram.

Parallel lines remain parallel under this linear action.

---

# Part XVI — Example LA-EX-049: shear from basis directions

Take:

```math
S=
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}.
```

Then:

```math
S\mathbf{e}_1=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
S\mathbf{e}_2=
\begin{bmatrix}2\\1\end{bmatrix}.
```

Now let:

```math
\mathbf{v}=3\mathbf{e}_1+4\mathbf{e}_2.
```

By linearity:

```math
S\mathbf{v}
=3S\mathbf{e}_1+4S\mathbf{e}_2
=3\begin{bmatrix}1\\0\end{bmatrix}
+4\begin{bmatrix}2\\1\end{bmatrix}
=\begin{bmatrix}11\\4\end{bmatrix}.
```

We predicted the output entirely from the two transformed coordinate directions.

That is the column-combination view from `LA-0010` expressed geometrically.

---

# Part XVII — Lines through the origin stay structurally special

Take all points on a line through the origin:

$$ \mathbf{x}=t\mathbf{v}. $$

Apply a linear transformation:

$$ T(\mathbf{x})=T(t\mathbf{v})=tT(\mathbf{v}). $$

So the transformed points still lie on a line through the origin, unless all of them collapse to the origin.

This gives a geometric fingerprint of linearity.

---

# Part XVIII — Parallel grids remain linear grids

Imagine a square coordinate grid.

Under a linear transformation:

- the origin remains fixed;
- straight coordinate lines remain straight or collapse;
- evenly spaced points remain evenly related by linear combinations;
- parallelogram structure is preserved.

The grid may stretch, rotate, reflect, shear, flatten, or collapse.

But it does not bend into curves.

---

# Part XIX — A nonlinear counterexample

Consider:

$$ T(x,y)=(x^2,y). $$

The origin stays fixed:

$$ T(0,0)=(0,0). $$

So it passes the origin test.

But scalar preservation fails.

For example:

$$ T(2x,2y)=(4x^2,2y), $$

while:

$$ 2T(x,y)=(2x^2,2y). $$

These are generally different.

Therefore fixing the origin is not enough to guarantee linearity.

---

# Part XX — Informal linearity test workflow

When given a transformation in the plane:

```text
1. Check the origin.
2. Ask whether addition is preserved.
3. Ask whether scalar multiplication is preserved.
4. If a matrix rule Ax is given, recognize it as linear.
5. Interpret the columns as transformed coordinate directions.
6. Check what geometry is preserved or lost.
```

At L0, this workflow is more valuable than memorizing a long catalog of matrices.

---

# Part XXI — Scaling, reflection, projection, rotation, shear compared

| Transformation | Typical effect | Origin fixed? | Information loss possible? |
|---|---|---:|---:|
| nonzero uniform scaling | expand or contract equally | yes | no |
| nonuniform scaling | stretch axes differently | yes | only if a scale factor is zero |
| reflection | flip across a line through origin | yes | no |
| projection | flatten onto a line | yes | yes |
| rotation about origin | turn all directions by same angle | yes | no |
| shear | slant the grid | yes | no for the standard nondegenerate shear |
| translation | shift every point | generally no | no, but not linear |

The table is a recognition aid, not a substitute for the linearity test.

---

# Part XXII — Transformation versus matrix representation

At this level we often say:

> the matrix transforms the vector.

That language is useful.

But keep the deeper distinction from `LA-0009`:

```text
geometric action / linear map
≠
its coordinate matrix representation
```

Later, after bases are developed, the same abstract linear map can be represented by different matrices in different coordinate systems.

For now, standard coordinates in $\mathbb{R}^2$ keep the picture concrete.

---

# Part XXIII — Why columns determine the transformation

Suppose:

```math
\mathbf{x}=
\begin{bmatrix}x\\y\end{bmatrix}
=x\mathbf{e}_1+y\mathbf{e}_2.
```

Then:

$$ T(\mathbf{x})=xT(\mathbf{e}_1)+yT(\mathbf{e}_2). $$

If we know $T(\mathbf{e}_1)$ and $T(\mathbf{e}_2)$, we know $T(\mathbf{x})$ for every vector in the plane.

This is why a $2\times2$ matrix needs exactly two columns to describe a linear transformation from $\mathbb{R}^2$ to $\mathbb{R}^2$ under standard coordinates.

---

# Part XXIV — Connection to solution geometry

`LA-0012` studied lines and plane-like families as solution sets.

A linear transformation can move such sets.

For example, if a line through the origin is generated by $\mathbf{v}$:

$$ \{t\mathbf{v}:t\in\mathbb{R}\}, $$

then its image is:

$$ \{tT(\mathbf{v}):t\in\mathbb{R}\}. $$

So the transformation viewpoint and solution-geometry viewpoint are different, but they will eventually connect through spaces, null spaces, images, and rank.

Do not formalize those later topics yet.

---

# Part XXV — Failure modes

## Failure mode 1: "Every geometric transformation is linear"

False.

Translation is geometric but not linear in ordinary coordinates.

---

## Failure mode 2: "If the origin stays fixed, the transformation is linear"

False.

The nonlinear rule $(x,y)\mapsto(x^2,y)$ fixes the origin but fails scalar preservation.

---

## Failure mode 3: "Linear means the graph is a straight line"

False.

Here, linearity means preserving vector addition and scalar multiplication.

---

## Failure mode 4: "A linear transformation must scale every direction equally"

False.

Nonuniform scaling and shear are linear.

---

## Failure mode 5: "Projection is not linear because it loses information"

False.

A transformation can be linear and still collapse dimensions.

---

## Failure mode 6: "Rotation is always linear"

Only rotation about the origin is linear in the current coordinate system.

Rotation about another point includes translations.

---

## Failure mode 7: "Matrix entries are only arithmetic coefficients"

False under operator interpretation.

The columns encode where coordinate directions go.

---

## Failure mode 8: "If two matrices look different, they must represent different abstract maps"

Too strong.

Representation can depend on the chosen basis, a topic developed later.

---

# Part XXVI — Active work

## Exercise 1 — origin test

Which of these immediately fail the origin test?

```text
T1(x,y) = (2x,3y)
T2(x,y) = (x+4,y)
T3(x,y) = (-x,y)
T4(x,y) = (x,y+1)
```

---

## Exercise 2 — scalar test

For:

$$ T(x,y)=(x^2,y), $$

choose one vector and one scalar that demonstrate failure of scalar preservation.

---

## Exercise 3 — identify the action

Interpret:

```math
A=
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}.
```

Where do $\mathbf{e}_1$ and $\mathbf{e}_2$ go?

What familiar transformation is this?

---

## Exercise 4 — projection

For:

```math
P=
\begin{bmatrix}
1&0\\
0&0
\end{bmatrix},
```

find two different input vectors that produce the same output.

What information is lost?

---

## Exercise 5 — build a matrix from transformed basis directions

Suppose:

```math
T(\mathbf{e}_1)=
\begin{bmatrix}2\\1\end{bmatrix},
\qquad
T(\mathbf{e}_2)=
\begin{bmatrix}-1\\3\end{bmatrix}.
```

Construct the matrix of $T$ in standard coordinates.

Then compute $T(4,-2)$ using a column combination.

---

## Exercise 6 — rotation

Apply the $90^\circ$ rotation matrix to:

```math
\begin{bmatrix}3\\-2\end{bmatrix}.
```

Sketch the input and output mentally or on paper.

---

## Exercise 7 — shear

Use:

```math
S=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}.
```

Transform the four corners:

```text
(0,0), (1,0), (0,1), (1,1)
```

What shape does the unit square become?

---

## Exercise 8 — linearity explanation

Explain in words why knowing only $T(\mathbf{e}_1)$ and $T(\mathbf{e}_2)$ is enough to know a linear transformation everywhere in $\mathbb{R}^2$.

---

# Retrieval check

Without looking back:

1. What is a transformation?
2. What two properties define linearity here?
3. What does it mean to preserve addition?
4. What does it mean to preserve scalar multiplication?
5. What is the linear-combination form of the rule?
6. Why must a linear transformation send the origin to the origin?
7. Why is the origin test not sufficient by itself?
8. Why is translation not linear?
9. What does $T(\mathbf{x})=A\mathbf{x}$ mean geometrically?
10. What do the columns of a $2\times2$ operator matrix represent?
11. How do you decompose $(x,y)$ using $\mathbf{e}_1$ and $\mathbf{e}_2$?
12. Why do the images of $\mathbf{e}_1$ and $\mathbf{e}_2$ determine the whole transformation?
13. What is uniform scaling?
14. What is nonuniform scaling?
15. How does reflection across the $x$-axis act?
16. How does projection onto the $x$-axis act?
17. Why can projection be linear even though it loses information?
18. What does a $90^\circ$ counterclockwise rotation do to $\mathbf{e}_1$?
19. What does it do to $\mathbf{e}_2$?
20. Why is rotation around a non-origin point not linear in the current coordinates?
21. What does a shear do to a square grid?
22. Why does $(x,y)\mapsto(x^2,y)$ fail linearity?
23. What happens to a line through the origin under a linear transformation?
24. Can a linear transformation collapse all vectors to the origin?
25. Why does "linear" not mean "same scale in every direction"?
26. What is the difference between a transformation and its matrix representation?
27. Which earlier lesson supplied the two operations used to test linearity?
28. Which earlier lesson introduced matrices as operators?
29. Which next lesson will interpret matrix multiplication as composition?
30. Why is composition the natural next question after studying individual transformations?

---

# Connection backward: LA-0004

`LA-0004` introduced vector addition and scalar multiplication.

At that time they were operations on vectors.

Now they become the **contract** that defines a linear transformation:

$$ T(\mathbf{u}+\mathbf{v})=T(\mathbf{u})+T(\mathbf{v}) $$

and:

$$ T(c\mathbf{v})=cT(\mathbf{v}). $$

So the earlier operations were not isolated arithmetic rules.

They define what structure a linear map must preserve.

---

# Connection backward: LA-0009 and LA-0010

`LA-0009` introduced the matrix-as-operator viewpoint.

`LA-0010` interpreted matrix-vector multiplication as a column combination.

This lesson makes those ideas geometric:

```text
column 1 = image of e1
column 2 = image of e2

input coordinates
→ weights on transformed basis directions
→ output vector
```

So matrix-vector multiplication is now a visible transformation of the plane, not merely an arithmetic procedure.

---

# Connection backward: LA-0012

`LA-0012` focused on solution geometry and degrees of freedom.

This lesson asks a different question:

```text
not:
which vectors satisfy these constraints?

but:
where does this rule send every vector?
```

Both viewpoints will later meet in null spaces, images, rank, and invertibility.

---

# Connection to neural engineering

A simplified neural decoder can map a feature vector to an output command:

$$ \mathbf{u}=A\mathbf{x}. $$

At L0, this can be treated as a linear transformation between coordinate spaces.

The columns of $A$ describe how unit changes in each input feature contribute to the output command.

This does **not** imply the biological nervous system is linear.

It means the engineered decoder is using a linear operator model.

---

# Connection forward: LA-N-0014

The next canonical lesson is:

`LA-N-0014 — Composition and matrix multiplication`.

Now suppose one transformation happens after another:

```text
input
→ transformation A
→ intermediate vector
→ transformation B
→ output
```

The natural question is:

> can the two-step action be represented as one transformation?

Yes.

The algebraic operation that represents composition will be matrix multiplication.

That is why matrix multiplication should be learned next as **composition**, not as a disconnected row-by-column recipe.

---

# What this unlocks

You should now be able to look at a planar transformation and ask:

```text
What is the input space?
What is the output space?
Does the origin stay fixed?
Is addition preserved?
Is scalar multiplication preserved?
Where do e1 and e2 go?
What do the matrix columns mean geometrically?
Does the map stretch, rotate, reflect, project, shear, or collapse directions?
Does it lose information?
How would another transformation act after this one?
```

That last question leads directly to composition and matrix multiplication.

---

# References

- **LA-REF-001** — MIT OpenCourseWare, `18.06 Linear Algebra`.
- **LA-REF-002** — MIT OpenCourseWare, `18.06SC Linear Algebra`.
- **LA-REF-003** — Sheldon Axler, *Linear Algebra Done Right*, 4th ed.
- **LA-REF-004** — Stephen Boyd and Lieven Vandenberghe, *Introduction to Applied Linear Algebra — Vectors, Matrices, and Least Squares*.
