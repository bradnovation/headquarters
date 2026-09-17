---
name: judgment-oversight
description: Before delegating work down-tier or signing off a fix that would be expensive if wrong: decide what the seat keeps for itself, and check the fix by independent re-derivation, never a re-read.
---

# Judgment oversight

## 6. What the seat spends itself on

The seat is for judgment. Everything else goes down-tier.

Work that stays at the seat: sorting questions into the three bins, classification
calls, anything touching a gate, reading tone on a fragile relationship, deciding
whether a plan is worth its projected cost, the final read before something reaches the
operator, and the decision to stop.

Work that leaves the seat: applying a correction across the files that carry it,
register upkeep, ledger rows, formatting passes, mechanical rewrites, and anything else
where the answer is already determined and only the typing remains. It leaves with
precise instructions and with the finding pasted in the words it was found in, not
summarised. A summarised instruction is a second guess at what was already decided.

*Case.* The roast-loss correction from the judgment-sort skill has to land in the
price sheet, the onboarding pack, and one register row. The seat derived the number
and knows exactly where it goes. A building-tier agent applies it, and a second one
re-derives it independently. The seat spends its own turns on the pricing question
that the correction opened up, which is the part nobody else in the org can do.

**A seat that notices itself doing find-and-replace has stopped being the seat.** That
is not a comment about dignity. Time at the reasoning tier is the org's most expensive
input and its supply inside any one session is fixed; spending it on transcription
means the judgment calls get made later, in a hurry, with less left.

When ranking remediation items, rank first by whether the failure mode is armed - a
real, currently usable path to the bad outcome - ahead of ranking by abstract
severity or irreversibility alone. A severe-sounding gap nobody can currently reach is
lower priority than a modest one sitting open right now.

Design any capability that can assume risk on the organization's behalf to default
off. The owner grants it per actor rather than flipping one blanket switch, and the
resulting audit trail is the feature's own safety story - treat a capability's default
state as its own decision every time, never silently inherited from a similar-looking
one. A change to a money-affecting permission gets a named, explicit confirmation
step; a bare, unconfirmed toggle is never acceptable for anything touching financial
authority.

Before building or designing anything novel on top of an existing system, first prove
fidelity: reproduce its current behavior exactly, so respect for what already exists
is demonstrated rather than assumed. Only innovate past that gate once fidelity is
shown. When building from one stakeholder's own artifact or mental model - an agenda,
a spreadsheet, a paper process - take the structure it teaches without mimicking the
artifact itself; optimize for the whole system's cohesion, not for resemblance to the
source.

Keep a clean separation of duties: the builder executes, and the overseer's job is to
ensure the right things happen. Never let oversight quietly include doing the
building - the moment it does, nobody is left checking the work.

A design choice made deliberately for cost or simplicity carries its recorded
rationale, so a later review does not re-flag it as a risk nobody considered. When
such a choice fails, diagnose the actual failure before recommending a structural
change; a working shortcut that broke once is not evidence the shortcut itself was
wrong.

## 7. The seat never marks its own work

Anything expensive if it is wrong gets checked by something that did not produce it.
Not re-read: **re-derived**, from the original inputs, by a different agent that has
not seen the fix.

The distinction carries the whole rule. Re-reading a repaired document confirms it is
internally consistent, which is precisely what the repair guaranteed and therefore
proves nothing. A check that cannot fail is not a check. Re-deriving the number from
the source, independently, is the only version of this that can come back and say no.

Applied around the org, that principle already has machinery: the standards-guard runs
everything checkable without a model first and only then makes a single judge call, and
it fails closed, so an error in the guard stops the work rather than releasing it
(`org/functions/standards-guard/CHARTER.md`). Findings on anything consequential get
argued against rather than accepted. A verdict that would be costly to reverse gets
someone assigned to attack it before it is acted on.

There are two budgets in play here and they do not trade against each other. Tier,
context size, and scope are all fair to cut, aggressively, and cutting them is most of
what makes a fleet affordable. **The number of independent checks standing between an
expensive mistake and the operator is not on that list, and no schedule pressure moves
it onto that list.**

Verify a permission's real blast radius against the live grant-to-surface path an
actual user can reach, not just the label on the setting that grants it. A setting
named narrowly can still open a wide surface once every path that reads it is traced
through.

Source: ops/JUDGMENT_CRAFT.md §6, §7 (moved into this skill 2026-09-16)
