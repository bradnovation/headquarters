# OPERABILITY - session discipline
<!-- file-class: DOCTRINE -->

*This file ships with the product and is upstream-pullable. Edit it
only if you intend to own your own copy of it forever.*

*Purpose: `ops/COLD_RESUME.md` says how a fresh session rebuilds the picture. This
file says what every session owes the next one so that rebuilding is possible. One is
the reader's contract; this is the writer's.*

---

## 1. The bar

**Repo state is truth.** Everything this org knows lives in files. Nothing lives in a
session's memory, because a session's memory ends when the session does - and it ends
without warning more often than anyone plans for.

The bar a session must clear before it ends: **a stranger who has never spoken to the
operator, reading only this repo, can answer all six of these.**

1. What is blocked, and on whom.
2. What work is in flight, at what phase, and who owns it.
3. What has been ruled, and where the ruling is recorded.
4. What has been spent against which cap, and what is still unreconciled.
5. What the last session actually did.
6. What the obvious next step is, and what must not be touched until the operator
   speaks.

If any of the six cannot be answered from the files, the session has not finished its
work, no matter how much of the actual task got done.

Whenever the operator has to go open, paste, or upload something themselves, hand it
to them as a complete path, from the root, sitting alone on its own line - not a bare
filename and not a reference relative to wherever the session happens to be. Anything
short of that turns into a search on their end, which erases the reason for pointing
them at the file at all.

Time discipline - never guessing a timestamp, and always rendering a time back to a
person in their own local timezone - is covered in full in
`ops/MEASUREMENT_CRAFT.md`; this file's only addition is that a checkpoint commit
(section 3) and the park ritual (section 5) are exactly the moments that discipline
has to hold.

---

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

Two corollaries worth stating plainly:

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

---

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

---

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

---

## 5. The park ritual

**Any session that leaves this repository different from how it found it parks before
closing.** There is no version of this that gets caught up tomorrow. It is the forcing function against
the single most common failure in a system like this: a handoff file that quietly stops
matching reality until nobody trusts it, and then nobody updates it, and then the org
is only operable by whoever remembers.

Park, in order:

1. **Reconcile the ledgers.** Any spend authorised this session gets its actual
   recorded against its projection. Overage is attributed and explained, not smoothed.
2. **Record every ruling.** Anything the operator decided goes into `DECISIONS.md` as
   the next numbered entry, transcribed in his own words where he stated it plainly. A
   ruling that lives only in a chat window did not happen.
3. **Update the registers.** Task statuses flipped, blocked-board items opened or
   resolved, project rows touched by the session's work.
4. **Update mission and meeting artifacts.** `STATE.md` headers set to the true status
   and checkpoint; findings filed in `FINDINGS.md`, separate from state.
5. **Append the session record.** A new entry at the top of `SESSION_LOG.md`: what was
   done, what was decided, what it cost, what is left.
6. **Rewrite `HANDOFF.md`'s topmost entry** - the live picture, as of now, for whoever
   opens this repo next. This rewrite belongs on the near side of the session's last
   commit. A handoff written after the last commit is a handoff that is one commit
   wrong from the moment it exists.
7. **Commit and push.** The final commit of the session carries the handoff update in
   it.

**A close that leaves the handoff untouched is not a close.** Say so plainly rather
than declaring a park that did not happen.

Show before you save. The session log entry, the handoff rewrite, and any ledger row
get shown to the operator before they are written, with an explicit chance to edit.
Rejected drafts get workshopped in conversation, never silently overwritten.

---

## 6. Failure classes this discipline exists to prevent

These are the ways operability actually breaks. Each is stated as a class, with the
rail that answers it.

- **The stale handoff.** A session ends in a hurry; the handoff still describes
  yesterday. Every later session either wastes time on a wrong picture or stops trusting
  the file at all. *Rail: parking is mandatory, and the handoff gets rewritten on the
  near side of the last commit.*
- **Work that exists only in the conversation.** A decision, a number, or a finding
  discussed at length and never written down. It is gone. *Rail: capture at the change
  point, not at the close.*
- **The unrecorded ruling.** The operator says yes; the session acts on it; nobody
  writes it into the decisions ledger. Six weeks later nobody can say what was
  authorised or why. *Rail: a ruling is recorded before its consequences are executed.*
- **The silent packet edit.** A mission's charge is quietly reinterpreted mid-flight to
  match what turned out to be easy. The record now shows a mission that succeeded at
  something nobody asked for. *Rail: packets are immutable once fanned out; a redirect
  comes from the operator and gets logged as a change.*
- **Spend without a projection.** A run is launched on optimism, costs several times
  what anyone assumed, and the overage is discovered after the fact. *Rail: project
  before launching, reconcile at close, and treat an unreconciled ledger as a blocker on
  the next launch.*
- **Assuming background work survived.** A session ends believing something is still
  running. Nothing is running. *Rail: nothing outlives the session that started it, so
  only what reached the disk counts as done.*
- **The single-session org.** Everything works beautifully as long as one particular
  conversation continues, and collapses the moment it does not. *Rail: this entire
  file, and the bar in section 1.*
- **A tool that rewrites its own leash.** A third-party tool or plugin quietly
  rewrites your constitution or config files, or injects unrequested instructions into
  prompts, without being asked. *Rail: treat this as a trust violation serious enough
  to warrant full removal, not just disabling, and flag any future tool that touches
  core doctrine files before it is allowed to stay installed.*

None of these are hypothetical failure modes invented for a document. They are what
goes wrong, repeatedly, in any system where a capable session is trusted to remember
things.

---

## 7. The check before you close

Five questions. If any answer is no, the session is not finished.

1. Could a stranger answer the six questions in section 1 from the files alone?
2. Is every ruling from this session in `DECISIONS.md`?
3. Does `HANDOFF.md`'s topmost entry describe reality as of right now?
4. Is every unit of work committed, with nothing sensitive in the diff?
5. Is the named next step something the next session can start without asking anyone
   what happened?
