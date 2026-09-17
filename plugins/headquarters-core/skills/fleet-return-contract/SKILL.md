---
name: fleet-return-contract
description: Landing a fleet's output or closing out a run: the budget guard embedded in the script, the branch-or-trunk landing mechanic, the close-out obligations.
---

A fleet is a single session, one script, many agents. This skill is the contract
that governs three moments in that shape's lifecycle: the guard every fleet script
must carry so it cannot overspend unnoticed, the mechanic by which a fleet's output
becomes an authoritative change rather than a silent mutation, and the obligations
a session owes before it can park having run one.

## The budget guard, embedded in every fleet script

Projection is a promise made before the run. The guard is what keeps the promise
while the run is happening and nobody is watching the meter.

**Every fleet script carries a two-threshold guard. This is not optional, and a
script without one is not ready to launch.**

- **At 80% of the run's projection: warn.** The script logs one line naming what has
  been spent, what was projected, the agent-count cap, how many agents have
  launched, and how many remain. The run continues. The line exists so that the
  overage, if one is coming, is visible while there are still choices.
- **At the agent-count cap: stop launching.** No further agents are convened.
  In-flight agents are allowed to finish and write their files. The script writes its
  close-out record, files what exists, names the gap, and exits.

**Why the second threshold counts agents, not spend.** A harness's own running
"spent" figure typically counts generated output tokens only, and can silently miss
the cache-write and input cost that dominates the real bill. A guard set purely
against that figure can look fine while the real spend has already passed the cap.
Make the second threshold a hard cap on the number of agents this run may convene
instead: a count is exact where a live cost figure is not.

**Keep the counter run-local.** If the counter has to read from a pool shared with
other concurrent runs, subtract that pool's already-spent carry-in at launch, so a
run never inherits another run's convened agents as its own. Before launching, check
that the environment is not already carrying another run: one fan-out at a time is
far easier to hold inside a budget than several running in parallel, even when each
one looks reasonable alone.

**Never retry into a wall.** When a run stops on a spend limit, the correct behaviour
is to stop, commit, and report. Retrying a run against a ceiling it has already hit
burns whatever is left of the budget on failures and buys nothing.

Keep the two numbers distinct in your head and in the script. **The projection is your
estimate; the agent-count cap is the ceiling you agreed the run may not cross.** They
are usually different, and the guard needs both: the first threshold is early warning
against your own estimate, the second is a hard floor under your money.

A harness-neutral shape:

```
spent        = running total this run has consumed (output tokens; a lower bound)
projection   = the figure stated at launch
agents_cap   = the maximum agents this run may convene, net of any shared-pool carry-in
agents_count = agents convened so far this run, tracked run-local
warned       = false

before launching each batch of agents:
    if agents_count >= agents_cap:
        stop launching
        let in-flight agents finish and write their files
        write the close-out record, name the gap, exit GUARD-TRIPPED
    if spent >= 0.8 * projection and not warned:
        log: spent, projection, agents_cap, agents_count, remaining
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

## Landing the work: a session's output arrives as a change request

A fleet can rewrite more of a repository in ten minutes than a person can read in an
hour. The rule that makes that safe is simple and it is structural rather than
procedural: **a session's work reaches the authoritative history as a reviewed change
the operator approves, never as a silent mutation discovered later.**

**The default mechanics, branch per session:**

1. The session opens a branch of its own at the start, named for the mission and the
   date, and does all of its work there.
2. Checkpoint commits land on that branch throughout the run, exactly as
   `ops/OPERABILITY.md` requires. The work is durable from the first checkpoint
   without being authoritative.
3. At close, the session writes a change summary: what changed and why, what it cost
   against its projection, what it deliberately did not do, and anything it is
   unsure about. Findings go in the summary, not in the merge message.
4. The operator reads the diff and the summary, and merges or declines. **Merging is
   the operator's act.** A session may prepare the request, explain it, and revise
   it. It does not land it.

The property worth naming: this separates durability from authority. Work is saved
continuously, so nothing is lost to an interruption, and yet nothing has become the
official record until the operator said so. Those two goals fight each other in a
trunk-only setup and stop fighting here.

**Batch what ships together.** When several small, individually approved changes
are meant to land together, test them once against the exact combined result, and
write one release line and one rollback line for the batch. Piecemeal partial
releases multiply risk and blur the rollback story.

**If the operator works trunk-only**, which is a reasonable choice for a solo
operator on a small repository, the same discipline still binds through
show-before-save: the session shows the operator what it intends to write, waits for
their word, and writes only then. Pick one mode deliberately and record which one is
run in the operator's rulings, so a fresh session does not have to guess whether an
uncommitted working tree is normal here.

**What never lands in either mode:** anything from `vault/`, anything classed above
what the fork's posture permits (`doctrine/CONSTITUTION-CORE.md`, section 5), and
edits to doctrine files nobody asked for. A change request containing any of the
three is declined as a whole rather than merged selectively.

*Adapted pattern: the branch-per-session landing mechanic follows Kortix / Suna's
isolated sessions and approved change requests. See `ATTRIBUTIONS.md`.*

## Closing out a run

Four things happen before the session that ran a fleet can park.

1. **Reconcile the meter.** The actual cost lands in `ledgers/SPEND.md` against the
   projection it was measured by.
2. **Attribute any overage in plain words.** Scope that grew, mechanics that
   misfired, a window that closed mid-run, a resume that re-paid for finished work.
   "It cost more than expected" restates the number rather than accounting for it.
   Where no honest account is available, the absence is itself what gets written up:
   money the run consumed for reasons nobody can name yet is precisely the material
   the friction log collects (see reference.md), and it goes there marked
   unattributed rather than smoothed over with a plausible guess.
3. **Write the after-action note** into the owning seat's ledger, per
   `org/functions/agent-quality/CHARTER.md`: where the brief held up, where the brief
   and the agents pulled against each other, and one candidate change.
4. **File any friction row** the run produced, before the session closes. A row
   nobody wrote because the run ultimately succeeded is the most expensive kind of
   omission here, because the same friction is now guaranteed to arrive again at full
   price. Read reference.md for the friction-log ritual itself: when to log mid-task
   friction instead of stopping to fix it, and how a row closes.
5. **Report a lane's status only from its landed return.** Never narrate an
   expected shape or a likely outcome before the actual result is in hand, even when
   a guess later turns out right. Label anything not yet received as unmeasured.
6. **Hand off commits the moment the session's own shell degrades.** The moment a
   session detects its own tool or shell layer failing, it writes a clear handoff
   record immediately: the exact commands, their order, and who is meant to run
   them. Durable-state discipline extends to the commit act itself, not only to
   file writes.
7. **Track tier savings as an auditable deliverable.** Report actual spend by tier
   alongside a stated counterfactual: what an all-reasoning-tier run would have
   cost, with its assumptions named. A savings claim should be checkable, not
   asserted.
8. **Compare like units when comparing runs.** A harness's reported usage figure
   for a run is often dominated by cache-write input, not generated output.
   Compare the same unit of measurement across runs and periods, and keep an
   independent tally from the transcript records themselves rather than trusting one
   dashboard's own weighting.

Source: ops/FLEET_CRAFT.md §3 §6 §9 §10 (moved into this skill 2026-09-16)
