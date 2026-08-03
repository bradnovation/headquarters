---
name: init
description: First-run onboarding interview for a fresh copy of this repository. Run it on the first session, whenever the generated layer of CLAUDE.md still carries bracketed placeholders, or when the operator asks to redo setup. It verifies the sensitive-material quarantine before it asks anything real, interviews the operator one topic at a time, and drafts every file it would write for approval before writing a single line.
---

# init - the first-run onboarding interview
<!-- file-class: DOCTRINE -->

*File class DOCTRINE: upstream owns this ritual the way it owns `doctrine/` and
`ops/`. Pull improvements to it; hand-edit it and you own your own copy of it
from then on, per `EXTENDING.md` section 6. Everything the ritual produces is
yours and upstream never touches it.*

---

## 1. What this ritual is

A fresh clone of this repository is a staff with no idea who it works for. Every
file marked GENERATED ships as a filled-in shape with the facts left blank:
brackets where a name goes, `[UNSET]` where a spend cap goes, unpinned model
tiers, an empty project register. This ritual is the conversation that turns
that shape into somebody's organization.

It is an interview, not a form. The session asks, listens, reads the answer
back, and moves on. At the end it drafts every file it proposes to write, shows
each one, and waits. The operator's approval is what makes any of it real.

Three properties decide whether this ritual is trustworthy, and all three cost
something to hold:

- **It refuses to start before the quarantine exists.** Section 2.
- **It never fills a blank by inference.** An unanswered question stays
  unanswered and becomes a visible open item, never a plausible guess that
  reads like a fact six months later.
- **It writes nothing on the strength of conversation alone.** A sentence typed
  in chat is context. The approval of a shown draft is what authorizes a write,
  and the two are not the same event.

The ritual convenes no other agents and launches no fan-out, so it spends only
the session it runs inside. There is nothing here for gate G1 to hold back.

---

## 2. PRECONDITION: the quarantine, before question one

`doctrine/CONSTITUTION-CORE.md` states the rule this section enforces: the
ignore mechanics that keep `vault/` out of version control exist before any
interview asks a real question about the operator's business. The reason is that
version-control history is permanent. A first business answer given into a
repository whose quarantine is missing is a mistake with no clean undo, and the
question that invited it was asked by this ritual.

Run four checks, in order, before any topic in section 4:

1. **This is the product tree.** `CLAUDE.md` and `doctrine/CONSTITUTION-CORE.md`
   both exist at the repository root. If they do not, this is the wrong
   directory; stop and say so.
2. **The ignore file exists** at the repository root.
3. **It excludes the vault's contents and keeps the vault's README tracked** -
   the two-line idiom, the contents excluded and the README negated. One bare
   directory line is not sufficient and is not accepted as sufficient.
4. **`vault/README.md` exists and is readable.**

Check the README's presence and read that one tracked file if you need to. Do
not list, open, or sample anything else inside that directory, now or later.
Gate G5 does not soften for setup.

**If any check fails, the ritual stops.** Name the exact check that failed and
what is missing. Offer one repair and nothing else: draft the missing rule or
the missing README, show the draft, and write it only on approval. Then run all
four checks again from the top. Do not offer to begin the interview and fix the
gap afterward, do not accept an assurance that the operator will handle it, and
do not proceed on the reasoning that the first few questions are harmless. This
check fails closed, which means an unclear result is a failed result.

Say what passed, in one line, and move on. The operator should know the boundary
was verified rather than assumed.

---

## 3. How the interview is conducted

**One topic per exchange.** Ask about one thing, settle it, then ask about the
next. Never present the nine topics as a questionnaire and never bundle three
questions into one message to save turns. A questionnaire produces answers
shaped to fill boxes; a conversation produces facts.

**Read the answer back before moving on.** One short line confirming what was
heard, in the operator's own terms. This catches the misunderstanding while it
costs a sentence to fix rather than after it has been written into four files.

**Keep exact wording where exact wording will be quoted later.** The values
line, the spend cap, the fork posture, and anything that becomes a founding
ruling get recorded as the operator said them. A tidied sentence is the
session's sentence wearing the operator's name.

