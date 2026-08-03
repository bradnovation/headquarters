# FLEET_CRAFT - how a fan-out is projected, run, landed, and learned from
<!-- file-class: DOCTRINE -->

*This file ships with the product and is upstream-pullable. Edit it only if you
intend to own your own copy of it forever.*

*Purpose: a fan-out is the one thing this org does that can spend real money in
minutes and produce work faster than you can read it. This file governs all of it:
what must be true before a fleet launches, how its script has to behave while it
runs, how its output reaches you for approval, what a resume is allowed to cost, and
how the org gets cheaper at this over time instead of repeating itself. A mission
packet that contradicts anything here surfaces the conflict rather than proceeding.*

---

## 1. What a fleet is, and when one is the wrong shape

A fleet is any run where a session convenes more than one agent: lanes in parallel,
stages in a pipeline, a set of reviewers over a finished package. One session, one
script, many agents, one envelope.

Three properties follow from that and drive everything below.

**A fleet dies with the session that launched it.** Nothing in this system picks up
abandoned work, because nothing in this system runs unattended
(`doctrine/CONSTITUTION-CORE.md`, section 6). When the session ends, every agent
still running ends with it, and what you are left holding is exactly what reached the
disk.

**A fleet multiplies the brief, including its mistakes.** Ten agents working from a
brief with a hole in it produce ten holed deliverables and a review bill. The
constitution's own words for this are that a plan nobody attacked is a guess with
formatting on it. Sharpen the brief while it is one document, not after it is
twelve.

**A fleet spends before it reports.** By the time anything is on screen, the money is
gone. This is why projection happens at the front, where refusing is still free.

**When a fleet is the wrong shape.** One agent doing one pass is cheaper than three
agents and a merge step, and it stays cheaper until the work genuinely splits into
independent pieces. Do not fan out work whose specification is still moving, work
whose pieces all need to read each other, or work whose review cost is larger than
the time the parallelism saves. Convening more agents than the job needs is its own
failure mode, exactly the way convening more seats than an intent needs is.

---

## 2. The three numbers, stated before any launch

No fleet launches until three figures have been said out loud, at the launch moment,
in a form you can refuse.

1. **Projected tokens.** Derived, not asserted: agents multiplied by expected passes
   multiplied by expected output size per agent, plus the orchestrator's own
   overhead, plus the review lanes. Show the arithmetic. A bare number reads to you
   as an estimate when it is frequently a wish.
2. **Projected wall-clock.** How long the run will occupy the session, end to end,
   including the gate and closure work.
3. **Your meter position, read fresh.** Whatever your plan and harness expose as
   remaining usage, read at the launch moment. A remembered reading from earlier in
   the session is not a reading.

Then four rules bind what happens next.

**Over the cap means filed, not launched.** When the projection lands above what is
left of the ceiling you set, the run reaches you as a written proposal instead of as
a thing already in motion: what it would do, what it would cost, what a smaller
version would give up. Filing is the normal outcome of a projection that comes in
high. It is not a failure of the run and it should never read as one.

**Long runs do not launch into thin headroom.** If the projected wall-clock consumes
most of what is left in the current usage window, park the launch to the next window.
Crossing a window mid-fleet costs twice: once for the work that was interrupted, and
again for whatever a resume drags back through (section 6). The cheapest fleet you
will ever run is the one that started with room to finish.

**The projection is written down before the launch, not after.** It lands in
`ledgers/SPEND.md` as that ledger's own rule requires, and an unreconciled projection
sitting there from a previous run blocks the next launch of the same shape until it
is closed out.

**Gates and closure are budgeted separately from production.** A fleet whose envelope
covers only its writers has under-projected by the entire cost of making its output
trustworthy. Give the review lanes, the fix round, and the closure pass their own
line in the projection.

---

## 3. The budget guard, embedded in every fleet script

Projection is a promise made before the run. The guard is what keeps the promise
while the run is happening and nobody is watching the meter.

**Every fleet script carries a two-threshold guard. This is not optional, and a
script without one is not ready to launch.**

- **At 80% of the run's projection: warn.** The script logs one line naming what has
  been spent, what was projected, what the cap is, how many agents have launched, and
  how many remain. The run continues. The line exists so that the overage, if one is
  coming, is visible while there are still choices.
- **At 100% of the run's cap: stop launching.** No further agents are convened.
  In-flight agents are allowed to finish and write their files. The script writes its
  close-out record, files what exists, names the gap, and exits.

**Never retry into a wall.** When a run stops on a spend limit, the correct behaviour
is to stop, commit, and report. Retrying a run against a ceiling it has already hit
burns whatever is left of the budget on failures and buys nothing.

Keep the two numbers distinct in your head and in the script. **The projection is your
estimate; the cap is the ceiling you agreed the run may not cross.** They are usually
different, and the guard needs both: the first threshold is early warning against
your own estimate, the second is a hard floor under your money.

