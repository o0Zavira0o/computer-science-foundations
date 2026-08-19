---
id: LNX-EXR-0006
title: Navigate, Inspect, and Verify
track: linux-systems
level: L0
status: complete
curriculum_nodes: ["LNX-N-0006"]
concepts_used: ["LNX-C-0005", "LNX-C-0006"]
references_used: ["LNX-REF-004", "LNX-REF-005"]
last_reviewed: 2026-08-19
---

# LNX-EXR-0006 — Navigate, Inspect, and Verify

**Track:** Linux Systems

**Companion lesson:** [`LNX-0006`](../lessons/LNX-0006-navigate-and-inspect-directories.md)

## Goal

Turn `pwd`, `cd`, and `ls` into a prediction-and-verification workflow rather than a sequence of guesses.

## Part A — create a safe map

Build this disposable tree:

```bash
mkdir -p "$HOME/csf-nav-0006/one/two"
mkdir -p "$HOME/csf-nav-0006/one/three"
mkdir -p "$HOME/csf-nav-0006/four"
touch "$HOME/csf-nav-0006/one/note.txt"
touch "$HOME/csf-nav-0006/one/.hidden-note"
```

Draw the tree on paper or in a text block before continuing.

## Part B — predict every destination

Start here:

```bash
cd "$HOME/csf-nav-0006/one/two"
```

For each step below, write the predicted `pwd` output **before** running the command:

```bash
pwd
cd ..
pwd
cd three
pwd
cd ../../four
pwd
cd -
pwd
```

For each `cd`, label the pathname argument as absolute or relative.

## Part C — separate cwd from inspection target

Return to:

```bash
cd "$HOME/csf-nav-0006/one"
```

Predict whether the current working directory will change after each command:

```bash
ls
ls ../four
ls .
ls -d ../four
pwd
```

Explain why `ls ../four` can inspect another directory while `pwd` still reports `.../one`.

## Part D — ordinary versus hidden entries

Before running these, write the names you expect each command to display:

```bash
ls
ls -A
ls -a
```

Then answer:

1. Which command revealed `.hidden-note`?
2. Which command showed `.` and `..` too?
3. Why is a dot-prefixed filename not a security boundary?

## Part E — directory entry versus directory contents

Run:

```bash
cd "$HOME/csf-nav-0006"
ls one
ls -d one
ls -ld one
```

Explain what object each command is asking `ls` to describe.

Do not interpret every long-listing column yet. Just identify whether the target is the directory entry `one` or the entries inside it.

## Part F — failure must not rewrite your mental state

Start at:

```bash
cd "$HOME/csf-nav-0006/one"
```

Predict the final cwd:

```bash
cd does-not-exist
pwd
```

Then explain why a failed `cd` is different from a successful `cd` followed by a failed `ls`.

## Transfer challenge

You see this transcript:

```text
$ pwd
/home/ada/project/src
$ ls config
ls: cannot access 'config': No such file or directory
```

The project documentation says there is a directory at `/home/ada/project/config`.

Without using `find`, write the shortest sequence of reasoning and commands that would verify whether the problem is simply the current working directory.

<details>
<summary>One defensible approach</summary>

Reason first:

- `config` is relative.
- From `/home/ada/project/src`, it points toward `/home/ada/project/src/config`.
- The documented directory is one level above `src`.

Then inspect without unnecessary movement:

```bash
ls -d ../config
```

or move deliberately:

```bash
cd ..
pwd
ls -d config
```

The important part is that the commands follow from pathname reasoning rather than search-by-guessing.

</details>

## Completion criterion

You can navigate an unfamiliar small tree while narrating:

> “This command changes cwd / does not change cwd; this pathname resolves from here; this listing describes the directory itself / its contents; these hidden entries are omitted / included.”

Clean up when finished:

```bash
rm -rf "$HOME/csf-nav-0006"
```

Only run the cleanup after verifying the pathname is exactly the disposable lab directory you created.
