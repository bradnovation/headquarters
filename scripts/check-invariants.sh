#!/usr/bin/env bash
# check-invariants.sh
# <!-- file-class: DOCTRINE -->
#
# A generic, warn-only guard for two of this product's standing gates:
#   G2 - a git invocation whose target is a repository this one does not own.
#   G5 - any tool call whose input references the vault/ directory, the one
#        place this product keeps sensitive material out of version control.
#
# Adapted pattern: the invariant-checker idea follows AI Team OS. See
# ATTRIBUTIONS.md.
#
# scripts/README.md carries the longer explanation: why warn-only is the
# right starting posture, what a future deny-mode switch would involve,
# and the specific cases this checker cannot see. What follows here is
# enough on its own to read and run the script without opening that file.
#
# Run it one of two ways, chosen by whether --self-test is on the command
# line:
#   - plain invocation: a single tool-call description in JSON form is
#     waiting on stdin; check it, log anything that trips, always exit 0.
#   - `--self-test`: ignore stdin entirely and instead walk through the
#     fixed set of cases defined near the bottom of this file, printing one
#     ok/FAIL line per case and a nonzero exit if any of them came back
#     wrong.
#
# WARN-ONLY IS THE WHOLE DESIGN, NOT A PLACEHOLDER FOR SOMETHING STRICTER.
# A guard that can crash the pipeline it is wired into is worse than no
# guard at all, so every unexpected shape of input (malformed JSON, a
# payload missing the fields this script expects, no python3 on the box)
# degrades to complete silence and a clean exit rather than a nonzero exit
# or a stack trace. Do not add `set -e` or `set -u` here without re-proving
# that guarantee still holds end to end.
#
# GENERIC BY CONSTRUCTION: this script contains no absolute path belonging
# to any one person's machine. It locates its own repository root at
# runtime from its own location on disk (one directory above wherever this
# file lives) and checks everything relative to that, so the same file
# works unmodified in any clone, on any machine, at any path.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." >/dev/null 2>&1 && pwd)"
LOG_FILE="${SCRIPT_DIR}/invariant-guard.log"

# --- embedded python3 checker -------------------------------------------
# Reads exactly one JSON payload from stdin: the shape a pre-execution
# tool-call hook typically hands a guard script, a dict carrying at least
# a tool name and a tool-input dict. On stdout, a tripped rule prints exactly one
# line: "<GATE>|<reason>|<fragment>". Anything that does not trip a rule -
# including a payload that fails to parse at all - prints nothing. That
# silence, not an error code, is how the fail-open contract above is kept.
read -r -d '' PY_CHECKER <<'PYEOF' || true
import json
import re
import sys


def collect_strings(value, bucket, depth=0):
    # Walk any JSON-shaped value and gather every string leaf it contains.
    # Depth-limited so a pathological payload cannot spin this forever.
    if depth > 8:
        return
    if isinstance(value, str):
        bucket.append(value)
    elif isinstance(value, dict):
        for v in value.values():
            collect_strings(v, bucket, depth + 1)
    elif isinstance(value, list):
        for v in value:
            collect_strings(v, bucket, depth + 1)


def strip_quotes(token):
    if len(token) >= 2 and token[0] == token[-1] and token[0] in ("'", '"'):
        return token[1:-1]
    return token


def foreign_git_targets(command, repo_root):
    """Return target paths a git-bearing command points outside repo_root.

    Only looks at the flags and idioms that actually name a target
    repository: -C, --git-dir=, --work-tree=, and a preceding `cd`. A git
    command with no such marker is left alone; that is a known, documented
    scope limit rather than an oversight (see scripts/README.md).
    """
    if not re.search(r'\bgit\b', command):
        return []

    candidates = []
    token = r'''(?:"([^"]*)"|'([^']*)'|(\S+))'''
    for pat in (r'-C\s+' + token, r'--git-dir=' + token, r'--work-tree=' + token,
                r'\bcd\b\s+' + token):
        for m in re.finditer(pat, command):
            raw = next((g for g in m.groups() if g), "")
            path = strip_quotes(raw)
            if path:
                candidates.append(path)

    normalized_root = repo_root.rstrip("/")
    foreign = []
    for path in candidates:
        if not path.startswith("/"):
            continue  # relative path: cannot be resolved without a cwd, see README
        p = path.rstrip("/")
        if p == normalized_root or p.startswith(normalized_root + "/"):
            continue
        foreign.append(path)
    return foreign


