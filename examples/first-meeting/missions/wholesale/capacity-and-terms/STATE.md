# STATE - wholesale capacity and terms - WORKED EXAMPLE - fictional
<!-- file-class: DOCTRINE -->

```
status: sealed
needs-local: no
last-checkpoint: seal recorded 2026-04-24; standards-guard passed all five
                 deliverables, General Counsel passed D3 and D4, after-action
                 note filed to org/seats/operations/LEDGER.md
```

*Worked example. Bookkeeping only: where the mission is, what moved it, what it
is waiting on. What the mission actually discovered lives in `FINDINGS.md`, and
the moment substance starts appearing here both files stop being useful.*

*Transitions are dated lines, newest on top. The machine never skips a state and
never moves backward except through a logged redirect.*

---

## 2026-04-24 - review to sealed

All five deliverables passed the standards-guard. General Counsel passed D3 and
D4 as the conditional second gate, money and liability being plainly in play, and
its pass carries the standing recommend-human-review flag rather than an approval.

Standards-guard's verdict, as appended to `ledgers/STANDARDS_LOG.md`:

- Deterministic checks: clean on all five deliverables.
- Judge call: **one soft finding on D3.** A sentence in the counter-offer read
  "we have the capacity to support the full six-store schedule from month one",
  which asserted a volume claim without pointing at D1 or D2 as its source, and
  which the model does not support in any case. Rewritten to cite the measurement
  and to state the ceiling. Soft findings warn rather than block; this one was
  fixed before seal anyway, because it was wrong as well as unsourced.
- No hard findings. No guard error.

Operations appended its after-action note to `org/seats/operations/LEDGER.md`:
the charter's instinct to measure before committing was correct and cheap, and
the place the seat fought its brief was D2, where writing the cash ceiling into
the model's own text felt redundant against `04-ruling.md` and turned out to be
the single line every later reader used first.

Task row in `registers/TASKS.md` moved to `sealed`. The concentration risk stays
open in `registers/PROJECTS.md`, because sealing a mission does not retire a risk
the mission created.

## 2026-04-22 - in-flight to review

D3 and D4 landed. All five deliverables complete and awaiting their gates.

`ledgers/SPEND.md` reconciled: **391K actual against 275K to 420K projected,
within projection**, across the whole mission. Wall-clock 2 hours 10 minutes of
session time spread over nine calendar days. No variance explanation owed, and
none invented to look thorough.

## 2026-04-20 - checkpoint, no state change

D1 and D2 complete. Findings F-1 and F-2 filed to `FINDINGS.md`.

**F-2 produced an operator dependency, and it was posted to
`registers/BLOCKED_ON_OPERATOR.md` the same day**, not held for the seal. A
blocker discovered on day seven and surfaced on day eleven would have cost four
days, and the board is the only place the operator looks for things that are
waiting on him.

## 2026-04-14 - ruled to in-flight

D1 measurement began. D4's clause structure started in parallel, per the ruled
sequencing: the shape of the clauses does not depend on the volume number, only
the blanks do.

Launch projection for the mission's own lanes filed to `ledgers/SPEND.md` before
work began: **275K to 420K tokens**, re-derived after the ruling dropped the
two-shift lane rather than carried over from the plan's 300K to 460K. 1 hour 35
minutes to 2 hours 25 minutes of session time, against the 600K cap. Meter read
fresh at the launch moment rather than remembered from the meeting.

## 2026-04-13 - proposed to ruled

Packet fanned from `meetings/2026-04-13-wholesale-capacity/04-ruling.md` and
recorded in that meeting's `05-missions/`. Four ruled amendments carried into the
packet: two-shift variant dropped, exclusivity ruled out rather than left open,
one-cycle cash ceiling written into D2's own text, payment-terms question
reserved to the operator. No work started.
