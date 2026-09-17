---
name: dream-run
description: Operator asks by name for an off-cycle generative/dreaming pass: arm-check, project cost, diverge unjudged across lenses, log, converge afterward, file.
---

# dream-run - the off-cycle generative pass

*The engine behind the Innovation Desk's charter, which defines what dreaming is
for; this skill is the procedure - six steps, two of them refusals. File class
DOCTRINE, per `EXTENDING.md`: upstream owns this ritual; the knobs it reads live
in files the operator owns.*

---

## 0. The principle the whole ritual protects

**Generation is unjudged; convergence never edits the divergent record, it only
selects from it.**

Every step below protects that sentence; it never shapes what gets generated.
Produced and judged together, candidates and judgment always collapse the same
way: the judge wins, because a half-formed idea cannot argue back. What survives
an inline filter is whatever already sounded reasonable - the one category of idea
a run was not needed to find.

So the divergent record is written once, never rewritten. Convergence reads it,
selects from it, and files the selection elsewhere; nothing in that pass may tidy,
delete, merge, or soften a line of the raw record. If a run produced forty
candidates and one survives, the file still holds forty - too early this quarter
is exactly what next quarter needs, in its original words.

---

## 1. When to invoke this skill, and when not to

Invoke it when the operator asks for a dream run by any of its names: dreaming, an
off-cycle run, a seam hunt, an idea pass across the projects.

Do not invoke it to speed up ordinary work: not research on a named question, not
a plan already decided, not a substitute for a meeting when a real decision is on
the table - if the operator already knows what the answer needs to cover, the
router in `CLAUDE.md` sends it elsewhere.

Dreaming runs by hand, inside a session, always; nothing here starts itself.
`doctrine/CONSTITUTION-CORE.md` forbids resident and scheduled work outright; its
narrow exception still needs its own protocol document - its own projection,
failure brake, and off switch - resuming only work a live session had begun. This
skill is not that document and does not stand in for one.

---

## 2. Step one: the armed check, which fails by default

**Read `CLAUDE.md` section (f) before anything else. If the dream cap line is still
unset, stop here and say so.**

Dreaming ships disarmed - the refusal is the feature. All three below are the
operator's to satisfy:

1. **A spend cap the operator typed**, in the generated layer of `CLAUDE.md`, as a
   figure with a period attached (per-run or per-day both work); a suggested or
   inferred number is not a cap - only a figure the operator wrote counts, standing
   in for their presence during the run.
2. **A read scope confirmed as public and internal business only.** No restricted
   or third-party material reaches a dreaming run, ever. Where setup consults a
   separate project directory, consent was recorded when configured; this skill
   reads that recorded answer, never re-asking or widening it.
3. **An off switch the operator has actually used.** Section 8 is the switch;
   arming is not complete until the operator has stopped a run with it once, on
   purpose.

When any is missing, refuse plainly, naming which one and what would fix it -
never a smaller or free-looking run instead. Enthusiasm in the conversation is not
the cap: `doctrine/CONSTITUTION-CORE.md` says something said in chat is context,
not a signature.

---

## 3. Step two: project the cost, before a single agent starts

With the cap in hand, work out the run's cost while refusing is still free.

For the generic mechanics of a pre-launch projection - the numbers a fan-out
states before launching, refusing rather than self-shrinking when they miss a
ceiling - see skill:fleet-sizing. Dream-run is a fan-out too, one agent per lens,
following those mechanics with one cap-specific delta:

- Write the projection into `ledgers/SPEND.md` as a `projected` entry before
  launch, naming the run's shape (lens count, one agent each, rough depth) and the
  projected cost and wall-clock, each as a range rather than a single figure.
- **The projection is measured against what remains, not the headline cap** - the
  cap read at the armed check in section 2, minus anything already consumed inside
  its window.

**If the projection lands above what is left, the run does not start.** File a
note instead: what was going to run, its cost, what remains, the shortfall -
optionally a smaller shape, never a quiet self-resize under the line.
Self-resizing converts the operator's ceiling into the operator's decision;
projecting first only works because refusing stays theirs while it costs nothing.

---

## 4. Step three: diverge, with no judge in the room

Once approved, generation begins - one agent per lens, in parallel, each
generating freely inside its own frame.

**Lenses.** A lens is a vantage point, not a topic. The default set spans the
org's seats plus two that belong to nobody:

- **Revenue** - demand going unmet, unnoticed, or unasked.
- **Marketing** - value nobody has been told about yet.
- **Finance** - where money leaks, margin hides, pricing runs on habit.
- **Operations** - what breaks repeatedly and gets absorbed rather than fixed.
- **Engineering** - what gets rebuilt by hand that should exist once, reused.
- **Cross-project seams** - visible only with two projects side by side, the
  vantage no single seat has.
- **Outside in** - what's happening in the wider world that matters here, argued
  from public sources, not the repository.

Name the lens set in the run card before launching; add, drop, or write your own.
The set is not doctrine, and cost scales almost linearly with size - the natural
dial for bringing a projection down.

**Rules binding every dreamer agent while generating:**

- **No filtering.** Weak-seeming candidates get written down anyway; weakness on
  read is a judgment for the later pass.
- **No scoring.** Never consulted, applied, or previewed during generation -
  scoring while generating steers toward what scores well.
