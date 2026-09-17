# GETTING STARTED - your first session, end to end
<!-- file-class: DOCTRINE -->

*A narrative walkthrough, not a mechanism. Everything described here already exists
somewhere in this repository as a file with its own doctrine; this page tells the
story of running that machinery once, in order, and points at the real thing every
time it names one. If a claim here and the file it points to ever disagree, the file
wins.*

---

## 1. What the first sitting actually is

A fresh clone of this repository is a complete staff with no idea whose work it is
doing. Every file marked GENERATED ships as a filled-in shape with the facts left
blank: brackets where your name goes, `[UNSET]` where a spend ceiling goes, an empty
project register, unpinned models. Nothing is broken about that state. It is simply
waiting for one conversation to fill it in.

This walkthrough covers that conversation and the two rituals that bracket every
session after it: orienting when you open one, and parking when you close it. Reading
it takes longer than living it does. The whole first sitting, clone to a parked
repository with a real meeting behind it, comfortably fits inside fifteen minutes of
actual attention; most of that time is you answering questions about your own work,
not waiting on anything.

---

## 2. Clone it, and open a session inside it

There is no signup and no separate account. Install Claude Code first, if you have
not already: the native installer (`curl -fsSL https://claude.ai/install.sh | bash`
on macOS, Linux, or WSL; `irm https://claude.ai/install.ps1 | iex` in Windows
PowerShell), or a package manager (`brew install --cask claude-code`, or
`winget install Anthropic.ClaudeCode`), then confirm it with `claude --version`. Get
your own copy of this repository, most simply with GitHub's **Use this template**
button on the repository page followed by an ordinary `git clone` of the copy it
creates for you; `README.md`'s install section covers the other two paths. Then `cd`
into that directory and run `claude`. Everything downstream, the interview, the
meetings, the missions, runs from files sitting in that same tree. Nothing about
this product lives anywhere else, and nothing calls out to a service you have not
already set up for yourself.

The moment a session opens inside a fresh clone, the read order at the top of
`CLAUDE.md` runs: this file first, then `doctrine/CONSTITUTION-CORE.md`, then
`HANDOFF.md`'s topmost entry, then `DECISIONS.md`'s newest rulings. On a bare clone
that last pair is a placeholder and an empty ledger, which is itself informative: it
tells the session, correctly, that nothing has happened here yet. Because the
generated layer of `CLAUDE.md` still carries bracketed placeholders, the session's own
router points at exactly one thing worth doing first: the onboarding interview.

As of 0.3, the doctrine those rituals run on is invoke-loaded from
`plugins/headquarters-core` rather than kept only in `doctrine/CONSTITUTION-CORE.md`.
It loads automatically from the in-repo `.claude/skills/headquarters-core` symlink
this template ships with, once you trust the folder, or you can symlink it into your
own `~/.claude/skills/` instead so it follows you machine-wide - see
`plugins/README.md` for both routes. The `local-lane` plugin next to it is a separate,
optional add-on: skip it entirely if you don't run local models.

---

## 3. The interview

The interview is a conversation, not a form. It asks about one thing at a time,
listens, reads the answer back in a short line so a misunderstanding costs a sentence
to fix rather than a rewritten file, and only then moves to the next topic. Nine
topics, in a deliberate order: who you are, then whether this copy is public or
private, then your businesses, then where else your context lives, then how you
already work, your values in your own words, your model tiers, your dream ceiling,
and finally the first piece of real work worth running through the whole machine.

**Before any of that, four checks run silently.** The interview will not ask a real
question about your business until it has confirmed the ignore rules exist, that they
actually exclude a sensitive-material directory while keeping that directory's own
readme tracked, and that the readme is there to read. This is the one place in the
whole ritual that fails closed on purpose: an unclear result is treated as a failed
result, and the interview stops and asks for the one missing piece rather than
proceeding on the assumption that you will handle it later. You will see one plain
line confirming the boundary passed, and then the real questions start.

**"I don't know yet" is a complete answer, every time it's true.** A blank left
standing becomes a visible row on the board of things only you can settle, never a
plausible guess that reads like a decided fact six months from now. The interview
would rather carry an open item forward honestly than fabricate a number to keep
moving.

**The consent moment, when it comes up.** If any of your context, about the
business or about your working life, sits somewhere other than this repository,
the interview asks, once, whether such a place exists and where. It handles exactly
one such place at a time, in this order: what it is, what the staff may read it
*for* (a stated purpose, not a general sense that it sounds useful), any part of it
that stays off limits, and then your consent, given in your own words, to that
specific purpose. Only once that is written down and shown back to you does anything
get read from it, and even then it is a plain file read, nothing that touches version
control, and nothing ever written back. A place that never comes up in this
conversation is simply never read. There is no informal tier where a folder gets
opened because its name seemed relevant.

