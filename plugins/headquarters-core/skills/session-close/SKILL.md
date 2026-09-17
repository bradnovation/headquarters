---
name: session-close
description: Use before ending any session that leaves this repo different from how it opened: the ten-step park ritual ending in a trailer-stamped commit.
---

# session-close - the park ritual

## 1. When to invoke, and the one honest exception

Invoke before ending any session that leaves this repository different from
how it opened: a file written, a register row added, a ruling recorded, a
mission's status moved. Step ten's bar (below) sets the standard; it is not
"the work got done" but that somebody arriving cold tomorrow can pick the
thread up from the repository alone. Skip the close and that condition goes
unmet, however much the session accomplished.

Sessions that only talked are the one case where skipping is available, and
the call belongs to the operator, not the session: name the situation, state
that nothing was drafted and no file moved, and let the operator decide.
Where the answer is unclear, run the ritual anyway, with `SESSION_LOG.md` as
the one file it writes - a close nobody needed costs a few minutes; a close
nobody ran leaves the next session reading a handoff that quietly stopped
being true.

## 2. Step one - gather what actually happened

Before drafting anything, assemble in parallel:

1. `HANDOFF.md`, topmost entry only. This ritual writes above it, never over
   it.
2. `SESSION_LOG.md`, topmost entry only, for the same reason.
3. The commit slice: recent commits and whatever is still sitting
   uncommitted.
4. A plain recollection of the session: what it actually set out to do, what
   landed, what the operator ruled or approved, what broke or had to be
   redone, and what is genuinely left for the next session to pick up.

## 3. Step two - reconcile the spend ledger

If this session authorized anything metered beyond itself - a fan-out, a
dream run, anything already sitting in `ledgers/SPEND.md` with a `projected`
entry - write its reconciled entry now: actual cost, actual wall-clock, and
the variance against what was projected. An overage gets a plain-language
reason, never left blank. A projection with no reconciled entry blocks the
next launch of that same shape, per the ledger's own rules; this is what
keeps every future projection worth trusting.

If nothing metered ran this session, say so and move on.

## 4. Step three - record every ruling

Anything the operator decided this session, in conversation or otherwise,
lands in `DECISIONS.md` as the next numbered entry before this ritual goes any
further - a decision that lives only in a chat window did not happen. Where a
meeting ritual already produced a ruling file of its own, confirm it was
replicated into `DECISIONS.md` in the same sitting; a ruling recorded in only
one of the two places is half recorded, and closing that gap belongs to
whichever session notices it.

## 5. Step four - update the registers

Check whether this session touched a project, a task, or anything only the
operator can unblock. If it did:

- `registers/PROJECTS.md` and `registers/TASKS.md` get a new dated section
  for anything whose status changed - append a new section, never edit an
  old one, per those files' own append-only shape.
- `registers/BLOCKED_ON_OPERATOR.md` gets a new row for anything now waiting
  on the operator's own hand, and a resolving entry for anything this session
  actually cleared.

Show the diff before writing, the same as every other draft this ritual
produces. **Refuse to close past a register both sides already know is
stale.** If the operator wants to skip straight to the commit, name the stale
register out loud and hold the line.

## 6. Step five - update mission and meeting artifacts

If a mission is in flight, bring its `STATE.md` header current: `status`,
`needs-local`, and the checkpoint line naming what actually completed and the
file that proves it, plus a new dated line if the status machine moved. If a
meeting is mid-ritual, its own numbered sequence gets whatever file the
sitting actually reached. Findings belong in a mission's own `FINDINGS.md`,
kept apart from its state file.

## 7. Step six - draft the SESSION_LOG.md entry, and show it first

**The default is show-first, always.** An autosave option exists only where
the operator has said outright, in writing, that they do not personally read
these routine end-of-session drafts - and even then, only for the two
administrative artifacts this ritual writes on its own account: the
session-log entry and the handoff rewrite. There, the ritual saves the draft
directly and reports what it wrote in one line. Anything else keeps the full
show-before-save discipline below, regardless of how routine it looks.

Use `SESSION_LOG.md`'s own entry format - the file states its shape at the
top, and this ritual follows it exactly. Draft the entry in full, then show
it verbatim with an explicit two-way choice:

```
Drafted the session-log entry:

---
<the entry>
---

Save as written, or change something first?
```

Nothing gets appended until the operator answers; an edit gets applied and
shown again, never replaced with a second draft carrying reasoning the
operator did not see.

## 8. Step seven - update HANDOFF.md's topmost entry (mandatory, and first)

Of everything this discipline asks of a closing session, this one comes
first, for a mechanical reason: the closing commit is what makes the position
durable, so the position has to exist before that commit does. **This ritual
holds no path that arrives at the commit step with the handoff entry
unwritten.** Asked to jump ahead, name what is missing, write it, then
commit.

