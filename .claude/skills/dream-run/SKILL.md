---
name: dream-run
description: Run the off-cycle generative pass the Innovation Desk calls dreaming. Invoke when the operator asks to dream, to run a dream run, to hunt for seams across projects, or to generate ideas off-cycle. The ritual is fixed - refuse unless a spend cap has been set in CLAUDE.md's generated layer, project the cost against that cap before anything launches, generate across named lenses with no judging in the loop, preserve every candidate in a resumable memlog, and only then score and file surviving rows into inbox/INNOVATION.md. Results wait for the next meeting; they never interrupt.
---

# dream-run - the off-cycle generative pass
<!-- file-class: DOCTRINE -->

*The engine behind `org/functions/innovation-desk/CHARTER.md`. The charter says what
dreaming is for and what may be done with its output. This skill is the procedure:
six steps in a fixed order, two of which are refusals. File class DOCTRINE, so
upstream owns it; the knobs it reads are all in files you own.*

---

## 0. The principle the whole ritual protects

**Generation is unjudged; convergence never edits the divergent record, it only
selects from it.**

Every step below exists to hold that sentence up. The structure is here to protect
free generation, never to shape it. A ritual this tight around something as loose as
idea generation looks like a contradiction until you see what it is actually holding
apart: the moment of producing candidates and the moment of judging them. Left
together they collapse, and they always collapse the same direction. The judge wins,
because a half-formed idea cannot argue back yet. What survives an inline filter is
whatever already sounded reasonable, which is the one category of idea you did not
need a run to find.

So the divergent record is written once and never rewritten. Convergence reads it,
selects from it, and files what it selects somewhere else. Nothing in the convergence
pass has permission to reach back and tidy, delete, merge, or soften a line of the
raw record. If the run produced forty candidates and one row survives, the file still
holds forty. That is not archival sentiment. A candidate that was too early this
quarter is exactly the thing you want to find again next quarter, in the words it was
first written in.

---

## 1. When to invoke this skill, and when not to

Invoke it when the operator asks for a dream run by any of its names: dreaming, an
off-cycle run, a seam hunt, an idea pass across the projects.

Do not invoke it as a way of doing ordinary work faster. Dreaming is not research on
a named question, not a plan for something already decided, and not a substitute for
convening a meeting when a real decision is on the table. If the operator already
knows what the answer needs to cover, that is a mission or a meeting, and the router
in `CLAUDE.md` sends it somewhere else.

Dreaming is invoked by hand, inside a session, always. Nothing here starts itself.
`doctrine/CONSTITUTION-CORE.md` forbids resident processes and scheduled work outright,
and the exception it describes is narrow and heavily conditioned: a scheduled routine
would need a protocol document of its own carrying its projection, its failure brake,
and its off switch, and it could only resume what a live session had already begun.
This skill does not create that document and does not stand in for one. If you want
dreaming to run on a clock, that is a separate piece of design, written and ruled
before anything is wired.

---

## 2. Step one: the armed check, which fails by default

**Read `CLAUDE.md` section (f) before anything else. If the dream cap line is still
unset, stop here and say so.**

Dreaming ships disarmed. The refusal is the feature, not a rough edge somebody left
in. Three conditions have to hold before a run is permitted, and all three are the
operator's to satisfy:

1. **A spend cap the operator typed**, sitting in the generated layer of `CLAUDE.md`
   as a figure with a period attached. Per run and per day are both workable shapes;
   what matters is that the line names an amount and the window it applies to. A
   suggested number is not a cap. A number a session inferred from context is not a
   cap. Only a figure the operator wrote counts, because the cap is the one
   authorization that stands in for the operator's presence while a run is going.
2. **A read scope confirmed as public and internal business only.** No restricted or
   third-party material reaches a dreaming run, ever. Where the setup consults a
   separate project directory for context, that consent was recorded when that
   connection was configured; this skill reads the recorded answer and does not
   re-ask, widen, or assume it.
3. **An off switch the operator has actually used.** Section 8 below is the switch.
   Arming is not complete until the operator has stopped a run with it once, on
   purpose, and seen what stopping looks like.