A harness-neutral shape:

```
spent      = running total this run has consumed
projection = the figure stated at launch
cap        = the ceiling this run may not cross
warned     = false

before launching each batch of agents:
    if spent >= cap:
        stop launching
        let in-flight agents finish and write their files
        write the close-out record, name the gap, exit GUARD-TRIPPED
    if spent >= 0.8 * projection and not warned:
        log: spent, projection, cap, launched so far, remaining
        warned = true
```

**A guard-tripped run is a success that ended early, and gets reported that way.** It
produced whatever it produced, it stopped where it said it would, and the remaining
work is a named gap that a small closure run can finish later for a known price. That
is the outcome this mechanism exists to produce. Treating it as a failure teaches the
next session to set the cap too high, which is the only way this rail can actually
break.

*Adapted pattern: the two-threshold guard follows Paperclip's tiered budget stop.
See `ATTRIBUTIONS.md`.*

---

## 4. Script-craft rules

Each rule is stated with the failure class it exists to prevent. They are hard rules:
embed them in every fleet script you write, and treat a script that skips one as
unfinished rather than as a stylistic variant.

1. **Work travels through files, not through returns.** Every lane writes its output
   to disk at the moment it has it, not at the end when it hands something back. An
   agent that dies mid-run must have already left its value behind. Returns are for
   short digests the orchestrator uses to sequence the next step; they are never the
   only copy of anything.

2. **No single agent's failure kills the run.** Every awaited call outside a managed
   group catches its own error and continues. A dead lane costs one log line and
   whatever it had not yet written. This rule is only survivable because of rule 1:
   the two are one design, not two preferences.

3. **Reasoning-tier calls return prose, not schema-constrained structure.** Strict
   output formats and the most capable tier are a poor pairing: the retries pile up,
   and a retry cap reached mid-run can take the whole script down with it. Keep
   structured returns on the lighter tiers, where they behave, and let the reasoning
   tier answer in plain text the orchestrator parses loosely or not at all.

4. **A writer's first move is inspection, and production is what happens after it.**
   Every writer prompt carries an instruction to this effect, in these words or your
   own:

   > Look at the target path before you produce anything. Where something is already
   > sitting there, your assignment changes shape: find each place the existing
   > content falls short of this brief, close those specific gaps, and leave whatever
   > already satisfies the brief untouched. Producing the file from nothing is the
   > exception, and it needs a reason you can state.

   The economics are why this is a hard rule rather than a preference. Checking a file
   that turns out to be sound costs a fraction of producing that same file a second
   time, and the second copy is no better than the first. On a resume, where much of
   the target set is usually fine already, this one instruction decides most of the
   bill.

5. **Pin the tier on every call.** Each agent's tier comes from `org/models.yml`,
   named explicitly at the call site, never inherited by accident. The interactive
   seat you sit with never appears in a fan-out at all: that rail is stated in
   `org/models.yml` and no script may quietly override it.

6. **Prefer a pipeline to a barrier.** Stage work so that each piece proceeds as soon
   as its own input exists, rather than gathering everything at a checkpoint. A
   barrier concentrates risk: if a window closes or a limit trips while many agents
   are waiting at one, they all die together, whereas a pipeline loses only what was
   moving.

7. **Say honestly what the run needs.** If a fleet writes to a path that exists only
   on your machine, or depends on a local tool or credential, the mission's `STATE.md`
   header says so plainly. A header that overstates portability wastes somebody's
   time later on a pickup that was never possible.

8. **Checkpoint while the fleet runs.** Commit output at material change points
   during the run, not at the end of it, per `ops/OPERABILITY.md`. Insurance this
   cheap is worth buying every time, and it is what turns an interrupted run into an
   inconvenience rather than a loss.

---

## 5. The review layer: two blind spots and one hazard

Checking a fleet's output is not one job. The first two rules below cover what
ordinary review does not detect at all; the third covers the damage review itself
causes on the way to fixing what it found. A fleet that hires generic reviewers and
hopes for all three gets none of them.

**Nobody recalculates a figure unless recalculating is somebody's stated assignment.**
Lanes reading for accuracy, for tone, or for coverage all treat a total on the page as
settled input and move past it. That is how a package ships carrying two figures that
cannot both be true: every pass saw them and no pass owned them. So write the
assignment into one lane's brief in plain terms, and make it arithmetic worked again
from the underlying inputs rather than a comparison of the copies against each other.
Two identical wrong totals agree with one another perfectly.

**A finding is a sample of a class, and somebody has to be given the class.** One
flagged sentence is evidence about how the whole package was written, which usually
means the same mistake is sitting in two or three places nobody quoted. The lane
following a gate therefore works from the category rather than from the citation list:
it searches everything for that kind of error and reports what its search covered, so
that turning up nothing is a result you can rely on instead of silence you have to
interpret.

