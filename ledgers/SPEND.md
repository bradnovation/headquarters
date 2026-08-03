<!-- file-class: PERSONAL -->

# SPEND - projected against actual, one run at a time

*Owned by the Finance seat (`org/seats/finance/CHARTER.md`). Append-only: one
H2 dated section per authorization, newest on top. This ledger is the record
gate G1 depends on - "no spend beyond the current session without you" only
means something if every fan-out's projection and every fan-out's actual are
both written down where a later session can check them.*

## The two rules this ledger exists to enforce

**Projection before launch.** Nothing that convenes more than the current
session - a fleet, a fan-out, a scheduled or dream run once one is armed -
launches without a stated projection first: what is launching, roughly how
much it will cost, roughly how long it will take, and what cap, if any, it is
being measured against. That projection is written into this ledger *before*
the launch, not reconstructed afterward from memory. A launch with no entry
here first has skipped the gate, whatever else about it went well.

**Overage attributed at close, not smoothed over.** When a run's actual cost
lands, it gets reconciled against its own projection in a second, later
entry - and if the actual came in over the projection, that entry states why
in plain language: what ran longer than expected, what retried, what scope
crept mid-run. "It cost more than planned" is not a reconciliation; a named
reason is. An unreconciled projection - a run that launched and never got its
actual written down - blocks the next launch of the same shape until it is
closed out, because an unreconciled ledger makes every projection after it
unreliable.

## Format

Two entries per authorization, both dated, both append-only.

**At launch**, status `projected`:

```
## [DATE] - [what is launching] - status: projected

**Projected cost:** [range, in whatever unit you track - tokens, dollars,
model-hours]. **Projected wall-clock:** [range]. **Measured against:** [a
cap, if one applies - e.g. the day's remaining dream-run balance under
CLAUDE.md §(f) - or "no standing cap, one-off authorization"].
```

**At close**, status `reconciled`, referencing the launch entry by date and
name:

```
## [DATE] - [what launched] - status: reconciled (see [launch date] above)

**Actual cost:** [figure]. **Actual wall-clock:** [figure]. **Variance:**
[within projection / over projection - by how much]. **If over: why:** [the
plain-language reason - never left blank when the actual exceeded the
projection].
```

---

No spend recorded yet. This ledger stays empty and honest until the first run
this staff actually authorizes.
