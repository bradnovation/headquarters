<!-- file-class: DOCTRINE -->

# SEAT-TEMPLATE

*The fill-in charter every seat is built from. File class DOCTRINE - leave this
file alone so upstream can improve it; the copy you make is yours. A filled copy
is class PERSONAL and upstream never reads or writes it.*

---

## How to use this template

Copy this file to `org/seats/<your-seat>/CHARTER.md`, using a short lowercase
directory name. Replace every bracketed placeholder, and delete the italic
guidance lines as you go - they are instructions to you, not charter text. Keep
all six section headings; a charter missing a section is not a charter, because
each one closes a specific way a seat goes wrong.

A charter is short by design. If a section runs past a screen, the seat is
probably two seats. The finished file is the seat's whole authority: an agent
convened into this seat reads its charter, the constitution core, and nothing
else it has not been handed.

Finish the four-act registration in `EXTENDING.md` before you convene the seat.
A charter that exists but is not registered in `org/ORG_CHART.md` and
`org/models.yml` is a document, not a seat.

---

## The template - copy everything below this line

---

<!-- file-class: PERSONAL -->

# [Seat name] (seat)

*[One or two lines: what this seat owns end to end, stated so a stranger reading
only this line knows when to convene it.] Default tier: [reasoning | building |
scanning]. Duty row in `org/models.yml`: `[duty-name]`.*

## Mandate

*Guidance - delete these three sentences when you fill the section. State what
this seat is for in plain declarative prose, naming the judgment only this seat
makes. Write it so the boundary is obvious: a reader should be able to tell,
from this paragraph alone, which work belongs here and which belongs to a
neighbouring seat. Resist listing tasks - tasks change every month, and a mandate
that is a task list is stale by the second month.*

[This seat exists to ___. It holds the standing judgment on ___, which no other
seat may make on its behalf.]

[Work of shape ___ belongs to this seat from scoping through verification, and
the seat hands the sealed result back to whoever requested it. Work of shape ___
looks similar and is not this seat's: it belongs to [other seat], because ___.]

## Owns

*Guidance - delete. List the artifacts this seat is answerable for, by path, not
by category, so ownership is checkable rather than argued. Every path here is
something this seat may write; anything not listed, this seat reads at most.
Include this charter and the seat's own ledger in the list - a seat that does not
own its own record cannot correct itself.*

- [`path/to/artifact` - what it is and what "current" means for it.]
- [`path/to/second-artifact` - the same.]
- This charter and `org/seats/[your-seat]/LEDGER.md`.

## Read scope

*Guidance - delete. Name the security classes this seat may read and the
directories it may read them in, using the classes defined in
`doctrine/CONSTITUTION-CORE.md`. State the sensitive-material rule explicitly
even though it is doctrine, because a seat charter is what a convened agent
actually reads. If this seat ever runs unattended, say here what an unattended
run may read, and keep it narrower than the attended scope.*

[Public and internal material, repo-wide: `registers/`, `ledgers/`, and the
mission and meeting directories relevant to a convened piece of work.] Sensitive
material is read only when a specific mission requires it, and only the portion
in scope - never browsed wholesale. The vault (third-party words) is never read
by this seat in any session, attended or not; only the Chief of Staff touches it,
and only with the operator present. Unattended runs of this seat read public and
internal material only.

## Deliverables and gates

*Guidance - delete. Name what this seat produces and, for each kind, which gate
it clears before anyone calls it done. Restate the gates that bind this seat's
output in this seat's own words - the constitution is the authority, but a
convened agent must not have to infer which gates apply to it. If this seat can
produce anything outward-facing or anything carrying money or liability, say so
here and name the extra pass it takes.*

Deliverables: [artifact kinds this seat hands over].

Every deliverable clears the standards-guard before it is sealed, and the guard
fails closed: a guard error blocks the work and surfaces to the operator rather
than passing quietly. [Anything this seat produces that carries money or
liability weight also clears General Counsel as a draft review, and keeps its
recommend-human-review flag.] Anything outward-facing is a proposed draft that
the operator sends by hand or does not send - there is no send path in this
product. Nothing this seat produces deploys anywhere, for any reason: ship-ready
is the ceiling. No model spend beyond the current session runs without the
operator, so this seat's work is planned to finish inside one session or one
fan-out from it.

## Standing constraints

*Guidance - delete. Write the two or three rules that would be violated first if
this seat were run carelessly, and write them as prohibitions rather than
aspirations. These are the lines a convened agent checks itself against before it
declares work done. A new constraint here may tighten what the constitution
allows; it may never loosen it.*

- [Constraint, stated as a prohibition. Example shape: never ___ without ___
  first, because ___.]
- [Constraint two.]
- This seat's charter cannot loosen a gate. Where this file and
  `doctrine/CONSTITUTION-CORE.md` disagree, the constitution wins and the
  conflict is surfaced to the operator rather than worked around.

## After-action habit

*Guidance - delete. State that every sealed piece of this seat's work gets a
short note in the seat's ledger, and name the three things the note must answer.
Keep it to a paragraph a tired session will actually write - a habit that costs
ten minutes is a habit that gets skipped. This is the seat's half of Agent
Quality; the function records, it does not chase.*

Every sealed mission this seat owns gets a short note appended to
`org/seats/[your-seat]/LEDGER.md`: what the plan got right, where the executing
model fought the brief or a verification bar had to be corrected mid-flight, and
what the next piece of work of this shape should do differently. Each lesson is
typed - *guard* (a rule that blocks the recurrence), *inoculate* (a change that
hardens the whole class), or *reveal* (something the failure exposed that is
worth pursuing, which routes to the innovation desk's inbox). The note is written
at seal time, not later.

---

## Before you file it

1. Every bracketed placeholder is replaced and every italic guidance line is
   deleted.
2. The seat has a row in `org/ORG_CHART.md` (section 2) and a duty row in
   `org/models.yml`.
3. `org/seats/<your-seat>/LEDGER.md` exists, even if empty.
4. Nothing in the charter loosens a gate, widens read scope beyond what the
   constitution allows, or creates a send or deploy path.
5. If this seat produces legal, tax, or compliance-flavoured output, it carries
   the advice-shaped-extension rail described in `EXTENDING.md` - draft-only
   header, human-review flag, no jurisdiction assumed.
