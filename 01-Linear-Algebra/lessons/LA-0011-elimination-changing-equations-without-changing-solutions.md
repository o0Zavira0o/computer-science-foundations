---
id: LA-0011
title: "Elimination: changing equations without changing solutions"
track: linear-algebra
level: L0
status: complete
curriculum_node: LA-N-0011
concepts_introduced: ["LA-C-0011"]
concepts_deepened: ["LA-C-0008", "LA-C-0009", "LA-C-0007"]
concepts_used: ["LA-C-0010", "LA-C-0006", "LA-C-0005", "LA-C-0004", "LA-C-0002"]
examples_added: ["LA-EX-037", "LA-EX-038", "LA-EX-039", "LA-EX-040"]
references_used: ["LA-REF-001", "LA-REF-002", "LA-REF-003", "LA-REF-004"]
last_reviewed: 2026-08-27
version_sensitive: false
review_after: null
---

# Elimination: changing equations without changing solutions

## If you landed here directly

This lesson assumes:

- `LA-0008 — Systems of linear equations and solution sets`;
- `LA-0009 — Matrices as organized coefficients and operators`.

You should already know:

- a linear system is a set of simultaneous constraints;
- the solution set contains points satisfying every equation;
- a matrix can package the coefficients;
- an augmented matrix appends the right-hand side.

Now we ask:

> can we rewrite a system into an easier one without changing which points solve it?

That is the purpose of elimination.

The central mental model is:

```text
same solution set
→ different equations
→ easier structure
```

Elimination is not magic arithmetic.

It is a controlled replacement of constraints by equivalent constraints.

By the end, you should be able to:

- explain why elementary row operations preserve the solution set;
- use row swaps, nonzero row scaling, and row replacement;
- convert a system to a simpler triangular/echelon-like form;
- back-substitute in simple cases;
- distinguish a legal solution-preserving row operation from an illegal transformation;
- explain what equations like `0 = 5` and `0 = 0` mean during elimination;
- understand why elimination exposes contradictions and redundancy;
- explain why numerical arithmetic can complicate elimination in computation;
- prepare for pivots, free variables, and the geometry of solution sets.

---

## The problem worth understanding

Consider:

```math
\begin{aligned}
x+y &= 5,\\
2x+2y &= 10.
\end{aligned}
```

The second equation says nothing new.

Subtract twice the first equation from the second:

```math
\begin{aligned}
x+y &= 5,\\
0 &= 0.
\end{aligned}
```

The equations changed.

The solution set did not.

Now consider:

```math
\begin{aligned}
x+y &= 5,\\
2x+2y &= 11.
\end{aligned}
```

Do the same operation:

```math
\begin{aligned}
x+y &= 5,\\
0 &= 1.
\end{aligned}
```

The contradiction becomes obvious.

Elimination is a method for revealing structure that was already present.

---

# Part I — Equivalent systems

## Equivalent systems

Two systems are **equivalent** if they have exactly the same solution set.

Example:

```math
\begin{aligned}
x+y &= 5,\\
x-y &= 1
\end{aligned}
```

and:

```math
\begin{aligned}
x+y &= 5,\\
2y &= 4
\end{aligned}
```

are equivalent if the second system was obtained by subtracting the second original equation from the first in a solution-preserving way.

Equivalent systems need not look similar.

They need only describe the same set of solutions.

---

## The invariant

During elimination, the quantity we preserve is:

```text
solution set
```

Not:

- equation order;
- coefficient values;
- row lengths;
- visual appearance.

This is the invariant that organizes the whole lesson.

---

## Why rewriting helps

A complicated system may hide:

- contradiction;
- redundancy;
- a uniquely determined variable;
- a variable that remains free.

A simpler equivalent system makes these patterns visible.

---

# Part II — Three elementary row operations

## Operation 1 — swap two rows

You may exchange the order of two equations.

Notation:

$$ R_i \leftrightarrow R_j. $$

Why is it safe?

Because:

```text
satisfy equation A and equation B
```

means the same thing as:

```text
satisfy equation B and equation A
```

Order does not change the intersection of constraints.

---

## Example: row swap

Start:

```math
\begin{aligned}
0x+y &= 2,\\
x+3y &= 7.
\end{aligned}
```

Swap equations:

```math
\begin{aligned}
x+3y &= 7,\\
y &= 2.
\end{aligned}
```

Now the first equation has a convenient `x` coefficient.

Same solutions.

Better working order.

---

## Operation 2 — multiply one row by a nonzero scalar

Notation:

$$ R_i\leftarrow cR_i,\qquad c\neq0. $$

Example:

$$ 2x+4y=6 $$

can be divided by 2:

$$ x+2y=3. $$

Same geometric line.

---

## Why nonzero matters

If you multiply an equation by zero:

$$ x+y=5 $$

becomes:

$$ 0=0. $$

That destroys the original constraint.

Every point satisfies `0=0`.

Therefore:

```text
multiply by nonzero scalar:
safe

multiply by zero:
not equivalent
```

---

## Operation 3 — replace one row by itself plus a multiple of another row

Notation:

$$ R_i\leftarrow R_i+cR_j. $$

This is the core elimination move.

Example:

```math
\begin{aligned}
x+y &= 5,\\
2x-y &= 1.
\end{aligned}
```

Replace row 2 by:

$$ R_2\leftarrow R_2-2R_1. $$

Then:

```math
\begin{aligned}
x+y &= 5,\\
-3y &= -9.
\end{aligned}
```

The `x` term disappeared from row 2.

---

# Part III — Why row replacement is safe

## Forward direction

Suppose a point satisfies both original equations:

$$ E_1 $$

and:

$$ E_2. $$

Then it must also satisfy:

$$ E_2+cE_1. $$

So every original solution solves the transformed system.

---

## Reverse direction

Suppose a point satisfies:

$$ E_1 $$

and:

$$ E_2+cE_1. $$

Subtract:

$$ cE_1 $$

from the transformed second equation.

Then the point satisfies:

$$ E_2. $$

So every transformed solution solves the original system.

Therefore the solution sets are identical.

---

## Reversibility is the key

All elementary row operations are reversible:

### Swap

Swap again.

### Nonzero scaling

Multiply by the reciprocal.

### Row replacement

Subtract the same multiple.

Because each operation can be undone, information about the solution set is preserved.

---

# Part IV — Augmented matrix view

## System

```math
\begin{aligned}
x+2y &= 7,\\
3x-y &= 5.
\end{aligned}
```

Augmented matrix:

```math
\left[
\begin{array}{cc|c}
1 & 2 & 7\\
3 & -1 & 5
\end{array}
\right].
```

Perform:

$$ R_2\leftarrow R_2-3R_1. $$

Result:

```math
\left[
\begin{array}{cc|c}
1 & 2 & 7\\
0 & -7 & -16
\end{array}
\right].
```

The matrix operation is just shorthand for an equation operation.

---

## Do not detach rows from equations too early

A common mistake is to manipulate rows mechanically while forgetting what they represent.

At this stage, keep translating:

```text
matrix row
↔
linear equation
↔
constraint
```

That prevents symbolic mistakes from becoming meaningless procedures.

---

# Part V — Example LA-EX-037: a unique solution

Solve:

```math
\begin{aligned}
x+y &= 5,\\
2x-y &= 1.
\end{aligned}
```

Augmented matrix:

```math
\left[
\begin{array}{cc|c}
1 & 1 & 5\\
2 & -1 & 1
\end{array}
\right].
```

Eliminate `x` from row 2:

$$ R_2\leftarrow R_2-2R_1. $$

Then:

```math
\left[
\begin{array}{cc|c}
1 & 1 & 5\\
0 & -3 & -9
\end{array}
\right].
```

So:

$$ -3y=-9. $$

Hence:

$$ y=3. $$

Back-substitute into:

$$ x+y=5. $$

Then:

$$ x=2. $$

Solution:

```math
\begin{bmatrix}
2\\
3
\end{bmatrix}.
```

---

## What elimination accomplished

The original system coupled `x` and `y`.

After elimination:

```text
second row:
only y

first row:
x and y
```

This triangular dependency makes solving easier.

---

# Part VI — Back substitution

## Triangular system

A simple three-variable form:

```math
\begin{aligned}
x+2y-z &= 3,\\
y+4z &= 5,\\
2z &= 6.
\end{aligned}
```

Solve from the bottom.

Third equation gives `z`.

Then second gives `y`.

Then first gives `x`.

This is **back substitution**.

---

## Why triangular form helps

A triangular system creates a dependency chain:

```text
last variable
→ previous variable
→ earlier variable
```

Instead of solving all unknowns simultaneously, we solve them sequentially.

---

# Part VII — Example LA-EX-038: contradiction appears

Consider:

```math
\begin{aligned}
x+2y &= 4,\\
2x+4y &= 9.
\end{aligned}
```

Apply:

$$ R_2\leftarrow R_2-2R_1. $$

Then:

```math
\begin{aligned}
x+2y &= 4,\\
0 &= 1.
\end{aligned}
```

The second equation is impossible.

Therefore:

```text
solution set = empty
```

Elimination did not create the contradiction.

It exposed a contradiction that was already implicit.

---

# Part VIII — Example LA-EX-039: redundancy appears

Consider:

```math
\begin{aligned}
x-3y &= 2,\\
2x-6y &= 4.
\end{aligned}
```

Apply:

$$ R_2\leftarrow R_2-2R_1. $$

Result:

```math
\begin{aligned}
x-3y &= 2,\\
0 &= 0.
\end{aligned}
```

The second equation adds no independent constraint.

Therefore infinitely many solutions remain along the line:

$$ x-3y=2. $$

---

## `0 = 0` versus `0 = c`

These are fundamentally different.

### `0 = 0`

```text
redundant row
```

It places no new restriction.

### `0 = c`, with `c ≠ 0`

```text
contradiction
```

No solution exists.

This distinction becomes central in the next lesson.

---

# Part IX — Eliminate one variable at a time

## Strategy

For a system:

```text
row 1
row 2
row 3
```

a common strategy is:

```text
use row 1
to eliminate variable 1
from rows below

then use row 2
to eliminate variable 2
from rows below

continue
```

This creates a staircase-like structure.

---

## Why this is algorithmic

Each step has a local goal:

```text
choose a useful leading coefficient
→ eliminate below it
→ move right and down
```

The details become formalized through pivots and echelon form.

For now, focus on preserving the solution set.

---

# Part X — Choosing a convenient row

## Zero leading coefficient

Suppose:

```math
\begin{aligned}
0x+2y &= 4,\\
x+y &= 3.
\end{aligned}
```

Trying to eliminate with the first row is inconvenient.

Swap:

$$ R_1\leftrightarrow R_2. $$

Now:

```math
\begin{aligned}
x+y &= 3,\\
2y &= 4.
\end{aligned}
```

This is why row swaps are operationally useful.

---

## Small versus large coefficients

By hand, a coefficient of `1` is convenient.

In floating-point numerical computation, the choice can also affect numerical stability.

This later motivates **pivoting**.

At L0, remember:

> mathematically equivalent row choices can behave differently numerically.

---

# Part XI — Fractions are not errors

Suppose:

```math
\begin{aligned}
2x+y &= 1,\\
x-y &= 2.
\end{aligned}
```

Elimination may create fractions if you normalize early.

That is acceptable.

A fraction is not evidence that the method failed.

Sometimes postponing division keeps arithmetic simpler.

---

## Avoid unnecessary normalization

You do not have to make every leading coefficient equal to `1` immediately.

Example:

```text
3y = 12
```

can remain as-is until back substitution.

This can reduce arithmetic clutter.

---

# Part XII — Legal versus illegal transformations

## Legal

```text
swap equations
multiply an equation by nonzero scalar
replace an equation by itself plus a multiple of another equation
```

These preserve the solution set.

---

## Illegal example 1 — multiply only one term

Start:

$$ x+y=5. $$

Change to:

$$ 2x+y=5. $$

This is not a row scaling.

Only one coefficient changed.

The line changed.

The solution set changed.

---

## Illegal example 2 — square both sides

Start:

$$ x=2. $$

Square:

$$ x^2=4. $$

New solutions:

$$ x=2,\quad x=-2. $$