**The dream question.** Off-cycle generative work, the kind that looks for a seam in
your business you have not had time to notice yourself, ships turned off by design.
The interview asks whether it is worth spending on at all and, if so, what ceiling you
want on it, in whatever unit and period you actually think in. It will offer a small
starting figure and say plainly that it is only a starting point, then take whatever
number you actually give. Recording that figure is one condition of three, not an
on switch by itself: a confirmed read scope and a kill switch you have verified
you can operate are the other two, and all three have to hold before anything runs.
Leaving the ceiling unset is a fully supported answer. It just means the honest
answer to "can we let it run tonight" stays no until you decide otherwise.

**Nothing is written on the strength of the conversation.** Every answer you give is
held in the conversation, not on disk, until the write pass. When that pass comes,
each file the interview proposes gets drafted in full, shown to you in full, and then
the session stops. You have exactly two live choices at that point: keep it as
written, or change it. A chat reply is context; your explicit answer to a shown draft
is what turns it into a file. Nothing changes on disk between one topic and the next,
which means an interrupted sitting loses nothing: whatever was actually approved and
written stands, and whatever was still bracketed stays bracketed until you come back.

By the end, if you carried the interview through, your founding facts sit in a small
number of places: the generated section of `CLAUDE.md`, your founding statement in
`MISSION.md`, your model pins, a first project register, and a founding ruling in
`DECISIONS.md` recording your own words on posture and any ceiling you set. A
first handoff entry, written as the position this sitting is leaving behind rather
than a description of the interview itself, becomes the bottom of the stack in
`HANDOFF.md` for good.

**Running it again, later.** The interview is not only for a bare clone. Re-run it
against a repository that has been live for months, with real projects, rulings, and
seat charters already filled in, and it drafts a diff against what is already there
instead of drafting from scratch, so a stale answer is a visible change rather than a
silent overwrite. It also covers the harder shape of the same case: the underlying
template itself has moved on since your copy was created. When that happens, run the
upstream pull in `EXTENDING.md` section 6 first, reviewing only the doctrine-path
diff, then re-run the interview so your generated layer catches up to what the
doctrine now expects from it.

---

## 4. Your first orientation

However the interview ended, the next time a session opens in this repository, the
same read order runs, and it reports back in a fixed shape before anything else
happens:

```
Where things stand:
Open gates awaiting your word:
Blocked items (registers/BLOCKED_ON_OPERATOR.md):
Suggested next moves (CLAUDE.md's router):
Recent commits:
Uncommitted on disk:
```

On a repository that has just been through its founding sitting, this is usually a
short, quiet report: the founding entry as the live picture, no rulings pending
beyond the founding one, nothing blocked unless you deliberately deferred something,
and a short list of numbered routes drawn straight from `CLAUDE.md`'s own router. This
step reads and nothing more. It does not write a register row, does not touch
`HANDOFF.md`, and does not treat anything it read as permission to keep going past the
report. It stops, and waits for you to say which route you actually want, or to name
the task in plain words instead.

---

## 5. Convening your first real meeting

The most useful thing to do with that first orientation is pick a genuine open
question about your own business, something small enough to argue through in one
sitting but real enough that you actually care which way it lands, and convene a
meeting over it.

A meeting lives entirely on disk, at `meetings/<date>-<short-slug>/`, and every step
of it is a file rather than a conversation that evaporates when the session ends.
Your intent gets written down first, in your own words, along with which seats the
question actually touches and which two or three constraints you already consider
settled. Only the seats the question genuinely touches get convened; a small
question convenes two, plus three standing attendees who show up at every meeting
by right because a plan that ignored any of them would be one nobody could seal,
fund, or track.

Each convened voice then writes its own position independently, without reading
anyone else's first, because a brief written after seeing another one tends to argue
inside that brief's frame rather than staking out its own. Once every position is in,
the chair writes an honest synthesis: where independent positions agreed without
being asked to, where they genuinely disagreed and who held which side, and the
weakest point in each position pressed on directly rather than smoothed into a
false consensus.

From that synthesis comes one proposed plan: what gets built, in what order, what it
is expected to cost, and a table of every open question the plan cannot answer on
its own. Every row in that table is marked one of two ways. A row asking for a fact
only you actually hold gets a safe default: draft against a placeholder, and commit,
spend, or send nothing until you supply the real number. A row asking you to accept
or overrule a judgment call gets the chair's actual recommendation, argued for on the
page. Before any of it reaches you, a small set of skeptical readers goes over the
whole document set looking specifically for a position that got softened on the way
through, a number that will not rebuild from its own inputs, or a step that assumes
authority nobody actually handed over.

