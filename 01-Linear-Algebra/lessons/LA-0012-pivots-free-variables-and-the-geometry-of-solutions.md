---
id: LA-0012
title: "Pivots, free variables, and the geometry of solutions"
track: linear-algebra
level: L0
status: complete
curriculum_node: LA-N-0012
concepts_introduced: ["LA-C-0012"]
concepts_deepened: ["LA-C-0011", "LA-C-0008", "LA-C-0007", "LA-C-0009"]
concepts_used: ["LA-C-0010", "LA-C-0006", "LA-C-0005", "LA-C-0004", "LA-C-0003", "LA-C-0002"]
examples_added: ["LA-EX-041", "LA-EX-042", "LA-EX-043", "LA-EX-044"]
references_used: ["LA-REF-001", "LA-REF-002", "LA-REF-003", "LA-REF-004"]
last_reviewed: 2026-08-28
version_sensitive: false
review_after: null
---
# Pivots, free variables, and the geometry of solutions

## If you landed here directly

This lesson assumes `LA-0011 — Elimination: changing equations without changing solutions`.

You should already know:

- a linear system is a set of simultaneous constraints;
- the solution set contains every point satisfying all equations;
- an augmented matrix packages coefficients and right-hand sides;
- elementary row operations preserve the solution set;
- elimination exposes contradictions and redundancy;
- a triangular or echelon-like system is easier to solve.

`LA-0011` asked:

> how can we change the equations without changing the solution set?

This lesson asks the next question:

> once elimination has exposed the structure, what does that structure tell us about how many solutions exist and what those solutions look like geometrically?

The central mental model is:

```text
elimination
→ exposes leading structure
→ pivot variables are determined by the constraints
→ nonpivot variables remain free
→ free variables become parameters
→ parameters describe the geometry of the solution set
```

By the end, you should be able to:

- identify pivot positions in a row-echelon form;
- distinguish pivot variables from free variables;
- explain why a pivot variable can depend on free variables;
- convert free variables into parameters;
- write simple solution sets parametrically;
- connect the number of free variables to degrees of freedom in a consistent system;
- distinguish unique, infinite, and empty solution sets;
- explain why a contradiction row overrides free-variable counting;
- interpret one-parameter solution families geometrically;
- connect row structure to underdetermined engineering models;
- prepare for invertibility, null spaces, rank, and later transformation ideas without prematurely formalizing them.

---

# The problem worth understanding

Suppose elimination gives:

```math
\begin{aligned}
x + 2y - z &= 4,\\
y + 3z &= 2,\\
0 &= 0.
\end{aligned}
```

`LA-0011` taught you how a zero row can appear.

Now we want to interpret the result.

The second equation gives:

$$ y = 2-3z. $$

The first equation then gives:

$$ x = 4-2y+z. $$

But nothing determines $z$ by itself.

So choose:

$$ z=t. $$

Then:

$$ y=2-3t, $$

and:

$$ x=4-2(2-3t)+t=7t. $$

The solutions are:

```math
\begin{aligned}
x &= 7t,\\
y &= 2-3t,\\
z &= t.
\end{aligned}
```

or, as vectors:

```math
\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}
=
\begin{bmatrix}
0\\
2\\
0
\end{bmatrix}
+
t
\begin{bmatrix}
7\\
-3\\
1
\end{bmatrix}.
```

The zero row did not mean "nothing happened."

It revealed that the system contains fewer independent constraints than variables.

One degree of freedom remains.

That is the beginning of pivot and free-variable structure.

---

# Part I — Row-echelon structure

## Leading entries

After elimination, a nonzero row often begins with zeros and then reaches its first nonzero coefficient.

That first nonzero coefficient is called a **leading entry**.

Example:

```math
\begin{bmatrix}
1 & 2 & -1 & | & 4\\
0 & 1 & 3  & | & 2\\
0 & 0 & 0  & | & 0
\end{bmatrix}
```

The first row has its leading entry in column 1.

The second row has its leading entry in column 2.

The third row has no leading entry because it is a zero row.

A row-echelon pattern also has two structural features worth noticing:

- as you move downward through nonzero rows, each leading position moves to the right;
- entries below a leading position are zero.

