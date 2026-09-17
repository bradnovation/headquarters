# scripts/ - check-invariants.sh, usage-meter-tally.py, doctrine-diff.sh, token-audit/
<!-- file-class: DOCTRINE -->

*This directory holds mechanical tooling that supports the constitution
rather than restating it. `doctrine/CONSTITUTION-CORE.md` is still the
authority on what G2 and G5 mean and why they exist; this script is one
best-effort way to notice, mechanically, when a tool call is about to
touch either one.*

*Adapted pattern: keeping a small script that re-checks stated rules follows
AI Team OS's invariant checker. See `ATTRIBUTIONS.md`.*

---

## What it checks

`check-invariants.sh` reads a single tool-call payload (`tool_name` plus a
`tool_input` object, the shape a pre-execution hook typically hands a
guard script) and looks for two things:

- **G2 - a git command aimed outside this repository.** It looks
  specifically at the flags and idioms that actually name a target
  repository: `-C <path>`, `--git-dir=<path>`, `--work-tree=<path>`, and a
  `cd <path>` that precedes a `git` invocation in the same command string.
  If any of those name an absolute path that is not this repository's own
  root or somewhere inside it, it flags.
- **G5 - anything touching `vault/`.** Rather than checking only a
  `command` string or a `file_path` field, it walks every string value
  anywhere inside `tool_input`, however deeply nested, and flags if any of
  them contains `vault/`. That is deliberately broader than "the two
  fields today's tools happen to use," so the same check keeps working if
  a differently-shaped tool call is added later without anyone having to
  remember to widen this script by hand.

Everything it checks is repo-root relative. The script finds its own
repository root at runtime, one directory above wherever it itself is
installed, so it carries no path belonging to any one person's machine and
runs unmodified in any clone.

## Warn-only, and why that is the whole point right now

This script never blocks anything and always exits `0`, whether or not a
rule tripped. When one does, standard error gets a short human-readable
notice and the same finding, timestamped, is appended to a log file kept
next to the script:

```
GUARD-FLAG [G2|G5]: <one-line reason>
  fragment: <the piece of input that tripped it, truncated at 120 chars>
```

The reasoning: a mechanical check that can be wrong is only safe to wire
into a live pipeline if being wrong costs a visible line of output rather
than a blocked action. Running warn-only for a while is how the operator
finds out this script's own false-positive rate before trusting it with
anything sharper. It is enforcing gates that already exist; it invents no
new rule of its own.

## Log location

`scripts/invariant-guard.log`, created the first time something actually
trips a rule and not before. An absent log file is informative: it means
nothing has flagged yet, not that logging is broken.

## Flipping warn to deny (a later, separate, operator choice)

Nothing here implements a deny path, on purpose. If the operator later
decides this script has earned a stricter role, the mechanical change is
small: make `run_hook`'s exit code depend on whether a rule tripped
(instead of always returning `0`), and then actually wire this script into
whatever hook configuration the operator's own tooling reads. Both of
those are real decisions with real consequences (a false positive now
blocks work instead of merely logging it), so this script deliberately
stops short of making them. Treat "should this deny" as a question for the
operator to answer explicitly, not a setting a session flips because the
warn-only period felt long enough.

## Known limits, stated rather than hidden

- **Relative paths are not resolved.** `cd ../elsewhere && git status`
  names a path this script cannot safely resolve without knowing the
  shell's working directory at the moment the command actually runs, so it
  is left alone rather than guessed at. This is a real gap, not an
  oversight papered over; a stricter posture would need the actual
  execution context, not just the command string.
- **A git command with no explicit target flag is invisible to this
  check.** Plain `git status` run from inside a foreign checkout, with no
  `-C`, `--git-dir`, `--work-tree`, or preceding `cd` naming the path in
  the same string, does not trip G2. The check looks for a command that
  names its target explicitly; it does not track what directory a shell
  happens to be sitting in.
- **This is a net, not a wall.** It is one mechanical layer on top of the
  actual rule, which lives in `doctrine/CONSTITUTION-CORE.md` and binds
  regardless of whether any tool happens to be flagging violations of it
  today.

## Wiring it in

This script does not wire itself into anything. Whatever harness runs
tool calls in your setup will have its own place to register a
pre-execution check; point that configuration at this script, feeding it
the same JSON shape described above on standard input. That wiring is left
out of this script deliberately: writing to the operator's own tool
configuration is a change with its own consequences, and it belongs to the
operator's hand, the same way every other durable change in this product
does.

## Self-test

```
bash scripts/check-invariants.sh --self-test
```

Runs a fixed set of embedded cases (a foreign-repo target through each of
`-C`, `--git-dir`, and a preceding `cd`; the same repository referenced by
each of those forms, which must stay silent; an absolute and a relative
`vault/` reference; a `vault/` reference nested inside an unrelated field,
proving the recursive scan; a plain non-git, non-vault call; and malformed
JSON) and prints one line per case, exiting nonzero if anything fails. It
writes to a temporary log file for the duration of the run and never
touches the real `scripts/invariant-guard.log`.

