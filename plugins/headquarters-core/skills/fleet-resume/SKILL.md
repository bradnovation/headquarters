---
name: fleet-resume
description: Use when resuming after a wall or a found failure mid-fleet: disk inventory first, closure-fleet-vs-full-rerun economics, the six-row failure-class table.
---

# Fleet resume

This skill governs how a fleet's resume is priced and chosen, and how to react to
the specific ways a fleet run goes wrong.

## Resume economics

Nothing survives the session that launched it. What survives is what reached the
disk. A resume therefore starts as an inventory, never as a re-launch.

**Inventory first, always.** Before deciding anything, list the mission's output
directories and mark every promised deliverable as absent, partial, or complete. Read
enough of each partial file to know which. This costs minutes and it decides
everything that follows.

**Then choose deliberately between two options, and the default is the smaller one.**

- **A closure fleet sized to the actual gap.** A short script convening only the
  agents the missing pieces need, briefed with what is already good on disk and
  carrying the inspect-first instruction from the fleet-brief skill. This is the
  right answer in most interruptions, and the gap between the two options is not
  small: a closure run aimed at a real gap routinely costs a fraction of what
  re-running the original script costs for the same remaining work.
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

## Failure playbooks

Quick reference. Each entry is a class, not an anecdote.

| What happened | What is probably true | What to do |
|---|---|---|
| An agent died on repeated output-format failures | Its file is often already written; the write usually happens before the return does | Check the disk before assuming loss. Drop the strict format on that call per the fleet-brief skill's rule 3, convert the re-run into a verify-and-patch pass |
| A provider error interrupted a lane mid-response | Its file may be partial and its own checks never ran | Re-run that lane. Force any downstream writer that consumed the partial file to rebuild rather than trusting what it read |
| The usage window closed mid-fleet | Whatever reached the disk is intact; everything in flight is gone | Commit the tail, partials included. Write the handoff entry with the exact resume instruction. Wait out the reset, then run the inventory-first step above before choosing how to resume |
| The budget guard tripped | The run ended where it promised to | Report it as a success that ended early: what landed, what the gap is, what closing it would cost |
| Two sessions found the same mission | Both believe they own it; both are about to write | The session holding the live run keeps it. The other stands down loudly, in writing, rather than working quietly around it. (Fuller collision-handling mechanism: the multi-session skill's stand-down rule.) |
| A file another process is still actively writing needs restoring | A generic revert can silently discard that other process's own in-progress work along with what you meant to undo | Restore from an explicit snapshot you made yourself, never from a generic revert command |

Source: ops/FLEET_CRAFT.md §7 Resume economics | §8 Failure playbooks (moved into this skill 2026-09-16)