When any of the three is missing, the correct output is a short, plain refusal naming
which one and what would fix it. Do not launch a smaller run instead. Do not launch a
free-looking run instead. Do not treat enthusiasm in the conversation as the cap:
`doctrine/CONSTITUTION-CORE.md` is explicit that something said in chat is context,
not a signature.

---

## 3. Step two: project the cost, before a single agent starts

With the cap in hand, work out what this run would cost and put that in front of the
operator while refusing is still free.

Write the projection into `ledgers/SPEND.md` as a `projected` entry before the launch,
in the format that ledger specifies. The projection states four things:

- **The shape of the run.** How many lenses, one agent each, and roughly how deep each
  one goes.
- **The projected cost**, in whatever unit the operator tracks, as a range rather than
  a single confident figure.
- **The projected wall-clock**, also as a range.
- **What it is measured against.** The cap from section (f), minus anything already
  consumed inside the cap's window. That remainder is the number the projection has to
  clear, not the headline cap.

**If the projection lands above what is left, the run does not start.** File a note for
the operator instead: what was going to run, what it would have cost, what remains, and
what the shortfall is. The note may offer a smaller shape as an option, listing which
lenses would be dropped and what the reduced run would cost. What it must not do is
quietly shrink itself down under the line and go. A run that self-resizes to fit has
converted the operator's ceiling into the operator's decision, and the whole point of
projecting first is that the refusal is theirs to make while it costs nothing.

Projection is not paperwork. It is the only moment in the entire run where saying no
is cheap.

---

## 4. Step three: diverge, with no judge in the room

Once the projection is approved, generation begins. One agent per lens, running in
parallel, each generating freely inside its own frame.

**Lenses.** A lens is a stated vantage point, not a topic. The default set runs across
the seats the org already has plus two that belong to nobody:

- **Revenue** - where demand is going unmet, unnoticed, or unasked.
- **Marketing** - what the work is worth that nobody has been told about yet.
- **Finance** - where money leaks, where margin hides, what is priced by habit.
- **Operations** - what breaks repeatedly and gets absorbed rather than fixed.
- **Engineering** - what is being rebuilt by hand that should exist once and be reused.
- **Cross-project seams** - patterns visible only because two projects sit side by
  side, which is the vantage no single seat has.
- **Outside in** - what is happening in the wider world that would matter here, argued
  from public sources rather than from the repository.

Name the lens set in the run card before launching. Add lenses, drop lenses, or write
your own. The set is not doctrine and the cost scales almost linearly with its size,
which makes it the natural dial when a projection needs to come down.

**The rules that bind every dreamer agent while it is generating:**

- **No filtering.** A candidate that seems weak gets written down. Weak on first
  reading is a judgment, and judgments belong to the later pass.
- **No scoring.** The rubric is not consulted, not applied, and not previewed during
  generation. An agent that scores while it generates has started steering toward what
  scores well.
- **No fit-checking.** Whether an idea suits the current plan, the current budget, or
  the operator's stated priorities is a convergence question. Asked early it becomes a
  gag order, because almost nothing genuinely new fits the plan that was made before
  it existed.
- **No cross-talk.** Lenses do not read each other mid-run. Independence is what makes
  two lenses landing on the same seam a real signal at convergence time rather than an
  echo of whichever agent wrote first.
- **Write as generated.** Each candidate lands in the memlog in the words it arrived
  in, including the ones that read as half-formed. Cleaning up phrasing is editing,
  and editing the divergent record is the one thing this ritual does not permit.

Read scope during generation is public and internal business material only: the
registers, sealed mission artifacts, session and decision history, and public sources
where a lens needs outside grounding. Restricted and third-party material is out of
bounds under gate G5 with no exception for how good the idea would have been. When a
candidate genuinely depends on something the run may not read, it is written down as a
candidate that names the gap. It is never written down as though the grounding exists.

Tiering follows `org/models.yml` and nothing else. Generation runs at the tier the
duty map names for it, and where the map has no row yet, the escalation rule in that
file applies: building tier is the default until a stated reason moves it. The
interactive tier the operator sits with is excluded from this fan-out the same way it
is excluded from every other one.

