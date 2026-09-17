#!/usr/bin/env bash
# doctrine-diff.sh
# <!-- file-class: DOCTRINE -->
#
# Run this INSIDE YOUR OWN COPY of this repository to see what an upstream
# release changed, limited to the doctrine-class paths. It never applies
# anything. It runs git only against the repository it lives in: the one
# whose scripts/ directory holds this file, found at runtime the same way
# check-invariants.sh does, so this script carries no path belonging to any
# one person's machine and works unmodified in any clone.
#
# Usage:
#   scripts/doctrine-diff.sh [remote] [ref]
#
#   remote  defaults to "upstream"
#   ref     defaults to "upstream/main" if remote is left at its default,
#           or "<remote>/main" if you pass a remote name and no ref
#
# What it does, in order:
#   1. Fetches the named remote.
#   2. Prints `git diff --stat` between HEAD and the named ref, restricted
#      to the doctrine paths below, so you see the shape of the change
#      before the detail.
#   3. Prints the full `git diff`, same restriction, same two points.
#
# What it never does: it never merges, rebases, cherry-picks, or writes a
# single file. Reviewing this output and deciding what to apply, and in
# which of your own commits, is your act, not this script's - see
# EXTENDING.md section 6, "The upstream pull, honestly."

set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." >/dev/null 2>&1 && pwd)"

REMOTE="${1:-upstream}"
REF="${2:-${REMOTE}/main}"

# The doctrine-class path list, copied verbatim from EXTENDING.md section 5
# ("The three file classes" / "Where the classes land in the shipped
# tree"). If that table ever changes, update this array to match it - this
# script does not read EXTENDING.md itself, so the two can drift apart if
# only one of them is edited.
DOCTRINE_PATHS=(
  "doctrine/"
  "ops/"
  "org/STAFF_MEETING.md"
  "org/SEAT-TEMPLATE.md"
  "EXTENDING.md"
  "org/functions/*/CHARTER.md"
  "README.md"
  "docs/"
  "examples/"
  "scripts/"
  ".claude/skills/"
  "ATTRIBUTIONS.md"
  "SISTER-REPOS.md"
  "CONTRIBUTING.md"
  "CODE_OF_CONDUCT.md"
  "counsel/README.md"
)

cd "${REPO_ROOT}" || exit 1

if ! git remote get-url "${REMOTE}" >/dev/null 2>&1; then
  echo "No remote named '${REMOTE}' in this repository." >&2
  echo "Add the upstream repository as a remote once, then re-run this script." >&2
  exit 1
fi

echo "Fetching ${REMOTE}..."
if ! git fetch "${REMOTE}"; then
  echo "Fetch of '${REMOTE}' failed; nothing else to show." >&2
  exit 1
fi

echo
echo "=== doctrine-path diff: HEAD..${REF} ==="
echo "remote:        ${REMOTE}"
echo "ref:           ${REF}"
echo "paths checked: ${#DOCTRINE_PATHS[@]} entries from EXTENDING.md section 5"
echo

echo "--- stat -------------------------------------------------------------"
git diff --stat "HEAD..${REF}" -- "${DOCTRINE_PATHS[@]}"

echo
echo "--- full diff ----------------------------------------------------------"
git diff "HEAD..${REF}" -- "${DOCTRINE_PATHS[@]}"

echo
echo "This script applied nothing. Reviewing this diff and applying any of"
echo "it, in your own commit, is your own act - see EXTENDING.md section 6."
