# CUTOVER-0.3 - the doctrine-as-skills cutover

<!-- file-class: DOCTRINE -->

*What moved where in the 0.3 public cutover, what's retained this release
purely as reference, and how to verify the cutover landed cleanly.*

---

## 1. What this cutover did

Before 0.3, every session read `CLAUDE.md` and then `doctrine/CONSTITUTION-CORE.md`
in full - 23.6KB of mandatory reading before any other work - and the five
project rituals (`session-open`, `session-close`, `init`, `dream-run`,
`sister-repo-consent`) lived as one-shot skills under `.claude/skills/`.

0.3 repackages that doctrine as invoke-loaded skills under
`plugins/headquarters-core/skills/`, loaded on demand rather than read whole
every session, and rewrites `CLAUDE.md` itself to route to them by name.
`doctrine/CONSTITUTION-CORE.md` is no longer a mandatory read - `CLAUDE.md`
now carries the load-bearing rules (the five gates, the approval doctrine's
core premise, no-daemons, state discipline, security classes) in short form,
and a session opens the full doctrine core only when a gate, classification,
or approval question is actually live.

## 2. What moved where

### `CLAUDE.md` itself

The router, the five gates, the repo map, and the generated layer stayed in
`CLAUDE.md` - that was already the always-on-only shape. What changed:

| Was | Now |
|---|---|
| `doctrine/CONSTITUTION-CORE.md` read every session, unconditionally (READ ORDER item 2) | Read only when a gate/security/approval question is live - see `CLAUDE.md` (b) |
| Session router pointed at `ops/*.md` files and function charters for procedure | Session router names exact skills under `plugins/headquarters-core/skills/` by name |
| No standalone approval-doctrine or state-discipline text in `CLAUDE.md` | Both now stated in `CLAUDE.md`, short form, absorbed from the doctrine core |

### `doctrine/CONSTITUTION-CORE.md` sections absorbed into `CLAUDE.md`

| Doctrine core section | Landed in `CLAUDE.md` as |
|---|---|
| §2 the five gates (G1, G2, G5 essentials; G3/G4 already short) | (d) THE FIVE GATES, IN SHORT |
| §3 intro + "Nothing durable happens before the operator says yes" | APPROVAL DOCTRINE, IN BRIEF |
| §4 "The repository is the record", "One unit of work, one commit", "Write state down along the way" | STATE DISCIPLINE AND SECURITY CLASSES, IN BRIEF |
| §5 SECURITY CLASSES (C0-C3) | STATE DISCIPLINE AND SECURITY CLASSES, IN BRIEF |
| §6 NO DAEMONS AND WHO RUNS UNATTENDED (core line, plus both constitutional model-policy rules: no interactive-only/premium tier unattended, and never a global sub-agent-model override) | (d), closing "No daemons" paragraph |
| §7 THE CONSTITUTION WINS | (g) AMENDING THIS FILE, AND THE GOVERNANCE HIERARCHY |
| §1, Title/preamble, G3, G4 full text | Not carried forward - already fully covered by `CLAUDE.md`'s own short form, or by this file's own maintenance framing, which a template user has no need to duplicate |
| §3 "Every draft is read before it is kept", "Four postures, cheapest first", "A plan nobody attacked...", §4 "The session-close ritual is mandatory", §5 "The fork posture question, named plainly" | Not in `CLAUDE.md` (never were - these are procedural, not always-on); live in `skill:draft-review`, `skill:four-postures`, `skill:fleet-sizing`, `skill:session-close`, `skill:init-identity-and-scope` respectively |

### Repo-map entries not individually named in `CLAUDE.md` (e) any more

The trimmed (e) REPO MAP names paths by category to hold its byte budget. Four
paths that the pre-0.3 map named individually still exist on disk, unchanged,
and are simply no longer called out by name - they fall under a category
entry above (`org/` etc.) or are just not re-listed:

| Path | Status |
|---|---|
| `inbox/` (`INNOVATION.md`, the ranked proposal inbox) | Unchanged on disk; not named in the trimmed map |
| `SESSION_LOG.md` | Unchanged on disk; not named in the trimmed map |
| `meetings/` | Unchanged on disk; not named in the trimmed map |
| `counsel/` | Unchanged on disk; not named in the trimmed map |

None of these were removed, retired, or folded into a skill - this is a
disclosure of the repo map's own trim, not a functional change.

### The five old project skills

| Old skill (`.claude/skills/<name>`, removed) | New skill(s) (`plugins/headquarters-core/skills/`) |
|---|---|
| `session-open` | `session-open` |
| `session-close` | `session-close` |
| `init` | `init-identity-and-scope` → `init-context-and-work` → `init-tiers-and-caps` → `init-close` (split into four topic-ordered skills) |
| `dream-run` | `dream-run` |
| `sister-repo-consent` | `sister-repo-consent` |

The `.claude/skills/headquarters-core` symlink to `plugins/headquarters-core`
is unchanged and still how this repo auto-loads the plugin in-repo.

## 3. Retained this release, retiring next

Two things stay on disk this release purely as reference, superseded in
practice by the skills above, and are slated for removal once nothing in the
repo still points to them:

- **`doctrine/CONSTITUTION-CORE.md`** - the full-text doctrine core. Kept as
  the canonical fuller reasoning behind `CLAUDE.md`'s short form and as the
  source document for the skills that absorbed it. `CLAUDE.md` (b) and (e)
  both say so explicitly.
- **`ops/*.md`** (`COLD_RESUME.md`, `FLEET_CRAFT.md`, `HEARTBEAT.md`,
  `HIGH-JUDGMENT-BANK.md`, `JUDGMENT_CRAFT.md`, `MULTI-SESSION.md`,
  `MEASUREMENT_CRAFT.md`, `OPERABILITY.md`) - their procedural content is, by
  name and description, already substantially covered by skills shipped this
  release (`cold-resume`/`cold-resume-classify`, `fleet-brief`/`fleet-sizing`/
  `fleet-resume`/`fleet-return-contract`/`fleet-verify`, `heartbeat`,
  `judgment-when-to-escalate`, the `judgment-*` family, `multi-session`,
  `measurement`, `checkpoint-discipline`/`session-park`). This cutover did not
  line-by-line verify every ops file against its skill, so treat the mapping
  above as directional, not a guarantee of 1:1 coverage - confirm before
  deleting an `ops/*.md` file that its content is actually gone from nowhere
  else.

Neither is referenced as a mandatory read from `CLAUDE.md` any longer; both
are pointer targets only, named in the REPO MAP.

## 4. How to verify

```bash
# CLAUDE.md is within the target size
wc -c CLAUDE.md

# The plugin's skills are valid and discoverable
claude plugin validate plugins/headquarters-core
claude plugin details headquarters-core@skills-dir

# The generic invariant guard still behaves (independent of this cutover -
# it checks tool calls, not file layout, so it should be unaffected)
bash scripts/check-invariants.sh --self-test

# No operator-identifying facts or absolute local paths leaked into the
# public layer - substitute your own operator handle and home-directory
# pattern for the placeholders below
grep -rniE '<your-operator-handle>|<your-home-path-prefix>' \
  CLAUDE.md plugins/headquarters-core docs/CUTOVER-0.3.md

# Nothing was committed or stashed by this cutover
git status --short
```

`claude plugin details headquarters-core@skills-dir` should list the plugin
loaded from the `.claude/skills/headquarters-core` symlink (or from
`~/.claude/skills/headquarters-core` if you installed it machine-wide per
`plugins/README.md`), and enumerate the skills under
`plugins/headquarters-core/skills/` by name.
