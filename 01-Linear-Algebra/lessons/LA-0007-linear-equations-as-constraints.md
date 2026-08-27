---
id: LA-0007
title: "Linear equations as constraints"
track: linear-algebra
level: L0
status: complete
curriculum_node: LA-N-0007
concepts_introduced: ["LA-C-0007"]
concepts_deepened: ["LA-C-0002", "LA-C-0003"]
concepts_used: ["LA-C-0001", "LA-C-0004", "LA-C-0005", "LA-C-0006"]
examples_added: ["LA-EX-021", "LA-EX-022", "LA-EX-023", "LA-EX-024"]
references_used: ["LA-REF-001", "LA-REF-002", "LA-REF-003", "LA-REF-004"]
last_reviewed: 2026-08-27
version_sensitive: false
review_after: null
---

# Linear equations as constraints

## If you landed here directly

This lesson assumes only the early L0 foundations.

You should already be able to:

- distinguish scalars from coordinate vectors;
- read simple coordinate notation;
- interpret a vector as data, displacement, or state;
- understand that equations can express relationships among quantities.

You do **not** need elimination or matrices yet.

This lesson introduces the central idea that a linear equation is not merely something to "solve for x."

It is a **constraint**.

A constraint says:

> among all possible assignments of values, only some are allowed.

By the end, you should be able to:

- recognize a linear equation;
- distinguish linear from nonlinear expressions in simple cases;
- interpret one linear equation as a geometric set of allowed points;
- explain why a two-variable linear equation usually describes a line;
- explain why a three-variable linear equation usually describes a plane;
- interpret coefficients and constants structurally;
- move between algebraic, geometric, and application views;
- understand why several simultaneous equations mean intersecting constraints;
- connect linear equations to span membership and future systems of equations.

---

## The problem worth understanding

Suppose two quantities `x` and `y` must satisfy:

$$ 2x+y=6. $$

A beginner may immediately ask:

> What is x?

But there is not one unique `x`.

Examples of valid pairs include:

```text
x = 0, y = 6
x = 1, y = 4
x = 2, y = 2
x = 3, y = 0
x = 4, y = -2
```

The equation is therefore not naming one point.

It is selecting an entire set of allowed points.

That set is the solution set of the constraint.

---

## Equation as a filter

Imagine all possible points in the plane:

```text
(x, y)
```

The equation:

$$ 2x+y=6 $$

acts like a filter.

Only points satisfying the relationship survive.

```text
all possible (x,y)
→ apply equation
→ keep only valid points
```

That surviving set is a line.

So a linear equation can be understood as:

> a rule that removes degrees of freedom.

---

## What makes an equation linear?

A simple scalar equation is linear when the variables appear only to the first power and are combined by scalar multiplication and addition.

Examples:

$$ 2x+3y=7 $$

$$ -x+4z=2 $$

$$ 5x-2y+z=0 $$

These are linear.

Examples that are not linear:

$$ x^2+y=3 $$

$$ xy=5 $$

$$ \sin(x)+y=2 $$

$$ \frac{1}{x}+y=4 $$

The distinction matters because linear equations have especially structured solution sets.

---

## General form in two variables

A linear equation in `x,y` can be written:

$$ ax+by=c. $$

Here:

- `a,b` are coefficients;
- `c` is a constant;
- `x,y` are variables.

When `a` and `b` are not both zero, the solution set is a line in the plane.

---

## Why a line?

Solve for `y` when `b` is nonzero:

$$ y=-\frac{a}{b}x+\frac{c}{b}. $$

This is the familiar slope-intercept form:

$$ y=mx+k. $$

where:

$$ m=-\frac{a}{b} $$

and:

$$ k=\frac{c}{b}. $$

So the coefficient pair `(a,b)` determines the orientation of the line.

The constant `c` shifts where the line sits.

---

## Constraint versus formula

The equation:

$$ y=2x+1 $$

can be read as a formula computing `y` from `x`.

But it can also be read as a constraint:

$$ -2x+y=1. $$

These are the same relation.

The second form emphasizes symmetry:

> a pair `(x,y)` is valid if it satisfies the equation.

This viewpoint becomes more powerful in systems of equations.

---

## Example LA-EX-021 — one budget equation

Suppose a project buys:

- `x` units of component A at \$2 each;
- `y` units of component B at \$3 each.

Total cost must be \$12.

Constraint:

$$ 2x+3y=12. $$

If fractional quantities are allowed mathematically, the solution set is a line.

If the application requires nonnegative integer quantities, only selected points on that line are physically valid.

This separates:

```text
algebraic solution set
from
application-valid solution set
```

The equation captures one linear relationship.

Domain restrictions add extra constraints.

---

## Coefficients define sensitivity

In:

$$ 2x+3y=12, $$

changing `x` by one unit changes the left side by `2`.

Changing `y` by one unit changes it by `3`.

So coefficients encode how strongly each variable contributes to the constraint.

This becomes important in:

- resource accounting;
- mixtures;
- physical balance equations;
- linear models;
- optimization.

---

## Zero coefficients remove a variable

Consider:

$$ 0x+2y=8. $$

This simplifies to:

$$ y=4. $$

The variable `x` is unconstrained by this equation.

Geometrically, the solution set is a horizontal line.

So a zero coefficient means:

> this equation imposes no direct restriction on that variable.

---

## Constant term shifts the allowed set

Compare:

$$ x+y=0 $$

and:

$$ x+y=5. $$

They have the same coefficients.

Therefore they have the same orientation.

But they are different parallel lines.

The constant determines which level set is selected.

---

## Homogeneous equation

An equation with zero right-hand side:

$$ ax+by=0 $$

is called **homogeneous**.

Its solution set always contains the origin because:

$$ a(0)+b(0)=0. $$

This connects to span and subspace ideas.

For example:

$$ x-2y=0 $$

describes a line through the origin.

---

## Nonhomogeneous equation

An equation such as:

$$ ax+by=c $$

with `c` nonzero is nonhomogeneous.

Its solution line generally does not pass through the origin.

This is the first hint of the difference between:

- linear subspaces through zero;
- shifted affine sets.

---

## Equation normal vector

For:

$$ ax+by=c, $$

the coefficient vector:

```math
\mathbf{n}=
\begin{bmatrix}
a\\
b
\end{bmatrix}
```

is perpendicular to the solution line.

Why?

If two solution points differ by a direction vector `d`, moving along the line must not change the constraint value.

So:

$$ \mathbf{n}\cdot\mathbf{d}=0. $$

You do not need dot-product mastery here.

Keep the geometric intuition:

> the coefficient vector points across the line, not along it.

---

## Moving along a solution line

Suppose:

$$ x+2y=4. $$

One solution is:

```math
(x,y)=(4,0).
```

A direction that preserves the equation is:

```math
\begin{bmatrix}
-2\\
1
\end{bmatrix}.
```

Why?

If we change:

```text
x by -2
y by +1
```

then:

$$ \Delta(x+2y)=-2+2(1)=0. $$

So the constraint remains satisfied.

This is a powerful idea:

> directions tangent to a constraint leave its left-hand side unchanged.

---

## Parametric description

For:

$$ x+2y=4, $$

let:

$$ y=t. $$

Then:

$$ x=4-2t. $$

So every solution can be written:

```math
\begin{bmatrix}
x\\
y
\end{bmatrix}
=
\begin{bmatrix}
4\\
0
\end{bmatrix}
+
t
\begin{bmatrix}
-2\\
1
\end{bmatrix}.
```

This says:

```text
one particular solution
+
any multiple of a direction preserving the constraint
```

Later this pattern will become central for solution sets.

---

## Connection to span

The direction part:

```math
t
\begin{bmatrix}
-2\\
1
\end{bmatrix}
```

belongs to the span of one vector.

So a nonhomogeneous solution line can be seen as:

```text
particular point
+
span of allowed direction
```

This is an affine shift of a span.

That is an important bridge from `LA-0006`.

---

## One equation in three variables

Consider:

$$ x+2y-z=3. $$

Now there are three variables but only one scalar constraint.

The solution set is generally a plane in `R^3`.

Why?

There are many ways to vary two directions while still satisfying one relationship.

One equation removes one degree of freedom from three-dimensional ambient space.

---

## Example LA-EX-022 — a plane of valid states

Suppose a simplified state vector is:

```math
\mathbf{x}=
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}.
```

The state must satisfy:

$$ x_1+x_2+x_3=1. $$

This equation selects a plane in `R^3`.

If we also impose:

```text
x_i >= 0
```

then the physically valid region becomes only a triangular portion of that plane.

Again:

```text
linear equality
+
domain restrictions
=
application-specific feasible set
```

---

## Number of variables versus number of constraints

A single equation involving many variables typically leaves many possibilities.

Example:

$$ x_1+x_2+x_3+x_4=10. $$

There are four variables and one equation.

We should not expect one unique solution.

This is a useful diagnostic habit:

> count unknowns and independent constraints before expecting uniqueness.

Formal rank comes later.

---

## Linear equation as balance

Many physical laws can be written as balances.

Example:

$$ \text{inflow}-\text{outflow}=0. $$

If each term depends linearly on variables, the result is a linear equation.

Examples can include simplified:

- current balance;
- force balance;
- mass balance;
- budget balance;
- conservation constraints.

The equation expresses compatibility, not merely arithmetic.

---

## Linear equation as measurement

Suppose a sensor returns:

$$ y=2x_1-x_2. $$

This can be rewritten:

$$ 2x_1-x_2-y=0. $$

So a measurement relation is also a constraint linking hidden variables and observed variables.

This viewpoint will matter in inverse problems.

---

## Linear equation as prediction relation

A regression model may say:

$$ \hat{y}=b_0+b_1x_1+b_2x_2. $$

For fixed coefficients, each input pair determines a prediction.

But if we treat `x_1,x_2,\hat{y}` jointly, the relation defines a plane.

So the same equation supports both:

- function view;
- geometric constraint view.

---

## Linear equation as hyperplane

In higher dimensions:

$$ a_1x_1+\cdots+a_nx_n=c $$

defines a hyperplane when the coefficient vector is nonzero.

You cannot visualize `R^100`.

But the structural rule survives.

A hyperplane is the higher-dimensional analogue of:

- a line in `R^2`;
- a plane in `R^3`.

---

## Degrees of freedom intuition

If one independent linear equation constrains `n` variables, the solution set usually has roughly:

```text
n - 1
```

degrees of freedom.

Examples:

```text
2 variables - 1 constraint → line
3 variables - 1 constraint → plane
4 variables - 1 constraint → 3D-like hyperplane in R4
```

This is intuition, not yet a complete theorem.

Dependence and degeneracy can complicate counting.

---

## Degenerate cases

Consider:

$$ 0x+0y=0. $$

Every point satisfies it.

So the solution set is all of `R^2`.

Now consider:

$$ 0x+0y=5. $$

No point satisfies it.

So the solution set is empty.

These cases show why the condition:

```text
a and b not both zero
```

matters when saying `ax+by=c` describes a line.

---

## Solving for one variable can hide geometry

Take:

$$ 3x-2y=6. $$

Solving for `y`:

$$ y=\frac32x-3. $$

This is useful.

But if we stop there, we may miss:

- the coefficient normal direction;
- the solution set as a constraint;
- the connection to systems.

The best practice is to switch views.

---

## Three views of the same equation

For:

$$ 2x+y=6 $$

### Algebraic view

A relationship among scalar variables.

### Geometric view

A line of valid points in the plane.

### Constraint view

A filter selecting allowed states.

These are not competing interpretations.

They are three views of one object.

---

## Example LA-EX-023 — same equation, three narratives

Consider:

