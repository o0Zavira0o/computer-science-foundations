---
id: LA-EXR-0003
title: Interpret One Vector in Three Worlds
track: linear-algebra
level: L0
status: complete
curriculum_nodes: ["LA-N-0003"]
concepts_used: ["LA-C-0001", "LA-C-0002", "LA-C-0003"]
references_used: ["LA-REF-001", "LA-REF-004"]
last_reviewed: 2026-08-20
---

# Interpret One Vector in Three Worlds

## Goal

Demonstrate that you can separate vector structure from domain interpretation and construct clear displacement, data, and state-vector meanings without changing the underlying coordinate notation.

## Part A — three interpretations of the same coordinates

Start with

$$
v=(2,-1,3).
$$

Construct three semantic interpretations:

1. a displacement-like interpretation;
2. a data-record interpretation;
3. a state-vector interpretation.

For each, specify:

```text
meaning of coordinate 1:
meaning of coordinate 2:
meaning of coordinate 3:
units (if any):
what the whole vector represents:
```

Then write which facts stay unchanged across all three interpretations.

## Part B — point or displacement?

Suppose

$$
p=(4,2)
$$

is a point measured from an origin, while

$$
d=(4,2)
$$

is a displacement instruction.

Answer:

1. What is numerically identical?
2. What is semantically different?
3. Why can a coordinate list alone fail to tell you the role?

Draw a small diagram if useful.

## Part C — coordinate-contract debugging

A health model expects

$$
x=(\text{age},\text{resting heart rate},\text{hours of sleep}).
$$

A data pipeline emits the same three values in this order:

$$
(\text{hours of sleep},\text{age},\text{resting heart rate}).
$$

Explain why both objects can have the correct mathematical shape while the second is still a serious representation error.

## Part D — design a state

Choose a system you understand and define

$$
s\in\mathbb{R}^n.
$$

Use at least three coordinates.

Document:

- every coordinate meaning;
- units;
- why each variable belongs in the model;
- one important aspect of the real system that your vector omits.

Then explain what “state” means relative to your chosen model rather than to reality in full detail.

## Part E — unit-awareness challenge

Suppose

$$
x=(180,70)
$$

means height in centimeters and mass in kilograms.

A colleague computes a geometric length from the raw pair and compares people by that number.

Do not decide automatically that the computation is forbidden. Instead list the modeling questions that must be answered before treating that length as meaningful.

Your answer should mention scale and units.

## Part F — zero means different things

Interpret

$$
0=(0,0,0)
$$

as:

1. zero displacement;
2. an all-zero feature vector;
3. a zero-change state variable vector.

Explain what is mathematically shared and what is application-specific.

## Transfer challenge

Open a technical source from a field that uses vectors: physics, graphics, machine learning, economics, control, robotics, or another field.

Choose one vector expression and annotate only:

```text
vector symbol:
mathematical shape if stated:
coordinate meanings if stated:
likely interpretation (displacement/data/state/other):
units or scale information:
what the source leaves implicit:
```

Do not try to understand the entire paper or chapter. This is an interpretation exercise.

## Completion criterion

You can explain, with examples, why all of the following can be true at once:

```text
A vector can be drawn as an arrow.
A vector need not represent physical displacement.
A data row can be represented as a vector.
A state vector is a modeling choice.
Two equal coordinate lists can have different semantic roles in different contexts.
R^n describes mathematical structure but does not supply domain meaning.
```