Zero rows, if any, sit below the nonzero rows.

You do not need every pivot to equal `1` to recognize this structure.

---

## Pivot positions

In row-echelon form, the locations of the leading entries are **pivot positions**.

For the matrix above:

```text
column 1 → pivot
column 2 → pivot
column 3 → no pivot
```

The variable columns containing those pivot positions are called pivot columns in this lesson.

More precisely, elimination identifies pivot *positions* in an echelon form; those positions tell us which variable columns carry leading constraints. Later lessons will use the corresponding columns of the original coefficient matrix for deeper structural questions.

The variables corresponding to pivot columns are pivot variables.

Here:

```text
x → pivot variable
y → pivot variable
z → free variable
```

---

## Pivot is a position, not merely a nonzero number

A common mistake is:

> every nonzero matrix entry is a pivot.

No.

A row can contain several nonzero entries.

Only the leading location in the echelon structure identifies the pivot position.

For:

```math
\begin{bmatrix}
1 & 5 & -2\\
0 & 3 & 7
\end{bmatrix}
```

the entries `5`, `-2`, and `7` are nonzero, but they are not pivot entries in this echelon form.

The pivots are in columns 1 and 2.

---

# Part II — Pivot variables

## What a pivot variable means

A pivot variable is constrained by a leading equation.

This does not always mean the variable equals one fixed number.

For:

$$ y+3z=2, $$

$y$ is a pivot variable, but:

$$ y=2-3z. $$

Its value depends on the free variable $z$.

So a better mental model is:

```text
pivot variable
= determined once the free variables are chosen
```

not:

```text
pivot variable
= always a fixed constant
```

---

## Back substitution becomes dependency tracing

In `LA-0011`, back substitution was an algorithm.

Here we reinterpret it.

When you back-substitute, you are discovering which pivot variables depend on which remaining degrees of freedom.

Example:

```math
\begin{aligned}
x - 2y + z &= 5,\\
y + 4z &= 1.
\end{aligned}
```

Choose:

$$ z=t. $$

Then:

$$ y=1-4t, $$

and:

$$ x=5+2y-z. $$

Therefore:

$$ x=7-9t. $$

The pivot variables $x$ and $y$ are functions of the free parameter $t$.

---

# Part III — Free variables

## What "free" means

A **free variable** corresponds to a nonpivot column.

It is free in the specific sense that the simplified system does not determine one unique value for it.

You may assign it a parameter.

Example:

$$ z=t. $$

Then every allowed value of $t$ generates one solution after the pivot variables are computed.

---

## Free does not mean unconstrained by reality

The word *free* is local to the mathematical system.

It does not mean:

- physically arbitrary;
- scientifically meaningless;
- allowed to violate external constraints;
- irrelevant.

If a real system later adds another independent equation, the variable may stop being free.

---

## Free variable as a coordinate for a family

Suppose:

```math
\begin{aligned}
x+y+z &= 4,\\
y-z &= 1.
\end{aligned}
```

Let:

$$ z=t. $$

Then:

$$ y=1+t, $$

and:

$$ x=4-y-z=3-2t. $$

So:

```math
\begin{aligned}
x &= 3-2t,\\
y &= 1+t,\\
z &= t.
\end{aligned}
```

The parameter $t$ labels different points in the solution set.

---

# Part IV — Parameters turn algebra into geometry

## Vector form

The previous solution can be written:

```math
\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}
=
\begin{bmatrix}
3\\
1\\
0
\end{bmatrix}
+
t
\begin{bmatrix}
-2\\
1\\
1
\end{bmatrix}.
```

Read this as:

```text
one particular solution
+
any scalar multiple of one direction
```

That is a line in $\mathbb{R}^3$.

---

## One free variable gives one degree of freedom

For a consistent linear system:

```text
one free variable
→ one independent parameter
→ one degree of freedom
```

Geometrically, this often produces a line-like affine solution set.

The word *affine* will be treated more formally later.

At this level, think:

> a shifted line rather than necessarily a line through the origin.

---

## Two free variables

Suppose elimination produces:

$$ x-2y+z+3w=5. $$

There is one pivot variable, $x$.