**"I do not know yet" is a complete answer.** Take it, leave the placeholder
standing, and carry the item to section 7. Pressing for a figure the operator
has not decided produces a number nobody chose, and this repository will treat
it as settled policy.

**Nothing is written during the interview.** Answers are held in the
conversation until the write pass in section 6. If the sitting will be long, it
is better to run the write pass in stages, topic group by topic group, than to
write early on chat answers.

**Ask about the operator's work, never about anything under `vault/`.** If an
answer starts moving toward third-party material - what a client said, a
recording, a forwarded message - stop it there, say where that material belongs,
and carry on with the question that was actually asked.

---

## 4. THE INTERVIEW

Nine topics. The order is deliberate: identity, then the posture question that
decides what may be committed at all, then the facts that posture governs.

### Topic 1 - Who you are, and how the staff addresses you

**Ask:** their name, and what the staff should call them in the writing it
produces. First name, a title, or simply "the operator" are all real answers.
Then, optionally, the working rhythm worth knowing: hours, time zone, when they
are reachable and when they are not.

**Why:** every charter, handoff entry, and draft in this repository addresses
somebody. Getting this wrong is small and constant.

**Lands in:** the generated layer of `CLAUDE.md`, section (f); the founding line
of `MISSION.md`.

**If deferred:** it cannot usefully be. Take the address form at minimum; the
rhythm is genuinely optional.

### Topic 2 - Public or private, decided before the first business fact

**Ask:** will this working copy stay private, or is it going somewhere others
can read? Then explain what turns on it, briefly and in plain terms: a private
copy may hold ordinary internal business material in committed files; a public
copy may hold public-class material only, which excludes a project register
naming real clients, a handoff describing a negotiation, and a ledger showing a
real meter. The classes are defined in `doctrine/CONSTITUTION-CORE.md`.

**Why it is asked second:** the next topic produces this repository's first
internal-business fact. Asking afterward means asking whether something already
written down was safe to write, which is the wrong order for a decision that
history does not let anyone take back.

**Consequences to state out loud:** if the answer is public, every later topic
in this interview records only what the operator confirms is publishable, or
records nothing and keeps the detail out of the repository entirely. A public
answer also makes the standards guard's private denylist a prerequisite rather
than a later refinement - see `org/functions/standards-guard/CHARTER.md`, which
names it as the one onboarding step that is neither optional nor deferrable
before publishing.

**Lands in:** the generated layer of `CLAUDE.md`; the founding ruling in
`DECISIONS.md`.

**If deferred:** the interview continues, but every artifact it drafts is
written to the private standard and nothing is published until the question is
answered. File it as an open item; it is exactly the kind of gap the founding
handoff entry expects to see named.

### Topic 3 - Your businesses and projects

**Ask:** what they run, one at a time, with a one-line description of each: what
it is and who it serves. Then, for each, a sentence on what "going well" looks
like this year. Assume nothing about the count. One business is as ordinary as
five.

**Why:** this is the landscape every seat reasons against. Without it the staff
produces work that is competent and about nothing in particular.

**Lands in:** the founding statement in `MISSION.md`; the short pointer list in
`CLAUDE.md` section (f); one dated section per project in
`registers/PROJECTS.md`, in that file's own format, with status `active` unless
the operator says otherwise.

**If deferred:** rare, and usually a sign the sitting should stop and resume
later. A staff with no projects has nothing to be a staff about.

### Topic 4 - Where else your context lives

This is the topic with the sharpest rule attached, so it is worth conducting
exactly as written.

**Ask, first:** does context about their work or their life live anywhere
outside this repository - another project directory on the same machine, a
working repository, a notes system, somewhere else entirely - that this staff
would be better for reading? And is there somewhere they would rather it look
first?

**Then handle exactly one source at a time.** For each source, before mentioning
any other:

1. What it is and where it sits.
2. What the staff may read it **for**. Consent is purpose-bound, not general.
3. Any carve-out: parts of it that stay off limits.
4. Consent, given explicitly, in their own words.

Only then ask whether there is another source. A source is settled or it is not
raised again in this topic.

**The rules that bind this topic**, stated to the operator rather than assumed:

- **Nothing is read before its entry is written and approved.** Not to confirm
  it exists, not to see whether it is worth including.
- **Consent is asked once and recorded**, in `SISTER-REPOS.md`. It is never
  re-derived later from the fact that a path came up in conversation, and it is
  never assumed from a directory sitting next to this one.
- **Do not go looking for candidates.** The staff does not sweep the machine for
  likely directories and present a list to tick. The operator names sources;
  this ritual does not nominate them.
- **Reads are plain file reads.** No version-control command is ever run against
  a source, read-only ones included, and nothing is ever written back to one.
  That is gate G2, and it does not bend for a directory the operator owns.
- **A source not in the registry is not read.** There is no informal tier.

**Lands in:** one entry per consented source in `SISTER-REPOS.md`. The full
mechanism for adding a source later, and for re-asking when the purpose changes,
is `.claude/skills/sister-repo-consent/SKILL.md`; this topic is that ritual's
first pass, not a separate mechanism.

**If deferred:** the registry stays empty and the staff reads this repository
only. That is a complete, working configuration, not a degraded one.

### Topic 5 - How you already work

**Ask:** what standards of practice, tools, conventions, or agents already exist
in their working life that this staff has to fit around. A build process. A
ticketing system. Coding agents already running under their own rules. A
documentation convention they will not be giving up.

**The framing matters:** this organization works with what is already there
rather than replacing it. An answer here is not a feature request; it is a
constraint on how the seats behave.

**One follow-up worth always asking:** does any of it own something a default
seat in this roster also claims? Two owners of one artifact is the failure mode
that produces contradictory registers, and `EXTENDING.md` section 2 says to
settle it in writing, in both charters, rather than leaving it to be discovered.

**Also ask here:** where their standards of voice and vocabulary come from - a
style guide, a brand document, a piece of their own writing they would hold up
as the standard. Name the source; do not paraphrase it into the guard's rule
files from memory. `org/functions/standards-guard/CHARTER.md` asks for that
source to be mirrored rather than summarized, and mirroring is its own pass with
the source open, not an interview answer.

**Lands in:** the affected seat charters, which are yours to edit; a note in the
founding ruling if the constraint is org-wide; a first task in
`registers/TASKS.md` for the standards-mirroring pass. If a role turns up that
the default roster has no seat for, go to section 5.

**If deferred:** the seats run on their default charters, which is the shipped
state and is safe.

### Topic 6 - Your values line

**Ask:** how they want work done in their name, in their own words. One line or
a short list. Not a mission statement - the sentence a colleague would recognize
as theirs.

**Why:** it is quoted into seat charters and it is what the standards guard
measures a draft against when it asks whether something sounds like the
operator. Left blank, the staff has no standard to hold work to beyond plain
competence, and it will say so honestly rather than inventing one.

**Lands in:** the generated layer of `CLAUDE.md`, section (f), transcribed
exactly as given.

**If deferred:** the placeholder stands and the guard runs without a voice
standard. Worth revisiting; not worth pressing for in the moment, because a
values line produced under mild pressure is nobody's values line.

### Topic 7 - Your model tiers

**Ask:** which models their own plan actually grants them, and let
`org/models.yml` do the sorting into reasoning, building, and scanning. That
file is the single source of truth for tier assignment and its comments explain
each tier's shape.

**Three things to state plainly while asking:**

- If their plan grants exactly one usable model, all three pins get that model.
  `org/models.yml` names this collapse case as a supported configuration and
  says what is lost by it. Configure it deliberately rather than leaving two
  pins blank.
- If they have a premium or interactive-only tier they reserve for their own
  keyboard, it is never pinned into a duty row. That rail is constitutional, and
  this product assumes nothing above the ordinary reasoning tier anywhere.
- Never set a global environment override for the subagent model. It wins
  silently over every pin in the file and nothing in a run's output records that
  it did.

**Lands in:** the three pins in `org/models.yml`. The duty map below them
already ships filled and needs no interview answer.

**If deferred:** the pins stay bracketed and the first fan-out has no tier to
read. File it as an open item; a missing model tier is one of the gaps the
founding handoff entry is written to surface.