def touches_vault(strings):
    for s in strings:
        if "vault/" in s:
            return s
    return None


def main():
    repo_root = sys.argv[1] if len(sys.argv) > 1 else "."

    try:
        payload = json.loads(sys.stdin.read())
    except Exception:
        # Whatever arrived was not valid JSON. Say nothing and stop here;
        # an unreadable payload is exactly the case this checker must
        # never turn into a crash.
        return

    if not isinstance(payload, dict):
        return

    tool_name = payload.get("tool_name", "")
    if not isinstance(tool_name, str):
        tool_name = ""

    tool_input = payload.get("tool_input", {})
    if not isinstance(tool_input, dict):
        tool_input = {}

    command = tool_input.get("command", "")
    if not isinstance(command, str):
        command = ""

    # G2 first: a Bash call carrying a git invocation aimed outside repo_root.
    if tool_name == "Bash" and command:
        foreign = foreign_git_targets(command, repo_root)
        if foreign:
            fragment = foreign[0]
            if len(fragment) > 120:
                fragment = fragment[:117] + "..."
            sys.stdout.write(
                "G2|git command targets a repository outside this one|" + fragment + "\n"
            )
            return

    # G5 next: scan every string value anywhere in tool_input, not only the
    # fields a Bash or file-editing tool happens to use, so a guard case
    # holds for whatever tool shape a future integration adds.
    strings = []
    collect_strings(tool_input, strings)
    hit = touches_vault(strings)
    if hit is not None:
        fragment = hit.strip()
        if len(fragment) > 120:
            fragment = fragment[:117] + "..."
        sys.stdout.write(
            "G5|tool input references vault/, kept out of version control and unattended runs|" + fragment + "\n"
        )
        return


main()
PYEOF

# Hands a JSON string ($1) to the embedded interpreter above and passes
# back whatever it printed, which is nothing on every path where nothing
# tripped. Standard error from python is thrown away here on purpose: a
# bug inside the embedded checker must show up as silence, never as this
# wrapper failing loudly, or the fail-open promise stops being a promise.
run_checker() {
  if ! command -v python3 >/dev/null 2>&1; then
    return 0
  fi
  printf '%s' "$1" | python3 -c "$PY_CHECKER" "$REPO_ROOT" 2>/dev/null
  return 0
}

# Takes one "<GATE>|<reason>|<fragment>" result and turns it into both a
# human-readable line on stderr and a permanent, timestamped row appended
# to $LOG_FILE.
log_finding() {
  local finding="$1" gate reason fragment ts
  IFS='|' read -r gate reason fragment <<< "$finding"
  if [ -z "$gate" ]; then
    return 1
  fi
  ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null)"
  {
    echo "GUARD-FLAG [${gate}]: ${reason}"
    echo "  fragment: ${fragment}"
  } >&2
  printf '%s GUARD-FLAG [%s]: %s :: %s\n' "$ts" "$gate" "$reason" "$fragment" >> "$LOG_FILE" 2>/dev/null
  return 0
}

# --- HOOK MODE -----------------------------------------------------------
run_hook() {
  local payload finding
  payload="$(cat 2>/dev/null)"
  finding="$(run_checker "$payload")"
  if [ -n "$finding" ]; then
    log_finding "$finding"
  fi
  # Warn-only: this exit is always 0. Flipping that is an operator's own
  # deliberate later choice - see "Flipping warn to deny" in the README.
  exit 0
}