---

# usage-meter-tally.py

## What it checks

`usage-meter-tally.py` is a read-only instrument, not a guard. It walks
your local Claude Code transcripts (`~/.claude/projects/**/*.jsonl`,
skipping `journal.jsonl`, which is an index rather than a record of API
responses) and sums every recorded API response it finds. Each `assistant`
record it reads carries a model name, a usage block (input, cache-write,
cache-read, and output tokens), and a timestamp; records are de-duplicated
by their message id, keeping whichever copy of a given id has the largest
output token count, since a streamed or resumed session can otherwise
persist the same response more than once.

Totals are grouped into week windows on a configurable boundary, then
broken out by model family and by lane - the main keyboard versus
subagents, decided purely from whether a transcript's own path contains
`/subagents/`. Every period is priced against a list-price table so two
weeks, or two lanes, compare on one consistent scale even when the mix of
models between them changed.

Run it when the meter reading and the amount of actual work done seem to
disagree with each other. Read the ratios between periods and between
lanes, not the absolute total: a subscription plan's own metering weighs a
run its own way, and that weighting belongs to the provider, not to this
script's price table.

## How to run it

```
python3 scripts/usage-meter-tally.py
```

No arguments and no configuration file. The constants block at the top of
the script (timezone, week boundary weekday and hour, the price table, and
the long-context threshold) is the whole configuration surface; edit those
constants directly if your own setup differs from the defaults.

## What it never does

- It never writes to any transcript, ledger, or any other file. It only
  prints a table to standard output.
- It never makes a network call, and never contacts a provider's billing
  or usage API. Every figure it reports is computed from records already
  sitting on disk.
- It never reads or reports anything about the content of a conversation.
  It reads only the model name, the usage counters, the timestamp, and the
  file's own path (to decide the lane); message text is never opened.
- It never asserts that its own price table matches what you were actually
  billed. The table is a set of constants you maintain, priced at list, so
  that periods compare on one scale; it is not a bill.

---

# doctrine-diff.sh

## What it checks

`doctrine-diff.sh` prepares and explains an upstream doctrine diff so you
do not have to assemble one by hand every time you want to review a new
release. It runs entirely inside your own copy of this repository, against
your own repository only: it fetches the upstream remote you name (or
`upstream` by default), then prints `git diff --stat` and the full `git
diff` between your current commit and the ref you name (or
`upstream/main` by default), restricted to the doctrine-class paths listed
in `EXTENDING.md` section 5. Those paths are copied into an array near the
top of the script, with a comment pointing back at that section, so the
list this script checks and the list that section documents can be
compared directly.

## How to run it

```
scripts/doctrine-diff.sh [remote] [ref]
```

Both arguments are optional. Add the upstream repository as a remote once,
in your own copy, before the first run; the script tells you plainly if
the named remote does not exist yet rather than guessing at one.

## What it never does

- It applies nothing. No merge, rebase, cherry-pick, or file write happens
  at any point; the script only fetches and prints.
- It never runs a git command against any repository other than the one it
  lives in. There is no path in this script naming a foreign repository,
  and none of its git commands accept one.
- It never widens its own path list beyond what `EXTENDING.md` section 5
  states. If that section's table changes, the array in this script needs
  a matching edit; the script does not read that file at run time to stay
  in sync automatically.
- It never decides what to apply. The diff it prints is for your own
  review; applying any of it, in your own commit, stays your act, exactly
  as `EXTENDING.md` section 6 describes.

---

# token-audit/

## What it does

`token-audit/` is a directory of four read-only scripts -
`token_audit.py`, `permodel.py`, `rewarm.py`, `read_audit.py` - plus a
shared `prices.py` module, that measure token burn from your own local
Claude Code transcripts (`~/.claude/projects/<project-dir>/**/*.jsonl`).
Each takes `--since`/`--until` (default: the last 21 days) and an optional
`--projects` substring filter, so the same four scripts serve both a
one-off look and a repeatable before/after comparison across any window.
`token-audit/README.md` says what each script measures, how to take a
baseline and compare a later run against it, and what the numbers - context
p50/p90, cache write vs cache read, re-warm events - mean.

## What it never does

- It never writes to any transcript or any other file, and never makes a
  network call. Every number comes from `.jsonl` files already on disk.
- It never reads message text as content. The one partial exception
  (`read_audit.py` taking a text field's length, and checking one fixed
  literal as a substring match) is documented in `token-audit/README.md`;
  the text itself is never printed, stored, or returned.
- It never bills anything. `permodel.py`'s dollar figures are computed
  against the list-rate table in `prices.py` (or your own override file),
  for comparing two runs on one scale - never a claim about what a provider
  actually charged.
