# HEARTBEAT - the one scheduled routine this product permits
<!-- file-class: DOCTRINE -->

*This file is the protocol document `doctrine/CONSTITUTION-CORE.md` section 6
promises before any scheduled routine may exist: a spend projection, a brake
that trips after repeated failure, a switch that kills it outright, and a
charter that is resumption only. Everything a scheduled routine in this
product may ever do lives here, in one place, so "did we write the rules
down before turning it on" never has to be asked twice.*

---

## 1. What this is, in one sentence

A resume-only scheduled routine that picks up work a session already started
and left running when it ended, and does nothing else. It does not plan, it
does not decide, it does not originate a mission, and it never dreams. If
nothing is in flight when it wakes up, it does nothing, on purpose, every
single time it finds that to be true.

This is the one narrow exception the no-daemons rule allows, and it earns
that exception by being structurally unable to do anything a live session
did not already authorize. Everything this routine ever touches was
approved once already, in a session the operator was present for. Resuming
that work is not a second approval; it is finishing a thing the first
approval already covered.

## 2. What it is not

Worth stating in the negative, because a scheduler invites scope creep by
default, one small convenience at a time.

- **Not an orchestrator.** It convenes nothing new. Any agent it causes to
  run again was already named in a resume protocol a live session wrote
  down before that session ended.
- **Not the generative engine.** Wherever this product's dreaming capability
  lives, it is invoked by hand, inside a session, and stays that way. This
  file does not schedule dreaming, arm it, or stand in for whatever separate
  protocol dreaming would need if it were ever put on a clock. That is a
  different decision, for a different day, ruled on its own.
- **Not a second chance to reconsider a plan.** If a mission's own resume
  instructions look wrong by the time this routine reaches them, it does
  not improvise a fix. It flags the mismatch and stops, exactly as any
  session in this product would when it finds itself about to act past
  what was actually approved.

## 3. Shipped disarmed

```
armed: false
per-cycle ceiling: [UNSET]
cycle marker: none
```

That block sits at the top of this file, in plain sight, the first thing
anyone opening it sees. Two of its three lines belong to the operator; the
third the routine writes to itself.

- **`armed`** starts `false` and stays `false` until the operator changes
  it. While it reads `false`, the honest answer to "is anything running on
  a schedule" is no, regardless of whether a schedule mechanism has been
  wired up underneath it. Reading this line is the routine's own first act
  every cycle, before anything else, including the guard in section 5; a
  schedule pointed at a disarmed routine produces cycles that do nothing,
  which is the safe failure and exactly the design intent.
- **`per-cycle ceiling`** is a token or spend figure the operator sets, the
  same discipline a dream-run cap follows elsewhere in this product: a
  suggested figure is not a ceiling, a figure a session inferred from
  context is not a ceiling, only a number the operator actually wrote
  counts as one. Left at `[UNSET]`, treat the ceiling as already spent:
  nothing gets measured against it, so nothing clears it, so nothing runs.
- **`cycle marker`** is the one line here the routine writes itself rather
  than the operator. It reads `none` when no cycle is mid-flight and a
  timestamp when one is; section 5 explains exactly how it gets used.

Every other file under `ops/` is upstream's to improve and not the
operator's to hand-edit, and ordinarily that rule would apply here too.
This block is the deliberate exception, and it is safe to make one because
`EXTENDING.md` already requires any doctrine update to land through a merge
the operator reviews personally, never a blind overwrite. That review is
where the operator's own values on these three lines get carried forward,
the same way any other hand-customized line would survive a merge done by
a person rather than a script. An upstream change that actually touches
what this block means will say so in its own diff; a change that leaves
this section alone changes nothing the operator set here.

## 4. Arming it, in order

Three things have to be true, and all three require the operator's own
act. No session may satisfy any of them on the operator's behalf.

