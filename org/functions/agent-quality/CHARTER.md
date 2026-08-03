# Agent-quality (function)

<!-- file-class: DOCTRINE -->

*Compares a charter as it was written against that charter as it was actually
run. v1 is a recorded habit rather than machinery: one honest note when a
mission seals, gating nothing.*

## Mandate

An agent opening a charter treats it as correct. That assumption is usually
close enough to true, and the places where it is not true stay invisible from
inside the run. They show up only afterward, when somebody sits down and puts
in writing what the brief actually did to whoever was following it. Left alone,
that writing never happens: the mission seals, attention moves to the next
thing, and a paragraph that cost an agent twenty minutes of confusion survives
untouched because nobody recorded the confusion.

The purpose of this function is to lift that recording out of the category of
good intentions. v1 stops there deliberately. It is not a performance review;
there may be nobody in the org to review but you. It runs no metrics against
any agent. What it judges is charters, using the missions that ran under them
as evidence, one note at a time, so that whenever a growth phase becomes worth
building there is accumulated evidence to build it from instead of
recollection.

Nothing here carries an agenda. v1 has no register, no ranked inbox and no
scoring rubric. The habit is the artifact, and it lives in the ledger of
whichever seat the mission belonged to.

## Convening

One trigger, one convening: a mission seals, and the note is written at that
moment. No schedule stands behind it and no standing chair waits at the meeting
ritual. This function holds no seat. It stays quiet in a debate unless the
question on the table is whether some charter is fit for its job.

Whatever tier the mission was already running at is the tier that writes the
note. A few honest sentences do not justify convening a separate
reasoning-tier pass for them alone.

## Owns

No ledger of its own in v1. What it writes into:

- The `LEDGER.md` of whichever seat held the mission that just sealed, one
  after-action entry per seal.

The tasks register is not its, the innovation inbox is not its, and no
standards-guard artifact is its. Should a later phase hand this function a log
or a charter-revision queue of its own, that gets written into this section
when the thing is actually built, never assumed ahead of the build.

## Read scope

Public and internal-business material, and nothing above it: the packet and
state files of the mission that sealed, the charter and ledger of the seat that
owned it, and any ruling bearing on the work. Material classified restricted or
third-party-sourced stays out of reach here, as it does for everything but the
one seat that handles it in live, attended sessions. Writing an honest note has
never required that material anyway. Where a mission's substance is sensitive,
the note describes the shape of what happened and leaves the sensitive content
unquoted.

## Deliverables and gates

One deliverable exists: the after-action note, a short dated entry appended to
the owning seat's `LEDGER.md`. Because it stays inside the repo and travels
nowhere, no standards-guard pass is required before it is written. The voice is
still the plain, declarative one used everywhere else here, and a note reading
as either careless or self-congratulatory is itself a finding for the next note
to catch.

Money and liability language stays out of these notes entirely. Where a failure
mode touches spend or exposure, that fact routes where it normally would, to
the blocked-on-operator register or to the counsel function, and the note
records only that the routing happened. This function sends nothing, builds
nothing and spends nothing: no send path, no build path and no spend path
exists here at all. Honesty is the requirement that stands in their place. A
note recording only what worked has failed at its one job; where the charter
fought the agent is the part that has to reach the page.

Three things get covered, a few sentences each:

1. **Where the brief held up.** The parts that fit this mission as written and
   needed no interpretation on the fly.
2. **Where the brief and the agent pulled against each other.** Scope that was
   never granted, wording open to two readings, a gate that held longer than
   the risk warranted, whole sections nobody opened because they answered some
   question other than the one actually in front of the agent.
3. **One candidate change.** A single specific edit, to the charter or to a
   register's format. One, small, and named. Not a list of wishes.

## The lesson-typing discipline

Findings in an after-action note are not interchangeable, and treating them as
one undifferentiated pile throws away the most useful thing about them. Any
genuine failure lesson, meaning an actual miss rather than ordinary friction,
gets assigned exactly one of three types:

- **Guard.** The remedy is a hard rule stopping this specific mistake from
  happening twice: a deterministic check, a gate, a clause closing the precise
  hole that opened. Lessons of this type are repaired in place, in the charter
  or the process, by whoever writes the note.
- **Inoculate.** The remedy protects the whole class of mistake rather than the
  single occurrence: a pattern folded into a shared template so everyone using
  that template afterward is covered, or a principle written once somewhere
  enough charters read that it spreads without per-charter repetition. Lessons
  of this type belong at the template or doctrine layer, not in the one charter
  that surfaced them.
- **Reveal.** The failure pointed at something this function has no business
  repairing: a need nobody had named, work nobody had proposed, a hole in what
  the org offers rather than in how it runs. Nothing gets repaired here. The
  lesson is written up as a short proposal and handed to the innovation inbox
  for scoring on its next ordinary cycle. Never patched inline, never raised as
  an interrupt, and never quietly relabelled guard or inoculate because that
  would have been the faster thing to write down.

Getting the type right is worth more than getting the fix out fast. Call a
reveal a guard and some charter acquires a rule it never needed while the
opportunity underneath goes nowhere. Call a guard a reveal and a five-minute
edit takes a trip through a scoring cycle for no reason. Where a lesson
genuinely straddles two types, write that down instead of forcing the choice;
an ambiguity recorded honestly serves the next reader better than a confident
wrong label.

## Standing constraints

- v1 ships no eval loop, no scoring, no automated charter-revision mechanism
  and no re-pin tooling for whatever model or prompt layer sits under this
  product. All of it is deferred on purpose, and nothing above smuggles any of
  it back in wearing a different name.
- Rulings on charter changes are not this function's to make. It puts
  candidates on the table: guard and inoculate lessons as small proposed diffs,
  reveal lessons routed to the innovation inbox. A charter is revised only by
  you, through the meeting ritual.
- No standing presence at the meeting ritual. This is a function rather than a
  seat, and mission seals are the only thing that convene it.
- The habit applies to this charter too. Whichever seat runs into friction with
  it writes that friction up in the same after-action note any other charter
  would get; there is no separate instrument reserved for judging the judge.

## Later phases (not built in v1)

Written down so the direction stays visible while none of it is built:

1. **Eval loops.** Once notes accumulate across enough missions, the pattern
   across them supports a lightweight recurring review, still triggered by hand
   or by a dream run rather than standing on its own, that reads the collected
   ledger entries and flags any charter showing the same friction repeatedly.
2. **Charter-revision proposals.** When the eval loop or a cluster of notes
   makes a pattern unmistakable, this function drafts the diff it would make
   and never applies it. The draft arrives at the meeting ritual as intent like
   anything else, and you rule on it under the same discipline every other
   change to this org goes through.
3. **A re-pin procedure for the prompt and charter layer.** Whatever discipline
   this product already uses when a model pin moves (edit, re-run a known case,
   diff the result for drift, commit with a written record of what moved and
   why) applied with equal rigor to a charter edit.

None of the three exists. This section states a direction; it is not a queue.
