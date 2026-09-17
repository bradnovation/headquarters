---
name: fleet-sizing
description: Before any fan-out launches: say the three numbers aloud (tokens, wall-clock, meter reading, boost line), and test whether a fleet is even the right shape.
---

This skill is the sizing gate that runs before a fleet is convened: the test for
whether fanning out is even the right shape for the work, and the numbers that must
be said aloud - refusably - before any agent launches.

## What a fleet is, and when one is the wrong shape

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

**A good composition beats a good prompt.** For open-ended synthesis work, convene
distinct roles rather than one generic pass repeated: a context-gatherer, several
independent drafters each working a different angle, one or more judges checking
different concerns, and one assembler. This shape consistently outperforms a single
linear pipeline running the same total number of agents.

## The three numbers, stated before any launch

No fleet launches until four figures have been said out loud, at the launch moment,
in a form you can refuse.

**The building tier is the default that figure one is built on.** Builders,
drafters, researchers, verifiers, and judges all run at the building tier unless a
role is explicitly boosted. The reasoning tier costs roughly five times as much per
token, so a fleet whose roles get pinned up piece by piece can burn a week's meter
in two days with no more work actually done.

1. **Projected tokens.** Derived, not asserted: agents multiplied by expected passes
   multiplied by expected output size per agent, plus the orchestrator's own
   overhead, plus the review lanes. Show the arithmetic. A bare number reads to you
   as an estimate when it is frequently a wish. For build work with a visual or
   exploratory shape, add roughly half again to the bottom-up estimate, and reserve
   part of the projection for a final walkthrough pass after the last unit lands.
2. **Projected wall-clock.** How long the run will occupy the session, end to end,
   including the gate and closure work.
3. **Your meter position, read fresh.** Whatever your plan and harness expose as
   remaining usage, read at the launch moment. A remembered reading from earlier in
   the session is not a reading.
4. **The boost line.** Say out loud, before launch, whether this run wants anything
   above the default tier. "No roles above building" is a complete answer by
   itself; wanting more means naming which role, why building would not hold up
   there, and what the jump costs relative to staying put. Silence is not a yes -
   you have to actually say the word, every time, and a blanket yes for a
   recurring category of work only counts once it is written down as a ruling
   rather than remembered as "we always do it that way."

**The notify rule.** A session can reach the middle of a run and start to suspect
the tier underneath it is the wrong one for what just showed up - two failed
attempts at the bar from a building-tier unit, or a turn toward something in
counsel, architecture, money, privacy, or a review where getting it wrong is
costly. That suspicion goes to you, with the reasoning and the price gap laid out,
rather than getting resolved quietly in either direction by whichever agent had the
thought. Nobody is present to ask in an unattended run, so the concern gets logged
and the work stays put at building until a person looks at it.

**Effort is set per stage, not uniformly across a plan.** Keep effort lower for
routine extraction and drafting; reserve higher effort for synthesis, adversarial
review, judging, and final verification, where the real judgment work concentrates.

**Any multi-agent launch is a fleet.** A run counts as a full fleet under this
doctrine the moment it convenes more than one agent, even when it is framed
informally as "just a quick investigation." It gets the same projection and the
same guard.

**One probe before a fan-out hits one target.** Before sending several lanes at the
same external site or service, run a single cheap access probe first. Share what it
finds, the working approach or the block, with every lane. Otherwise each lane
burns its own effort rediscovering the same wall.

**Review bandwidth is usually the real bottleneck.** In a pipeline that includes
automated review, the limit is normally how much a checker can get through, not how
fast lanes can generate. Tune a build for review capacity first.

**Adversarial review is often the largest line in the budget.** Independent
verification passes, refutation rounds, and re-verification after fixes routinely
cost as much as the original work, sometimes more. Project for that honestly rather
than treating it as a rounding error.

**Watch for tier drift, not just totals.** A sudden spend spike is often driven by
which tier delegated work happens to run on, not by any real change in the work
itself. When you see a spike, check whether the shape of the work changed or only
the per-unit price did. Treat an expensive tier that has quietly become the default
for a whole class of work as policy drift worth correcting, even when each
individual escalation had a reason at the time.

Then four rules bind what happens next.

**Over the cap means filed, not launched.** When the projection lands above what is
left of the ceiling you set, the run reaches you as a written proposal instead of as
a thing already in motion: what it would do, what it would cost, what a smaller
version would give up. Filing is the normal outcome of a projection that comes in
high. It is not a failure of the run and it should never read as one.

**Long runs do not launch into thin headroom.** If the projected wall-clock consumes
most of what is left in the current usage window, park the launch to the next window.
Crossing a window mid-fleet costs twice: once for the work that was interrupted, and
again for whatever a resume drags back through. The cheapest fleet you
will ever run is the one that started with room to finish.

**The projection is written down before the launch, not after.** It lands in
`ledgers/SPEND.md` as that ledger's own rule requires, and an unreconciled projection
sitting there from a previous run blocks the next launch of the same shape until it
is closed out.

**Gates and closure are budgeted separately from production.** A fleet whose envelope
covers only its writers has under-projected by the entire cost of making its output
trustworthy. Give the review lanes, the fix round, and the closure pass their own
line in the projection.

## A plan nobody attacked is a guess with formatting on it

Before a fleet of agents is pointed at anything, the work in front of them gets
examined: what is genuinely required, what is already true, what the run will cost.
That examination is itself proposed, with its own estimated cost stated, and it is
refusable like everything else.

This belongs in the constitution rather than in a style guide because skipping it
does not produce a faster staff with rougher edges. It produces a staff that is
confidently wrong at speed and at scale, which is worse than having no staff at all.

Source: ops/FLEET_CRAFT.md §1 What a fleet is | §2 The three numbers, doctrine/CONSTITUTION-CORE.md § A plan nobody attacked is a guess with formatting on it (moved into this skill 2026-09-16)
