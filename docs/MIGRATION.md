# Migration Notes

This scaffold is designed to replace the current educational-content layout while preserving Git history in the local repository.

## Intended migration

- Remove the old Linux lesson files from `02-Linux-Systems/`.
- Replace the old root README with the new curriculum README.
- Add the structural documents, templates, audit script, and seven subject scaffolds.
- Do **not** delete `.git/`.

## Why the old Linux files are not included

The previous Linux sequence is treated as legacy content. The new track should be planned from zero according to `docs/LEARNING_SYSTEM.md`.

If a future review finds high-quality pieces worth salvaging, they should be imported deliberately, assigned concept/example IDs, checked for accuracy, and rewritten into the new curriculum rather than copied wholesale.