The variables $y$, $z$, and $w$ are free.

Let:

```math
\begin{aligned}
y &= s,\\
z &= t,\\
w &= u.
\end{aligned}
```

Then:

$$ x=5+2s-t-3u. $$

The solution has three independent parameters.

In four-dimensional coordinate space, this is a three-degree-of-freedom flat solution set.

You do not need to visualize four dimensions to understand the algebra.

The parameter count tells you how many independent coordinates remain adjustable.

---

# Part V — Unique solutions

## No free variables in a consistent system

Suppose echelon form is:

```math
\begin{aligned}
x+2y-z &= 4,\\
y+3z &= 2,\\
z &= -1.
\end{aligned}
```

There is a pivot in every variable column.

So:

```text
no free variables
```

Back substitution determines one value for every variable.

Therefore:

```text
consistent
+
pivot in every variable column
→ unique solution
```

---

## Example

From:

$$ z=-1, $$

we obtain:

$$ y+3(-1)=2, $$

so:

$$ y=5. $$

Then:

$$ x+2(5)-(-1)=4, $$

so:

$$ x=-7. $$

The solution set contains exactly one point:

$$ (-7,5,-1). $$

---

# Part VI — Infinite solution families

## At least one free variable and no contradiction

If the system is consistent and at least one variable is free, then the system has infinitely many solutions over the real numbers.

Why?

Because the free parameter can take infinitely many real values.

For one free parameter:

$$ t\in\mathbb{R}. $$

Each valid value generates a solution.

---

## A zero row does not automatically imply infinitely many solutions

Consider a system with two variables:

```math
\begin{aligned}
x &= 2,\\
y &= 3,\\
0 &= 0.
\end{aligned}
```

There is a zero row.

But both variable columns have pivots.

The solution is still unique:

$$ (2,3). $$

So:

```text
zero row
≠ automatically infinite solutions
```

The correct question is:

> after checking consistency, are there any nonpivot variable columns?

---

# Part VII — Inconsistency comes first

## Contradiction row

Suppose elimination produces:

```math
\begin{aligned}
x+2y-z &= 4,\\
y+3z &= 2,\\
0 &= 5.
\end{aligned}
```

The last equation can never be true.

Therefore:

```text
solution set = empty
```

Stop.

Do not continue classifying free variables as if solutions existed.

---

## Consistency test before freedom count

The correct order is:

```text
1. look for a contradiction row
2. if one exists → no solution
3. otherwise identify pivots
4. identify free variables
5. parameterize the solution family
```

This order prevents a common error:

> "There is a free variable, so there must be infinitely many solutions."

Not if the system is inconsistent.

---

# Part VIII — Example LA-EX-041: three echelon forms, three outcomes

Compare three systems in variables $x,y,z$.

## Case A — pivot in every variable column

```math
\begin{aligned}
x+y+z &= 4,\\
y-2z &= 1,\\
z &= 3.
\end{aligned}
```

Classification:

```text
consistent
3 pivot variables
0 free variables
→ unique solution
```

---

## Case B — one free variable

```math
\begin{aligned}
x+y+z &= 4,\\
y-2z &= 1,\\
0 &= 0.
\end{aligned}
```

Classification:

```text
consistent
2 pivot variables
1 free variable
→ infinitely many solutions
→ one-parameter family
```

---

## Case C — contradiction

```math
\begin{aligned}
x+y+z &= 4,\\
y-2z &= 1,\\
0 &= 3.
\end{aligned}
```

Classification:

```text
inconsistent
→ no solution
```

This comparison is the core classification logic of the lesson.

---

# Part IX — Example LA-EX-042: one free variable becomes a line

Consider:

```math
\begin{aligned}
x + 2y - z &= 3,\\
y + z &= 2.
\end{aligned}
```

The variable $z$ is free.

Let:

$$ z=t. $$

Then:

$$ y=2-t. $$

Substitute into the first equation:

$$ x+2(2-t)-t=3. $$

So:

$$ x=-1+3t. $$

Therefore:

```math
\begin{aligned}
x &= -1+3t,\\
y &= 2-t,\\
z &= t.
\end{aligned}
```

Vector form:

```math
\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}
=
\begin{bmatrix}
-1\\
2\\
0
\end{bmatrix}
+
t
\begin{bmatrix}
3\\
-1\\
1
\end{bmatrix}.
```

Interpretation:

```text
particular point = (-1,2,0)
direction = (3,-1,1)
```

As $t$ changes, the point moves along a line.

---

# Part X — Why the direction vector works

Take:

$$ t=0. $$

Then one solution is:

$$ (-1,2,0). $$

Take:

$$ t=1. $$

Then another solution is:

$$ (2,1,1). $$

The difference is:

```math
\begin{bmatrix}
2\\
1\\
1
\end{bmatrix}
-
\begin{bmatrix}
-1\\
2\\
0
\end{bmatrix}
=
\begin{bmatrix}
3\\
-1\\
1
\end{bmatrix}.
```

That difference is exactly the direction vector.

So the free parameter describes how we can move from one solution to another while staying inside every constraint.

This idea will later connect to null spaces.

For now, keep the simpler interpretation:

> the direction tells us how variables can change together without breaking the equations.

---

# Part XI — Example LA-EX-043: multiple free variables and a plane-like family

Consider:

$$ x+2y-z=4. $$

This is one equation in three variables.

Let:

```math
\begin{aligned}
y &= s,\\
z &= t.
\end{aligned}
```

Then:

$$ x=4-2s+t. $$

Therefore:

```math
\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}
=
\begin{bmatrix}
4\\
0\\
0
\end{bmatrix}
+
s
\begin{bmatrix}
-2\\
1\\
0
\end{bmatrix}
+
t
\begin{bmatrix}
1\\
0\\
1
\end{bmatrix}.
```

There are two independent parameters.

Geometrically in $\mathbb{R}^3$, the solution set is a plane.

The equation is one plane constraint, and the solution set is that plane itself.

---

# Part XII — Constraint geometry revisited

## One equation in two variables

Example:

$$ x+y=5. $$

The solution set is a line in $\mathbb{R}^2$.

There are two variables but only one independent linear constraint.

One degree of freedom remains.

---

## Two independent equations in two variables

Example:

```math
\begin{aligned}
x+y &= 5,\\
x-y &= 1.
\end{aligned}
```

Two independent line constraints intersect at one point.

No free variable remains.

---

## Two redundant equations in two variables

Example:

```math
\begin{aligned}
x+y &= 5,\\
2x+2y &= 10.
\end{aligned}
```

The second equation does not add a new independent constraint.

Elimination reveals:

$$ 0=0. $$

One free variable remains.

The solution set is the same line.

---

## Two incompatible equations in two variables

Example:

```math
\begin{aligned}
x+y &= 5,\\
2x+2y &= 11.
\end{aligned}
```

Elimination reveals:

$$ 0=1. $$

There is no common point.

The solution set is empty.

---

# Part XIII — Number of equations is not enough

## More equations do not automatically mean more information

Consider:

```math
\begin{aligned}
x+y &= 3,\\
2x+2y &= 6,\\
-4x-4y &= -12.
\end{aligned}
```

There are three equations.

But all three describe the same line.

Elimination produces two zero rows.

There is still one free variable.

---

## Fewer equations can still determine a unique solution if there are fewer variables

Example:

```math
\begin{aligned}
x+y &= 4,\\
x-y &= 2.
\end{aligned}
```

Two independent equations determine two variables uniquely.

The important object is not raw equation count.

It is the independent constraint structure exposed by pivots.

We will later formalize this with rank.

Do not use rank as a black box yet.

---

# Part XIV — Pivot columns and degrees of freedom

Suppose a consistent system has:

```text
n variables
p pivot-variable columns
```

Then the number of free variables is:

$$ n-p. $$

At this level, this is a counting rule after echelon structure is known.

Later, dimension and rank-nullity will give a deeper structural explanation.

---

## Example

A consistent system has five variables and three pivot columns.

Then:

$$ 5-3=2 $$

free variables remain.

So the solution family has two independent parameters.

---

## Caution

This counting rule does not rescue an inconsistent system.

If a contradiction row exists, the solution set is empty.

There is no valid solution family to parameterize.

---

