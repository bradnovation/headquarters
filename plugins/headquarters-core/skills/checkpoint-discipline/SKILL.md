---
name: checkpoint-discipline
description: Any point mid-session where state could fail to survive an interruption: capture at the material change, one commit per unit with the trailer, the STATE.md header.
---

# Checkpoint Discipline

A session's own memory can end without warning, at any point, not only at a close it
chose. Repo state is the only thing a later session, or a stranger, can trust, and
this skill is the mechanism that keeps that state trustworthy: when to capture
(section 2), how a commit records it (section 3), and the machine-readable header
that lets work in flight survive an interruption cleanly (section 4). Deciding
*whether a session should stop and park at all* is a separate question answered
elsewhere; this skill is what any checkpoint, planned or forced, is made of.

## 2. Durability is continuous, not something you do at the end

The instinct is to work all session and tidy up at the close. That instinct fails on
the exact sessions where tidying matters most: the ones that get cut short.

The rule: **capture at material change points, not at the end.** A material change
point is any moment where the picture of reality changed and losing that change would
cost real work to rebuild.

- A ruling landed.
- A plan was approved.
- A phase completed and produced a file.
- A finding was discovered that changes what happens next.
- A spend was authorised, or a run reconciled.
- Something failed in a way a later session must not repeat.

At each one: write the file, then commit it. Not "note it and commit at close."
Between the change and the commit, the change exists only in a context window, and
context windows do not survive anything.

Five corollaries worth stating plainly:

- **Write evidence at the moment of capture.** A number, a filename, a quote recorded
  when you had it in front of you is worth more than the same thing recalled an hour
  later. Reconstructed detail is where fabrication creeps in.
- **Nothing you launch outlives the session that launched it.** A fan-out, a long
  build, a watcher left going: when the session ends, so does it, and what you are left
  holding is whatever it managed to put on disk before that moment. Everything else it
  knew is simply gone. This is why a later session can pick the thread up at all, and
  why nothing here is permitted to hold state that the files do not hold too.
- **A fact discovered mid-task that would change a higher-level decision gets
  promoted into the top-level status record the same session it is found.** Never
  leave it buried in a sub-task's own notes for a later reader to rediscover by
  chance.
- **An ask sent through someone's personal channel rather than a shared inbox still
  needs a register or ledger line watching for its reply**, the same as any other
  tracked send. Otherwise silence goes stale unnoticed instead of getting caught.
- **As a session's own context fills up mid-task, checkpoint proactively because of
  that pressure specifically**, not only at the material change points a task's own
  milestones define. Treat compaction, when it happens, as a signal to re-read live
  state files rather than trust compacted memory of what was in progress.

## 3. Checkpoint commits

**One commit per unit of work.** Not one per session, not one per day. A unit of work
is something a later reader would want to see land, revert, or point at on its own.

Every commit that lands org work carries a trailer identifying what executed it:

```
Executed-By: <the model or tier that did the work>
Session: <session identifier or link>
```

The point is not ceremony. It makes the ledger of who-did-what into the commit history
itself, auditable without a second system, and it is the only reason `git log` can
serve as the tie-breaker in the trust order.

What a good message does: names the unit, states what changed in the world (not which
files were touched), and marks status transitions explicitly - *ruled*, *in-flight*,
*sealed*, *parked*. What a bad message does: "updates", "wip", or a week of unrelated
work lumped together. A degraded history degrades every future cold resume, not just
your own.

**Never commit anything from `vault/`.** Sensitive third-party material is quarantined
by the constitution and by `.gitignore`, and a public repository's history is
permanent. Check before any commit that adds files you did not personally place. This
is the one gate where "I'll clean it up later" does not exist as an option.

**Check a named brand, domain, or product name against a canonical source before it is
written into any register, report, or public-facing text.** A wrong name that reaches
a log or a draft can propagate and needs a hard correction later. When a factual error
is found in a standing record, correct it in place with an open, dated note explaining
what was wrong and its practical consequence - never a silent rewrite of history.

## 4. Work in flight, and how it survives an interruption

Any mission with work that may outlive the session carries a machine-readable header at
the top of its `STATE.md`:

```
status: proposed | ruled | in-flight | review | sealed
needs-local: yes | no
last-checkpoint: <what completed, and the file that proves it>
```

`status` is the state machine every mission moves through. `needs-local` says whether
the work can only run on the operator's own machine (a local path, a local tool, a
local credential) - if yes, nothing remote can pick it up and nobody should pretend
otherwise. `last-checkpoint` is the resume anchor: the phase that actually completed
and the artifact that proves it, not the phase somebody hoped to reach.

Under the header, a mission that could be interrupted carries a short **resume
protocol**: what to read first, what to verify on disk before continuing, and what must
never be re-run blindly. The resume rule that matters most: **inventory the disk before
resuming.** A session that assumes work is unfinished and redoes it wastes budget; a
session that assumes work is finished and skips it ships a hole. Look first.

There are no daemons in this system. Nothing picks work up on its own, nothing runs on
a schedule unless the operator explicitly stands it up and arms it, and no process
holds state that the files do not. That is a deliberate constraint: it means the only
thing that can be stale is a file, and files can be read.

Source: ops/OPERABILITY.md §2, §3, §4 (moved into this skill 2026-09-16)
