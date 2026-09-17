# session-close - reference material

Read this when step eight needs a worked example of what counts as a promise
still owed, or when you want the full statement of the failure classes this
ritual exists to prevent.

## Worked example: a promise still owed (step eight)

Step eight asks the ritual to look back across the session for any commitment
the operator made to somebody outside the repository - a document he said he
would send, a call he agreed to make, a date he named to a counterparty.
Nothing built here ever sends on the operator's behalf, since the
communication gate is structural rather than a setting, and that is exactly
why a promise like this cannot simply be marked done and forgotten. It stays
a live human obligation until the operator's own hand actually discharges it.

A concrete shape, invented for illustration only: a session's conversation
includes the operator saying he will get a new price list to a wholesale
customer by the end of the week. Nothing about that belongs in a file this
ritual writes on its own initiative. What belongs on
`registers/BLOCKED_ON_OPERATOR.md` is a single row naming the act, the
deadline, and the plain fact that only the operator's own hand can close it
out.

## Failure classes this discipline exists to prevent

These are the ways operability actually breaks. Each is stated as a class,
with the rail that answers it.

- **The stale handoff.** A session ends in a hurry; the handoff still
  describes yesterday. Every later session either wastes time on a wrong
  picture or stops trusting the file at all. *Rail: parking is mandatory, and
  the handoff gets rewritten on the near side of the last commit.*
- **Work that exists only in the conversation.** A decision, a number, or a
  finding discussed at length and never written down. It is gone. *Rail:
  capture at the change point, not at the close.*
- **The unrecorded ruling.** The operator says yes; the session acts on it;
  nobody writes it into the decisions ledger. Six weeks later nobody can say
  what was authorised or why. *Rail: a ruling is recorded before its
  consequences are executed.*
- **The silent packet edit.** A mission's charge is quietly reinterpreted
  mid-flight to match what turned out to be easy. The record now shows a
  mission that succeeded at something nobody asked for. *Rail: packets are
  immutable once fanned out; a redirect comes from the operator and gets
  logged as a change.*
- **Spend without a projection.** A run is launched on optimism, costs
  several times what anyone assumed, and the overage is discovered after the
  fact. *Rail: project before launching, reconcile at close, and treat an
  unreconciled ledger as a blocker on the next launch.*
- **Assuming background work survived.** A session ends believing something
  is still running. Nothing is running. *Rail: nothing outlives the session
  that started it, so only what reached the disk counts as done.*
- **The single-session org.** Everything works beautifully as long as one
  particular conversation continues, and collapses the moment it does not.
  *Rail: this entire discipline, and the bar in step ten.*
- **A tool that rewrites its own leash.** A third-party tool or plugin
  quietly rewrites your constitution or config files, or injects unrequested
  instructions into prompts, without being asked. *Rail: treat this as a
  trust violation serious enough to warrant full removal, not just
  disabling, and flag any future tool that touches core doctrine files
  before it is allowed to stay installed.*

None of these are hypothetical failure modes invented for a document. They
are what goes wrong, repeatedly, in any system where a capable session is
trusted to remember things.

Source: .claude/skills/session-close/SKILL.md §9 (worked example); ops/OPERABILITY.md §6 (moved into this skill 2026-09-16)
