<!-- file-class: GENERATED -->

# ORG_CHART

*The organization at a glance: who holds intent, who holds a charter, and who
gates what. File class GENERATED - the onboarding interview seeds this map from
your answers, and it is yours to edit from then on. The gate rules in section 4
restate doctrine: you may add a gate in your own copy, you may never remove one.
See `EXTENDING.md` before you change anything here.*

---

## 1. The shape

This organization has no seat for the operator, because the operator stands
outside it and over it. Everything chartered below runs one conversion, in both
directions of it: intentions you hold become work someone executes, and rulings
you make become records the next session can read. Nothing below convenes
itself, and nothing below outranks the operator's word.

Read what follows as a map rather than a chain of command: no seat answers to
another seat. Seats come together as peers at the meeting
(`org/STAFF_MEETING.md`) and work against mission packets you have already
ruled on, under `missions/`.

```
                          THE OPERATOR
            all intent starts here, all rulings end here, and
               nothing downstream moves without your word
                               |
              -------------------------------------
              |                                   |
       CHIEF OF STAFF                  DECISIONS.md / HANDOFF.md
     (chairs the meeting;               (the operator's word and
      org/STAFF_MEETING.md)              the live state, written down)
              |
  ------------------------------------------------------------------
  |             |            |             |               |
OPERATIONS   MARKETING    REVENUE     ENGINEERING       FINANCE
 (seat)       (seat)       (seat)       (seat)           (seat)
                                             (the sixth seat, Chief of Staff,
                                              is drawn one row up)

      FUNCTIONS - nothing of their own to push; each stays quiet until
                  something inside its domain comes up
  ------------------------------------------------------------------
  |                  |                    |                   |
STANDARDS-GUARD  GENERAL COUNSEL     AGENT QUALITY      INNOVATION DESK
(gates every      (drafts only,       (notes work once   (ranked inbox;
 seal)             never sends)        it is done)        dreaming, disarmed)
```

The two rows above differ in what they carry. A seat holds state that persists
between sessions and takes a chair whenever the staff convenes; there are six of
them. A function holds a charter and gets called in, sometimes as a gate that
work has to clear, sometimes as a service a seat asks for; there are four. In
between those calls a function has nothing of its own to advance and nothing to
say.

**Seat names are defaults, not doctrine.** Rename any of them to match how you
already talk about your business. What makes a seat real is its charter file
plus its row in the tables below plus its duty row in `org/models.yml` - never
its name. Nothing in the constitution keys off a seat's label.

---

## 2. Seats

| Seat | Mandate, one line | Default tier | Charter | Ledger |
|---|---|---|---|---|
| Chief of Staff | Chairs the meeting, turns ruled intent into mission packets, owns handoff and session-log discipline, sole steward of sensitive material. | reasoning | `org/seats/chief-of-staff/CHARTER.md` | `org/seats/chief-of-staff/LEDGER.md` |
| Operations | Owns the registers - `registers/PROJECTS.md`, `registers/TASKS.md`, `registers/BLOCKED_ON_OPERATOR.md` - and runs freshness sweeps when the operator asks for one, never on a schedule. | scanning (reasoning at the meeting) | `org/seats/operations/CHARTER.md` | `org/seats/operations/LEDGER.md` |
| Marketing | Content, positioning, and voice. Every fact traces to a named source; nothing is invented to fill a gap; writing rules are enforced through the standards-guard. | building | `org/seats/marketing/CHARTER.md` | `org/seats/marketing/LEDGER.md` |
| Revenue | Sales oversight. Compliance check before drafting, every outbound draft queued to the operator, and no send machinery anywhere in the product. | building | `org/seats/revenue/CHARTER.md` | `org/seats/revenue/LEDGER.md` |
| Engineering | Build plans a lighter model can execute unattended and correctly: named required reading, ordered work items, falsifiable verification bars, stated non-goals. | reasoning for plans, building for builds | `org/seats/engineering/CHARTER.md` | `org/seats/engineering/LEDGER.md` |
| Finance | Owns `ledgers/SPEND.md` and the projection-before-launch habit. Drafts and classifies; never files anything with anyone. | building | `org/seats/finance/CHARTER.md` | `org/seats/finance/LEDGER.md` |

Tier names come from `org/models.yml`, which maps duties to model tiers. Building
tier is the default for execution; reasoning tier is used on a stated reason, not
by habit.

---

## 3. Functions