# --- CHECK MODE (--self-test) --------------------------------------------
run_self_test() {
  local tmp_log real_log passed total outside_dir
  tmp_log="$(mktemp -t check-invariants-selftest.XXXXXX)"
  real_log="$LOG_FILE"
  LOG_FILE="$tmp_log"
  total=0
  passed=0
  # A sibling directory of the repo root, guaranteed outside it, computed
  # at runtime so no absolute path from any real machine is baked into
  # this script. It does not need to exist on disk for the string check.
  outside_dir="$(dirname "$REPO_ROOT")/a-different-project"

  expect_gate() {
    local name="$1" json="$2" want="$3"
    local got
    total=$((total + 1))
    got="$(run_checker "$json")"
    got="${got%%|*}"
    if [ "$got" = "$want" ]; then
      passed=$((passed + 1))
      echo "ok   - ${name}"
    else
      echo "FAIL - ${name} (wanted '${want:-silence}', got '${got:-silence}')"
    fi
  }

  echo "check-invariants.sh --self-test"
  echo "repo root under test: ${REPO_ROOT}"
  echo "--------------------------------------------------"

  expect_gate "G2: git -C pointed at a foreign repo" \
    "{\"tool_name\":\"Bash\",\"tool_input\":{\"command\":\"git -C ${outside_dir} status\"}}" \
    "G2"

  expect_gate "G2: cd into a foreign repo then git push" \
    "{\"tool_name\":\"Bash\",\"tool_input\":{\"command\":\"cd ${outside_dir} && git push origin main\"}}" \
    "G2"

  expect_gate "G2: --git-dir pointed at a foreign repo" \
    "{\"tool_name\":\"Bash\",\"tool_input\":{\"command\":\"git --git-dir=${outside_dir}/.git log\"}}" \
    "G2"

  expect_gate "G2: git -C inside this repo must stay silent" \
    "{\"tool_name\":\"Bash\",\"tool_input\":{\"command\":\"git -C ${REPO_ROOT} status\"}}" \
    ""

  expect_gate "G2: git -C a subdirectory of this repo must stay silent" \
    "{\"tool_name\":\"Bash\",\"tool_input\":{\"command\":\"git -C ${REPO_ROOT}/scripts log\"}}" \
    ""

  expect_gate "G2: a non-git command mentioning a foreign path must stay silent" \
    "{\"tool_name\":\"Bash\",\"tool_input\":{\"command\":\"ls ${outside_dir}\"}}" \
    ""

  expect_gate "G5: Read of an absolute vault/ path" \
    "{\"tool_name\":\"Read\",\"tool_input\":{\"file_path\":\"${REPO_ROOT}/vault/transcript.md\"}}" \
    "G5"

  expect_gate "G5: Write to a relative vault/ path" \
    '{"tool_name":"Write","tool_input":{"file_path":"vault/notes.md","content":"x"}}' \
    "G5"

  expect_gate "G5: a nested tool_input field mentioning vault/ still trips" \
    '{"tool_name":"SomeFutureTool","tool_input":{"options":{"path":"vault/x.md"}}}' \
    "G5"

  expect_gate "G5: an ordinary file outside vault/ stays silent" \
    "{\"tool_name\":\"Read\",\"tool_input\":{\"file_path\":\"${REPO_ROOT}/HANDOFF.md\"}}" \
    ""

  expect_gate "malformed JSON degrades to silence, not a crash" \
    '{not json at all, missing quotes' \
    ""

  expect_gate "a tool call with no command or file_path stays silent" \
    '{"tool_name":"WebSearch","tool_input":{"query":"weather"}}' \
    ""

  # One case proves the file-append side actually works, writing into the
  # throwaway log created for this run only; the real log this script
  # ships next to never gets opened during a self-test.
  total=$((total + 1))
  local sample
  sample="$(run_checker "{\"tool_name\":\"Bash\",\"tool_input\":{\"command\":\"git -C ${outside_dir} status\"}}")"
  log_finding "$sample" 2>/dev/null
  if [ -s "$tmp_log" ] && grep -q 'GUARD-FLAG \[G2\]' "$tmp_log"; then
    passed=$((passed + 1))
    echo "ok   - log-append path writes a flag line to the (temp) log"
  else
    echo "FAIL - the temp log is missing the flag line it should have received"
  fi

  echo "--------------------------------------------------"
  echo "${passed}/${total} self-test cases passed"

  rm -f "$tmp_log"
  LOG_FILE="$real_log"

  if [ "$passed" -ne "$total" ]; then
    return 1
  fi
  return 0
}

# --- dispatch --------------------------------------------------------------
if [ "${1:-}" = "--self-test" ]; then
  run_self_test
  exit $?
fi

run_hook
