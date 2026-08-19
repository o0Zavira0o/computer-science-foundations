#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 /path/to/computer-science-foundations"
  exit 2
fi

TARGET="$(cd "$1" && pwd)"
SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ "$SOURCE" == "$TARGET" || "$SOURCE" == "$TARGET/"* ]]; then
  echo "ERROR: extract this scaffold OUTSIDE the target repository before installing."
  echo "The installer refuses to delete a directory that contains its own source files."
  exit 1
fi

if [[ ! -d "$TARGET/.git" ]]; then
  echo "ERROR: target does not look like a Git repository: $TARGET"
  exit 1
fi

echo "Target: $TARGET"
echo "Scaffold: $SOURCE"
echo

if [[ -n "$(git -C "$TARGET" status --porcelain)" ]]; then
  echo "ERROR: target repository has uncommitted changes."
  echo "Commit or stash them before installing the scaffold."
  exit 1
fi

BACKUP="backup/pre-curriculum-reset-$(date +%Y%m%d-%H%M%S)"
git -C "$TARGET" branch "$BACKUP"
echo "Created recovery branch: $BACKUP"

echo "Removing old tracked/untracked working-tree content except .git ..."
find "$TARGET" -mindepth 1 -maxdepth 1 ! -name ".git" -exec rm -rf {} +

echo "Copying new scaffold ..."
cp -a "$SOURCE"/. "$TARGET"/

# Never copy package-side git metadata even if added later.
rm -rf "$TARGET/.git.tmp" 2>/dev/null || true

echo
echo "Running structural audit ..."
python "$TARGET/scripts/repo_audit.py"

echo
echo "Done. Review with:"
echo "  cd \"$TARGET\""
echo "  git status"
echo
echo "Then commit when satisfied:"
echo "  git add -A"
echo "  git commit -m \"Rebuild repository as extensible learning system\""
