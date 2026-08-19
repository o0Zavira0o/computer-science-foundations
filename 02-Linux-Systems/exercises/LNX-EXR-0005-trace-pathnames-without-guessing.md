---
id: LNX-EXR-0005
title: Trace Pathnames Without Guessing
track: linux-systems
level: L0
status: complete
curriculum_nodes: ["LNX-N-0005"]
concepts_used: ["LNX-C-0003", "LNX-C-0005"]
references_used: ["LNX-REF-001", "LNX-REF-004", "LNX-REF-005"]
last_reviewed: 2026-08-19
---

# LNX-EXR-0005 — Trace Pathnames Without Guessing

**Track:** Linux Systems
**Companion lesson:** [`LNX-0005`](../lessons/LNX-0005-paths-names-and-the-single-filesystem-tree.md)

## Goal

Turn pathname reading into an explicit reasoning process: choose the starting point, walk components, and predict the target before running commands.

## Part A — classify the starting point

For each pathname, label it **absolute** or **relative**:

```text
/etc/hosts
notes/today.txt
./build/output.log
../archive
/home/ada
.config
```

Then write the rule you used in one sentence.

<details>
<summary>Check</summary>

Only a leading `/` makes a pathname absolute in this set. A leading dot does not make a path absolute.

</details>

## Part B — resolve on paper

Assume:

```text
cwd = /home/ada/projects/csf/notes
```

Resolve these component by component:

```text
../README.md
../../archive/report.txt
./draft.md
../../../etc/hosts
/etc/hosts
```

Do **not** run commands until you have written your predicted target.

For every `..`, write the directory reached after that component.

## Part C — build a safe lab

Create a disposable tree under your home directory:

```bash
mkdir -p "$HOME/csf-path-lab/red/blue"
mkdir -p "$HOME/csf-path-lab/red/green"
cd "$HOME/csf-path-lab/red/blue"
```

Before running each `pwd`, predict its output:

```bash
pwd
cd ..
pwd
cd ./green
pwd
cd ../blue
pwd
```

If a prediction is wrong, identify whether your error concerned:

- the starting directory;
- the meaning of `.`;
- the meaning of `..`;
- the directory tree you actually created.

## Part D — dot does three different jobs

Explain the difference among:

```text
.
..
.hidden
```

Then run:

```bash
cd "$HOME/csf-path-lab/red"
mkdir .hidden
ls
ls -a
```

Record what changed between the two listings.

## Part E — separate shell syntax from pathname syntax

Explain why these are not the same kind of thing:

```text
/
/root
~
$HOME
```

Then inspect what your current shell does:

```bash
printf '%s\n' ~
printf '%s\n' "$HOME"
```

Do not assume all programs independently understand `~`.

## Transfer challenge

A program reports:

```text
cannot open ../config/app.conf
```

List at least four questions you would ask before concluding that the file “does not exist.”

<details>
<summary>Possible reasoning</summary>

Useful questions include:

- What is the process's current working directory?
- Where does `..` take us from there?
- Does each intermediate component exist and name a directory?
- Is traversal permitted through those directories?
- Did a shell or program transform the pathname first?
- Are symbolic links involved?

The lesson has not yet taught all of these mechanisms in depth; the point is to stop treating the final filename as the whole path-resolution problem.

</details>

## Completion criterion

You can look at an unfamiliar pathname and narrate:

> “Resolution starts here, then walks these components in this order, with `.` and `..` handled explicitly.”

If you are still resolving pathnames by visual intuition, repeat Part B with your own directory tree.