# Part XV — Reduced row-echelon form is useful, but not required

## Echelon form is enough to identify pivots and free variables

You do not have to reduce every pivot column to zeros above the pivot.

For example:

```math
\begin{bmatrix}
1 & 2 & 3 & | & 4\\
0 & 1 & 5 & | & 2\\
0 & 0 & 0 & | & 0
\end{bmatrix}
```

already reveals:

```text
pivot columns: 1, 2
free column: 3
```

Back substitution is enough to parameterize the solutions.

---

## Reduced row-echelon form

A more fully simplified form can make dependencies easier to read directly.

But the conceptual content is the same:

```text
pivots
free variables
consistency
solution family
```

Do not mistake extra normalization for extra mathematical truth.

---

# Part XVI — Example LA-EX-044: underdetermined sensor calibration

Suppose an engineering model has three unknown calibration parameters:

```text
g = gain
b = offset
c = cross-sensitivity coefficient
```

but current experiments produce only two independent linear constraints.

After elimination, suppose the model becomes:

```math
\begin{aligned}
g + 2c &= 1.8,\\
b - c &= 0.1.
\end{aligned}
```

The variable $c$ is free.

Let:

$$ c=t. $$

Then:

```math
\begin{aligned}
g &= 1.8-2t,\\
b &= 0.1+t.
\end{aligned}
```

Many parameter triples fit the same available calibration constraints.

This does **not** mean every parameter triple is physically reasonable.

It means:

> the current linear measurements do not uniquely identify all three parameters.

Additional independent information is needed to remove the ambiguity.

This is an engineering meaning of a free variable.

---

# Part XVII — Free variables and identifiability

## Mathematical nonuniqueness

If multiple vectors $\mathbf{x}$ satisfy:

$$ A\mathbf{x}=\mathbf{b}, $$

the data and model do not determine one unique $\mathbf{x}$.

That is a mathematical statement.

---

## Scientific interpretation requires care

In a real inverse problem, nonuniqueness may mean:

- not enough independent measurements;
- redundant sensors;
- parameters enter the model in indistinguishable combinations;
- the model is too flexible for the available data.

But the algebra alone does not tell you which experimental redesign is best.

That requires domain knowledge.

---

## Connection to NNE-0009

The neural measurement chain introduced identifiability as the question:

> can the available observations distinguish one underlying explanation from alternatives?

Pivot/free-variable structure gives a simple linear-algebra version of that idea.

If a parameter direction remains free, many parameter settings can produce the same exact constraints.

---

# Part XVIII — Homogeneous preview

Consider:

$$ A\mathbf{x}=\mathbf{0}. $$

The zero vector is always a solution.

If there are no free variables, the only solution is:

$$ \mathbf{x}=\mathbf{0}. $$

If free variables exist, there are nonzero solutions too.

This observation will later become central to the null space.

For now, remember:

```text
free directions
→ ways to change x
→ without changing A x
```

That is only a preview.

The formal null-space lesson comes later.

---

# Part XIX — Unique solvability preview

Suppose a square system has one pivot in every variable column and is consistent.

Then it has a unique solution.

This prepares a later question:

> when does a matrix represent a reversible linear action?

That question becomes invertibility.

Do not jump ahead and use determinants yet.

At this point, pivot structure already tells us a great deal.

---

# Part XX — Failure modes

## Failure mode 1: every nonzero entry is a pivot

False.

A pivot is the leading structural position of a nonzero row in echelon form.

---

## Failure mode 2: pivot variable means fixed constant

False.

A pivot variable can depend on free variables.

Example:

$$ y=2-3z. $$

$y$ is a pivot variable even though its value changes with $z$.

---

## Failure mode 3: free variable means irrelevant variable

False.

A free variable parameterizes genuine variation inside the solution set.

---

## Failure mode 4: zero row means infinitely many solutions

False.

A zero row only says one row carries no additional constraint after elimination.

You still need to compare pivot columns with variable columns.

---

## Failure mode 5: free variable guarantees infinitely many solutions

False if a contradiction exists.

Always test consistency first.

---

## Failure mode 6: square system means unique solution

False.

A square system can have:

- one solution;
- infinitely many solutions;
- no solution.