---

## 5. Step four: the memlog, which makes a dead run resumable

*Adapted pattern: the generation-from-selection split and the resumable log carrying
it follow BMAD-METHOD. See `ATTRIBUTIONS.md`.*

Each run gets a directory: `inbox/dream-runs/<date>-<short-name>/`. Mark every file in
it `<!-- file-class: PERSONAL -->`; these hold the operator's own material and upstream
has no business with them.

Three files:

**`RUN.md`** - the run card, written at launch and updated at each transition. It
carries the cap that was read, the projection as filed, the lens set, and a status line
a resuming session can act on without reading anything else:

```
status: diverging | diverged | converging | filed | halted
lenses: 7 named, 4 complete
last-write: [DATE, time]
```

**`MEMLOG.md`** - the divergent record. Append-only, written continuously as
generation happens rather than assembled at the end. Every candidate carries its lens,
the order it arrived in, and whatever the agent wrote about where it came from. Nothing
is ever removed from this file, and nothing in it is ever rewritten. Not during
convergence, not when a candidate turns out to be wrong, not when a later run finds a
better version of the same thought. Corrections and second thoughts are appended, and
they say what they are correcting.

**`CONVERGENCE.md`** - written in step five, in a separate file for exactly this
reason. Selection lives here so that selection cannot touch the record it is selecting
from.

**Why continuous writing rather than a tidy write at the end.** Background work does
not survive the session that started it, but files do. A run that dies at the seventy
percent mark with everything still in context has lost seventy percent of a paid run.
The same run writing as it goes has lost the last thirty and can be resumed. On resume,
read `RUN.md` for the status line, read `MEMLOG.md` for what already exists, and
restart only the lenses that never finished. Do not re-run a completed lens for
tidiness. Do not start convergence on a partial record without saying plainly that the
record is partial and which lenses are missing from it.

---

## 6. Step five: converge, afterward and never during

Convergence begins only when generation has finished, or when the operator has ruled
that a partial record is worth converging anyway. It runs as its own pass, at the tier
`org/models.yml` names for the desk's scoring duty, and it produces `CONVERGENCE.md`.

Four moves, in order:

1. **Dedup against what already exists.** Read `inbox/INNOVATION.md` if it is there.
   A candidate matching a row already filed is not filed again. If the new phrasing is
   genuinely better or the grounding is genuinely stronger, note that against the
   existing row rather than creating a second one. Duplicate rows are how a ranked
   inbox stops being readable, and an unreadable inbox reaches no meeting.
2. **Merge within the run, in the convergence file only.** Two lenses landing on the
   same seam become one candidate row, with both lenses credited, because independent
   arrival is itself evidence. The merge is recorded in `CONVERGENCE.md`. The memlog
   keeps both originals, untouched.
3. **Score on the desk's four axes** as the charter defines them: payoff, size,
   grounding, and scope fit, each written as a short justification rather than a bare
   number. Grounding is where honesty costs something and matters most: a hunch is
   written down as a hunch. A row that dresses up a hunch as a signal corrupts the
   ranking for everything it outranks.
4. **Record what did not survive, and why.** One line each. This is the cheapest part
   of the pass and the part most worth having later, because the reason a candidate was
   cut is usually a fact about this quarter rather than a fact about the candidate.

The surviving rows then clear the gates every deliverable clears.
`org/functions/standards-guard/CHARTER.md` passes each row before it counts as scored,
and that gate fails closed: a
guard that errors blocks the row and surfaces the failure, rather than waving it
through or dropping it quietly. Any row with money or liability in it takes a
draft-flagging pass through `org/functions/general-counsel/CHARTER.md` before it is
ranked.

---

## 7. Step six: file, log, and then say nothing until the meeting

**Filing.** Surviving rows are appended to `inbox/INNOVATION.md`. That file does not
ship with the template and it is not created empty in advance; the desk creates it at
the moment of its first filing, which may well be this run. When creating it, open with
a short statement of what the file is, the four axes it scores on, and the rule that
rows are marked rather than deleted, then the ranked table itself. When it already
exists, append in the shape it already has and do not restructure it.

