---
id: LNX-EXR-0003
title: Autopsy a Command Invocation
track: linux-systems
level: L0
status: complete
curriculum_nodes: ["LNX-N-0003"]
concepts_used: ["LNX-C-0001", "LNX-C-0002", "LNX-C-0003"]
references_used: ["LNX-REF-004", "LNX-REF-005"]
last_reviewed: 2026-08-19
---

# Autopsy a Command Invocation

## Task

Inside a user-owned lab directory, inspect these command lines without modifying anything outside the lab:

```bash
printf '%s\n' alpha beta
uname -r
id -u
mkdir -p demo/subdir
ls -ld demo
true
false
```

For every line, write down:

1. the command name;
2. the ordered arguments after the command name;
3. which arguments appear to be options;
4. which appear to be operands or data;
5. whether you expect normal output, diagnostics, neither, or both;
6. whether you expect a zero or nonzero exit status;
7. what state, if any, the command can change.

Then choose **one unfamiliar but non-destructive command** from your system documentation. Before running it, predict the same seven properties. Run it only after the prediction, then compare the observed behavior with your model.

## Evidence of success

A strong submission distinguishes the shell-visible command line from the receiving command's argument interface. It should also separate:

- visible terminal text from `stdout`/`stderr` as conceptual streams;
- output from exit status;
- option-like syntax from the broader category of arguments;
- command invocation from the state changes the command may cause.

At least one prediction should be corrected after consulting documentation. The point is not perfect guessing; it is learning to refine a model from evidence.

## Transfer challenge

Find a command line from an online tutorial that contains at least four words. Do **not** execute it.

Annotate every word and symbol you currently understand. Mark the rest as one of:

- shell syntax not yet understood;
- command option not yet understood;
- operand/data not yet understood;
- completely uncertain.

This turns “copy this command” into a concrete list of questions for future lessons.
