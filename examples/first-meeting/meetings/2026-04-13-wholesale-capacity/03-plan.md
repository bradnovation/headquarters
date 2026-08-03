# 03-plan - WORKED EXAMPLE - fictional
<!-- file-class: DOCTRINE -->

*Worked example. Drafted by the chair at reasoning tier, then put through the
pre-ruling adversarial pass. Every finding that pass returned is shown in section
6, and each one is also marked inline at the place it was applied. Both blocking
findings were resolved before this document was put in front of the operator.*

---

## 1. Proceed-on-default

**This plan assumes every row of the table in section 4 at its recommended
default.** One word approves the whole table; ruling row by row, or overruling
some rows and accepting the rest, costs no more. The typing is what makes "go"
safe: on `[judgment]` rows the operator accepts reasoning that is on the page and
can be overruled; on `[fact]` rows no default answers anything, because a default
that answered a fact about his own business would be a fabrication wearing a
recommendation's clothes.

## 2. The mission

One mission, one owning seat: **`missions/wholesale/capacity-and-terms/`, owner
Operations.** Operations owns it because the measurement gates everything else in
it. Revenue contributes the counter-offer and General Counsel the term sheet;
neither co-owns. Shared ownership means nobody owns it.

| # | Deliverable | Contributed by |
|---|---|---|
| D1 | One week of measured usable roast hours, logged by shift, against the machine's rated hours | Operations |
| D2 | Capacity model in two variants, single shift and two shift, each stated against the working-capital ceiling the operator supplies | Operations |
| D3 | Counter-offer draft, with every volume figure carrying both its source and its cash consequence | Revenue |
| D4 | Term sheet skeleton: exclusivity, volume ceiling with a named ramp trigger, termination notice sized to unwind green coffee | General Counsel |
| D5 | Register consequences: task row, wholesale-line concentration risk, and any operator dependency posted the day it appears | Operations |

**A note on D1.** Operations asked for the usable-hours figure as a `[fact]` row.
It is not one. A fact row asks for something only the operator holds; this is
something a week of logging produces, so it became a deliverable instead of a
question. That is the same mistake as converting a fact into a judgment, pointed
the other way, and it is the smaller of the two.

## 3. Sequencing

1. **D4's clause structure starts immediately.** Its shape does not depend on the
   volume number; only its blanks do.
2. **D1 runs for one calendar week.** Nothing downstream of the number moves
   until it lands.
3. **D2 is built from D1**, in both variants, each against the ceiling from table
   row 6.
4. **D3 is drafted once D2 lands, and queued for the operator.** *(Adversarial
   finding A2, applied here.)* The draft plan said the counter was sent to the
   buyer once the model landed. There is no send path in this system and no
   version of this plan produces one. The counter is drafted, checked, and put in
   the operator's hands. What happens next is his act.
5. **Each deliverable is gated as it lands**, per table row 4, rather than batched
   into one pass at seal.
6. **Seal**, once the standards-guard has passed every deliverable and General
   Counsel has passed D3 and D4, which carry money and liability.

## 4. The rulings table

| # | Type | Ask | Recommended default |
|---|---|---|---|
| 1 | `[judgment]` | Counter for the full order on a phased ramp, or cap the account at partial volume permanently? Revenue holds the first position, Operations the second. | **Phased ramp, with a written ceiling and a named trigger for step two.** *(Adversarial finding A3, applied here.)* Revenue is right that a permanent cap declares our ceiling to the buyer forever. Operations is right that a ramp with no trigger is a promise this business has no mechanism to keep. The ceiling and the trigger are what make the ramp the safer option; without them the chair would recommend the cap. |
| 2 | `[judgment]` | Build the capacity model before drafting terms, or in parallel? | **Model first for anything that carries the number; clause structure in parallel.** Drafting a volume-bearing document twice costs more than waiting a week to draft it once. |
| 3 | `[judgment]` | Draft the term sheet now with flagged blanks, or wait for the facts? | **Now, with blanks.** Propose-only by structure, nothing leaves the operator's hands, and a skeleton with three flagged blanks is filled in an hour once the facts land. |
| 4 | `[judgment]` | Gate each deliverable as it lands, or run one pass at seal? | **Each deliverable.** A single pass at the end batches every finding into the least convenient moment of the mission. |
| 5 | `[fact]` | Does the operator want this buyer at all, given that they become the largest single line in the wholesale book? | Safe provisional: the model and the drafts are built, and nothing is prepared for release, no volume is committed, and no figure is quoted to anyone until he answers. |
| 6 | `[fact]` | How much working capital can be tied up in green coffee across one sixty-day cycle, without touching the storefront's float? | Safe provisional: D2 and D4 build against a clearly flagged placeholder, and every volume figure in D3 carries the placeholder next to it rather than omitting the consequence. |
| 7 | `[fact]` | Will the operator run a second roasting shift, and does he have someone to run it? | Safe provisional: D2 is built in both variants and recommends neither. |
| 8 | `[fact]` | Will he accept any exclusivity restriction, in any territory? | Safe provisional: D4 carries no exclusivity clause at all, plus a flagged note recording that the question is open and unanswered. |
| 9 | `[fact]` | Are the buyer's sixty-day payment terms negotiable? | *(Adversarial finding A1, applied here. This row reached the chair's draft typed `[judgment]`, with a confident default assuming the terms would come down to thirty days.)* Safe provisional: D2 carries a sixty-day and a thirty-day variant and recommends neither. Nothing in any draft assumes a term this staff has never heard the buyer state. |