### Topic 8 - Your dream cap

**Ask:** whether off-cycle generative work is worth spending on, and if so, what
ceiling they want on it, in whatever unit they meter in, over whatever period
they think in. Offer a conservative figure **as a starting point and say that is
what it is**: something small enough that a surprise is an annoyance rather than
an event. Then take whatever number they actually give.

**Never assume one.** Dreaming ships disarmed for exactly this reason: no
default figure is safe on somebody else's meter, and the number that governs has
to be one they typed.

**Say what the number does and does not do.** Recording a cap is one of three
conditions in `org/functions/innovation-desk/CHARTER.md`. The other two are a
confirmed read scope - public and internal material, with any external source's
consent already recorded under topic 4 rather than re-asked here - and a kill
switch they have verified they can operate. Until all three hold, dreaming does
not run by hand or otherwise, and setting the figure alone has not armed
anything.

**Lands in:** the dream cap line in `CLAUDE.md` section (f), which is the
governing figure; `ledgers/SPEND.md` is where each run is projected and
reconciled against it afterward.

**If deferred:** the line stays `[UNSET]`, router item 4 declines and says why,
and the item goes on the open list. This is a fully supported state, not a
half-finished setup.

### Topic 9 - Your first proving ground

**Ask:** what the first real mission should be. Genuinely useful, small enough
to finish, concrete enough that they will know whether it worked. Nothing urgent
and nothing expensive, because the point of the first run is watching the
machinery work end to end rather than betting on it.

**Then ask the falsifiable question:** what observable result settles whether it
worked? One sentence. "It felt useful" is not an answer, and accepting it here
is how a first mission ends without anyone able to say whether it succeeded.

**Lands in:** the first proving ground section of `MISSION.md`, and a first
dated row in `registers/TASKS.md` with status `proposed`.

**If deferred:** the section stays bracketed and the first session picks a
starting point instead. Harmless.

---

## 5. When the roster is missing a seat: one-command packaging

If a topic surfaces a role this roster does not name - their own engineering
lead over coding agents already running, a delivery or project-management seat,
a support or research seat - offer to stamp it in one pass rather than leaving
them a procedure to follow later.

**The offer is:** one bundle, drafted for review like everything else, that
carries out all four acts from `EXTENDING.md` section 2 at once:

1. A charter at `org/seats/<seat>/CHARTER.md`, filled from
   `org/SEAT-TEMPLATE.md`, every bracket replaced and every guidance line
   deleted.
2. A row in section 2 of `org/ORG_CHART.md`: one-line mandate, default tier,
   paths to charter and ledger.
3. At least one duty row in `org/models.yml`, building tier unless a stated
   reason moves it.
4. An empty `org/seats/<seat>/LEDGER.md` carrying its two lines of format prose.

Plus a line in `DECISIONS.md` recording that the seat exists and why, which is
what lets a cold session reconstruct the organization from the files.

**Check before offering, not after drafting:** nothing in the proposed charter
loosens a gate, widens read scope past what the constitution allows, or creates
a send or deploy path. If the seat's output would be advice-shaped - legal, tax,
compliance, safety - the rail in `EXTENDING.md` section 7 goes into the charter
in writing, not by inheritance anybody has to infer.

**One pass means one review moment, not zero.** The bundle is shown whole and
approved whole, or edited and shown again. Offer it once; if the operator would
rather add seats later, that is the correct answer and the ritual moves on.

---

## 6. SHOW BEFORE WRITE

Everything above produced answers. Nothing above produced a file. This section
is where writing happens, and it happens one artifact at a time.

For each artifact: draft it in full, show it in full, and stop. Two live
options, always: keep it as written, or change it. Silence is not the first
option. If the operator wants a change, work it through in conversation and show
the revision - never replace a shown draft with a second guess they did not ask
for, and never write the revision straight to disk on the strength of the
comment that prompted it.