| Function | Mandate, one line | Default tier | Charter |
|---|---|---|---|
| Standards-guard | Whatever can be checked without a model is checked without one, first. Only what survives that reaches a single judge call, held against the standards you wrote down, and its findings come back typed hard or soft. **Fails closed**: a guard error is not a pass, so the work stops there and surfaces to the operator instead of slipping by. | building for the judge call; the deterministic checks are not model-tiered | `org/functions/standards-guard/CHARTER.md` |
| General Counsel | Produces the paperwork you will hand to a lawyer of your own: agreements, scopes of work, engagement letters, notices. Propose-only is structural here rather than configured, because the function holds no transmission mechanism of any kind and there is accordingly no setting to find and switch off. | reasoning | `org/functions/general-counsel/CHARTER.md` |
| Agent Quality | Closer to a habit than to machinery. Every seal ends with the seat that owned the work writing a few lines in its own `LEDGER.md` about how the run actually went, and any lesson worth keeping gets typed. It records. It stops nothing. | not convened as its own run | `org/functions/agent-quality/CHARTER.md` |
| Innovation desk | Ideas arrive in a ranked inbox, get scored where they sit, and are heard at a meeting or not at all; nothing here interrupts you. Its generative mode, dreaming, reaches you disarmed: router item 4 declines every request to run one for as long as the dream cap in `CLAUDE.md` (f) sits unfilled. | scanning for scoring | `org/functions/innovation-desk/CHARTER.md` |

**Two absences worth naming.** Compliance appears nowhere in the tables above,
because it is not the kind of thing a chair can hold: it is built into the gates,
the guards, and the charters themselves, which is to say it is everywhere and
belongs to no single row. Security is missing for a different reason. It runs
through the whole design as a property the Chief of Staff answers for, visible in
the sensitive-material gate and in the security classes set out in
`doctrine/CONSTITUTION-CORE.md`.

---

## 4. Which function gates which flow

| Flow | Standards-guard | General Counsel | Agent Quality | Innovation desk |
|---|---|---|---|---|
| Any mission moving to sealed | **Gates.** No pass, no seal. | Only where money or liability is in play. | Notes it afterward; blocks nothing. | No role. |
| A deliverable carrying money or liability (agreements, pricing, commitments, scope promises) | **Gates.** | **Gates**, as a draft review, in addition to the standards-guard. | Notes it afterward. | No role. |
| Anything outward-facing | **Gates.** | Gates when it commits money or liability. | Notes it afterward. | No role. |
| A new proposal or idea | No role until it becomes work. | No role until it becomes work. | Receives lessons typed as *reveal*. | Ranks it; surfaces it at the next meeting only. |

Four rules sit underneath that table:

- **Nothing seals without the standards-guard.** Authorship is beside the point,
  whichever seat did the writing: a paragraph of positioning and a schema
  migration meet the identical bar. A guard that errors out has passed nothing.
- **General Counsel is the conditional second gate.** Any deliverable that moves
  money or creates exposure goes through it as well as through the standards
  pass, never in place of that pass. What comes back is a reviewed draft and
  nothing further, since the function puts no document into effect, and the
  standing recommend-human-legal-review flag rides along with it.
- **Agent Quality holds no stopping power.** Its note comes after the fact. A
  mission may seal while that note is still owed; what the missing note holds up
  is the closing-out of the seal, never the seal itself.
- **The innovation desk sits outside the gating question.** It can neither
  withhold a seal nor confer one. Its single point of contact with everything
  else here is the intent it carries into a meeting.

**The seal rule reduces to this:** the standards-guard passes every seal or
nothing seals; General Counsel joins in whenever money or exposure is at stake;
the note from Agent Quality completes a seal and is never able to withhold one.

---

## 5. Changing this chart

Adding a seat is four small acts, in this order: copy `org/SEAT-TEMPLATE.md` to
`org/seats/<your-seat>/CHARTER.md` and fill it, add the row here, add a duty row
in `org/models.yml`, and create the seat's empty `LEDGER.md`. Removing a seat is
the same four acts in reverse, plus a line in `DECISIONS.md` saying why.

A new seat adds domain rules. It never loosens a gate, and it cannot grant itself
read scope the constitution withholds. The full procedure, the file-class rules,
and the honest account of what happens when you edit doctrine live in
`EXTENDING.md`.

---

## 6. Cross-reference index

Every charter this chart names, by path:

- `org/seats/chief-of-staff/CHARTER.md`
- `org/seats/operations/CHARTER.md`
- `org/seats/marketing/CHARTER.md`
- `org/seats/revenue/CHARTER.md`
- `org/seats/engineering/CHARTER.md`
- `org/seats/finance/CHARTER.md`
- `org/functions/standards-guard/CHARTER.md`
- `org/functions/general-counsel/CHARTER.md`
- `org/functions/agent-quality/CHARTER.md`
- `org/functions/innovation-desk/CHARTER.md`

Documents this chart sits inside: `CLAUDE.md` (the entry file and router),
`doctrine/CONSTITUTION-CORE.md` (the gates, the state discipline, the security
classes), `MISSION.md` (your founding charter), `org/STAFF_MEETING.md` (the
ritual these seats convene for), `org/models.yml` (duty-to-tier map),
`org/SEAT-TEMPLATE.md` and `EXTENDING.md` (how this chart grows).
