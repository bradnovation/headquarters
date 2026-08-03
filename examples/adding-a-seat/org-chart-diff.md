# Org-chart diff - WORKED EXAMPLE
<!-- file-class: DOCTRINE -->

*What acts two and three of `WALKTHROUGH.md`'s procedure actually change,
shown as before/after diffs against this product's own shipped
`org/ORG_CHART.md` and `org/models.yml`. These are displayed diffs inside
this example only. The shipped files are untouched: the default roster stays
six seats, and the duty map stays the default duty rows. Nothing outside this
directory was edited to produce this page.*

---

## 1. `org/ORG_CHART.md`, section 2 (Seats table)

Before, the table's last row and the sentence under it:

```diff
  | Finance | Owns `ledgers/SPEND.md` and the projection-before-launch habit. Drafts and classifies; never files anything with anyone. | building | `org/seats/finance/CHARTER.md` | `org/seats/finance/LEDGER.md` |

  Tier names come from `org/models.yml`, which maps duties to model tiers. Building
  tier is the default for execution; reasoning tier is used on a stated reason, not
  by habit.
```

After, with one row added:

```diff
  | Finance | Owns `ledgers/SPEND.md` and the projection-before-launch habit. Drafts and classifies; never files anything with anyone. | building | `org/seats/finance/CHARTER.md` | `org/seats/finance/LEDGER.md` |
+ | Delivery | Project management over your wholesale accounts: owns onboarding, delivery cadence, and renewal timing end to end. | building | `org/seats/delivery/CHARTER.md` | `org/seats/delivery/LEDGER.md` |

  Tier names come from `org/models.yml`, which maps duties to model tiers. Building
  tier is the default for execution; reasoning tier is used on a stated reason, not
  by habit.
```

One row, added at the bottom of the table. Its position in the table carries
no meaning: nothing in the constitution or the chart ranks seats by row
order, and `org/ORG_CHART.md` §1 says so directly (no seat answers to
another seat).

## 2. `org/ORG_CHART.md`, section 6 (Cross-reference index)

Before, the seat half of the index:

```diff
  - `org/seats/chief-of-staff/CHARTER.md`
  - `org/seats/operations/CHARTER.md`
  - `org/seats/marketing/CHARTER.md`
  - `org/seats/revenue/CHARTER.md`
  - `org/seats/engineering/CHARTER.md`
  - `org/seats/finance/CHARTER.md`
```

After:

```diff
  - `org/seats/chief-of-staff/CHARTER.md`
  - `org/seats/operations/CHARTER.md`
  - `org/seats/marketing/CHARTER.md`
  - `org/seats/revenue/CHARTER.md`
  - `org/seats/engineering/CHARTER.md`
  - `org/seats/finance/CHARTER.md`
+ - `org/seats/delivery/CHARTER.md`
```

One line. The index exists so a cold session can find every charter the
chart names without walking the whole `org/` tree; a seat missing from this
list is exactly as hard to find as a seat missing from the chart entirely.

## 3. `org/models.yml`, the duty map

Before, the end of the `duties:` block:

```diff
  duties:
    chief-of-staff-chair:        reasoning  # turning a ruling into a mission packet, and owning handoff/session-log discipline, is judgment work by its nature
    operations-sweeps:           scanning   # freshness passes across the registers - cheap, frequent, fully disposable
    operations-meeting-brief:    reasoning  # a convened seat's own position brief at a meeting is judgment, the same as the chair's
    marketing-content:           building   # strategy, briefs, drafted copy, content production
    revenue-drafting:            building   # compliance-gated outbound drafts and candidate-row research
    engineering-plans:           reasoning  # a build plan a lighter tier will execute unattended is the single artifact where a mistake is most expensive
    engineering-builds:          building   # executing an already-approved plan
    finance-ledgers:             building   # ledger entries and the projection-before-launch habit
    general-counsel-drafting:    reasoning  # deciding what a clause says or what it exposes you to is the judgment call; mechanical fill-in after that call is settled runs at building tier inside the same convening, never on its own
    standards-guard-judge:       building   # the one bounded judgment call per deliverable; the deterministic checks beside it are not model-tiered at all
    innovation-desk-scoring:     scanning   # scoring a ranked inbox when the desk convenes
    research-and-indexing:       scanning   # cards built out of banked material, checking what is still current, wide sweeps of the open web
```

After, with two duty rows added for the new seat:

```diff
  duties:
    chief-of-staff-chair:        reasoning  # turning a ruling into a mission packet, and owning handoff/session-log discipline, is judgment work by its nature
    operations-sweeps:           scanning   # freshness passes across the registers - cheap, frequent, fully disposable
    operations-meeting-brief:    reasoning  # a convened seat's own position brief at a meeting is judgment, the same as the chair's
    marketing-content:           building   # strategy, briefs, drafted copy, content production
    revenue-drafting:            building   # compliance-gated outbound drafts and candidate-row research
    engineering-plans:           reasoning  # a build plan a lighter tier will execute unattended is the single artifact where a mistake is most expensive
    engineering-builds:          building   # executing an already-approved plan
    finance-ledgers:             building   # ledger entries and the projection-before-launch habit
    general-counsel-drafting:    reasoning  # deciding what a clause says or what it exposes you to is the judgment call; mechanical fill-in after that call is settled runs at building tier inside the same convening, never on its own
    standards-guard-judge:       building   # the one bounded judgment call per deliverable; the deterministic checks beside it are not model-tiered at all
    innovation-desk-scoring:     scanning   # scoring a ranked inbox when the desk convenes
    research-and-indexing:       scanning   # cards built out of banked material, checking what is still current, wide sweeps of the open web
+   delivery-account-tracking:    building   # day-to-day register upkeep across active wholesale accounts - cheap, frequent, disposable if wrong
+   delivery-renewal-risk-review: reasoning  # flagging an account as trending toward non-renewal is a pattern judgment read against history, not a lookup, so it claims reasoning per the escalation rule
```

Two rows, split the same way Engineering's two duties already split in the
default roster: the frequent, cheap-to-redo work at building tier, and the
one judgment call that earns reasoning tier on a reason written beside it
rather than by habit.

---

## What this diff does not touch

No gate moved. No seat's read scope widened. No row anywhere in
`org/ORG_CHART.md` §4 (which function gates which flow) changed: the
standards-guard still gates every seal, including this seat's, on the same
terms as every other seat's. Adding these three rows is the entire
footprint. Everything else in the chart and the duty map is exactly as
shipped.