$$ 4x+2y=8. $$

### Geometry

A line.

### Budget story

If `x` costs 4 units and `y` costs 2 units, combinations on the line use total budget 8.

### Measurement story

A sensor reading is fixed at 8 when it measures `4x+2y`.

Same equation.

Different semantic interpretation.

The algebra is reusable because the constraint structure is shared.

---

## Unit consistency matters

Suppose:

$$ 2x+3y=12. $$

If `x` is meters and `y` is seconds, adding them directly may be physically meaningless unless coefficients convert units appropriately.

Linear algebra does not automatically enforce unit consistency.

The modeler must.

---

## Scaling an equation does not change its solution set

Compare:

$$ 2x+y=6 $$

and:

$$ 4x+2y=12. $$

The second equation is just twice the first.

They define the same line.

Multiplying every term by a nonzero scalar does not change the solution set.

This fact becomes central to elimination.

---

## Dividing an equation by a nonzero scalar

Similarly:

$$ 6x+3y=9 $$

can be divided by `3`:

$$ 2x+y=3. $$

Same constraint.

This teaches an important principle:

> equations can change form without changing the allowed states.

Later row operations generalize this.

---

## But adding arbitrary terms changes the constraint

If you change only one side or one coefficient without a valid algebraic operation, you generally change the solution set.

Equation manipulation must preserve equivalence.

The point of algebraic transformations is to simplify the representation while keeping the same allowed points.

---

## Intersections preview systems

Now suppose two constraints must hold:

$$ x+y=5 $$

and:

$$ x-y=1. $$

Each equation is a line.

The valid states must lie on **both** lines.

Geometrically:

```text
solution set
=
intersection of constraint 1
and constraint 2
```

For these two lines, the intersection is one point.

This is the central idea of the next lesson.

---

## Example LA-EX-024 — two constraints as an intersection

Consider:

$$ x+y=4 $$

and:

$$ 2x-y=1. $$

Constraint 1 defines one line.

Constraint 2 defines another.

A point is a solution to the system only if it satisfies both.

Solve:

From the first:

$$ y=4-x. $$

Substitute into the second:

$$ 2x-(4-x)=1. $$

So:

$$ 3x=5. $$

Therefore:

$$ x=\frac53. $$

and:

$$ y=\frac73. $$

The point:

```math
\begin{bmatrix}
5/3\\
7/3
\end{bmatrix}
```

is the intersection.

This is not yet a full systems lesson.

It is a preview of constraint intersection.

---

## Zero, one, or many intersections

Two linear constraints can have:

### One solution

Two nonparallel lines intersect once.

### No solution

Two distinct parallel lines never intersect.

### Infinitely many solutions

Two equations describe the same line.

This trichotomy becomes a major theme in `LA-0008`.

---

## Same line, different equation

Example:

$$ x+y=3 $$

and:

$$ 2x+2y=6. $$

These look different.

But the second is twice the first.

They impose the same constraint.

So a system containing both does not add a new independent restriction.

This previews redundancy among equations.

---

## Parallel incompatible constraints

Consider:

$$ x+y=3 $$

and:

$$ x+y=5. $$

Same orientation.

Different constants.

No point can satisfy both.

The system is inconsistent.

This geometric picture will later correspond to elimination producing a contradiction.

---

## Constraint independence intuition

Two equations can be:

- genuinely independent constraints;
- redundant copies;
- contradictory.

This mirrors an earlier vector-side distinction:

- generators can add new directions;
- generators can be redundant.

Linear algebra repeatedly studies redundancy on both equation and vector sides.

---

## Span membership revisited

In `LA-0006`, target membership asked:

$$ a\mathbf{u}+b\mathbf{v}=\mathbf{t}. $$

Coordinate-wise, this becomes equations.

Suppose:

```math
\mathbf{u}=
\begin{bmatrix}
u_1\\
u_2
\end{bmatrix},
\qquad
\mathbf{v}=
\begin{bmatrix}
v_1\\
v_2
\end{bmatrix},
\qquad
\mathbf{t}=
\begin{bmatrix}
t_1\\
t_2
\end{bmatrix}.
```

