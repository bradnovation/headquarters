# CHANGELOG

<!-- file-class: DOCTRINE -->

*A single running, dated record of what changed between releases of the doctrine
itself, in Keep a Changelog form, newest release first.*

---

## [0.3.0] - 2026-09-16

### Added

- `plugins/headquarters-core/`: this template's own operating doctrine,
  repackaged as invoke-loaded skills under `skills/`, a `worker` subagent
  for delegated building-tier work (`agents/worker.md`), and a PreToolUse
  hook (`hooks/agent-cap.sh`) that asks before a session fans out past its
  subagent cap.
- `plugins/local-lane/`: an optional local-model safety lane for Apple
  Silicon - a PreToolUse hook (`hooks/ollama-preflight.sh`) that refuses
  commands which would load a local model until three memory rails are
  confirmed sound (`scripts/check-rails.sh`), plus a `local-model-rails`
  skill documenting the rails and how to restore them. Not enabled by
  default; an operator who doesn't run local models never sees it.
- `plugins/README.md` and `.claude-plugin/marketplace.json`: the three ways
  to enable a plugin from this repo (in-repo `.claude/skills/` symlink under
  workspace trust, a machine-wide `~/.claude/skills/` symlink, or installing
  from this repo as a plugin marketplace), and the marketplace manifest that
  makes the third route work.
- `ops/MULTI-SESSION.md`: six new sections, 14 to 19 - the context ceiling,
  park-before-idle and the cache-window wake rule, wake cadence, a peer's
  advice carried by pointer rather than copied in full, batched durability
  commits for a running record, and the HANDOFF entry template.
- `ops/templates/HANDOFF-ENTRY.md`: the entry template named by
  `ops/MULTI-SESSION.md` §19, factored out so a session fills in one file
  rather than reconstructing the shape from prose.
- `scripts/token-audit/`: four read-only scripts (`token_audit.py`,
  `permodel.py`, `rewarm.py`, `read_audit.py`, with shared helpers in
  `_common.py` and a list-price table in `prices.py`) that measure token
  burn from your own local Claude Code transcripts only - no writes, no
  network calls.
- `docs/TOKEN-ECONOMY.md`: doctrine on where a multi-session staff's token
  spend concentrates (cache writes from a re-warmed idle session, ahead of
  file size or message payload) and ranks the levers that move it by
  structural effect, largest first, naming no dollar figure of its own.
- `examples/settings/`: a worked user-level `settings.json` (effort level,
  per-model effort overrides, subagent-model and fan-out env vars, an
  autocompact window) plus `agents/explore.md`, a small-model lookup
  sub-agent worked example, and a `README.md` walking through each key.
- `docs/CUTOVER-0.3.md`: what moved where in this cutover, what's retained
  this release purely as reference, and how to verify the cutover landed
  cleanly.

### Changed

- `CLAUDE.md`: trimmed to about 6KB - the constitution's five gates, the
  approval doctrine's core premise, no-daemons, state discipline, and the
  security classes now stated in short form directly in this file, and the
  session router now names exact skills under
  `plugins/headquarters-core/skills/` by name instead of pointing at
  `ops/*.md` files and function charters.
- `doctrine/CONSTITUTION-CORE.md`: no longer mandatory reading every
  session - read only when a gate, classification, or approval question is
  actually live. Amended with pairing a stated rule with an automated check
  wherever one is technically possible, spend conservation as a discipline
  rather than an automatic ceiling on effort, a narrower read-only-inspection
  grant for a foreign repository distinct from write or deploy access, a
  brief that commissions foreign-repository work stating the no-version-
  control rule verbatim rather than pointing elsewhere, and shipping a
  capability versus turning it on for live use as two separately gated
  approvals. Kept on disk as the canonical fuller reasoning behind
  `CLAUDE.md`'s short form and as the source text the new skills were drawn
  from.
- The five project skills (`session-open`, `session-close`, `init`,
  `dream-run`, `sister-repo-consent`) moved out of `.claude/skills/` into
  `plugins/headquarters-core/skills/`; `init` split into four topic-ordered
  skills (`init-identity-and-scope`, `init-context-and-work`,
  `init-tiers-and-caps`, `init-close`).
- `README.md`, `docs/GETTING-STARTED.md`, `EXTENDING.md`: each gained a
  pointer paragraph on where the doctrine now lives and how to load it - the
  in-repo `.claude/skills/headquarters-core` symlink this template ships
  with, auto-loaded once the folder is trusted, or a machine-wide symlink
  into `~/.claude/skills/` instead - with both routes detailed in
  `plugins/README.md`, and a note that `local-lane` stays a separate,
  optional add-on.
- `scripts/README.md`: a new section documenting `scripts/token-audit/`
  alongside the existing script coverage.

### Deprecated