Pivot and contradiction structure determine the case.

---

## Failure mode 7: more equations means more independent information

False.

Equations may be redundant.

Elimination exposes this.

---

## Failure mode 8: parameters are extra unknowns introduced by the method

Not quite.

The free variables were already undetermined by the original constraints.

Parameter notation makes that freedom explicit.

---

## Failure mode 9: one-parameter family must pass through the origin

False.

A general solution can be:

```text
particular point
+
parameter × direction
```

The particular point can be nonzero.

---

## Failure mode 10: geometry and algebra are separate stories

False.

The parameter count and direction vectors are algebraic descriptions of the geometry of the solution set.

---

# Part XXI — Active work

## Exercise 1 — identify pivots

For:

```math
\begin{bmatrix}
1 & 4 & 0 & -2 & | & 3\\
0 & 0 & 1 & 5  & | & 7\\
0 & 0 & 0 & 0  & | & 0
\end{bmatrix}
```

identify:

- pivot columns;
- pivot variables;
- free variables.

---

## Exercise 2 — classify before solving

Classify:

```math
\begin{aligned}
x+y+z &= 5,\\
y-z &= 1,\\
z &= 2.
\end{aligned}
```

Does it have:

- no solution;
- one solution;
- infinitely many solutions?

Explain using pivots and free variables before computing the actual solution.

---

## Exercise 3 — parameterize

Solve:

```math
\begin{aligned}
x+y+z &= 3,\\
y+2z &= 1.
\end{aligned}
```

Use $z=t$.

Write the answer both as coordinate equations and in vector form.

---

## Exercise 4 — contradiction first

Consider:

```math
\begin{aligned}
x+y+z &= 1,\\
y+z &= 2,\\
0 &= 4.
\end{aligned}
```

Why should you stop before counting free variables?

---

## Exercise 5 — zero row

A system in two variables reduces to:

```math
\begin{aligned}
x &= 2,\\
y &= -1,\\
0 &= 0.
\end{aligned}
```

Why is the solution unique despite the zero row?

---

## Exercise 6 — two free variables

Parameterize:

$$ x-2y+3z=6. $$

Use:

```math
\begin{aligned}
y &= s,\\
z &= t.
\end{aligned}
```

Write the solution as:

```text
particular point
+
s(direction 1)
+
t(direction 2)
```

---

## Exercise 7 — engineering interpretation

A four-parameter calibration model has only three pivot columns after elimination and is consistent.

What does one free variable mean operationally?

What kind of additional experiment might help?

Do not answer merely "add an equation."

Explain what property the new measurement must have.

---

## Exercise 8 — predict geometry

For a consistent system in $\mathbb{R}^3$, predict the typical geometry when there are:

- zero free variables;
- one free variable;
- two free variables.

---

# Retrieval check

Without looking back:

1. What is a leading entry?
2. What is a pivot position?
3. What is a pivot column?
4. What is a pivot variable?
5. Why is every nonzero entry not a pivot?
6. What is a free variable?
7. Why can a pivot variable depend on a free variable?
8. What does it mean to parameterize a solution set?
9. Why do free variables become parameters?
10. What does one free variable mean in a consistent system?
11. What does two free variables mean?
12. How do you write a one-parameter solution in vector form?
13. What is a particular solution?
14. What is a direction vector in a parameterized solution?
15. Why does the direction keep you inside the solution set?
16. When does a consistent system have a unique solution?
17. When does a consistent real linear system have infinitely many solutions?
18. What does a contradiction row mean?
19. Why must consistency be checked before free-variable counting?
20. Why does a zero row not automatically imply infinitely many solutions?
21. Why does a square system not automatically have one solution?
22. Why is raw equation count not enough?
23. How do redundant equations appear after elimination?
24. If a consistent system has $n$ variables and $p$ pivot columns, how many free variables remain?
25. Why is reduced row-echelon form not required for identifying free variables?
26. What engineering meaning can a free parameter have?
27. What is the difference between mathematical nonuniqueness and a physical explanation of that nonuniqueness?
28. What does a free direction preview about homogeneous systems?
29. What later topic formalizes the set of vectors satisfying $A\mathbf{x}=\mathbf{0}$?
30. How does pivot structure prepare the idea of invertibility?
31. How does this lesson deepen the geometry of solution sets from `LA-0008`?
32. How does this lesson reinterpret elimination from `LA-0011`?

