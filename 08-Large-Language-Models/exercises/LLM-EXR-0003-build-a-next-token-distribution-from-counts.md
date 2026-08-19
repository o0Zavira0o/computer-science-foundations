---
id: LLM-EXR-0003
title: Build a Next-Token Distribution from Counts
track: large-language-models
level: L0
status: complete
curriculum_nodes: ["LLM-N-0003"]
concepts_used: ["LLM-C-0001", "LLM-C-0002", "LLM-C-0003"]
references_used: ["LLM-REF-001", "LLM-REF-019"]
last_reviewed: 2026-08-19
---

# LLM-EXR-0003 — Build a Next-Token Distribution from Counts

**Track:** Large Language Models (LLMs)

**Companion lesson:** [`LLM-0003`](../lessons/LLM-0003-probability-from-counts-uncertainty-without-mystery.md)

## Goal

Turn token counts into normalized conditional next-token distributions and distinguish empirical evidence from claims of certainty.

## Part A — normalize one count table

Observed next-token counts after one context are:

```text
cat:   15
dog:    9
bird:   4
fish:   2
```

Without a calculator first:

1. compute the total count;
2. estimate which probability should be largest;
3. compute every empirical probability;
4. verify that they sum to one.

Write the result as both fractions and decimals.

## Part B — the denominator depends on the condition

You observe:

```text
context = "the"
cat: 12
dog: 3
bird: 5

context = "a"
cat: 4
dog: 10
bird: 6
```

Compute:

$$
\hat{P}(\text{cat}\mid\text{the}),
\qquad
\hat{P}(\text{cat}\mid\text{a}),
$$

and:

$$
\hat{P}(\text{dog}\mid\text{the}),
\qquad
\hat{P}(\text{dog}\mid\text{a}).
$$

Explain why using the grand total across both contexts would answer a different question.

## Part C — separate zero count from impossibility

A tiny training sample contains no instance of:

```text
context: "the sleepy"
next token: "otter"
```

The naive empirical count estimate is zero.

Write two sentences:

1. one statement that the data **does** justify;
2. one stronger statement that the data **does not** justify.

The stronger unsupported statement should involve impossibility or certainty.

## Part D — same argmax, different uncertainty

Compare:

```text
Distribution A
red:   0.92
blue:  0.05
green: 0.03

Distribution B
red:   0.38
blue:  0.34
green: 0.28
```

Answer:

1. What token does argmax choose for each?
2. Which distribution is more concentrated?
3. What information is lost if you store only the argmax token?

## Part E — build a one-token-context language model by hand

Corpus:

```text
red fox runs
red fox sleeps
red bird flies
blue fox runs
blue bird flies
blue bird sings
```

For the context `red`, build the next-token count table and probability table.

Then repeat for `blue`.

Finally compare:

$$
\hat{P}(\text{fox}\mid\text{red})
$$

with:

$$
\hat{P}(\text{fox}\mid\text{blue}).
$$

## Part F — implement the estimator

Write a short Python program using only the standard library.

Input:

```python
pairs = [
    ("the", "cat"),
    ("the", "dog"),
    ("the", "cat"),
    ("a", "dog"),
    ("the", "cat"),
    ("a", "cat"),
]
```

Your program should construct a mapping shaped conceptually like:

```text
context -> next-token counts -> normalized probabilities
```

Required checks:

```text
for every observed context:
    sum(probabilities) == 1  approximately
```

Do not use a machine-learning library.

## Part G — unseen context failure

Ask your count model for a distribution after:

```text
context = "never-seen-before"
```

What happens?

Do not patch the issue immediately. First explain why exact-context counting lacks evidence for this query and why a learned model needs some mechanism for generalization.

## Part H — sequence-probability reading practice

Read this expression in plain English:

$$
P(x_1,x_2,x_3)
=
P(x_1)P(x_2\mid x_1)P(x_3\mid x_1,x_2).
$$

You do not need a formal proof. Explain why it matches the operational story of generating one token, then conditioning on what has already been generated.

## Transfer challenge

A colleague says:

> “The model gives token `Paris` probability 0.82, so it is 82% certain that the entire answer is factually correct.”

Write a technical correction in at most five sentences.

Your response must distinguish:

- next-token predictive probability;
- the current context;
- whole-answer factual correctness;
- calibration as a separate question.

## Completion criterion

You can look at a count table and narrate:

```text
condition/context:
relevant denominator:
outcome counts:
normalized probabilities:
check that mass sums to one:
what zero counts mean:
what this empirical estimator cannot generalize to:
```

If you cannot explain why the denominator changes under conditioning, repeat Parts B and E before moving to logits and softmax.