| Artifact | Class | What this ritual puts in it |
|---|---|---|
| `CLAUDE.md` section (f) | GENERATED | Operator and address form, rhythm, project pointer list, values line, dream cap, fork posture; the amendment line at the top of the file updated to say the generated layer was filled |
| `MISSION.md` | GENERATED | Founding date and name, the businesses block, ownership note if any, the first proving ground and its falsifiable line |
| `org/models.yml` | GENERATED | The three pins, or the single pin three times in the collapse case |
| `org/ORG_CHART.md` | GENERATED | Seeded from the answers: seats renamed, cut, or added; any new seat's row |
| `registers/PROJECTS.md` | PERSONAL | One dated section per project, in that file's format |
| `registers/TASKS.md` | PERSONAL | Any first tasks the interview produced, status `proposed` |
| `registers/BLOCKED_ON_OPERATOR.md` | PERSONAL | One row per deferred answer, per section 7 |
| `SISTER-REPOS.md` | PERSONAL | One entry per consented source, with purpose and carve-outs |
| `DECISIONS.md` | PERSONAL | The founding ruling, transcribing the operator's own words on posture, cap, and anything else ruled in the sitting |
| `HANDOFF.md` | PERSONAL | The founding entry, replacing the placeholder at the bottom of the stack |
| `SESSION_LOG.md` | PERSONAL | The first entry: this setup run, what landed, what was deferred |
| New seat files, if any | PERSONAL | The section 5 bundle |

**Three details that are easy to miss and awkward to fix later:**

- **The rulings ledger ships with a numbered example.** Before writing a real
  R-1, offer to delete that example block, which the file itself invites. Two
  entries numbered R-1 is a small mess that outlives the sitting.
- **The founding handoff entry is the bottom of the stack forever.** Write it as
  the position this session is leaving behind, including what is unfinished, not
  as a description of the interview.
- **The first log entry names its route honestly** as the setup run this is. The
  router's five routes describe ordinary sessions; this one runs before them.

**Doctrine files are not touched by this ritual.** Not `doctrine/`, not `ops/`,
not `EXTENDING.md`, not `org/SEAT-TEMPLATE.md`, not the function charters. If an
answer seems to require changing one, it does not: it is a ruling in
`DECISIONS.md`, or a rule in a seat's own charter, per `EXTENDING.md` section 6.

---

## 7. Deferrals, interruption, and running it again

**Every deferred answer becomes a visible row**, not a note in someone's memory.
One entry on `registers/BLOCKED_ON_OPERATOR.md` per deferral, saying what is
missing and what stays unavailable until it is settled - an unset cap keeps
dreaming disarmed, unpinned tiers block the first fan-out, an unanswered posture
question keeps everything at the private standard and unpublished.

**An interrupted sitting parks like any other session.** Write the artifacts
already approved, leave the rest bracketed, and record in `HANDOFF.md` exactly
which topics were covered and which are still open. State captured in the middle
survives; state carried in conversation to the end does not, and this ritual is
long enough for that difference to matter.

**Running it again is normal and is not destructive.** A re-run reads what is
already filled, asks only about placeholders and about anything the operator
names for revisiting, and shows a diff before touching a field that already has
a value. It never silently overwrites a filled field. Changing something
previously ruled - the cap, the posture - is a new ruling in `DECISIONS.md`
first, and only then an edit to the file it governs.

---

## 8. What this ritual never does

- Never asks a business question before section 2's checks pass.
- Never opens, lists, or samples the vault, in setup or afterward.
- Never reads an external source before its consent entry is written and
  approved, and never runs a version-control command against one.
- Never fills a bracket by inference, by plausible default, or because the
  answer seemed obvious from something else the operator said.
- Never arms dreaming. It records a figure; the desk's three conditions are what
  arm anything.
- Never sends, publishes, or deploys anything. Gates G3 and G4 have no switch to
  find here.
- Never edits a doctrine file to accommodate an answer.
- Never treats a chat reply as approval to write.

---

## 9. The close

Close in three sentences, and no more than three.

Your first session starts the way every session does: the read order at the top
of `CLAUDE.md`, then the router. When you have something real to decide, convene
the first meeting through `org/STAFF_MEETING.md` and let the seats argue it
before you rule. Whatever you do in that session, park it through the close
ritual in `ops/OPERABILITY.md`, so the next session inherits a true picture
instead of reconstructing one.
