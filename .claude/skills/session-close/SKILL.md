---
name: session-close
description: The park ritual that ends any session leaving this repository different from how it opened. Drafts the SESSION_LOG.md entry and shows it before saving, updates HANDOFF.md's topmost entry before the closing commit and refuses to close without it, reconciles the spend ledger and the registers, surfaces any promise still owed to a third party, and commits with this product's model/session trailer.
---

# session-close - the park ritual
<!-- file-class: DOCTRINE -->

*File class DOCTRINE: upstream owns this ritual the way it owns `doctrine/` and
`ops/`. Pull improvements to it; hand-edit it and the copy is yours to merge by
hand from then on, per `EXTENDING.md` section 6.*

---

## 1. When to invoke, and the one honest exception

Invoke before ending any session that leaves this repository different from
how it opened: a file written, a register row added, a ruling recorded, a
mission's status moved. `ops/OPERABILITY.md` sets the standard this ritual
exists to meet, and the standard is not "the work got done." It is that
somebody arriving cold tomorrow can pick the thread up from the repository
alone. Skip the close and that condition goes unmet, however much the session
accomplished on its way there.

Sessions that only talked are the single case where skipping is available, and
that call does not belong to the session by itself. Name the situation out
loud, state that nothing was drafted and no file moved, and let the operator
decide whether a close earns its few minutes. Where the answer comes back at
all unclear, run the ritual, and `SESSION_LOG.md` ends up being the one file
it writes. That default follows from the asymmetry: a close nobody needed
costs those few minutes, while a close nobody ran leaves the next session
reading a handoff that stopped being true without saying so.

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

If this session authorized anything metered beyond itself, a fan-out, a dream
run, anything already sitting in `ledgers/SPEND.md` with a `projected` entry,
write its reconciled entry now: actual cost, actual wall-clock, and the
variance against what was projected. An overage gets a plain-language reason,
never left blank. A projection with no reconciled entry blocks the next launch
of that same shape, per the ledger's own rules, so this step is not optional
bookkeeping; it is what keeps every future projection worth trusting.

If nothing metered ran this session, say so and move on.

## 4. Step three - record every ruling

Anything the operator decided this session, in conversation or otherwise,
lands in `DECISIONS.md` as the next numbered entry before this ritual goes any
further. A decision that lives only in a chat window did not happen, per this
product's own state discipline. Where the meeting ritual already produced a
ruling file of its own, confirm it was replicated into `DECISIONS.md` in the
same sitting; a ruling recorded in only one of the two places is half
recorded, and closing that gap belongs to whichever session notices it.

## 5. Step four - update the registers

Check whether this session touched a project, a task, or anything only the
operator can unblock. If it did:

- `registers/PROJECTS.md` and `registers/TASKS.md` get a new dated section for
  anything whose status changed. Append a new section; never edit an old one,
  per those files' own append-only shape.
- `registers/BLOCKED_ON_OPERATOR.md` gets a new row for anything now waiting
  on the operator's own hand, and a resolving entry for anything this session
  actually cleared.

Show the diff before writing it, the same as every other draft this ritual
produces. **Refuse to close past a register both sides already know is
stale.** If the operator wants to skip straight to the commit, name the stale
register out loud and hold the line rather than letting it stand uncorrected.

## 6. Step five - update mission and meeting artifacts

If a mission is in flight, bring its `STATE.md` header current: `status`,
`needs-local`, and the checkpoint line naming what actually completed and the
file that proves it, plus a new dated line if the status machine moved. If a
meeting is mid-ritual, its own numbered sequence gets whatever file the
sitting actually reached. Findings belong in a mission's own `FINDINGS.md`,
kept apart from its state file, the way `ops/OPERABILITY.md` and
`org/STAFF_MEETING.md` both ask.

## 7. Step six - draft the SESSION_LOG.md entry, and show it first

Use `SESSION_LOG.md`'s own entry format; the file states its shape at the top,
and this ritual follows it exactly rather than improvising a new one. Draft
the entry in full, then show it verbatim with an explicit two-way choice:

```
Drafted the session-log entry:

---
<the entry>
---

Save as written, or change something first?
```

Nothing gets appended until the operator answers. An edit gets applied and
shown again; it never gets replaced with a second draft carrying reasoning the
operator did not see.