Then:

$$ au_1+bv_1=t_1 $$

and:

$$ au_2+bv_2=t_2. $$

So a vector reachability problem becomes a system of linear constraints on coefficients.

This is one of the most important translations in the course.

---

## Constraint space versus variable space

When we solve:

$$ a\mathbf{u}+b\mathbf{v}=\mathbf{t}, $$

the unknowns are `a,b`.

The equations constrain the **coefficient space**.

This is different from the original geometric space where `u,v,t` live.

Always ask:

> Which quantities are variables in this equation?

Linear algebra often moves between spaces.

---

## Row viewpoint preview

Later, a matrix equation:

$$ A\mathbf{x}=\mathbf{b} $$

can be read row by row.

Each row gives one linear equation:

$$ \text{row}_i(A)\cdot\mathbf{x}=b_i. $$

So each row imposes one constraint on `x`.

The system solution is the intersection of all row constraints.

We are learning the row-constraint view before matrices are formally introduced.

---

## Column viewpoint preview

The same future equation:

$$ A\mathbf{x}=\mathbf{b} $$

also has a column-combination interpretation:

> combine columns of `A` using coefficients from `x` to reach `b`.

So one matrix equation has two major readings:

```text
row view:
constraints on x

column view:
combination of generators
```

Later lessons will connect them.

---

## Linear constraints in data

Suppose three measured features satisfy:

$$ x_3=2x_1-x_2. $$

Then valid data points lie on a plane in `R^3`.

This means the three coordinates are not freely varying.

There is structural dependence.

A dataset close to that plane may suggest an approximate linear relationship.

---

## Exact versus approximate constraints

Real data often do not satisfy equations exactly.

Instead of:

$$ 2x+y=6, $$

we may observe points near the line.

Then the model becomes approximate:

$$ 2x+y\approx6. $$

Later least squares will quantify closeness.

This lesson focuses on exact constraints.

---

## Constraint violation as residual

For a candidate point `(x,y)`, define:

$$ r=2x+y-6. $$

If:

$$ r=0, $$

the constraint is satisfied.

If `r` is nonzero, the point violates the equation.

This quantity is a **residual**.

Residuals become central in numerical methods and data fitting.

---

## Signed residual

The sign of:

$$ r=ax+by-c $$

tells which side of the constraint hyperplane the point lies on under the coefficient orientation.

The magnitude reflects algebraic violation.

Geometric distance requires normalization by the coefficient magnitude.

That refinement comes later.

---

## Hyperplanes divide space

A nondegenerate equation:

$$ a_1x_1+\cdots+a_nx_n=c $$

creates a hyperplane.

Points with:

$$ a_1x_1+\cdots+a_nx_n>c $$

lie on one side.

Points with:

$$ a_1x_1+\cdots+a_nx_n<c $$

lie on the other.

This becomes important in:

- classification;
- optimization;
- geometry;
- constraints.

---

## Equality versus inequality

A linear equality:

$$ ax+by=c $$

selects the boundary line itself.

A linear inequality:

$$ ax+by\le c $$

selects one side plus the boundary.

This course will later use inequalities in optimization-related contexts.

For now, keep the distinction:

```text
equality
→ hyperplane

inequality
→ half-space
```

---

## Why equations are useful models

A linear equation is compact.

It can encode:

- conservation;
- compatibility;
- balance;
- calibration;
- mixture relations;
- measurement laws;
- geometric boundaries.

The power comes from structure.

Many different stories reduce to the same mathematical object.

---

## But linearity is an assumption

A real system may be nonlinear.

Examples:

- saturation;
- products of variables;
- threshold effects;
- exponential growth;
- nonlinear sensors.

Writing a linear equation is a modeling choice.

Always separate:

```text
equation is mathematically linear
from
real system is adequately modeled as linear
```

