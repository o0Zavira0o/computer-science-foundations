# File Package Workflow

This repository is designed to be the **only persistent project folder**. Temporary scaffolds, upgrade folders, and generated delivery packages should live outside the repository and may be deleted after successful integration.

## Canonical local repository path

The intended local path is:

```text
/home/zavira/CPP_Projects/computer-science-foundations
```

## How future AI-delivered files are packaged

When an AI creates a new lesson, exercise, project, research note, curriculum update, or other repository change, the delivery should be a ZIP archive with this shape:

```text
<delivery-name>/
├── PLACEMENT.md
└── repo-root/
    └── <exact repository-relative paths>
```

`PLACEMENT.md` states the exact destination and summarizes which canonical files changed.

The user extracts the ZIP outside the repository, then copies the contents of `repo-root/` into the repository root. The internal paths determine the destination; files should never be guessed or manually renamed during placement.

Example:

```text
linux-lesson-LNX-0001/
├── PLACEMENT.md
└── repo-root/
    ├── 02-Linux-Systems/lessons/LNX-0001-example-title.md
    ├── 02-Linux-Systems/CURRICULUM.json
    ├── 02-Linux-Systems/registry/concepts.json
    ├── 02-Linux-Systems/registry/examples.json
    └── 02-Linux-Systems/registry/references.json
```

## After placing a package

From the repository root:

```bash
python scripts/csf.py sync
python scripts/csf.py audit --strict
python -m unittest discover -s tests -v
git status
git diff --check
git diff --stat
```

For ordinary educational-content updates, the unit test suite may be omitted when no tooling/schema/architecture code changed; `sync`, `audit --strict`, and Git review remain mandatory.

Then commit and push only after the diff has been reviewed.

## Learner-state rule

A content package must not mark a lesson as read, practiced, or demonstrated merely because the lesson file was added. `LEARNER_STATE.json` changes only after real learner activity.

## Architecture freeze rule

After V3.1, ordinary content packages should not modify `scripts/`, `schemas/`, `SYSTEM.json`, or the architecture documents unless a concrete problem requires an architecture change. Learning content takes priority over speculative infrastructure work.