## 8. Step seven - update HANDOFF.md's topmost entry (mandatory, and first)

Of everything `ops/OPERABILITY.md` asks of a closing session, this is the
requirement it puts ahead of the rest. The ordering has a mechanical reason
behind it rather than a stylistic one: the closing commit is what makes the
position durable, so the position has to exist while there is still a commit
coming to carry it. **This ritual holds no path that arrives at the commit
step with the handoff entry unwritten.** Asked to jump ahead to the commit,
name what is missing, write it, then commit.

Draft the new topmost entry in `HANDOFF.md`'s own format: where the sequence
stands, what this session actually changed, and a resume protocol if the
obvious next step is not already implied by the state itself. Name plainly
what must not be touched until the operator rules on it; that line is usually
the single most useful sentence in the entry. Show it the same way as step
six, draft and display and an explicit choice, before writing anything. On
approval, prepend above the current topmost entry; the file only ever grows
upward, and the oldest entries stay put at the bottom for good.

## 9. Step eight - surface any promise still owed to another human

Before staging anything, look back across the session for a commitment made
to somebody outside this repository: a document the operator said he would
send, a call he agreed to make, a date he named to a counterparty. Nothing
built here ever sends on the operator's behalf, since the constitution's
communication gate is structural rather than a setting, and that is exactly
why a promise like this cannot simply be marked done and forgotten. It stays a
live human obligation until the operator's own hand actually discharges it.

A concrete shape, invented for illustration only: a session's conversation
includes the operator saying he will get a new price list to a wholesale
customer by the end of the week. Nothing about that belongs in a file this
ritual writes on its own initiative. What belongs on `registers/BLOCKED_ON_OPERATOR.md`
is a single row naming the act, the deadline, and the plain fact that only the
operator's own hand can close it out.

Say "nothing owed" plainly when a genuine look turns up nothing. The look
itself is the part that is never skipped.

## 10. Step nine - stage named files and commit

1. Run a status check and read the full list it returns. Anything that looks
   like a secret, a credential, or a path under `vault/` stops this step
   entirely; flag it rather than staging around it. A vault path appearing
   here at all is a defect in the ignore rules, not a file to quietly work
   past.
2. Stage files by name, listed explicitly. Never a blanket stage-everything
   command; a blanket stage is exactly how something unintended rides along
   in a commit nobody meant to make that large.
3. Write a commit message with a title short enough to take in at a glance and
   a short body naming what actually changed in the world, not which files
   moved. Mark a status transition explicitly whenever one happened, ruled,
   in-flight, sealed, parked, the way `ops/OPERABILITY.md` asks of every
   commit. Close with this product's own trailer:

```
Executed-By: <the model or tier that did the work>
Session: <session identifier or link, if one exists>
```

4. If a pre-commit check fails, fix the actual cause, stage again, and make a
   new commit. Never force past a failing check and never fold the fix into a
   rewritten version of the commit that already failed; a fresh commit keeps
   the history honest about what really happened, in what order.

If the operator says to skip the commit, honor it, but hold the line on step
eight regardless; `HANDOFF.md` can describe work that is finished but still
sitting uncommitted on disk, and that is exactly the situation its own
narrative is built to carry.

## 11. Step ten - confirm the close

State plainly that the session is parked: the handoff entry is updated, the
session log carries the new entry, the commit landed with its trailer if one
was made, and the ledger and registers are either current or explicitly noted
as needing nothing this time. If the operator asked to skip a step along the
way, name exactly which one in this final line, so nothing about the close is
ambiguous to whoever reads this repository next.

## 12. What this ritual never does

- Never commits before `HANDOFF.md`'s topmost entry is updated to match. The
  order is fixed; it is not a matter of taste or of running short on time.
- Never reads or writes anything under `vault/`, in any step, under this
  product's third-party-material gate.
- Never treats a chat reply as approval to write. A shown draft gets an
  explicit answer before it becomes a file.
- Never stages a blanket set of files, and never commits on behalf of a
  repository this product does not own; a session that touched something
  outside this repository notes that state in `HANDOFF.md` instead of
  committing it here.
- Never leaves a register both sides know is stale in place because
  committing felt more urgent than fixing it first.
