---
name: heartbeat
description: Before arming, disarming, or troubleshooting this template's one scheduled routine, or when asked how it works: arming preconditions, the resume-only cycle, the failure brake, the kill switch.
---

# Heartbeat - the one scheduled routine this product permits

This skill is the protocol CONSTITUTION-CORE.md's own gate on scheduled routines
requires to exist before any such routine may run: a spend projection, a brake that
trips after repeated failure, a kill switch, and a charter that is resumption only.

## 1. What this is, in one sentence

A resume-only scheduled routine that picks up work a session already started and
left running when it ended, and does nothing else. It never plans, decides,
originates a mission, or dreams. Nothing in flight when it wakes means it does
nothing, on purpose, every time.

This is the one narrow exception the no-daemons rule allows, earned by being
structurally unable to do anything a live session did not already authorize. Every
mission it touches was approved once already, in a session the operator was present
for; resuming it is not a second approval, it is finishing what the first one
already covered.

## 2. What it is not

- **Not an orchestrator.** It convenes nothing new — any agent it re-runs was
  already named in a resume protocol a live session wrote down.
- **Not the generative engine.** Dreaming stays hand-invoked, inside a session; this
  skill never schedules it, arms it, or substitutes for its own separate protocol.
- **Not a second chance to reconsider a plan.** A mission's resume instructions that
  look wrong by the time this routine reaches them get flagged and stopped, never
  improvised on.

## 3. Shipped disarmed

```
armed: false
per-cycle ceiling: [UNSET]
cycle marker: none
```

Two of these three lines belong to the operator; the routine writes the third.

- **`armed`** starts `false` and stays `false` until the operator changes it.
  Reading it is the routine's first act every cycle, before the guard in section 5;
  a schedule pointed at a disarmed routine produces no-op cycles by design.
- **`per-cycle ceiling`** is a figure the operator sets. A suggested figure, or one a
  session inferred, is not a ceiling — only a number the operator wrote counts.
  Left `[UNSET]`, treat it as already spent: nothing is measured, so nothing runs.
- **`cycle marker`** is the one line the routine writes itself: `none` when no cycle
  is mid-flight, a timestamp when one is. Section 5 covers how it is used.

This block is the one exception to "ops files are upstream's to improve, not the
operator's to hand-edit," safe because any doctrine update lands through an
operator-reviewed merge, never a blind overwrite, which is where these three
operator-set values survive the merge.

## 4. Arming it, in order

Three things must be true, all requiring the operator's own act — no session may
satisfy any on the operator's behalf.

1. **A schedule exists, exactly once**, whatever the mechanism, and the operator is
   the one who stood it up. Two schedules aimed at it races itself before it has
   ever met a live session to race.
2. **The ceiling in section 3 is a real number** the operator chose, not a
   placeholder or a session's suggestion.
3. **The kill switch has been watched working.** Before the first unattended cycle,
   the operator sets `armed` to `false` and confirms the next cycle does nothing.
   An untested kill switch is prose, not a control.

Only once all three hold does `armed: true` mean what it says.

A scheduled wake — anything that brings a session back on its own, with no person or
peer message triggering it — is a scheduled run in every sense, needing the
operator's word before it exists like any other spend-class decision; arming this
routine at all *is* that word. Never let a resume plan depend on one running session
alone — build a second, independent path.

## 5. The cycle, start to finish

Every firing runs this in order and stops at the first step that says stop.

1. Read this skill. If `armed` isn't `true`, exit immediately.
2. Check `cycle marker`. A timestamp younger than one scheduling interval means a
   prior firing is plausibly still running: exit silently, touch nothing, and never
   queue the skipped firing — the work is still sitting in the repository.
3. Scan every mission's `STATE.md` header (section 7) for eligible ones. None
   eligible: write `cycle marker` back to `none` and exit.
4. Set `cycle marker` to now and commit that one line first — the cheapest commit
   the routine makes, so the next firing or a mid-cycle live session has something
   to check before assuming the coast is clear.
