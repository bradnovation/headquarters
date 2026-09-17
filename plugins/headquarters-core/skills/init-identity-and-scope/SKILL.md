---
name: init-identity-and-scope
description: First session on a fresh clone, or an explicit redo: the quarantine gate, then who the operator is and whether this copy stays public or private, before any business fact is asked.
---

# init-identity-and-scope - the quarantine gate and the first two topics
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

- **It refuses to start before the quarantine exists.** Section 2, below.
- **It never fills a blank by inference.** An unanswered question stays
  unanswered and becomes a visible open item, never a plausible guess that
  reads like a fact six months later.
- **It writes nothing on the strength of conversation alone.** A sentence typed
  in chat is context. The approval of a shown draft is what authorizes a write,
  and the two are not the same event.

The ritual convenes no other agents and launches no fan-out, so it spends only
the session it runs inside. There is nothing here for gate G1 to hold back.

## 2. PRECONDITION: the quarantine, before question one

`doctrine/CONSTITUTION-CORE.md` states the rule this section enforces: the
ignore mechanics that keep `vault/` out of version control exist before any
interview asks a real question about the operator's business. The reason is
that version-control history is permanent. A first business answer given into a
repository whose quarantine is missing is a mistake with no clean undo, and the
question that invited it was asked by this ritual.

Run four checks, in order, before either topic below:

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

Say what passed, in one line, and move on. The operator should know the
boundary was verified rather than assumed.

## 3. How the interview is conducted

**One topic per exchange.** Ask about one thing, settle it, then ask about the
next. Never present the topics as a questionnaire and never bundle three
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
standing, and carry the item forward as an open item on the deferrals list this
ritual keeps until it is settled. Pressing for a figure the operator has not
decided produces a number nobody chose, and this repository will treat it as
settled policy.

**Nothing is written during the interview.** Answers are held in the
conversation until the write pass at the end of the ritual, conducted in
init-context-and-work. If the sitting will be long, it is better to run that
write pass in stages, topic group by topic group, than to write early on chat
answers.

**Ask about the operator's work, never about anything under `vault/`.** If an
answer starts moving toward third-party material - what a client said, a
recording, a forwarded message - stop it there, say where that material
belongs, and carry on with the question that was actually asked.

## 4. THE FIRST TWO TOPICS

Nine topics make up the full interview; this skill conducts the first two, the
ones that must be settled before any other topic can safely proceed. The order
is deliberate: identity, then the posture question that decides what may be
committed at all, then - in init-context-and-work - the facts that posture
governs.

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

**Why it is asked second:** the next topic, taken up in init-context-and-work,
produces this repository's first internal-business fact. Asking afterward means
asking whether something already written down was safe to write, which is the
wrong order for a decision that history does not let anyone take back.

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

## 5. Proceeding

Once Topic 1 and Topic 2 are both answered and read back, continue the same
sitting into init-context-and-work: the remaining seven topics (businesses and
projects, external context sources, existing working conventions, the values
line, model tiers, the dream cap, and the first proving ground), the
one-command seat-packaging offer, the write pass, and the close. Nothing this
skill collects is written to disk on its own - the write pass happens once
every topic across both skills is settled and shown.

Source: .claude/skills/init/SKILL.md frontmatter, H1, §1, §2, §3, §4, Topic 1,
Topic 2 (moved into this skill 2026-09-16)
