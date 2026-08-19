---
id: LNX-EXR-0007
title: Mutate a Filesystem Tree Without Surprises
track: linux-systems
level: L0
status: complete
curriculum_nodes: ["LNX-N-0007"]
concepts_used: ["LNX-C-0005", "LNX-C-0006", "LNX-C-0007"]
references_used: ["LNX-REF-004", "LNX-REF-005"]
last_reviewed: 2026-08-19
---

# LNX-EXR-0007 — Mutate a Filesystem Tree Without Surprises

**Track:** Linux Systems

**Companion lesson:** [`LNX-0007`](../lessons/LNX-0007-create-copy-move-and-remove-files-safely.md)

## Goal

Demonstrate that you can predict filesystem mutations before executing them, including replacement, recursive scope, and destination-directory behavior.

## Part A — build the disposable tree

```bash
rm -rf "$HOME/csf-exr-0007"
mkdir -p "$HOME/csf-exr-0007/source/sub"
mkdir -p "$HOME/csf-exr-0007/archive"
printf 'one\n' > "$HOME/csf-exr-0007/source/one.txt"
printf 'two\n' > "$HOME/csf-exr-0007/source/two.txt"
printf 'existing\n' > "$HOME/csf-exr-0007/archive/one.txt"
cd "$HOME/csf-exr-0007"
```

Draw the tree before continuing.

## Part B — predict destination semantics

For each command, write the exact pathname that would be created or changed. Do **not** run them until you have an answer.

```bash
cp source/two.txt archive/
cp source/two.txt archive/two-copy.txt
mv source/one.txt source/renamed.txt
```

Then run them one at a time and verify with:

```bash
ls -R
```

Explain why the first copy chooses a basename automatically but the second copy does not.

## Part C — detect a replacement before causing it

Reset `archive/one.txt` if needed:

```bash
printf 'existing\n' > archive/one.txt
printf 'new\n' > source/new.txt
```

Now inspect:

```bash
ls -l source/new.txt archive/one.txt
```

Answer before running anything:

```text
Would `cp source/new.txt archive/one.txt` preserve the old destination contents?
```

Do not overwrite it. Instead choose a non-colliding destination pathname and perform the copy.

## Part D — copy a directory intentionally

Create:

```bash
mkdir -p source/sub/deeper
printf 'nested\n' > source/sub/deeper/nested.txt
```

Predict the resulting tree after:

```bash
cp -R source/sub archive/sub-copy
```

Then execute and verify.

Explain why recursive copying should trigger more pathname scrutiny than copying one ordinary file.

## Part E — choose `rmdir` when it expresses the real intent

Create:

```bash
mkdir empty-only
```

Remove it with the narrow operation designed for empty directories.

Then create:

```bash
mkdir nonempty
printf 'important\n' > nonempty/keep.txt
```

Try the same narrow operation.

Explain why the failure is useful evidence rather than an inconvenience to bypass immediately.

## Part F — a filename that looks like an option

Create:

```bash
touch ./-i
```

Explain why this is ambiguous/wrong as a deletion attempt:

```bash
rm -i
```

Then remove the file using either:

```bash
rm -- -i
```

or:

```bash
rm ./-i
```

State which parsing layer the fix addresses.

## Part G — mutation autopsy

For each scenario, identify the failed reasoning step.

### Scenario 1

```text
cwd = /home/ada/project/build
intent = delete /home/ada/project/tmp
command = rm -rf tmp
```

### Scenario 2

```text
archive/report.txt already exists
intent = add a second report
command = cp report.txt archive/report.txt
```

### Scenario 3

```text
intent = duplicate a directory tree
command = cp source-dir destination-dir
```

Your answer should classify the issue as pathname resolution, destination collision, recursive intent, or another precise category.

## Transfer challenge

Write a short preflight checklist for this command without running it:

```bash
mv results/final.csv archive/final.csv
```

Your checklist must determine:

- what `results/final.csv` resolves to;
- whether `archive` exists and is a directory;
- whether `archive/final.csv` already exists;
- what pathnames should exist after success.

## Completion criterion

You can narrate a mutation in this form:

```text
source resolves to:
destination currently is:
command semantics are:
recursive scope is:
replacement risk is:
after success I expect these pathnames:
verification command:
```

Clean up only after verifying the exact lab pathname:

```bash
pwd
ls -ld "$HOME/csf-exr-0007"
rm -rf "$HOME/csf-exr-0007"
```
