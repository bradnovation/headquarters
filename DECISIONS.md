# DECISIONS - the rulings ledger
<!-- file-class: PERSONAL -->

*This file is yours. It is written by your sessions on your word, it
is never overwritten by an upstream update, and nothing in it ships back anywhere.*

*This file answers one question: **what has the operator actually decided?** Every
ruling that changes how this org behaves lives here, numbered, dated, and in his own
words. A decision that lives only in a chat window did not happen.*

---

## How this file works

**Numbered, newest on top.** Rulings are numbered sequentially from R-1 and never
renumbered. A reader looking for current policy reads down from the top until they hit
the first entry that answers their question; a reader auditing how a policy came to be
reads up from the bottom.

**Superseded, never deleted.** A later ruling can reverse an earlier one. When it does,
the new entry names the number it supersedes and the old entry gets a one-line
*Superseded by R-n* note appended to it. The old text stays. The history of a reversal
is often more useful than the reversal.

**The operator's words are transcribed verbatim.** When a ruling is given in
conversation, the entry quotes it exactly as he said it, marked as a transcription. A
summary is a paraphrase, and paraphrase is where a decision quietly becomes what the
session wished had been decided. Where the ruling was terse ("yes, do it"), quote the
terse words and record the question they answered directly above.

**A ruling is recorded before its consequences are executed.** Not after. The order is:
the operator rules, the ruling is written here, and only then do statuses flip, packets
fan out, or board items resolve. This is what makes the ledger trustworthy under
interruption - if the session dies between the two, the record still exists and the
next session can finish the job.

**Only the operator rules.** No seat, no function, and no session writes an entry here
on its own authority. A seat can recommend a default and a plan can carry a
recommended-default column; neither becomes a ruling until the operator says so.

**Rulings that arrive through the meeting ritual live in two places.** The meeting's own
ruling file holds it in context; this ledger holds it as org-wide policy. A ruling
recorded in only one of the two is not fully recorded, and closing that gap is the
first job of any session that notices it.

---

## Entry format

```
## R-<n> - <short title> (<YYYY-MM-DD>)

**Question.** One or two sentences: what was actually being asked, and what turned on
the answer.

**Ruling.** The operator's decision. If given in conversation, transcribed verbatim and
marked as such.

**Scope.** What this binds: a single mission, a seat, a class of work, or the whole org.
Say plainly what it does NOT cover.

**Consequences.** What changes because of this - statuses, files, gates, defaults - and
whether each has been executed yet.

**Source.** Where the ruling was given: a meeting's ruling file, a session, a direct
instruction.
```

Keep entries short. The ledger's value is that it can be read end to end in a sitting;
a ledger of essays gets skimmed, and a skimmed ledger is a ledger nobody trusts.

---

## Rulings

<!-- The next ruling goes directly below this line, above the example. -->

---

## EXAMPLE - not a real ruling; delete this block once you have rulings of your own

*This block exists to show the shape. It is invented. The business, the numbers, and
the date are fictional. Nothing in it binds anything.*

## R-1 - Weekly spend cap set; dreaming armed at that cap (2026-03-04)

**Question.** Dreaming ships disarmed: it cannot run until an explicit spend cap
exists, because no default figure is safe to assume on someone else's meter. The
Innovation Desk asked for a cap so exploratory runs could start, and proposed a
conservative number with a per-run projection requirement attached.

**Ruling.** Transcribed verbatim from the session: *"Fine by me, but hold it at the
weekly number, not per run - if one run wants to eat the whole week, I want to be
asked first."*

**Scope.** Binds all exploratory dream runs. Does not touch mission spend, which stays
governed by per-launch projection and the operator's word at launch. Does not authorise
any recurring or scheduled run: there are still no daemons, and arming a schedule would
be a separate ruling.

**Consequences.**
- Weekly cap recorded in `ledgers/SPEND.md`. *Executed.*
- Dreaming's status flipped from disarmed to armed-within-cap in the Innovation Desk's
  charter. *Executed.*
- Any single run projected above half the weekly cap goes to the operator before it
  launches, not after. *Executed as a standing rule in the same ledger.*
- The blocked-board item asking for a cap is resolved. *Executed.*

**Source.** Direct instruction in session; no meeting was convened for it.