5. For each eligible mission, project cost and time before touching it. A
   projection above what remains of the ceiling means: don't touch it, file the
   projection on `registers/BLOCKED_ON_OPERATOR.md` naming the mission and
   estimate, move on. A filed projection is the cycle working as intended.
6. Follow that mission's own resume protocol exactly. Every gate binding the
   original live session binds this cycle identically: nothing sent, nothing
   deployed, nothing written into a repository this product doesn't own, nothing
   sensitive read. The resume protocol is the whole extent of what was approved,
   not raw material to improve on.
7. Commit whatever the resume produced with the required attribution trailer,
   update that mission's header to match reality, log actual cost against
   projection in `ledgers/SPEND.md`, and write `cycle marker` back to `none` in the
   same commit. Touch `HANDOFF.md` too if it's material enough to need saying first.

## 6. Why the marker exists, said plainly

Routines built exactly this way have collided with a live session mid-task on the
same work in real operation — this is not theoretical caution. Read reference.md
before ever treating that guard as safe to trim.

## 7. Eligibility belongs to the mission, not to this routine

This routine never decides for itself which missions it may touch — each mission
declares that on its own behalf, in its own `STATE.md` header. See
skill:checkpoint-discipline for the base header contract (`status`, `needs-local`,
`last-checkpoint`); this routine layers two more lines on top:

```
heartbeat: eligible | suspended | not-eligible
heartbeat-attempts: <count, reset by any human session>
```

A mission missing these two lines is treated as `not-eligible`. **Actionable**
means `status: in-flight`, `needs-local: no`, and `heartbeat: eligible` all hold at
once; missing any one, this routine leaves that mission alone.

`needs-local` carries extra weight here: a mission needing something local (a path,
a credential, a machine-bound tool) is invisible to a cloud-run schedule by
construction. This routine's job with one is to say so loudly — file a row on
`registers/BLOCKED_ON_OPERATOR.md` naming the local-session need — never to skip it
silently.

## 8. The failure brake

Two consecutive failed resume attempts on the same mission and this routine stops
trying it. `heartbeat-attempts` counts the run: increment on failure, and at two,
set `heartbeat: suspended`, file a `registers/BLOCKED_ON_OPERATOR.md` row naming
what failed and how many times, and leave it untouched until a human resets the
counter. Suspension scopes to that one mission only.

Never retry into a spend wall: a usage or spend-limit error mid-resume stops
everything for that cycle, gets filed, and is never retried that cycle or the next.
Hitting a wall twice only spends a second failure on top of the first.

## 9. The gates travel with every cycle unchanged

Nothing about a schedule loosens what this product's constitution already binds a
live session to:

- **G1 Spend** — bounded by section 3's ceiling and section 5 step 5's projection.
- **G2 Foreign repositories** — no write beyond a path a mission's own ruling
  already opened (in practice, an already-open pull request).
- **G3 External communication** — nothing sends; sending isn't implemented at all.
- **G4 Deploys** — nothing deploys, same reason.
- **G5 Sensitive material** — every read stays inside whatever security-class
  boundary this product enforces for a given clone or sandbox.

Whichever tier plays the operator's own hands-on, interactive role never runs
unattended inside this routine, same as any other unattended run in this product.

## 10. The kill switch

Set `armed` back to `false`. The effect is immediate and unconditional: the next
cycle to read it exits at step 1 of section 5, touching nothing. Pausing or
deleting the schedule itself is a second, fully independent path to the same
result — either alone suffices.

This routine holds no connectors of its own to mail, payment, or any third-party
account, by design — a resume-only routine has no legitimate use for a send
surface. If a platform ever attaches account connectors to routines by default,
strip them before the next cycle: something that could theoretically send no longer
needs to malfunction to become a G3 problem, it only needs to be asked.

Source: ops/HEARTBEAT.md §1-5, §7-10; ops/MULTI-SESSION.md §8 (moved into this skill 2026-09-16)