The transformation introduced an extra solution.

Not every algebraic manipulation is equivalence-preserving.

---

## Illegal example 3 — divide by a possibly zero expression

If you divide by a quantity that may be zero, you can lose valid solutions.

Linear row operations avoid this issue by allowing scaling only by known nonzero constants.

---

# Part XIII — Row operations versus column operations

## Row operations preserve a system's solution set

Why?

Rows represent equations.

Changing equations by reversible combinations preserves the constraint intersection.

---

## Column operations are different

Columns correspond to variables.

If you change columns without correspondingly redefining variables, you change the system.

Therefore:

```text
row operation
≠
column operation
```

Do not treat them symmetrically.

---

# Part XIV — Geometry of elimination

## Two equations in two variables

Each equation is a line.

Elimination replaces one line by another line derived from both constraints.

Yet the intersection point stays fixed.

So geometrically:

```text
change constraint representation
without moving common intersection
```

---

## Parallel inconsistent lines

If two lines are parallel but distinct, elimination exposes:

$$ 0=c,\qquad c\neq0. $$

---

## Coincident lines

If two equations describe the same line, elimination exposes:

$$ 0=0. $$

This is the algebraic shadow of geometric redundancy.

---

# Part XV — Example LA-EX-040: sensor calibration system

Suppose two unknown calibration parameters are:

```text
gain correction g
offset correction b
```

Two calibration observations produce:

```math
\begin{aligned}
2g+b &= 7,\\
5g+b &= 13.
\end{aligned}
```

Subtract row 1 from row 2:

$$ R_2\leftarrow R_2-R_1. $$

Then:

$$ 3g=6. $$

So:

$$ g=2. $$

Back-substitute:

$$ 2(2)+b=7. $$

Hence:

$$ b=3. $$

The mathematics is identical to a textbook system.

The interpretation is engineering calibration.

---

# Part XVI — Elimination as information exposure

## Before elimination

A system may look like:

```text
many coefficients
many variables
unclear structure
```

## After elimination

The same information may appear as:

```text
determined variables
redundant constraints
contradictions
remaining degrees of freedom
```

Elimination is therefore a structure-revealing process.

---

## It does not add information

Every legal row operation is reversible.

Therefore elimination cannot create genuinely new constraints.

It can only reorganize existing information.

---

## It can expose hidden redundancy

A row may become:

$$ 0=0. $$

This reveals that one original constraint was derivable from others.

---

## It can expose hidden contradiction

A row may become:

$$ 0=5. $$

This reveals that the original constraints could not all be satisfied simultaneously.

---

# Part XVII — Matrix equation connection

A system:

$$ A\mathbf{x}=\mathbf{b} $$

can be represented by the augmented matrix:

```math
\left[
\begin{array}{c|c}
A & \mathbf{b}
\end{array}
\right].
```

Row operations act on this augmented system.

They do not change the set of `x` values solving the equation.

---

## Column-combination view remains true

`LA-0010` taught:

$$ A\mathbf{x} $$

as a column combination.

Elimination does not invalidate that view.

Instead we now gain a second computational viewpoint:

```text
column view:
can columns reach b?

row view:
can we simplify the constraints?
```

Same system.

Different tools.

---

# Part XVIII — Elimination and invertible row actions

At a later level, each elementary row operation can itself be represented by multiplication by an invertible **elementary matrix**.

Conceptually:

$$ EA\mathbf{x}=E\mathbf{b}. $$

Because `E` is invertible, the solution set is preserved.

Do not memorize elementary matrices yet.

The important idea is:

> row operations are reversible linear actions on the equation representation.

---

# Part XIX — Computational complexity preview

For large dense systems, elimination requires many arithmetic operations.

Roughly, solving a dense `n × n` system by classical elimination scales on the order of:

$$ n^3 $$

arithmetic work.

This is why numerical linear algebra cares about:

- algorithm design;
- sparsity;
- memory access;
- stability.

At L0, you only need the qualitative point:

> elimination is simple conceptually but can become computationally substantial.

---

# Part XX — Floating-point arithmetic changes the practical story

## Exact arithmetic

On paper:

```text
0.1 + 0.2
```

