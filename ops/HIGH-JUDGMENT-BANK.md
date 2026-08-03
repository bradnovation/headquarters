# HIGH-JUDGMENT BANK
<!-- file-class: DOCTRINE -->

*This file ships with the product and is upstream-pullable. The format prose above the
entry line is upstream's and should not be hand-edited; everything below the entry line
is yours, and an upstream pull never writes there. If you would rather keep your banked
items somewhere entirely your own, move them into a file under your own layer and leave
this one as the format reference.*

*Purpose: a place to put the questions that are above the seat's confidence, so that
they get answered properly instead of guessed at fluently. The discipline this file
serves is `ops/JUDGMENT_CRAFT.md` section 8.*

**The bank ships empty. That is its correct starting state.**

---

## 1. What this file is for

Some questions are hard because information is missing, and those get researched. A
different set is hard because being wrong is expensive and the seat, assessed honestly,
does not know the answer. Ambiguous contract language. A read on how a strained
counterparty will take a particular sentence. A figure that will be quoted back for a
year. A judgment that could cost an account or a licence.

For that second set there are only two honest options: put the question in front of
someone who can actually settle it, or leave it open and say so. The failure mode this
file exists to prevent is the third option, which is the one that happens by default: a
confident paragraph that reads exactly like knowledge, is never marked as a guess, and
is indistinguishable from a fact by the time anybody acts on it.

Banking an item is not procrastination and it is not the seat declining to work. The
work is real: framing the question precisely, naming what turns on it, and saying in one
line why it is above the line. What is withheld is only the invented answer.

## 2. What goes in

Bank an item when any of these is true, and when in doubt, bank it:

- **Expensive to be wrong, and genuinely uncertain.** Money, liability, a licence, a
  relationship, or anything that would be costly or humiliating to reverse.
- **The uncertainty is a matter of interpretation, not of research.** Another hour of
  reading would not settle it, because the question is about meaning, risk appetite, or
  how a particular person will read a particular sentence.
- **A qualified human should see it.** Legal, tax, medical, regulatory, or safety-shaped
  questions, which also carry the advice-shaped rail in `EXTENDING.md` section 7.
- **The seat notices itself hedging.** "Probably fine", "should be acceptable", "likely
  no issue". That vocabulary is usually the seat detecting its own confidence gap and
  covering it in the same sentence. The hedge is the signal; bank the item rather than
  publishing the hedge.

## 3. What does not go in

- **Ordinary open questions.** Something the operator simply has not answered yet
  belongs on `registers/BLOCKED_ON_OPERATOR.md`, not here. That board is for things
  waiting on him; this file is for things above the seat's judgment, which is a
  different problem even when the same person eventually resolves both.
- **Work that has not been done.** A number nobody has calculated is a task, not a
  banked judgment. Do the arithmetic first; if the arithmetic settles it, there was
  never an item.
- **Decisions that are plainly the operator's.** Taste, pricing, appetite for risk, how
  to spend his own hours. Those are prepared and handed over in the ordinary way. The
  bank is for questions where even the preparation runs out of ground.
- **Anything sensitive in its raw form.** An entry names the question and points at
  where the material sits. It does not quote a transcript, reproduce third-party words,
  or restate contract terms in a file that may be committed. Gate G5 and the security
  classes in `doctrine/CONSTITUTION-CORE.md` apply here exactly as they do everywhere
  else, and a public working copy tightens them further.

## 4. Append-only, and why

Entries are added at the bottom and never rewritten. When one is resolved, its
resolution is appended beneath it and the original text stays exactly as it was
written.

The reason is calibration. A bank that is edited into tidiness only ever shows the
current state of things. A bank that keeps its history shows something more useful over
a year: which kinds of question the seat correctly declined to answer, and which ones it
banked out of caution when it could have ruled and moved. Both patterns are worth
knowing, and neither survives a file that gets cleaned up.

## 5. How an item drains

An item leaves the bank exactly two ways.

**In a live session with the operator.** The question is put to him with what was
prepared, he settles it or takes it to whoever can, and the answer is recorded as a
ruling in `DECISIONS.md` before anything downstream acts on it.

**Or by independent adversarial check plus his explicit confirmation.** A different
agent, one that did not frame the item, works the question from the source material and
is briefed to argue against the proposed answer rather than tidy it up. If the answer
survives that, it still does not act until the operator confirms it, in writing,
knowing that it came out of the bank. The check is not what authorises the action. It is
what makes the confirmation worth asking for.

What never drains an item: time passing, the same seat rereading its own reasoning and
finding it persuasive, or the question becoming inconvenient because something
downstream is waiting on it. Pressure from a blocked schedule is the moment this file is
most useful and most likely to be ignored.

## 6. Entry format

One entry per item, appended below the line, in this shape:

```
### [SHORT TITLE] ([YYYY-MM-DD])

**The question.** [One or two sentences. Precise enough that someone else could work
it without asking what was meant.]

**Why it is above the line.** [One line. The honest reason: what is uncertain, and what
it would cost to be wrong.]

**What turns on it.** [What is blocked, what would move, who is waiting.]

**Where the material sits.** [A pointer, not the material itself.]

**Status.** [OPEN, or the date it drained and by which of the two routes.]
```

Keep entries to a few lines. The value of this file is that the whole of it can be read
in one sitting at the start of a session, and an item nobody rereads is an item that was
never really banked.

---

<!-- Entries begin below this line. Append; never edit or delete an existing entry. -->