Write authority over that file belongs to the Innovation Desk. This skill files as the
desk, appending rows and marking existing rows. It does not rewrite scores that a
previous pass filed, and no other seat writes to that file at all.

**Logging.** Reconcile the run in `ledgers/SPEND.md` as a `reconciled` entry against
the projection filed in step two. If the actual came in over, name the reason in plain
words: which lens ran long, what retried, where the scope moved mid-run. An
unreconciled projection blocks the next dream run of the same shape, and that is
intentional, because a ledger of unclosed projections makes every future projection
worthless.

**Never interrupt.** The output of a dream run reaches the operator at the next
convening of the meeting ritual, curated into the agenda by the Chief of Staff
(`org/seats/chief-of-staff/CHARTER.md`). It does
not arrive as a message between meetings. It does not arrive as an urgent exception
because a row scored unusually well. Urgency is something a row states about itself in
its own justification; it is not grounds for breaking the discipline, and a run that
breaks it has taught the operator to expect interruptions from the one function that
was built specifically never to produce them.

The session that ran the dream run closes the way any session that touched the
repository closes, following `ops/OPERABILITY.md`: the handoff rewritten inside the
closing commit, the run directory and the ledger entries committed as part of it.

---

## 8. The off switch

Stopping a dream run is one act with three parts, and it is the operator's to perform:

1. **Stop the run.** Halt the session or the fan-out. Whatever is generating stops
   generating.
2. **Mark it.** Set `status: halted` in `RUN.md` and add a line saying when and why.
3. **Reconcile what it spent.** File the reconciled entry in `ledgers/SPEND.md` for the
   part that ran. A halted run still cost what it cost.

There is a fourth act available and it is the strongest one: return the cap line in
`CLAUDE.md` section (f) to unset. That disarms dreaming entirely, and every future
invocation refuses at section 2 until a figure is written again. Nothing in this skill
can re-arm itself, re-read a cap that was removed, or interpret an old cap as still
standing.

The operator should exercise all of this once before the first real run. An off switch
nobody has pulled is a claim, not a mechanism.

---

## 9. The failure classes this ritual is built against

Each of these has a step above that exists solely to prevent it.

- **The inline critic.** Scoring bleeds into generation, the run produces a clean list
  of reasonable ideas, and the seam nobody was looking at was killed at the moment it
  was least able to defend itself. Prevented by section 4 and by keeping convergence in
  a separate file.
- **The tidied record.** Convergence rewrites the memlog while it is in there anyway,
  and next year's version of this run reads a record that has already agreed with the
  judgment made about it. Prevented by the append-only rule in section 5.
- **The cheerful overrun.** A run that looked inexpensive costs several times its
  projection and nobody finds out until the meter says so. Prevented by projecting
  against the remaining cap in section 3 and reconciling in section 7.
- **The lost run.** Generation was excellent, the session died, and none of it was on
  disk. Prevented by writing the memlog continuously.
- **The interrupt.** One genuinely exciting row arrives between meetings, the surfacing
  discipline bends for it, and within a month the inbox is a notification stream.
  Prevented by section 7 holding absolutely.
- **The armed-by-drift run.** No cap was ever written, but the conversation was warm
  and the run went anyway. Prevented by section 2 refusing on the file rather than on
  the mood.

---

## 10. What this skill never does

It does not build, send, deploy, or spend beyond its own metered run. A high score is
not authorization to act on anything; it is authorization to appear on the next agenda,
where the operator decides whether it becomes a mission.

It does not read the vault or anything classified restricted or third-party, under any
framing, for any quality of idea.

It does not run a version-control command against a repository this org does not own,
including commands that only look.

It does not schedule itself, re-arm itself, raise its own cap, or carry a cap forward
from a window that has closed.

It does not score proposals about its own charter or about the agent-quality function's
charter. A charter-revision idea goes to the meeting ritual directly, because the
project-scoring lens this rubric was built for is the wrong instrument for judging the
rules themselves.