Then, and only then, you rule. That ruling is the one file in the whole system a
human writes rather than an agent drafting for review; everything before it can be
produced for you, this step cannot. Because every row is typed the way it is, a
single word of approval is safe: you are trusting the reasoning on judgment calls
only, never letting anything invent a fact about your own business on your behalf.
The ruling gets copied into the standing rulings ledger the same sitting, and only
after that copy exists do any packets get written out to become actual work.

The smallest honest version of this whole ritual is two convened positions plus the
three standing attendees: five short documents, one debate, one plan, one ruling.
That is not a stripped-down version of the process. It is the ordinary shape a real
first meeting takes.

---

## 6. Parking it

Any session that leaves this repository different from how it found it closes
through the same ritual before it ends, and the ritual is not satisfied by the work
having gotten done. The bar it holds itself to is narrower and more mechanical than
that: could a stranger who has never spoken to you, reading only these files, work
out what is blocked, what is in flight, what has actually been ruled, and what must
not be touched until you say so.

In order, closing reconciles anything metered against what it was projected to cost,
writes any decision you made this sitting into the rulings ledger if it is not
already there, updates whichever registers actually moved, and brings any mission or
meeting file's status current. Then it drafts the next dated entry for the session
log and shows it to you in full before appending a single line of it. It rewrites the
topmost entry of `HANDOFF.md` to describe the position this sitting is actually
leaving behind, and that rewrite has to exist before the closing commit, not after
it: the whole point of the rule is that the commit is what makes a position durable,
so the position needs to be written while a commit is still coming to carry it.
Before anything is staged, it also looks back across the sitting for any promise made
to somebody outside this repository, a document you said you would send, a date you
named to somebody, because nothing here ever sends on your behalf, and a promise like
that stays a live human obligation until your own hand actually discharges it.

Only then does it stage named files, never a blanket catch-all, and commit with a
message that says what actually changed and a trailer naming what executed the work.
It closes by telling you plainly that the repository is parked: the handoff is
current, the log has its new entry, the commit landed, and anything metered is
reconciled or explicitly noted as needing nothing this time.

---

## 7. Where to go from here

Five places are worth knowing about once the first sitting is behind you.

**`EXTENDING.md`**, for the day your work names a role the default roster does not:
a delivery seat, an engineering seat watching your own coding agents, a research
seat, whatever your business actually has that this repository shipped without.
Adding one is a normal act with four steps to it, not a fork of the product, and
that file walks all four.

**`examples/adding-a-seat/`**, a full worked instance of exactly that: one seat added
start to finish, so you can see the shape once before you do it for real.

**`examples/first-meeting/`**, a full worked instance of section 5 above: one
invented business running its own intent through to a sealed mission, so you can
watch the whole ritual play out in someone else's files before you trust it with
your own question.

**The doctrine, read in this order, whenever you want the full reasoning behind
something this walkthrough only narrated:** `CLAUDE.md`, then
`doctrine/CONSTITUTION-CORE.md` for the gates and the state discipline in full,
then `EXTENDING.md` for how the roster grows, then `org/STAFF_MEETING.md` for the
meeting ritual in full, then `ops/OPERABILITY.md` and `ops/COLD_RESUME.md` for what
a session owes the next one and how a cold session rebuilds the picture, then
`ops/FLEET_CRAFT.md` for the discipline behind any fan-out's cost projection, then
`ops/JUDGMENT_CRAFT.md` and `ops/HIGH-JUDGMENT-BANK.md` for the standing of the
questions expensive enough to bank rather than guess at. The function charters
under `org/functions/` are worth their own read the first time your work actually
touches one.

**`docs/TOKEN-ECONOMY.md`**, for the day the meter itself becomes the question: a
one-page account of where a multi-session staff's spend concentrates and the
levers that move it, ranked by effect rather than by how easy each one is to
flip. `examples/settings/` holds the worked settings block it points at, and
`scripts/token-audit/` is how you re-derive your own numbers instead of taking
anyone else's.

---

## 8. The promise this repository opened with

You started with an empty board and a staff that knew nothing about you. Nothing in
these files arrived pre-loaded with someone else's history, someone else's clients,
or a ruling nobody in your business ever made. Every fact sitting in this repository
from here forward, every project named, every seat added, every ruling recorded, is
one you put there yourself, in a conversation you had and approved. That is the
whole of what a clean start means here, and it is true of every line you add to it
from this point on.