---

## Local linearization preview

Even nonlinear systems can sometimes be approximated linearly near an operating point.

That is why linear equations remain useful far beyond exactly linear physics.

Formal linearization comes later.

The present lesson establishes the geometry that those local approximations use.

---

## Common failure mode: one equation means one answer

Not with several variables.

One equation usually describes a family of solutions.

---

## Common failure mode: solving for y is the whole meaning

No.

The equation is fundamentally a constraint set.

Slope-intercept form is one representation.

---

## Common failure mode: every linear equation is a line

Only in two variables.

In three variables it is typically a plane.

In higher dimensions it is a hyperplane.

---

## Common failure mode: coefficients only affect slope

In general they define the normal direction and relative variable contribution.

The constant shifts the constraint.

---

## Common failure mode: same-looking variables imply same units

No.

Semantic and unit consistency still matter.

---

## Common failure mode: multiplying an equation changes the solutions

Multiplying every term by the same nonzero scalar preserves the solution set.

---

## Common failure mode: homogeneous means one unique zero solution

Not necessarily.

A homogeneous equation always includes zero but usually has many other solutions.

---

## Common failure mode: two equations always produce one point

They can produce:

- one point;
- no points;
- infinitely many points.

---

## Common failure mode: redundant equation adds information

If one equation is a scalar multiple of another, it adds no new constraint.

---

## Common failure mode: span and equations are unrelated topics

They are closely connected.

Span membership becomes coefficient equations.

---

## Common failure mode: approximate data relations are exact equations

Real measurements often include noise and model mismatch.

Exact and approximate constraints must be distinguished.

---

## Active work

### Exercise 1 — classify equations

Label each as linear or nonlinear:

$$ 2x+3y=5 $$

$$ x^2+y=5 $$

$$ xy=2 $$

$$ -4x+z=0 $$

$$ \sin(x)+y=1 $$

Explain why.

### Exercise 2 — generate solutions

For:

$$ x+2y=8, $$

find five solution pairs.

Then describe the geometry.

### Exercise 3 — normal direction

For:

$$ 3x-y=4, $$

identify the coefficient vector.

Explain why it points normal to the line.

### Exercise 4 — parametric form

Convert:

$$ x+2y=4 $$

into:

```text
particular solution
+
t × direction vector
```

Verify by substitution.

### Exercise 5 — one equation in R3

Describe geometrically:

$$ x+y+z=1. $$

Give three valid points.

### Exercise 6 — equivalent equations

Determine whether these represent the same constraint:

$$ 2x+y=6 $$

$$ 6x+3y=18. $$

Explain.

### Exercise 7 — two constraints

Sketch or reason about:

$$ x+y=4 $$

$$ x-y=0. $$

Find their intersection.

### Exercise 8 — span connection

Given:

```math
\mathbf{u}=
\begin{bmatrix}
1\\
2
\end{bmatrix},
\qquad
\mathbf{v}=
\begin{bmatrix}
3\\
-1
\end{bmatrix},
\qquad
\mathbf{t}=
\begin{bmatrix}
7\\
3
\end{bmatrix},
```

write the coordinate equations for:

$$ a\mathbf{u}+b\mathbf{v}=\mathbf{t}. $$

Do not solve them yet.

Explain what the equations mean as constraints on `(a,b)`.

---

## Retrieval check

Without looking back:

1. What is a linear equation?
2. What does it mean to call an equation a constraint?
3. Why does one equation in two variables usually not have one solution?
4. What geometry does `ax+by=c` usually define?
5. What geometry does one linear equation in three variables usually define?
6. What is a hyperplane?
7. What is the role of coefficients?
8. What is the role of the constant?
9. What happens if one coefficient is zero?
10. What is a homogeneous equation?
11. Why does a homogeneous equation contain the origin?
12. What is a nonhomogeneous equation?
13. Why can scaling an equation by a nonzero constant preserve solutions?
14. What is the coefficient normal vector?
15. What does a tangent direction to the constraint do to the left-hand side?
16. How can a solution line be written parametrically?
17. How does that connect to span?
18. What is a degenerate equation?
19. What does `0=0` represent as a constraint?
20. What does `0=5` represent?
21. What is the difference between formula view and constraint view?
22. How can one equation represent a budget?
23. How can one equation represent a measurement relation?
24. What is a residual?
25. What does zero residual mean?
26. What does a linear inequality represent geometrically?
27. How do two equations combine geometrically?
28. What are the three possible intersection patterns for two lines?
29. What makes one equation redundant with another?
30. What does inconsistency mean?
31. How does span membership create equations?
32. In a future matrix equation, what will rows represent?
33. What will columns represent?
34. Why should we separate exact and approximate constraints?
35. Why is linearity a modeling assumption?

---

## Connection backward: LA-0006

`LA-0006` asked:

> can a target be reached by linear combinations?

That question became:

$$ a\mathbf{u}+b\mathbf{v}=\mathbf{t}. $$

Coordinate-wise, this creates scalar equations.

So span membership and linear constraints are two views of the same reachability problem.

---

## Connection backward: LA-0002

`LA-0002` introduced coordinates and tuples.

This lesson gives coordinates a new role:

> variables whose allowed combinations are restricted by equations.

A point is no longer merely a stored tuple.

It is a candidate state that may or may not satisfy the constraint.

---

## Connection forward: LA-0008

The next canonical lesson is:

`LA-N-0008 — Systems of linear equations and solution sets`.

One equation gives one constraint set.

Several equations require simultaneous satisfaction.

Geometrically:

```text
solution of system
=
intersection of constraint sets
```

The next lesson will study:

- zero solutions;
- one solution;
- infinitely many solutions;
- consistency;
- redundancy.

---

## Connection forward: matrices

Matrices will organize many coefficients.

Later:

```math
A\mathbf{x}=\mathbf{b}
```

will represent several linear constraints at once.

The row view will be:

```text
each row
→ one equation
→ one constraint
```

This lesson is therefore pre-matrix groundwork.

---

## Connection forward: elimination

Elimination changes equation representation while preserving the solution set.

The fact that:

$$ 2x+y=6 $$

and:

$$ 4x+2y=12 $$

define the same line is the simplest preview.

Later row operations will formalize solution-preserving transformations.

---

## Connection forward: row space

Much later, rows of a matrix will themselves form vectors.

Their span will describe the space of linear constraints generated by the equations.

So span returns on the **constraint side** of linear algebra.

---

## Connection to LLMs

A linear layer computes weighted sums plus biases.

Each output coordinate can be read as a linear equation relating:

- input coordinates;
- weights;
- output value.

Later, hyperplanes also appear in classification boundaries and representation geometry.

The simple constraint view scales directly into machine learning.

---

## Connection to neural engineering

Neural engineering models often impose linear constraints such as:

- current balance;
- mixing relations;
- sensor calibration;
- linear decoder equations;
- state relationships.

Even when the true biology is nonlinear, local linear models can be useful.

This lesson teaches how to interpret those equations geometrically rather than as opaque algebra.

---

## What this unlocks

You should now be able to move among:

```text
equation
↔
constraint
↔
geometric solution set
```

and understand:

```text
one equation in R2
→ usually a line

one equation in R3
→ usually a plane

several equations
→ intersection of constraints
```

You should also be able to translate span membership into coefficient equations.

That is enough to study systems of linear equations as structured intersections.

---

## References

- **LA-REF-001** — MIT OpenCourseWare, `18.06 Linear Algebra`.
- **LA-REF-002** — MIT OpenCourseWare, `18.06SC Linear Algebra`.
- **LA-REF-003** — Sheldon Axler, *Linear Algebra Done Right*, 4th ed.
- **LA-REF-004** — Stephen Boyd and Lieven Vandenberghe, *Introduction to Applied Linear Algebra — Vectors, Matrices, and Least Squares*.
