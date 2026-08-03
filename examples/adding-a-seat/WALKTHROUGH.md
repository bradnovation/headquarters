# Adding a seat: a worked example
<!-- file-class: DOCTRINE -->

*This is a demonstration, not a real seat in the default roster. It follows a
fictional small business (a coffee roastery that sells wholesale to cafes and
restaurants) through `EXTENDING.md`'s four-act procedure for adding a seat,
step by step, so the procedure can be checked against a finished result
rather than taken on faith. The finished charter lives in `CHARTER.md`
alongside this file, its empty ledger in `LEDGER.md`, and the exact chart and
duty-map changes in `org-chart-diff.md`. Nothing here touches the product's
own shipped `org/ORG_CHART.md` or `org/models.yml` - those stay the default
six-seat roster. This bundle only shows what changing them would look like.*

---

## The moment the need shows up

The roastery runs on the default roster: a Chief of Staff, Operations,
Marketing, Revenue, Engineering, Finance. That roster covers a business that
sells one way, direct to a single kind of customer. This one does not. Beside
the retail side, it carries a growing list of wholesale accounts - cafes and
a few restaurants that take a standing delivery every week or two, each on
its own cadence, each due for a renewal conversation before its contract
lapses.

Nobody currently owns the shape of that work end to end. Operations owns the
registers in general but does not track a single account's onboarding stage
against its delivery calendar against its renewal date. Revenue owns the
courting of a brand-new account but drops the thread the day the account
signs. Finance sees the invoices but not the schedule behind them. The
roastery's operator notices the same fact three separate ways in one week: an
account that should have renewed a month ago never got a follow-up, because
no seat's mandate actually said "watch this."

That is the shape `EXTENDING.md` calls a normal act, not a fork: a business
has a shape the default roster does not name, and a seat gets added for it.
Here, a Delivery seat: project management over the wholesale accounts,
nothing more.

## Act one: copy the template

The operator's session copies `org/SEAT-TEMPLATE.md` to
`org/seats/delivery/CHARTER.md`, a short lowercase directory name, exactly as
`EXTENDING.md` §2 describes. Every bracketed placeholder gets filled from the
roastery's own facts, and every italic guidance line comes out as it goes,
because those lines are instructions to the person filling the template, not
charter text a convened agent should ever read.

The mandate the session drafts first pass reads close to this:

> This seat exists to hold the standing view of a wholesale account from
> first shipment to renewal or churn. It owns the judgment on where an
> account actually stands, which no other seat holds end to end.

That is the easy part. The harder part of a mandate, per the template's own
guidance, is drawing the boundary against a neighbouring seat, and the first
draft does that too: courting a brand-new account before it signs stays with
Revenue; the account's invoice and payment terms stay with Finance; any
change to what an account is actually charged or promised is a General
Counsel draft, never something this seat decides alone.

## The two checks, applied before filing

`org/SEAT-TEMPLATE.md`'s own closing checklist and `EXTENDING.md` §7 both
apply before a new charter is considered finished. Both get run here, in the
open, because the value of a worked example is showing a check that actually
does something rather than asserting that it would.

**The constitution-wins check.** The first full draft of the Deliverables
section, written quickly, included a line that felt natural for a delivery
seat to have: *"when a shipment is going to be late, this seat lets the
account know."* Read back against `doctrine/CONSTITUTION-CORE.md`, that line
does not survive. Letting an account know is outbound communication to a
third party, and G3 puts every outbound message, however small and however
routine-sounding, on the operator's own side of the line. A seat charter
cannot hand itself a send path by describing the send as small. The line gets
rewritten: this seat drafts the delay notice; the operator sends it or does
not. Nothing about the seat's usefulness is lost by the correction, and that
is the point of catching it at draft time rather than the first time an
account actually gets an unreviewed message.

**The advice-shaped-extension check.** `EXTENDING.md` §7 asks one question of
every new seat: could a reasonable person, reading this seat's output without
context, mistake it for the work of a qualified professional and act on it?
Run against this charter, the answer is no. A renewal-risk flag, a delivery
schedule, an onboarding-stage note: none of it reads as legal, tax, medical,
or compliance judgment, even to a stranger. The moment that would flip the
answer is named explicitly in the charter anyway, because a boundary a
charter does not name is a boundary the next session has to guess at: the day
this seat's notes start reading like a decided change to what an account
owes or is owed, that output has crossed into General Counsel's rail, and the
charter says so rather than leaving it to be discovered the hard way. The
rail does not attach today. It is written down so that if the seat's work
ever drifts toward it, the drift is visible against a stated line instead of
invisible against a silent one.

With both checks run and the draft corrected, the charter is filed as
finished. The result is `CHARTER.md` in this same directory.

## Act two: register it in the chart

A charter nobody can find in the chart is a document, not a seat, per
`EXTENDING.md` §2 (point 2) and `org/ORG_CHART.md` §5. The next act adds one
row to `org/ORG_CHART.md` section 2: the seat's one-line mandate, its default
tier, and the paths to its charter and its ledger. The chart's section 6
cross-reference index gets the same one-line addition, because that index
exists precisely so a cold session can find every charter the chart names
without searching the whole tree.

Both edits, shown as they would actually land against the shipped chart, are
in `org-chart-diff.md`.

## Act three: add a duty row

`org/models.yml` is where a duty gets its tier, and `EXTENDING.md` §2 (point
3) calls this act out on its own because a seat with no duty row has nowhere
for a convened agent to look up what it should cost to run. The roastery's
Delivery seat splits its own work the same way Operations and Engineering
already do in the default roster: the everyday register upkeep is building
tier, cheap and frequent, while the judgment call of flagging an account as
trending toward non-renewal (a pattern read against history, not a fact
looked up) claims reasoning tier, with the reason written in the comment
beside the row exactly as the escalation rule requires.

Both duty rows, as they would land in the shipped file, are also in
`org-chart-diff.md`.

## Act four: create the ledger

The last act is the smallest and the easiest one to skip, which is exactly
why the template calls it out as its own numbered step. An empty
`org/seats/delivery/LEDGER.md` gets created the same session, two lines of
format prose and nothing else, so that the day the seat's first piece of work
seals, the after-action note has somewhere to land instead of waiting for
someone to remember to create the file first. The empty ledger, exactly as
act four produces it, is in `LEDGER.md`.

## What changed, and what did not

Four files moved: a new charter, one new row in two places in the chart, two
new lines in the duty map, one new empty ledger. Nothing about the five gates
moved at all. The seat can watch a wholesale account more closely than any
existing seat could, and it still cannot send a message to one, still cannot
change what one is charged, still cannot deploy anything, still cannot read
the vault, and still answers to the same standards-guard every other seat's
work answers to before anything is called sealed. That is what "extending
adds, it never loosens" looks like when it is actually followed rather than
just stated: a business gets a seat it needed, and the floor underneath every
seat stays exactly where it was before the roastery ever needed one.