**A repair brief draws the boundary of the edit, not only its target.** An instruction
naming just the defect leaves every surrounding sentence inside the fixer's
discretion, and discretion applied to a hedge somebody argued for once tends to
delete it. Name the material that has to come through the edit unchanged, and require
a report of anything altered outside the named target. Writing that report is the
cheap part; a caveat that quietly disappeared gets found later by whoever it was
protecting.

---

## 6. Landing the work: a session's output arrives as a change request

A fleet can rewrite more of this repository in ten minutes than you can read in an
hour. The rule that makes that safe is simple and it is structural rather than
procedural: **a session's work reaches your authoritative history as a reviewed change
you approve, never as a silent mutation you discover later.**

**The default mechanics, branch per session:**

1. The session opens a branch of its own at the start, named for the mission and the
   date, and does all of its work there.
2. Checkpoint commits land on that branch throughout the run, exactly as
   `ops/OPERABILITY.md` requires. The work is durable from the first checkpoint
   without being authoritative.
3. At close, the session writes a change summary: what changed and why, what it cost
   against its projection, what it deliberately did not do, and anything it is
   unsure about. Findings go in the summary, not in the merge message.
4. You read the diff and the summary, and you merge or you decline. **Merging is your
   act.** A session may prepare the request, explain it, and revise it. It does not
   land it.

The property worth naming: this separates durability from authority. Work is saved
continuously, so nothing is lost to an interruption, and yet nothing has become the
official record until you said so. Those two goals fight each other in a trunk-only
setup and stop fighting here.

**If you work trunk-only**, which is a reasonable choice for a solo operator on a
small repository, the same discipline still binds through show-before-save: the
session shows you what it intends to write, waits for your word, and writes only
then. Pick one mode deliberately and record which one you run in your rulings, so a
fresh session does not have to guess whether an uncommitted working tree is normal
here.

**What never lands in either mode:** anything from `vault/`, anything classed above
what your fork posture permits (`doctrine/CONSTITUTION-CORE.md`, section 5), and edits
to doctrine files nobody asked for. A change request containing any of the three is
declined as a whole rather than merged selectively.

*Adapted pattern: the branch-per-session landing mechanic follows Kortix / Suna's
isolated sessions and approved change requests. See `ATTRIBUTIONS.md`.*

---

## 7. Resume economics

Nothing survives the session that launched it. What survives is what reached the
disk. A resume therefore starts as an inventory, never as a re-launch.

**Inventory first, always.** Before deciding anything, list the mission's output
directories and mark every promised deliverable as absent, partial, or complete. Read
enough of each partial file to know which. This costs minutes and it decides
everything that follows.

**Then choose deliberately between two options, and the default is the smaller one.**

- **A closure fleet sized to the actual gap.** A short script convening only the
  agents the missing pieces need, briefed with what is already good on disk and
  carrying the inspect-first instruction from section 4. This is the right answer
  in most interruptions, and the gap between the two options is not small: a closure
  run aimed at a real gap routinely costs a fraction of what re-running the original
  script costs for the same remaining work.
- **A full re-run of the original script.** Correct when the specification itself
  changed, or when the existing output failed review on its merits rather than being
  merely incomplete.

**Why the arithmetic favours the closure fleet so heavily:** the discount that caching
gives you is positional. It attaches to the opening stretch of a conversation that has
not changed since the last time, counting forward from the very beginning, and the
first call that differs ends it. Everything the script does past that point is charged
at full rate. Restart an interrupted script and you therefore buy, a second time and
at full price, lanes that finished cleanly the first time and need no work at all. A
closure fleet never lands in that position, because the only thing in its context is
the gap.

**Write the resume protocol before you need it.** Any mission with a fleet in flight
carries, at the top of its `STATE.md`, what is running, what a resuming session must
verify on disk before touching anything, and what must never be re-run blindly. The
resume rule that matters most: a session that assumes work is unfinished and redoes it
wastes your money, and a session that assumes work is finished and skips it ships a
hole. Look before you choose.

---

## 8. Failure playbooks

Quick reference. Each entry is a class, not an anecdote.

| What happened | What is probably true | What to do |
|---|---|---|
| An agent died on repeated output-format failures | Its file is often already written; the write usually happens before the return does | Check the disk before assuming loss. Drop the strict format on that call per rule 3, convert the re-run into a verify-and-patch pass |
| A provider error interrupted a lane mid-response | Its file may be partial and its own checks never ran | Re-run that lane. Force any downstream writer that consumed the partial file to rebuild rather than trusting what it read |
| The usage window closed mid-fleet | Whatever reached the disk is intact; everything in flight is gone | Commit the tail, partials included. Write the handoff entry with the exact resume instruction. Wait out the reset, then run the section 7 inventory before choosing how to resume |
| The budget guard tripped | The run ended where it promised to | Report it as a success that ended early: what landed, what the gap is, what closing it would cost |
| Two sessions found the same mission | Both believe they own it; both are about to write | The session holding the live run keeps it. The other stands down loudly, in writing, rather than working quietly around it |

