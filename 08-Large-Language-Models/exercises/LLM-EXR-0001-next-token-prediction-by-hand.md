---
id: LLM-EXR-0001
title: Next-Token Prediction by Hand
track: large-language-models
level: L0
status: complete
curriculum_nodes: ["LLM-N-0001"]
concepts_used: ["LLM-C-0001", "LLM-C-0201", "LLM-C-0202", "LLM-C-0203", "LLM-C-0204"]
references_used: ["LLM-REF-001"]
last_reviewed: 2026-08-19
---

## Task

Use the toy vocabulary below:

```text
[" Paris", " London", " blue", "."]
```

For each context, invent a probability distribution that sums to 1.0 and defend the ordering of probabilities:

1. `The capital of France is`
2. `The sky is often`
3. `In my fictional world, the capital of France is`

Then answer:

- Which parts of your answer came from the **context**?
- Which step corresponds to the **model distribution**?
- If you choose the largest probability every time, what decoding rule are you using?
- If you sample according to the probabilities, why can two generations diverge?

Finally, write the chain-rule factorization for a three-token sequence using symbols only. You do not need to calculate any logarithms.

## Evidence of success

Your three distributions must each sum to 1.0, the context must visibly change at least one ranking, and your explanation must distinguish model probability from token selection. A correct answer is not judged by matching one invented numerical distribution; it is judged by internal consistency.

## Hints

Start with the highest-probability candidate, assign it a plausible mass, then distribute the remainder. The point is conditional reasoning, not guessing real model probabilities.