- `ops/*.md` doctrine files (`COLD_RESUME.md`, `FLEET_CRAFT.md`,
  `HEARTBEAT.md`, `HIGH-JUDGMENT-BANK.md`, `JUDGMENT_CRAFT.md`,
  `MULTI-SESSION.md`, `MEASUREMENT_CRAFT.md`, `OPERABILITY.md`) are retained
  this release as reference only - no longer a mandatory read from
  `CLAUDE.md`, superseded in practice by the skills shipped this release -
  and are slated for removal in 0.4 once nothing in the repo still points to
  them.

### Notes

- This cutover was made because always-on context had grown to the whole
  constitution plus doctrine reads on every session open; moving that
  content to invoke-loaded skills drops the always-on load to a 6KB entry
  file plus skill descriptions, with the rest loading only when a session
  actually invokes it.

## [0.2.0] - 2026-09-12

### Added

- `ops/MULTI-SESSION.md`: doctrine for peer sessions working in parallel on one
  machine, status asked rather than assumed, and durability across a session wall
  for ordinary, non-mission work.
- `ops/MEASUREMENT_CRAFT.md`: instrument-validity and verification doctrine, on
  proving a test can detect what it claims to, provenance on any number that
  crosses a boundary, and independent re-derivation of expensive-if-wrong claims.
- `scripts/usage-meter-tally.py`: a read-only script that sums recorded API usage
  from your own local transcripts, by model family and by lane, so a meter reading
  can be checked against actual work.
- `scripts/doctrine-diff.sh`: a script that prepares and explains an upstream
  pull's diff, limited to the doctrine paths, so taking a release does not mean
  reviewing the whole tree by hand.

### Changed

- `doctrine/CONSTITUTION-CORE.md`: amended on classifying read access and write
  access to the same thing separately, and item-level detail separately from an
  aggregate built from it.
- `ops/JUDGMENT_CRAFT.md`: amended with new sections on capability defaults,
  fidelity before novelty, naming and cross-referencing a partner's product, and a
  client's or partner's confidentiality surviving the lifting of an internal
  embargo.
- `ops/FLEET_CRAFT.md`: amended with an agent-count cap as a second brake on the
  budget guard, parallel-build namespace hygiene, and a section distinguishing a
  real spend increase from a tier change in what is doing the work.
- `ops/COLD_RESUME.md`: amended with two additions to the trust order: a peer
  session's own handoff outranks another session's account of it, and a session
  re-reads its own live state after any loss of context rather than trusting
  compacted memory.
- `org/models.yml`: comments amended with the building-tier default for fan-out
  roles, the boost line, the notify rule for a mid-work case to escalate tier, and
  short echoes of the tier-drift and cache-weighting notes carried in full
  elsewhere.
- `.claude/skills/session-close/SKILL.md`: amended with an autosave shortcut for
  administrative drafts the operator has said outright they do not read, and a
  scratch-directory sweep at close.
- `.claude/skills/session-open/SKILL.md`: amended to list live peer sessions and
  ask each its status, once, as a step after the read order.
- `README.md`: the old "Your first fifteen minutes" section replaced with an
  install-from-GitHub section a new user can follow cold, plus a short "What
  changed in 0.2" summary near the top.
- `docs/GETTING-STARTED.md`: section 2's narrative aligned with the README's
  install steps, and a new paragraph on re-running the interview against a
  long-lived repository or a template that has since changed shape.
- `EXTENDING.md`: section 6 now points at this changelog and at
  `scripts/doctrine-diff.sh` before taking a release.
- `CLAUDE.md`: repo map's `ops/` block updated to list the two new files above.
- `ops/OPERABILITY.md`: amended with the full-path-on-its-own-line handoff habit, a
  pointer to `ops/MEASUREMENT_CRAFT.md` for time discipline, three additions to the
  park-ritual checklist (mid-task fact promotion, tracking a personal-channel ask,
  checkpointing under context pressure), a name-verification rule, and a new
  fail-mode entry for a tool that rewrites its own leash.
- `org/STAFF_MEETING.md`: amended with scope-reopening on material change, a
  slipped-is-not-cancelled rule for missed sequencing, routing a decision that needs
  both technical and external facts to one convened group, an adversarial-pass
  charge to attack the self-serving conclusion and report a defect count, and
  running the compliance or legal review track in parallel with the build.
- `org/functions/standards-guard/CHARTER.md`: a new "Creative and design passes"
  section requiring hard-rail checklist enforcement over a general read-through.
- `scripts/README.md`: a new section documenting `usage-meter-tally.py` alongside
  the existing `check-invariants.sh` coverage.

### Notes

- This release keeps the standing fact that the doctrine runs fully with the
  reasoning tier at the keyboard; a more capable interactive-only tier stays a
  luxury for particular days, never a pinned duty in any fan-out.

## [0.1.0] - 2026-08-02

Initial release.