---

# Connection backward: LA-0011

`LA-0011` established the invariant:

```text
elementary row operations
→ change the equations
→ preserve the solution set
```

This lesson reads the result of that process.

The focus changes from:

```text
How do I simplify the system?
```

to:

```text
What does the simplified structure tell me?
```

The interpretation is:

```text
leading structure
→ pivots

nonpivot variable columns
→ free variables

free variables
→ parameters

parameters
→ geometry of the solution set
```

---

# Connection backward: LA-0008

`LA-0008` introduced:

```text
unique solution
no solution
infinitely many solutions
```

as possible solution-set outcomes.

This lesson gives an algebraic classification tool:

```text
contradiction
→ no solution

consistent + no free variables
→ unique solution

consistent + at least one free variable
→ infinitely many solutions
```

---

# Connection backward: LA-0007

`LA-0007` treated each equation as a geometric constraint.

This lesson explains how independent constraints remove degrees of freedom.

In $\mathbb{R}^3$:

```text
one independent plane constraint
→ typically a plane solution set

two compatible independent plane constraints
→ typically a line

three compatible independent constraints
→ potentially a point
```

Redundancy means a new equation did not remove another degree of freedom.

Contradiction means the constraints share no common point.

---

# Connection backward: LA-0010

`LA-0010` gave the column view:

$$ A\mathbf{x}=\mathbf{b}. $$

It asked:

> can the columns of $A$ combine to reach $\mathbf{b}$?

This lesson asks:

> if they can, are the coefficients $\mathbf{x}$ uniquely determined?

If free variables remain, then different coefficient choices can produce the same target $\mathbf{b}$.

That observation later connects span, independence, null space, and invertibility.

---

# Connection to neural engineering

Linear neural-engineering models often have the form:

$$ A\mathbf{x}=\mathbf{b} $$

or approximately:

$$ A\mathbf{x}\approx\mathbf{b}. $$

Possible meanings include:

- unknown source amplitudes;
- calibration parameters;
- decoder coefficients;
- stimulation commands;
- sensor-mixing parameters.

If an exact linear model has free variables, multiple parameter vectors may satisfy the same constraints.

That is a structural ambiguity.

It does not by itself tell us which solution is biologically correct.

Additional measurements, modeling assumptions, or later methods may be required.

---

# Connection forward

`LA-N-0013 — Linear transformations in the plane` remains a separate authorable branch.

This lesson develops the equation-solving structure.

`LA-N-0013` develops the operator/geometric action viewpoint.

Later topics reconnect these perspectives.

In particular:

- `LA-N-0015` will relate unique solvability to invertibility;
- `LA-N-0024` will formalize null space;
- `LA-N-0026` will formalize rank and rank-nullity.

For now, do not replace the present ideas with later vocabulary.

The important L0 understanding is already available:

```text
pivots tell us what is determined
free variables tell us what remains adjustable
contradictions tell us whether any solution exists
parameters reveal the geometry of all solutions
```

---

# What this unlocks

You should now be able to look at an echelon-form system and reason:

```text
Is there a contradiction?
Where are the pivots?
Which variables are pivot variables?
Which variables are free?
How many degrees of freedom remain?
Can I parameterize every solution?
Is the solution set empty, one point, or a family?
What geometric object does the parameterization describe?
What ambiguity would this represent in an engineering model?
```

Elimination gave you a way to reveal structure.

Pivots and free variables give you a language for interpreting that structure.

---

# References

- **LA-REF-001** — MIT OpenCourseWare, `18.06 Linear Algebra`.
- **LA-REF-002** — MIT OpenCourseWare, `18.06SC Linear Algebra`.
- **LA-REF-003** — Sheldon Axler, *Linear Algebra Done Right*, 4th ed.
- **LA-REF-004** — Stephen Boyd and Lieven Vandenberghe, *Introduction to Applied Linear Algebra — Vectors, Matrices, and Least Squares*.
