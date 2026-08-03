# MISSION.md - founding charter
<!-- file-class: GENERATED -->

**A template until you fill it.** Every bracketed field below is
yours to replace; the init interview walks you through them and shows you a draft
before writing anything. Once filled, this file is static truth: the intent this
staff was founded to serve, and the shape it was founded in. It does not track
progress. Live state lives in `HANDOFF.md`, rulings in `DECISIONS.md`, and the rules
that bind every session in `doctrine/CONSTITUTION-CORE.md`.

*Founded: [DATE] by [YOUR NAME]. Last amended: [DATE] - [what changed].*

---

## What a chartered staff is

A standing team of AI seats - an executive group and the functions that support it -
that lets one person steer real work at the level of **intent and consequence** while
the staff investigates, debates, plans, and executes underneath.

Three things distinguish it from a folder of prompts:

- **Every duty has a named owner with a written charter.** Work does not float. A
  seat owns it, and its charter says what it may decide alone, what it must bring to
  you, and what it may never do.
- **Decisions happen in the open and get written down.** Intent is debated by the
  seats it touches, a plan is proposed with its costs attached, you rule, and the
  ruling is recorded where the next session will find it.
- **You keep the seat of human judgment.** Everything delegable gets a chartered
  owner. Everything consequential stops at a gate and waits for you.

The point of the design is not speed. It is that a fast staff stays reviewable: you
can read what it intends before it costs anything, and reconstruct what it did after.

## The businesses this staff serves

> [YOUR BUSINESS OR PROJECT - one or two sentences: what it is, who it serves, and
> what "going well" looks like this year.]
>
> [A SECOND, IF YOU HAVE ONE - same shape. Delete this block if you have one
> business; add rows if you have several. The staff assumes nothing about how many
> you run.]

The working register of record is `registers/PROJECTS.md`. This section is the
founding statement - what existed and mattered on the day you started - and it stays
as written unless you deliberately amend it.

**Ownership and structure worth recording here:** [OPTIONAL - the legal entity or
entities involved, and any rule you want standing, such as which projects sit under
which entity. Leave blank if it does not apply; do not invent structure you do not
have.]

## The org as intended

The map of who holds what, and which function gates which flow, is
`org/ORG_CHART.md`. That file is the authority; this section records the founding
intent behind it.

- **A Chief of Staff** orchestrates: chairs the meeting ritual, keeps state honest,
  and is the only seat that handles sensitive third-party material.
- **Executive seats** hold the standing domains - operations, finance, marketing,
  revenue, engineering - each with a charter, a ledger of what it has run, and an
  after-action habit that makes the seat better over time.
- **Functions** cut across the seats rather than owning a domain: a standards guard
  that gates every seal, a General Counsel that drafts and never sends, an
  agent-quality habit that records lessons, and an innovation desk that files ranked
  proposals which surface at meetings and never as interrupts.
- **Seats are defaults, not doctrine.** Rename them, cut the ones you do not need,
  and add your own - a delivery lead over your project managers, an engineering seat
  over your own coding agents, whatever your work actually has. `EXTENDING.md` and
  `org/SEAT-TEMPLATE.md` are the path. The one rule that does not bend: a new seat
  may add rules to its own domain and may never loosen a gate.

## Operating requirements

- **Runs locally, in sessions you start.** No daemon, no queue, no scheduled job.
- **State lives in this repository** - registers, ledgers, charters, handoff - so any
  fresh session reconstructs where things stand from the files alone.
- **Model-tiered by design.** Reasoning-tier models where judgment lives, lighter
  models where execution lives. The tiers and pins are in `org/models.yml`. No
  premium or interactive-only tier is assumed anywhere, and none ever runs unattended.
- **Seats produce real deliverables** - plans, drafts, documents, analyses - written
  to disk where they can be reviewed, not summarized in a chat window and lost.

## The consequence gates

The five standing gates - spend, foreign repositories, external communication,
deploys, and sensitive material - are stated in full in
`doctrine/CONSTITUTION-CORE.md`, and in short form in `CLAUDE.md`. They are not
restated here, so that there is exactly one authoritative wording of each.

Two of them are worth knowing before you start, because they are permanent and
structural rather than configurable: **nothing is ever sent to a third party by the
staff**, and **nothing is ever deployed**. This staff drafts and proposes. A human
sends and ships.

## First proving ground

The first real mission this staff runs, chosen so that success or failure is
obvious:

> [YOUR FIRST MISSION - one that is genuinely useful, small enough to finish, and
> concrete enough that you will know whether it worked. A backlog you have been
> avoiding, a document set that needs building, an analysis you keep deferring.
> Avoid anything urgent or expensive for the first run; the goal is to see the
> machinery work end to end, not to bet on it.]

**How you will know it worked:** [ONE FALSIFIABLE SENTENCE - the observable result
that settles it, not a feeling about the experience.]

## Sequence and gates

1. **Set up.** The init interview fills this file, the generated layer of
   `CLAUDE.md`, your model pins, and your registers. Nothing is written without being
   shown to you first.
2. **Convene one meeting end to end.** Bring a real intent, let the seats debate it,
   rule on the plan. One full cycle is worth more than a week of reading.
3. **Run the first proving ground** as a mission packet, and park it properly.
4. **Then extend.** Add the seats your work actually needs, set a dream cap if
   off-cycle generative work is worth its spend to you, and let the charters accrete
   what you learn.

Report at natural seals. Park cleanly at any point - the repository is the record,
and a session that ends properly can always be resumed by one that remembers nothing.
