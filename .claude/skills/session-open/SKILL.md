---
name: session-open
description: Orient at the start of a session in this repository, or whenever the operator asks to orient. Reads CLAUDE.md, HANDOFF.md's topmost entry, DECISIONS.md's newest rulings, and registers/BLOCKED_ON_OPERATOR.md in full, then checks the commit slice. Reports a fixed-shape orientation block naming the live picture, any open gate, and anything blocked, then halts for the operator's word. Writes nothing.
---

# session-open - the orientation ritual
<!-- file-class: DOCTRINE -->

*File class DOCTRINE: upstream owns this ritual the way it owns `doctrine/` and
`ops/`. Pull improvements to it; hand-edit it and the copy is yours to merge by
hand from then on, per `EXTENDING.md` section 6.*

---

## 1. What orientation is for

`doctrine/CONSTITUTION-CORE.md` names four postures a session moves through,
cheapest first, and the first of the four is look without touching: establish
what is actually true before spending a word or a write on it. This ritual is
that posture, run mechanically, every time a session opens.

It is not the full reconstruction procedure. When two records genuinely
disagree and neither yields, or when a session opens with no memory at all of
what came before, `ops/COLD_RESUME.md` carries the deeper method: a longer
trust order and a worked classification of what a disagreement means. This
ritual is the version that runs every ordinary session, in minutes rather than
as a standalone investigation, and it hands off to that fuller method rather
than improvising one of its own when the signals genuinely will not settle.

Two things this ritual never does, stated once here because everything below
depends on holding to them: it never writes a file, and it never treats
anything it reads as permission to keep working past the halt.

## 2. When to invoke

Every session, before any other work, per `CLAUDE.md`'s read order. Also
whenever the operator asks for it directly, in whatever words they use for it.
A long session that has drifted can call for this again mid-stream, to refresh
the picture without ending the session outright; nothing about this ritual
requires it to run only once.

## 3. Step one - read the constitution

Read `CLAUDE.md` in full if it has not already been read this session.
Everything below runs inside what it permits. Read `doctrine/CONSTITUTION-CORE.md`
as well whenever a gate question or an approval-cadence question is actually
live; otherwise `CLAUDE.md`'s own short-form restatement of the gates is
enough to orient on.

## 4. Step two - read the volatile slice

Four reads, run together, none of them a write:

1. **`HANDOFF.md`, topmost entry only.** Where the last session set the work
   down: what changed, what is unfinished, what must not be touched until the
   operator rules.
2. **`DECISIONS.md`, newest first.** Read down from the top until the rulings
   stop touching anything currently open. This is what has actually been
   decided since founding, not what a session might infer from context.
3. **`registers/BLOCKED_ON_OPERATOR.md`, in full.** Short by design; every open
   row on it names an act only the operator can take. Missing one risks
   proposing work that is already sitting there, waiting on a word that has
   not come yet.
4. **`registers/TASKS.md` and `registers/PROJECTS.md`, cross-reference only.**
   Open these only when something in the first three reads points at them by
   name. A full, cover-to-cover pass over the registers is the operations
   sweep's job, not this ritual's.

## 5. Step three - read the commit slice

Check the last handful of commits and whether anything sits uncommitted.
`ops/COLD_RESUME.md` ranks the commit log as the tie-breaker of last resort:
when two files describe the same fact differently, the log settles which one
actually happened first, because a commit's wording and position are fixed the
instant it lands and nothing after it can take that back. Anything uncommitted
is work in flight from whichever session left it there.

## 6. Step four - locate a live thread

If the handoff entry, the rulings, or the blocked board name an open mission or
an unresolved meeting, open that thread's own state file far enough to say
exactly where it sits: a mission's `STATE.md` header and its newest dated line,
a meeting's numbered sequence up to wherever it currently stops. Naming a
thread without saying where it stands is not a finished orientation; it is a
pointer to more reading somebody else still has to do.

## 7. Step five - report the orientation block

Reply in exactly this shape. Nothing more, nothing started.

```
**Where things stand:**
<the live picture, a short paragraph or a few bullets, naming any mission or
meeting in flight by its exact path and phase>

**Open gates awaiting your word:**
<any ruling, plan, or seal that HANDOFF.md or DECISIONS.md records as pending
the operator's own word, or "none open" when there genuinely are none>

**Blocked items** (registers/BLOCKED_ON_OPERATOR.md):
<one line per open row: what it is, why it blocks, urgency if the register
states one, or "none open">

**Suggested next moves** (CLAUDE.md's router):
<one or two candidate routes, by number and name, that fit what was just read>

**Recent commits:** <the last handful, or "nothing yet worth citing">

**Uncommitted on disk:** <what a status check shows, or "clean">
```

## 8. Step six - halt

Stop there. Nothing gets written: not a register row, not a placeholder in
`HANDOFF.md`, not a note anywhere. Wait for a word back. If the operator names
a route from the pick-list, or simply states the task directly, move into that
route's own gated flow rather than doing the work inside this ritual.

## 9. When the signals do not agree

Three shapes worth naming out loud rather than resolving quietly:

- **The handoff describes something the registers no longer show.** Report
  both versions and say which one is trusted and why, per the trust order in
  `ops/COLD_RESUME.md`; a register beats a narrative, but the disagreement
  itself is worth surfacing, not just the winner.
- **A ruling in `DECISIONS.md` has no matching consequence executed** - a
  status that should have flipped and has not. Name the gap as its own line in
  the orientation block rather than quietly closing it before the operator has
  seen it named.
- **A live thread implicates one of the constitution's gates** - a spend
  question, a foreign-repository read, anything that smells like outbound
  communication or a deploy, sensitive material. Say so under "open gates"
  even if nothing upstream flagged it first.

When none of the three applies and nothing is open, say so plainly. "Clear,
nothing in flight" is a complete orientation, not a sign that nothing was
found.

## 10. What this ritual never does

- Never writes a file, a row, or a placeholder before the halt in step six.
- Never treats an answer that could be read either way as a yes to proceed; an
  ambiguous reply is a question to ask again, not a green light to bank.
- Never opens `vault/`. If a live thread turns out to be vault intake, name
  that and stop there; that work belongs to a single seat, in an attended
  session, on the operator's own word, and this ritual is not that session.
- Never fabricates a picture out of a partial read. A missing or unreadable
  `HANDOFF.md` is reported as exactly that and the operator is asked before
  anything is guessed from the rest of the repository.