1. **A schedule exists, exactly once.** This doctrine does not care whether
   the underlying mechanism is a cron entry, a scheduled cloud routine, or
   whatever the operator's own harness calls a recurring job. It cares only
   that one such schedule points at this routine and that the operator is
   the one who stood it up. A routine with two schedules aimed at it is
   racing itself before it has ever met a live session to race.
2. **The ceiling in section 3 is a real number.** Not a placeholder, not a
   figure a session suggested, a number the operator chose and is
   prepared to occasionally be wrong about.
3. **The kill switch has been watched working.** Before the first
   unattended cycle runs for real, the operator sets `armed` to `false`
   and confirms the very next cycle does nothing at all. An untested kill
   switch is a line of prose, not a control.

Only once all three hold does setting `armed: true` mean what it says.

## 5. The cycle, start to finish

Every firing of the schedule runs this sequence, in this order, and stops
at the first step that says stop.

1. **Read this file. If `armed` does not read `true`, exit immediately.**
2. **Check `cycle marker`.** A timestamp younger than one scheduling
   interval means a prior firing is plausibly still working; exit
   silently, touching nothing else. Never queue the skipped firing for
   later. A skipped cycle is correct behavior, because the work it would
   have picked up is still sitting in the repository, waiting for whichever
   cycle actually reaches it.
3. **Scan every mission's `STATE.md` header** (section 7 below) for ones
   declaring themselves eligible. Nothing eligible means nothing to do:
   write `cycle marker` back to `none` and exit. A no-op cycle should cost
   close to nothing, and proving that is exactly what this product's
   self-test discipline elsewhere is for.
4. **Set `cycle marker` to now, and commit that one line before anything
   else.** This is the cheapest commit the routine ever makes, and it
   exists only so the next firing, or a live session that starts mid-cycle,
   has something to check before assuming the coast is clear.
5. **For each eligible mission, project before touching it.** State what
   resuming it would cost and how long it would take, the same two figures
   any fan-out in this product states before launching. A projection above
   what remains of the ceiling in section 3 means that mission is not
   touched: file the projection on `registers/BLOCKED_ON_OPERATOR.md`
   instead, naming the mission and the estimate, and move to the next one.
   A filed projection is not a failure of the cycle. It is the cycle doing
   exactly what it is supposed to do.
6. **Follow that mission's own resume protocol, exactly as written.**
   Every gate that bound the live session that started this work binds
   this cycle identically: nothing sent, nothing deployed, nothing written
   into a repository this product does not own, nothing sensitive read.
   A resume protocol is not raw material for the routine to improve on; it
   is the whole extent of what was already approved.
7. **Commit whatever the resume produced**, carrying the attribution
   trailer `ops/OPERABILITY.md` requires of every checkpoint commit, then
   update that mission's header to match reality and log the actual
   cost against its projection in `ledgers/SPEND.md`, the same as any
   other run in this product. Write `cycle marker` back to `none` in that
   same commit. Touch `HANDOFF.md` too, if what happened is material
   enough that the next person to open this repository needs to hear it
   before anything else.

## 6. Why the marker exists, said plainly

None of the above is theoretical caution dressed up as procedure. Routines
built exactly this way, resume-only and running on a clock, have in real
operation fired while a live session was already mid-task on the very same
piece of work, and the two runs collided: duplicate output, a commit
history that briefly disagreed with itself, spend that should have counted
once counted twice. That is not a scenario this document is guessing might
someday happen. It is the entire reason the marker in section 3 exists, the
entire reason it gets checked before anything else in the cycle runs, and
the entire reason this file ships with `armed: false` rather than shipping
ready to fire and trusting everyone to remember to turn it off.

A routine that has never once been allowed to race a live session has never
had occasion to prove its guard actually works. Read that as a reason to
keep the guard exactly as strict as it is, never as a reason it has earned
the right to be trimmed.

## 7. Eligibility belongs to the mission, not to this routine

This routine never decides for itself which missions it may touch. Each
mission declares that on its own behalf, in its own `STATE.md` header,
extending the base header `ops/OPERABILITY.md` already defines for every
mission in this product:

```
status: proposed | ruled | in-flight | review | sealed
needs-local: yes | no
last-checkpoint: <what completed, and the file that proves it>
heartbeat: eligible | suspended | not-eligible
heartbeat-attempts: <count, reset by any human session>
```

The first three lines are the base contract every mission already carries.
The last two are what this file adds, and a mission that never adds them at
all is treated as `not-eligible`, exactly as if it had written the word out.
**Actionable** means `status: in-flight`, `needs-local: no`, and
`heartbeat: eligible` all hold at the same moment. Missing any one of the
three, this routine leaves that mission alone.

`needs-local` carries more weight here than almost anywhere else it
appears. A mission that can only run against something local (a path, a
credential, a tool that exists on one machine and nowhere else) is
invisible to a cloud-run schedule by construction, and pretending
otherwise is how work quietly stalls without anyone noticing. This
routine's entire job with a mission shaped that way is to say so loudly:
file a row on `registers/BLOCKED_ON_OPERATOR.md` noting plainly that a
local session is what the mission actually needs, rather than silently
skipping it and leaving the gap for someone to eventually stumble onto.

## 8. The failure brake

**Two consecutive failed resume attempts on the same mission, and this
routine stops trying that mission.** `heartbeat-attempts` in its header
counts the run: increment it on a failed attempt, and the moment it
reaches two, set `heartbeat: suspended`, file a row on
`registers/BLOCKED_ON_OPERATOR.md` naming what failed and how many times,
and leave that mission untouched until a human session resets the
counter. Suspension is scoped to the one mission; a failure on one mission
never changes another mission's eligibility.

Never retry into a spend wall. If a cycle hits a usage or spend-limit error
partway through a mission's resume, it stops everything it is doing right
then, files what happened, and does not attempt that mission again this
cycle or the next. A wall does not move because it gets hit twice; hitting
it twice only spends a second failure on top of the first.

## 9. The gates travel with every cycle unchanged

Nothing about running on a schedule loosens anything this product's
constitution already binds a live session to.

Spend stays bounded by the ceiling in section 3 and the projection in
section 5's fifth step; nothing here authorizes spend a human has not
already agreed to in some form. Nothing this routine does writes into a
repository this product does not own beyond whatever path a mission's own
ruling already opened, which in practice means an open pull request already
provided for, never a direct write to a branch belonging to someone else.
Nothing sends, because sending is not implemented anywhere in this
product, on a schedule or off one. Nothing deploys, for the identical
reason. And every read this routine performs stays inside public and
internal-business material: wherever this product enforces its own
security classes by keeping a sensitive directory physically absent from a
given clone or sandbox, this routine inherits that same absence rather
than being trusted to steer around the material on its own judgment.

Whichever tier plays the operator's own hands-on, interactive role in a
given setup never runs inside this routine, the same rule the constitution
states for every unattended run in this product. This routine is built to
be correct at the tier an ordinary working day already runs on; it assumes
nothing more capable is standing over it, because by definition nothing is
standing over it at all while it runs.

## 10. The kill switch

Set `armed` back to `false`. Any session capable of reading this file is
capable of writing that one word, and the effect is immediate and
unconditional: the very next cycle to read it, whenever the schedule next
fires, exits at step 1 of section 5 and touches nothing. Pausing or
deleting the schedule itself, at whatever level the operator's own
platform manages that, is a second and fully independent path to the same
result. Either one alone is sufficient; neither depends on the other
working correctly.

This routine holds no connectors of its own, to outbound mail, to payment,
to any third-party account, by design. A resume-only routine has no
legitimate use for a send surface, so none is wired to it in the first
place. If whatever platform runs the schedule ever attaches account
connectors to routines by default, strip them from this one before its
next cycle runs. A routine that could theoretically send something no
longer needs to malfunction to become a problem under gate G3; it only
needs to be asked.
