---
id: LNX-EXR-0004
title: Find the Right Documentation Layer
track: linux-systems
level: L0
status: complete
curriculum_nodes: ["LNX-N-0004"]
concepts_used: ["LNX-C-0001", "LNX-C-0003", "LNX-C-0004"]
references_used: ["LNX-REF-003", "LNX-REF-004", "LNX-REF-005"]
last_reviewed: 2026-08-19
---

# LNX-EXR-0004 — Find the Right Documentation Layer

**Track:** Linux Systems
**Companion lesson:** [`LNX-0004`](../lessons/LNX-0004-learn-to-ask-linux-for-help.md)

## Goal

Practice routing a Linux question to the documentation layer that owns it instead of reaching for undirected web search.

## Part A — classify before searching

For each item, first label it with the most likely category:

- shell builtin / shell feature;
- external user utility;
- system call;
- library function;
- file format;
- overview / convention;
- system-administration utility.

Items:

```text
cd
ls
open(2)
printf(3)
passwd(5)
signal(7)
```

Do this from memory before opening documentation.

## Part B — verify the implementation on your machine

Run:

```bash
type -a cd
type -a printf
type -a ls
command -V cd
command -V ls
```

Record what surprised you.

If your output differs from an example in the lesson, treat that as a finding, not an error.

## Part C — visit four different documentation namespaces

Try:

```bash
help cd
man 1 printf
man 2 open
man 5 passwd
man 7 signal
```

For each successful page, write one sentence answering:

> What kind of contract or behavior is this page trying to document?

If a page is unavailable, record the exact failure and investigate whether the relevant documentation package is installed.

## Part D — discover something whose name you do not know

Use a keyword query such as:

```bash
apropos filesystem
```

or:

```bash
man -k filesystem
```

Choose one result you did not already know. Explain why its manual section makes sense.

## Part E — resolve an ambiguity

Investigate `printf` using at least three of:

```bash
type -a printf
help printf
man 1 printf
man 3 printf
```

Write a short explanation of why the same spelling can legitimately lead to different documentation.

## Transfer challenge

A tutorial says:

> “See `credentials(7)` for the process credential model.”

Without opening the page, explain what the `(7)` tells you and why searching only for a command named `credentials` would be the wrong mental model.

<details>
<summary>Check your reasoning</summary>

The suffix identifies manual section 7, which is used for overviews, conventions, protocols, and miscellaneous conceptual material. The reference is naming a manual page in a documentation namespace, not asserting that `credentials` is an executable command.

</details>

## Completion criterion

You should be able to meet an unfamiliar Linux term and articulate a routing decision such as:

> “First I will identify what this name resolves to; because it is a Bash builtin I will start with shell help rather than treating it as an external executable.”

That reasoning is more valuable than memorizing any single help command.