Draft the new topmost entry in `HANDOFF.md`'s own format: where the sequence
stands, what this session actually changed, and a resume protocol if the
next step isn't already obvious. Name plainly what must not be touched until
the operator rules on it - usually the single most useful sentence in the
entry. Show it the same way as step six (or, under the same autosave
exception, save it and report it in one line). On approval or autosave,
prepend above the current topmost entry; the file only ever grows upward.

## 9. Step eight - surface any promise still owed to another human

Before staging anything, look back across the session for a commitment made
to somebody outside this repository: a document the operator said he would
send, a call he agreed to make, a date he named to a counterparty. Nothing
built here ever sends on the operator's behalf, since the communication gate
is structural rather than a setting - so a promise like this cannot simply be
marked done and forgotten. It stays a live human obligation until the
operator's own hand actually discharges it. See reference.md for a worked
example of what does, and does not, belong in this step's own file.

Say "nothing owed" plainly when a genuine look turns up nothing. The look
itself is the part that is never skipped.

## 10. Step nine - stage named files and commit

1. Run a status check and read the full list it returns. Anything that looks
   like a secret, a credential, or a path under `vault/` stops this step
   entirely - flag it rather than staging around it; a vault path appearing
   here at all is a defect in the ignore rules, not a file to quietly work
   past. Sweep any scratch or temp directory used mid-run too: a designated
   output location does not automatically cover a scratch area used along the
   way, so scratch and temp get checked for anything that accumulated outside
   it during the session.
2. Stage files by name, listed explicitly - never a blanket stage-everything
   command; that is exactly how something unintended rides along in a commit
   nobody meant to make that large.
3. Write a commit message with a title short enough to take in at a glance
   and a short body naming what actually changed in the world, not which
   files moved. Mark a status transition explicitly whenever one happened -
   ruled, in-flight, sealed, parked. Close with this product's own trailer:

```
Executed-By: <the model or tier that did the work>
Session: <session identifier or link, if one exists>
```

4. If a pre-commit check fails, fix the actual cause, stage again, and make a
   new commit - never force past a failing check, and never fold the fix
   into a rewritten version of the commit that already failed; a fresh commit
   keeps the history honest about what happened, in what order.

If the operator says to skip the commit, honor it, but hold the line on step
eight regardless; `HANDOFF.md` can describe work that is finished but still
sitting uncommitted on disk - exactly the situation its own narrative is
built to carry.

## 11. Step ten - confirm the close

Before declaring the session closed, clear two checks.

**The bar this ritual exists to meet.** Repo state is truth: everything the
venture knows lives in files, because a session's memory ends when the
session does, often without warning. A stranger who has never spoken to the
operator, reading only this repository, must be able to answer all six of
these:

1. What is blocked, and on whom.
2. What work is in flight, at what phase, and who owns it.
3. What has been ruled, and where the ruling is recorded.
4. What has been spent against which cap, and what is still unreconciled.
5. What the last session actually did.
6. What the obvious next step is, and what must not be touched until the
   operator speaks.

If any of the six cannot be answered from the files, the session's work is
not finished, no matter how much of the actual task got done. Hand the
operator a complete path, from the root, sitting alone on its own line,
whenever they have to go open, paste, or upload something themselves - never
a bare filename and never a path relative to wherever the session happens to
be, since either one just turns into a search on their end. Time discipline
- never guessing a timestamp, always rendering a time back to a person in
their own local timezone - has to hold at exactly two moments: a checkpoint
commit, and this park ritual.

**The check before you close.** Five questions; a "no" on any means the
session is not finished.

1. Could a stranger answer the six questions above from the files alone?
2. Is every ruling from this session in `DECISIONS.md`?
3. Does `HANDOFF.md`'s topmost entry describe reality as of right now?
4. Is every unit of work committed, with nothing sensitive in the diff?
5. Is the named next step something the next session can start without
   asking anyone what happened?

Once both checks clear, state plainly that the session is parked: handoff
updated, session log carries the new entry, commit landed with its trailer if
one was made, ledger and registers current or explicitly noted as needing
nothing this time. Name exactly which step was skipped, if any, so the close
is unambiguous to whoever reads this repository next.

## 12. What this ritual never does

- Never commits before `HANDOFF.md`'s topmost entry is updated to match - the
  order is fixed, not a matter of taste or of running short on time.
- Never reads or writes anything under `vault/`, in any step, under this
  product's third-party-material gate.
- Never treats a chat reply as approval to write; a shown draft gets an
  explicit answer before it becomes a file.
- Never stages a blanket set of files, and never commits on behalf of a
  repository this product does not own - a session that touched something
  outside this repository notes that state in `HANDOFF.md` instead of
  committing it here.
- Never leaves a register both sides know is stale in place because
  committing felt more urgent than fixing it first.

reference.md lists the eight failure classes this discipline exists to
prevent, each paired with the rail that answers it; read it for the reasoning
behind these ten steps rather than just the steps themselves.

Source: .claude/skills/session-close/SKILL.md §1-12; ops/OPERABILITY.md §1, §6, §7 (moved into this skill 2026-09-16)
