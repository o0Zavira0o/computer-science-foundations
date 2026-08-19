---
id: LNX-EXR-0002
title: Choose the Right Isolation Boundary
track: linux-systems
level: L0
status: complete
curriculum_nodes: ["LNX-N-0002"]
concepts_used: ["LNX-C-0001", "LNX-C-0002"]
references_used: ["LNX-REF-007"]
last_reviewed: 2026-08-19
---

# Choose the Right Isolation Boundary

## Task

For each experiment below, choose one starting environment:

- user-owned directory;
- container;
- disposable VM with snapshot;
- dedicated virtual disk/image inside an isolated environment.

Experiments:

1. practice `mkdir`, `cp`, redirection, and quoting;
2. install an unfamiliar command-line package and remove it afterward;
3. intentionally misconfigure a system service and recover it;
4. experiment with a bootloader entry;
5. create a new filesystem on a block-like target;
6. inspect process identity, kernel release, and distribution metadata.

For every choice, write:

- what state can change;
- what the isolation boundary protects;
- what the boundary does **not** protect;
- how you would recover.

## Evidence of success

A strong answer does not simply label tasks “safe” or “dangerous.” It explains **target, authority, blast radius, and recovery** and chooses the weakest environment that still contains plausible mistakes.

## Transfer challenge

Find one tutorial command you have previously copied or considered copying. Do not execute it. Annotate every argument and identify the state it could change. If any target is ambiguous, state what evidence you would gather before running it.
