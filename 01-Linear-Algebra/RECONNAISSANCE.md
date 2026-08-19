# Linear Algebra — Curriculum Reconnaissance (2026-08-19)

## Purpose

This track is designed as a zero-subject-specific-knowledge path that does not stop at a first matrix course. The roadmap combines three views that are often separated too early: **geometry**, **algebraic structure**, and **computation**. It then extends those views into numerical linear algebra, matrix analysis, modern large-scale methods, and research literacy.

## Evidence classes used

1. **Canonical undergraduate matrix course:** MIT 18.06 / 18.06SC.
2. **Proof-oriented finite-dimensional theory:** Sheldon Axler, *Linear Algebra Done Right*.
3. **Applied modeling and least squares:** Boyd–Vandenberghe and Stanford EE263 materials.
4. **Data/signal/ML matrix methods:** MIT 18.065.
5. **Numerical linear algebra:** Trefethen–Bau, Higham, Golub–Van Loan, and LAPACK documentation.
6. **Advanced matrix analysis:** Horn–Johnson.
7. **Modern scalable methods:** Halko–Martinsson–Tropp and recent randomized-linear-algebra overviews.
8. **Multilinear extension:** Kolda–Bader tensor-decomposition survey.

## Scope decisions

The track begins before formal vector-space axioms. A new reader first learns why vectors, combinations, equations, and transformations are the same story viewed from different angles. Formal abstraction arrives only after those objects have meaning.

The curriculum deliberately contains both exact and numerical linear algebra. Knowing that `Ax=b` has a unique mathematical solution is different from knowing whether a floating-point algorithm can recover it reliably. Conditioning, backward error, stability, sparsity, memory movement, and large-scale algorithms therefore belong to the track rather than being treated as optional implementation trivia.

Applications to machine learning, graphics, control, scientific computing, and graphs appear when they sharpen the mathematics, but those application domains do not replace the canonical treatment owned by their neighboring tracks.

## Depth policy

The 128 nodes are an audited **dependency spine, not a lesson quota or final ceiling**. L0-L1 establish intuitive and formal undergraduate foundations; L2 deepens finite-dimensional structure; L3 develops numerical and applied competence; L4 enters graduate matrix analysis and modern scalable methods; L5 trains paper reading and reproducible computational research; L6 remains an open research frontier.

## Public-reading policy

Lessons should support non-linear public reading. A reader may land directly on a page from search, a link, or a random browse. Each lesson therefore states the local mental model, points to prerequisites when they are genuinely needed, and avoids assuming that the repository owner has followed the sequence personally.