---

## 9. Closing out a run

Four things happen before the session that ran a fleet can park.

1. **Reconcile the meter.** The actual cost lands in `ledgers/SPEND.md` against the
   projection it was measured by.
2. **Attribute any overage in plain words.** Scope that grew, mechanics that misfired,
   a window that closed mid-run, a resume that re-paid for finished work. "It cost
   more than expected" restates the number rather than accounting for it. Where no
   honest account is available, the absence is itself what gets written up: money the
   run consumed for reasons nobody can name yet is precisely the material section 10
   collects, and it goes there marked unattributed rather than smoothed over with a
   plausible guess.
3. **Write the after-action note** into the owning seat's ledger, per
   `org/functions/agent-quality/CHARTER.md`: where the brief held up, where the brief
   and the agents pulled against each other, and one candidate change.
4. **File any friction row** the run produced, before the session closes. A row
   nobody wrote because the run ultimately succeeded is the most expensive kind of
   omission here, because the same friction is now guaranteed to arrive again at full
   price.

---

## 10. The friction log

*Append-only. Any session that hits fleet or process friction appends a row at close:
what happened, why it happened, what type of lesson it is, and what changed as a
result. The Chief of Staff surfaces open rows at the next Staff Meeting. **A row
closes only by amending a rule in this file, or by a recorded ruling that no change is
warranted.** That is the whole improvement loop: friction gets written down, gets
typed, and either changes a rule or gets explicitly declined. Nothing else bends this
org's operating cost downward instead of letting it repeat itself.*

### Lesson typing

Every closed row carries exactly one type, using the same three categories the Agent
Quality function applies to after-action findings
(`org/functions/agent-quality/CHARTER.md`), so a lesson means the same thing wherever
it is recorded:

- **Guard.** The remedy is a hard rule stopping this specific mistake from happening
  twice: a deterministic check, a gate, a clause closing the precise hole that opened.
  Repaired in place, here, by whoever writes the row.
- **Inoculate.** The remedy protects the whole class of mistake rather than the single
  occurrence: a pattern folded into the script template or into doctrine, so everyone
  working from it afterward is covered without per-script repetition.
- **Reveal.** The failure pointed at something this log has no business repairing: a
  capability nobody had named, work nobody had proposed, a hole in what the org offers
  rather than in how it runs. Nothing is repaired here. The lesson is written up as a
  short proposal and handed to `inbox/INNOVATION.md` for scoring on its next ordinary
  cycle. Never patched inline, never raised as an interrupt, and never quietly
  relabelled guard or inoculate because that would have been the faster thing to write
  down.

Getting the type right is worth more than getting the fix out fast. A reveal recorded
as a guard buys a rule nobody needed while the opportunity underneath goes nowhere. A
guard recorded as a reveal sends a five-minute edit through a scoring cycle for no
reason. Where a lesson genuinely straddles two types, write that down rather than
forcing the choice.

*Adapted pattern: typing a failure by the remedy it deserves follows AI Team OS's
failure handling. See `ATTRIBUTIONS.md`.*

### The log

| Date | Run | Friction | Root cause | Type | Outcome |
|---|---|---|---|---|---|
| | | | | | |

*No rows yet. This log stays empty and honest until your first fleet meets real
friction. The first row you write will be worth more than this entire file, because
it will be about your work rather than about fleets in general.*

---

## 11. Cross-references

- `doctrine/CONSTITUTION-CORE.md` - gate G1 and the approval doctrine every
  projection and every change request operates inside, plus the security classes that
  decide what may land at all.
- `ledgers/SPEND.md` - where the projection is written before launch and the actual is
  reconciled at close.
- `org/models.yml` - the tier map every agent call pins against, and the rail keeping
  your interactive seat out of fan-outs.
- `ops/OPERABILITY.md` - checkpoint commits, the park ritual, and what a session owes
  the next one.
- `ops/COLD_RESUME.md` - how a session with no memory works out where an interrupted
  fleet stopped.
- `org/STAFF_MEETING.md` - the ritual that produces the brief a fleet executes, and
  the adversarial pass that sharpens it while it is still one document.
- `org/functions/agent-quality/CHARTER.md` - the after-action note, and the lesson
  typing this log shares.
- `inbox/INNOVATION.md` - where reveal-typed lessons go.
- `EXTENDING.md` - the file classes, and how a doctrine improvement reaches a copy
  you are already running.
- `ATTRIBUTIONS.md` - the outside projects the adapted mechanics in this file came
  from, credited in one place.