can be treated exactly as rational arithmetic if written symbolically.

---

## Floating point

Computers store approximations to many real numbers.

Operations can accumulate rounding error.

Therefore two algebraically equivalent elimination paths can yield slightly different numerical outputs.

---

## Catastrophic amplification preview

Dividing by a very tiny coefficient can magnify error.

This is one reason numerical implementations choose pivots carefully.

---

## Partial pivoting preview

A common numerical strategy swaps rows so a larger-magnitude coefficient is used as the pivot.

Formal numerical stability comes later.

For now:

```text
row swap
```

is not only algebraically legal.

It can also be computationally wise.

---

# Part XXI — Sparse systems

Many real engineering systems contain mostly zeros.

Examples:

- network constraints;
- finite-element models;
- circuit equations.

Elimination can create new nonzero entries.

This phenomenon is called **fill-in**.

Sparse numerical solvers therefore care about row/column ordering.

This is an advanced preview, not a requirement for hand calculations.

---

# Part XXII — Failure modes

## Failure mode: elimination changes the solution

Legal elementary row operations do not.

Arithmetic mistakes can.

---

## Failure mode: `0 = 0` means no solution

Wrong.

It means a redundant constraint.

---

## Failure mode: `0 = 5` means a free variable

Wrong.

It means contradiction.

---

## Failure mode: every row must be normalized immediately

No.

Normalization is optional during many steps.

---

## Failure mode: row and column operations are interchangeable

No.

Rows encode equations; columns encode variables.

---

## Failure mode: multiplying a row by zero is allowed

No.

It destroys information.

---

## Failure mode: if elimination produces fractions, start over

No.

Fractions can be perfectly valid.

---

## Failure mode: back substitution is elimination

Related but distinct.

Elimination creates simpler structure.

Back substitution solves the triangular system.

---

## Failure mode: numerical Gaussian elimination is exactly the same as symbolic algebra

Conceptually similar.

Practically, floating-point error and pivot choice matter.

---

## Failure mode: a zero-looking number in floating point is exactly zero

Not necessarily.

Numerical algorithms use tolerances.

---

# Part XXIII — Active work

## Exercise 1 — classify row operations

For each transformation, say whether it is an elementary row operation:

1. swap rows 1 and 3;
2. multiply row 2 by `-5`;
3. multiply row 2 by `0`;
4. replace row 3 by row 3 plus `7` times row 1;
5. double only the first coefficient of row 2.

Explain each answer.

---

## Exercise 2 — unique solution

Solve by elimination:

```math
\begin{aligned}
x+2y &= 8,\\
3x-y &= 3.
\end{aligned}
```

State every row operation.

---

## Exercise 3 — contradiction

Use elimination to classify:

```math
\begin{aligned}
2x+y &= 3,\\
4x+2y &= 9.
\end{aligned}
```

What row reveals inconsistency?

---

## Exercise 4 — redundancy

Use elimination on:

```math
\begin{aligned}
x-2y &= 4,\\
3x-6y &= 12.
\end{aligned}
```

Explain the meaning of the resulting zero row.

---

## Exercise 5 — three variables

Reduce:

```math
\begin{aligned}
x+y+z &= 6,\\
2x-y+z &= 3,\\
3x+2y-z &= 4.
\end{aligned}
```

to a triangular form.

Then back-substitute.

---

## Exercise 6 — legal inverse

For:

$$ R_2\leftarrow R_2-4R_1, $$

write the row operation that undoes it.

Use this to explain why solution sets are preserved.

---

## Exercise 7 — geometry

Draw or describe two line systems:

- one inconsistent;
- one redundant.

Predict what elimination will produce before doing any arithmetic.

---

## Exercise 8 — numerical caution

Suppose one candidate leading coefficient is:

```text
0.0000001
```

and another available row has coefficient:

```text
2.3
```

Why might a numerical algorithm swap rows before eliminating?

---

# Retrieval check

Without looking back:

1. What does it mean for two systems to be equivalent?
2. What invariant does elimination preserve?
3. What are the three elementary row operations?
4. Why is row swapping safe?
5. Why is nonzero row scaling safe?
6. Why is scaling by zero unsafe?
7. What is row replacement?
8. Why is row replacement reversible?
9. How does an augmented matrix represent a system?
10. Why should you keep row meaning connected to equation meaning?
11. What is triangular structure?
12. What is back substitution?
13. What does `0 = 0` mean?
14. What does `0 = c`, `c ≠ 0`, mean?
15. Why does elimination expose rather than create contradiction?
16. Why does elimination expose redundancy?
17. Why can row swaps make elimination easier?
18. Why are fractions acceptable?
19. Why need leading entries not always be normalized immediately?
20. Give one illegal transformation that changes the solution set.
21. Why are column operations not automatically safe?
22. What do rows represent geometrically?
23. What does elimination do to line intersections?
24. How does `Ax=b` connect to an augmented matrix?
25. How does the column-span view coexist with elimination?
26. What is an elementary matrix preview?
27. Why are elementary row operations invertible?
28. Why can floating-point arithmetic affect elimination?
29. What is pivoting intended to help with?
30. Why can a tiny leading coefficient be troublesome numerically?
31. What is fill-in?
32. Why do sparse systems need special care?
33. Why can arithmetic mistakes change the apparent answer even when the method is valid?
34. What is the difference between elimination and back substitution?
35. Why is `0 = 0` not evidence of inconsistency?
36. Why is a square system not automatically uniquely solvable?
37. What does a redundant row tell you about independent information?
38. Why can elimination reveal free-variable structure before formal pivots are introduced?
39. What comes next conceptually after elimination?
40. Why is preserving the solution set more important than preserving the original equations?

---

# Connection backward: LA-0008

`LA-0008` introduced systems as simultaneous constraints.

Elimination now gives a systematic way to replace those constraints by easier equivalent ones.

The object being preserved is the same solution set.

---

# Connection backward: LA-0009

`LA-0009` introduced augmented matrices.

This lesson turns that representation into an algorithmic workspace.

Rows now become objects we intentionally transform.

---

# Connection backward: LA-0010

`LA-0010` gave the column view:

```text
Ax=b
→ can columns of A combine to reach b?
```

This lesson adds the row view:

```text
Ax=b
→ can the equations be simplified without changing which x values work?
```

The two perspectives describe the same problem.

---

# Connection forward: LA-N-0012

The next core dependency unlocked by elimination is:

`LA-N-0012 — Pivots, free variables, and the geometry of solutions`.

Elimination creates the simplified row structure.

The next lesson interprets that structure:

```text
leading information
→ pivots

undetermined coordinates
→ free variables

row structure
→ geometry of the solution set
```

---

# Connection to LA-N-0013

`LA-N-0013 — Linear transformations in the plane` remains a separate ready branch.

That branch develops the operator/geometric viewpoint.

This lesson develops the equation-solving viewpoint.

Both later reconnect in topics such as invertibility.

---

# Connection to neural engineering

Many calibration, decoding, source-estimation, and linear inverse models eventually produce systems:

$$ A\mathbf{x}\approx\mathbf{b}. $$

Exact elimination is the conceptual starting point for understanding how such systems are simplified.

Real neural-engineering problems often require:

- least squares;
- regularization;
- sparse solvers;
- numerical conditioning.

Those come later.

---

# What this unlocks

You should now be able to look at a linear system and reason:

```text
Which row operation is legal?
What variable can I eliminate?
What information is being preserved?
Did I expose a contradiction?
Did I expose redundancy?
Can I create triangular structure?
Can I back-substitute?
```

Most importantly, you should understand **why** the algorithm works:

> every allowed step replaces the system with another system having exactly the same solution set.

That invariant is the foundation for pivots, rank, invertibility, numerical linear algebra, and much more.

---

# References

- **LA-REF-001** — MIT OpenCourseWare, `18.06 Linear Algebra`.
- **LA-REF-002** — MIT OpenCourseWare, `18.06SC Linear Algebra`.
- **LA-REF-003** — Sheldon Axler, *Linear Algebra Done Right*, 4th ed.
- **LA-REF-004** — Stephen Boyd and Lieven Vandenberghe, *Introduction to Applied Linear Algebra — Vectors, Matrices, and Least Squares*.
