# HANDOFF - live state
<!-- file-class: PERSONAL -->

*This file is yours. It is written by your sessions, it is never
overwritten by an upstream update, and nothing in it ships back anywhere.*

*This file answers one question: **where does this org stand right now?** It is the
last session's own account of the live picture, written for whoever opens the repo
next - which is usually a session with no memory of anything.*

---

## How this file works

**Newest entry on top.** A reader takes the topmost entry and stops. Everything below
it is history, kept because it is occasionally useful to see how a situation developed,
never because it is current.

**One entry per session that changed anything.** A session that only read and proposed
adds nothing here. A session that wrote, ruled, spent, or moved a status writes an
entry.

**The entry is rewritten at the close of every such session, before its final commit.**
This is mandatory and it is stated as a rule in `ops/OPERABILITY.md`: a session has
not finished closing while this file still describes the repository it walked into
rather than the one it is leaving behind. Writing the handoff after the final commit
produces a handoff that is already one commit out of date.

**It is narrative, and it ranks accordingly.** Per the trust order in
`ops/COLD_RESUME.md`, this file loses to the registers, the ledgers, and any mission or
meeting artifact. Bearings are what it gives a reader, and bearings are the whole of
what it gives: authority over any open question sits with the role-owned records, never
with one session's account of them. If it disagrees with a register, the register wins
and the disagreement is itself worth reporting.

**Say what is unfinished, not just what is done.** The most valuable line in any entry
is usually the one naming what the next session must not touch until the operator
speaks.

---

## Entry format

Each entry is a dated heading followed by five short blocks. Keep it to what a reader
needs; this is a status file, not a diary.

```
## YYYY-MM-DD - <short title: what this session was about>

**Where things stand.** Two to five sentences. The live picture, in plain language.

**Done this session.** The units of work that actually landed, each pointing at the
file or artifact that proves it.

**In flight.** Anything unsealed: mission name, phase reached, owner, and what it is
waiting on. Say "nothing" when nothing is in flight.

**Blocked.** What is waiting on the operator, cross-referenced to the item on
`registers/BLOCKED_ON_OPERATOR.md`. Say "nothing" when nothing is blocked.

**Next.** The obvious next step, and explicitly what must NOT move until the operator
rules.
```

---

## Entries

<!-- Newest entry goes directly below this line. -->

## [YYYY-MM-DD] - [Founding entry - written by the onboarding interview]

*This placeholder is filled the first time this repo is set up, and shown to you
before it is written. Once it is filled, it is the bottom of the stack forever: every
later session adds its entry above it.*

**Where things stand.** [The org was constituted on this date. Name the operator's
businesses or projects as seeded into `registers/PROJECTS.md`, which seats and
functions were stood up in `org/`, and whether this working copy is public or private -
that answer changes which material is safe to commit here at all.]

**Done this session.** [The onboarding interview ran; the constitution's generated
layer in `CLAUDE.md` was filled; the model tiers in `org/models.yml` were pinned; the
spend posture and any dreaming cap were set in `ledgers/SPEND.md`; the founding ruling
was recorded in `DECISIONS.md`.]

**In flight.** [Nothing, unless the first mission was fanned out in the same sitting.]

**Blocked.** [Anything the interview surfaced that only the operator can settle - a
missing model tier, an unset spend cap, an unanswered public-or-private question.]

**Next.** [The first real piece of work: usually convening the first meeting, or a
first pass over the registers. Nothing spends, sends, or deploys until the operator
says so.]
