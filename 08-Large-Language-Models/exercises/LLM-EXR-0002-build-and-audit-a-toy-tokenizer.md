---
id: LLM-EXR-0002
title: Build and Audit a Toy Tokenizer
track: large-language-models
level: L0
status: complete
curriculum_nodes: ["LLM-N-0002"]
concepts_used: ["LLM-C-0001", "LLM-C-0002", "LLM-C-0202"]
references_used: ["LLM-REF-001", "LLM-REF-011"]
last_reviewed: 2026-08-19
---

# LLM-EXR-0002 — Build and Audit a Toy Tokenizer

**Track:** Large Language Models (LLMs)

**Companion lesson:** [`LLM-0002`](../lessons/LLM-0002-text-symbols-tokens-and-vocabularies.md)

## Goal

Make tokenization concrete enough that you can inspect and criticize a representation instead of saying “the tokenizer splits text somehow.”

## Part A — three representations of the same text

Use:

```text
unhappiness
```

Construct three hypothetical tokenizations:

1. whole-word;
2. character-level;
3. subword-style.

For each, record:

```text
token pieces:
sequence length:
what happens if the exact word was never seen while building the vocabulary:
```

Do not claim one representation is universally best. State one advantage and one cost of each.

## Part B — create a tiny vocabulary

Use this toy vocabulary:

```text
0  <BOS>
1  <EOS>
2  " the"
3  " cat"
4  " dog"
5  " sat"
6  " on"
7  " mat"
8  "."
9  " m"
10 "at"
```

Encode:

```text
 the cat sat on the mat.
```

in two ways:

- using token 7 for `" mat"`;
- using tokens 9 and 10 for the same surface substring.

Then compare sequence lengths.

## Part C — prove that IDs are not ordered meanings

Consider:

```text
3 → " cat"
4 → " dog"
```

Answer:

1. Does `4 > 3` imply that dog is semantically “greater than” cat?
2. If the two IDs are swapped in the tokenizer but model parameters are not swapped, should model behavior remain unchanged?
3. What additional structures would need to be permuted consistently for a pure ID relabeling to preserve behavior?

<details>
<summary>Check</summary>

The integer values are categorical indices. Their numeric ordering carries no semantic claim.

A tokenizer-only swap would make the model look up the wrong learned rows/outputs. A consistent vocabulary permutation would also need corresponding model parameters indexed by vocabulary ID to be permuted.

</details>

## Part D — expose the whole-word failure

Pretend your vocabulary contains only:

```text
cat
dog
happy
run
```

Try to represent:

```text
unhappiness
microarchitecture
Zavira
```

If you introduce a single `<UNK>` token, what information is lost?

Now propose a subword vocabulary that can represent all three strings without storing every complete word.

The goal is not to invent an optimal tokenizer; it is to see why reusable smaller pieces help with open-ended text.

## Part E — whitespace changes the input

Compare:

```text
hello
 hello
hello!
hello world
```

Design two different reasonable tokenizer policies:

- one where whitespace is represented separately;
- one where leading whitespace can be bundled into token pieces.

Show how the token sequences differ.

## Part F — round-trip audit

Define your own toy `encode` and `decode` rules on paper.

Test at least:

```text
cat
 cat
cat.
cat dog
```

For every case ask:

```text
decode(encode(text)) == text ?
```

If not, identify exactly which information your tokenizer discarded or normalized.

## Part G — tokenizer comparison without software

Two tokenizers encode the same passage as:

```text
Tokenizer A: 120 tokens
Tokenizer B: 185 tokens
```

Answer carefully:

1. Which one uses less token context for this passage?
2. Does this prove A is universally better?
3. Name at least four other factors you would inspect before judging the tokenizer.

Possible factors include language coverage, reversibility/normalization, vocabulary size, code/numeric behavior, training-data representativeness, special-token design, and downstream model performance.

## Transfer challenge

A developer says:

> “Our model supports 8,000 tokens, so users can always paste about 8,000 English words.”

Write a short technical correction suitable for a code review.

Your correction must distinguish **word count** from **token count** and explain why the ratio depends on the tokenizer and input text.

## Completion criterion

You can take an arbitrary visible string and ask, in order:

```text
What exact text representation enters the tokenizer?
What pieces does this tokenizer produce?
Which vocabulary IDs represent those pieces?
Can the IDs be decoded back reliably?
How long is the resulting token sequence?
What assumptions are tokenizer-specific rather than universal?
```

If “token = word” still feels natural, repeat Parts D and E with examples from a second language, source code, or numeric strings.