- **No fit-checking.** Fit with plan, budget, or priorities is a convergence
  question; asked early it becomes a gag order, since little genuinely new fits a
  plan already made.
- **No cross-talk.** Lenses do not read each other mid-run, so two landing on the
  same seam is a real signal at convergence, not an echo.
- **Write as generated.** Each candidate lands in the memlog in the words it
  arrived, half-formed or not - cleanup is editing, and editing the record is
  what this ritual forbids.

Read scope is public and internal business material only - registers, sealed
mission artifacts, session/decision history, public sources for grounding.
Restricted and third-party material is out of bounds under gate G5 regardless of
idea quality; a candidate depending on unreadable material names the gap, never
assumes it.

Tiering follows `org/models.yml` alone - the duty map's tier, building tier by
default until a stated reason moves it. The interactive tier the operator sits
with is excluded here like every other fan-out.

Every candidate is written continuously, as generated, to a resumable per-run log,
so a mid-flight death loses only unfinished lenses. Read reference.md for the
run-directory layout and the `RUN.md`/`MEMLOG.md`/`CONVERGENCE.md` shapes once a
run is underway - needed only then, not on first invoke.

---

## 6. Step five: converge, afterward and never during

Convergence begins only once generation has finished, or the operator has ruled a
partial record worth converging anyway. It runs as its own pass, at the tier
`org/models.yml` names for the desk's scoring duty, producing `CONVERGENCE.md`.

Four moves, in order:

1. **Dedup against what already exists.** Read `inbox/INNOVATION.md` if present; a
   candidate matching a filed row is not filed again - if the new phrasing or
   grounding is genuinely stronger, note it against the existing row instead of
   duplicating.
2. **Merge within the run, in the convergence file only.** Two lenses landing on
   the same seam become one row, both credited, since independent arrival is
   itself evidence; the memlog keeps both originals, untouched.
3. **Score on the desk's four axes** as the charter defines them: payoff, size,
   grounding, and scope fit, each a short justification rather than a bare number.
   Grounding is where honesty costs the most: a hunch is written down as a hunch,
   never dressed up as a signal.
4. **Record what did not survive, and why** - one line each: the cheapest part of
   the pass, and the part most worth having later, since why a candidate was cut
   is usually a fact about the quarter, not the candidate.

Surviving rows then clear the gates every deliverable clears: standards-guard's
charter passes each row before it counts scored, failing closed (an erroring
guard blocks and surfaces the failure, never waves through). Any row with money or
liability takes a draft-flagging pass through general-counsel's charter first.

---

## 7. Step six: file, log, and then say nothing until the meeting

**Filing.** Surviving rows append to `inbox/INNOVATION.md`; the desk creates it at
first filing (never ships empty), opening with what the file is, the four scoring
axes, and the mark-not-delete rule, then the ranked table. Once it exists, append
in its shape - never restructure it. Write authority is the Innovation Desk's
alone: append and mark rows, never rewrite a prior pass's scores; no other seat
writes here.

**Logging.** Reconcile the run in `ledgers/SPEND.md` as a `reconciled` entry
against the step-two projection, naming the reason in plain words if it ran over
(which lens ran long, what retried, where scope moved). An unreconciled
projection blocks the next dream run of the same shape - intentional, since
unclosed projections make every future one worthless.

**Never interrupt.** Output reaches the operator only at the next meeting ritual,
curated into the agenda by the Chief of Staff seat - never a message between
meetings, never an urgent exception for a well-scored row. Urgency belongs in a
row's own justification, not as grounds for breaking the discipline; breaking it
teaches the operator to expect interruptions from the one function built never to
produce them.

The session that ran it closes the way any session touching the repository
closes: the handoff rewritten inside the closing commit, the run directory and
ledger entries committed as part of it.

---

## 8. The off switch

Stopping a dream run is one act with three parts, the operator's to perform:

1. **Stop the run.** Halt the session or the fan-out - whatever is generating
   stops.
2. **Mark it.** Set `status: halted` in `RUN.md`, with a line saying when and why.
3. **Reconcile what it spent.** File the reconciled entry in `ledgers/SPEND.md`
   for the part that ran - a halted run still cost what it cost.

A fourth, stronger act: unset the cap line in `CLAUDE.md` section (f). That
disarms dreaming entirely - future invocations refuse at section 2 until a figure
is written again, and nothing here can re-arm itself or treat a removed cap as
standing.

The operator should exercise all of this once before the first real run; an off
switch nobody has pulled is a claim, not a mechanism. reference.md lists the
failure classes this ritual is built against, each paired with the step that
prevents it.

---

## 10. What this skill never does

This skill never:

- Builds, sends, deploys, or spends beyond its own metered run - a high score
  authorizes appearing on the next agenda, not action.
- Reads the vault or anything restricted or third-party, under any framing, for
  any quality of idea.
- Runs a version-control command against a repository this org does not own,
  including commands that only look.
- Schedules itself, re-arms itself, raises its own cap, or carries a cap forward
  from a closed window.
- Scores proposals about its own charter or the agent-quality function's charter -
  a charter-revision idea goes to the meeting ritual directly, since the
  project-scoring lens this rubric was built for is the wrong instrument for
  judging the rules themselves.

Source: .claude/skills/dream-run/SKILL.md frontmatter, §0-4, §6-8, §10 (moved into this skill 2026-09-16)
