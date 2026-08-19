# Install This Scaffold Into Your Existing Local Repository

The installer preserves `.git/`, creates a backup branch, removes the old working-tree files, and copies this scaffold into place.

## 1. Make sure your existing repository is clean

```bash
cd /path/to/computer-science-foundations
git status
```

If you have uncommitted work, commit or stash it first.

## 2. From the extracted scaffold folder, run

```bash
bash scripts/install_scaffold.sh /path/to/computer-science-foundations
```

The script will:

1. refuse to continue if the target has uncommitted changes;
2. create a recovery branch named `backup/pre-curriculum-reset-...`;
3. preserve the target `.git/`;
4. remove the old working-tree content;
5. copy in the new scaffold;
6. run the structural audit.

## 3. Inspect the result

```bash
cd /path/to/computer-science-foundations
git status
python scripts/repo_audit.py
```

## 4. Commit

```bash
git add -A
git commit -m "Rebuild repository as extensible learning system"
git push origin main
```

Do not push until you have reviewed `git status` and are satisfied with the deletions/additions.