Every row is typed and every row carries a recommended default. A table missing
either on any row is an incomplete plan and should be sent back rather than ruled
on.

## 5. Cost envelope

*(Adversarial finding A4, applied here: the first draft of this section had no
line for gates and closure, and its total did not rebuild from its phase lines.)*

| Phase | Projected tokens | Projected session wall-clock |
|---|---|---|
| Briefs fan-out (already run, reconciled) | 118K actual against 90K to 140K projected | 26 minutes |
| Adversarial pass, 3 skeptics over the full document set | 60K to 90K | 15 to 20 min |
| D1 and D2, measurement and model | 120K to 180K | 40 to 60 min |
| D3 and D4, drafting | 70K to 110K | 30 to 45 min |
| Gates and closure: per-deliverable passes, General Counsel review, seal, park | 50K to 80K | 20 to 30 min |

**Remaining after the briefs run: 300K to 460K tokens** (60 + 120 + 70 + 50 at
the low end; 90 + 180 + 110 + 80 at the high end), **1 hour 45 minutes to 2 hours
35 minutes of session time**, spread across one calendar week because D1 is a
week of measurement rather than a week of work.

**Whole-meeting total including the briefs run: 418K to 578K.**

**Hard cap: 600K.** The chair's judgment call, labeled as one. It is not derived.
It is the figure above which the chair would rather stop and re-plan than keep
spending on a decision this size.

**Launch discipline.** Every fan-out states three numbers at the launch moment:
projected tokens, projected wall-clock, and a fresh meter reading rather than a
remembered one. A projection over the remaining cap is filed as a written
proposal instead of launched, and long runs do not launch into thin headroom.

## 6. The adversarial pass

This plan did not reach the operator straight from the chair. Three skeptics at
building tier were each handed the whole document set, and none was asked whether
the plan was any good.

| # | Skeptic | Severity | Finding | Where applied |
|---|---|---|---|---|
| A1 | Fidelity | **BLOCKING** | A row asking whether to assume the payment terms were negotiable to thirty days was typed `[judgment]` and carried a confident default. That is a fact about a counterparty nobody here has spoken to. The plan had invented it. | Retyped `[fact]`, re-defaulted to safe provisional. Table row 9. |
| A2 | Gates | **BLOCKING** | Sequencing step 4 read "send the counter to the buyer once the model lands." No send path exists, and G3 puts every outbound message on the operator's own side of the line. | Struck and rewritten. Section 3, step 4. |
| A3 | Fidelity | MATERIAL | Row 1's original default read "phased ramp" flat, quietly resolving the live Revenue-versus-Operations disagreement in Revenue's favour and dropping the ceiling Operations asked for. The disagreement survived into `02-debate.md` and then disappeared. | Default rewritten to carry the ceiling and the named trigger, with both positions named in the row. Table row 1. |
| A4 | Numbers | MATERIAL | The envelope's total did not rebuild from its phase lines, and gates and closure had no line of their own. | Line added, arithmetic shown inline. Section 5. |
| A5 | Numbers and coverage | MINOR | The plan promised a renewal-risk view across all wholesale accounts, and no deliverable produced one. | Struck. A second intent gets a second meeting. |

**Nothing BLOCKING survives to the ruling ask.** A1 and A2 were both resolved
before this document was shown to the operator. Attaching a known blocking defect
to a plan as a caveat does not manage it; it moves it to him.

The honest argument for the pass: every other participant in this ritual gets
read by somebody, and the chair does not. A1 is the failure the protocol names by
name, it arrived on the first attempt, and it would have reached the operator
looking like diligence.
