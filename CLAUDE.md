# CLAUDE.md - entry file and session router
<!-- file-class: GENERATED -->

File class GENERATED: yours - the init interview fills the generated layer
(f) once, then it's yours. Doctrine now lives in `plugins/headquarters-core`;
upstream lands there, not here (`plugins/README.md` for loading,
`EXTENDING.md` for layer convention).

*Last amended: [DATE] - [one line: what changed, and why]*

---

## (a) What this repository is

A chartered staff: executive seats and support functions, each
charter-bound, that plan and execute your work while you keep human
judgment. Documents and rituals, not software - nothing runs on a schedule
or while you're away; every action begins in a session you open.

## (b) READ ORDER

Every session, before any other work:

1. **This file** - router, gates-in-short + approval doctrine after them,
   your generated layer. Orchestrating seat also reads
   `skill:judgment-preflight-checklist`.
2. **`HANDOFF.md`, topmost entry** - where the last session parked.
3. **`DECISIONS.md`, newest first** - ruled since founding.

Read `doctrine/CONSTITUTION-CORE.md` only when a gate, classification, or
approval question is live, not routinely - (d) and the approval doctrine
below define "live" in short form; the core wins on conflict.

## (c) SESSION ROUTER

1. **Fresh clone/redo:** `skill:init-identity-and-scope` →
   `init-context-and-work` → `init-tiers-and-caps` → `init-close`.
2. **Staff Meeting** (debate + ruling): `skill:staff-meeting-convene`.
3. **Mission execute/resume:** `skill:mission-lifecycle`,
   `skill:cold-resume` (no memory), `skill:checkpoint-discipline`,
   `skill:fleet-resume` (after a failure).
4. **Ops sweep** (read-only, `registers/`): `skill:coo-sweep`.
5. **Dream run - DISARMED:** `skill:dream-run`, blocked till (f)'s cap.
6. **Performance run** (worth keeping?): `skill:performance-run`.
7. **Park** (pause, not close): `skill:session-park`.
8. **Close** (owed once you touch this repo): `skill:session-close`.

Name ambiguity, don't guess. Money/liability/contract:
`org/functions/general-counsel/CHARTER.md` (propose-only); third-party
banking is operator-present, under G5 (`skill:transcript-banking`).

## (d) THE FIVE GATES, IN SHORT

Full reasoning: `doctrine/CONSTITUTION-CORE.md`, read only when live, per
(b).

- **G1 - Spend.** Only inside a session you opened; fan-outs project
  cost/time first, refusable; actuals log to `ledgers/SPEND.md`;
  over-ceiling is a decision.
- **G2 - Foreign repositories.** Version-control never targets another repo,
  read-only included; inspect via files, build in a throwaway clone.
- **G3 - External communication** / **G4 - Deploys.** Both structural:
  outbound stops with you (staff drafts, you release); nothing ships from
  here.
- **G5 - Sensitive material.** Third-party/sensitive material lives only in
  `vault/`, never a commit or unattended run; only a `transcripts/index/`
  card leaves it, and only the Chief of Staff touches it, with you present.

G1/G2/G5 loosen by amendment; G3/G4 don't.

**No daemons.** Nothing idles in the background (sole scheduled exception:
`skill:heartbeat`, resumption-only); no interactive-only or premium-tier
model ever runs unattended. Never set a global environment override for the
sub-agent model - it wins silently over `org/models.yml`, unrecorded.

## APPROVAL DOCTRINE, IN BRIEF

One phrase: propose-then-approve. A session gathers what it needs, forms a
view, puts it to you, and stops - your yes turns a proposal into an act.
Nothing durable happens before it: files written, money spent, agents
fanned out. Starting mid-discussion already spends money, pre-commits your
choice. This defines a live gate/security question: durable action
pending, no yes yet - stop and ask.

## (e) REPO MAP

`CLAUDE.md`, `MISSION.md`, `doctrine/CONSTITUTION-CORE.md` (full doctrine,
retained as reference this release, retiring next), `HANDOFF.md`,
`DECISIONS.md`, `EXTENDING.md`, `org/` (charters, seats, functions),
`missions/<project>/<mission>/{PACKET,STATE,FINDINGS}.md`, `registers/`,
`ledgers/`, `vault/` (gitignored, sensitive/third-party only),
`transcripts/index/` (derived cards, never raw source),
`plugins/headquarters-core/` (the doctrine, as skills), `ops/*.md`
(reference this release, retiring as skills land - `docs/CUTOVER-0.3.md`).

## STATE DISCIPLINE AND SECURITY CLASSES, IN BRIEF

The repository is the record for a successor with no memory;
conversation-only facts don't exist here. Never backfill with an invented
value - "not recorded" instead. Disagreeing files resolve in order:
registers/ledgers, mission artifacts (`STATE.md`, `FINDINGS.md`),
`HANDOFF.md`, then version-control history.

One unit of work, one commit, trailer naming model + session; write state
down along the way - background dies with the session, disk survives.

**Compaction insurance:** the recipe to continue must be on disk and
committed before compacting - context loss means re-read live state, not
compacted memory; a summary isn't the record.

**Security classes**, least to most: **C0 public**; **C1 internal**; **C2
sensitive** (money/counterparty terms, commits only where fork posture
allows); **C3 third-party words** (`vault/` only, G5: never a commit, a
remote, or an unattended run).

## (f) GENERATED LAYER

**Below this line, from the init interview, and owned by you** - upstream
never touches it, re-run anytime, draft-first.

- **Operator:** [YOUR NAME] - address form + optional rhythm.
- **Projects:** [ONE LINE EACH; add/remove freely] - of record in
  `registers/PROJECTS.md`.
- **Values:** [IN YOUR OWN WORDS] - quoted into charters, used by
  standards-guard; blank means plain competence only.
- **Dream cap: [UNSET]** - disarms router item 5 till set; over-cap files
  instead of launching, actuals to `ledgers/SPEND.md`.
- **Fork posture: [PUBLIC/PRIVATE]** - PUBLIC commits only C0; PRIVATE
  C0-C2, never C3.

## (g) AMENDING THIS FILE, AND THE GOVERNANCE HIERARCHY

Changes by your word, not a session's judgment: a ruling goes into
`DECISIONS.md` first, this file edited to match; a session may draft and show
an amendment, never write one on conversation alone.

Extensions only add stricter rules, never loosen a gate. A charter/doctrine
conflict is surfaced, not resolved - the core wins till you rule otherwise.
Keep personal rules in your own layer, not doctrine.
