---
name: init-context-and-work
description: Mid-init, after identity and posture are set: the operator's businesses, where else their context lives (sister-repo consent), and how they already work.
---

# init-context-and-work

Part of the init interview ritual (see skill:init for the full sequence, its
conduct rules, and the show-before-write discipline). These three topics are
asked mid-init, right after identity and posture
(skill:init-identity-and-scope) are settled, and before the ritual moves on to
the remaining topics. Ask one at a time, read each answer back before moving
on, and write nothing until the write pass.

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

**The rules that bind this topic** are skill:sister-repo-consent's own
five-step ritual, stated there in full - conduct this topic under those rules
rather than restating them here.

**Lands in:** one entry per consented source in `SISTER-REPOS.md`. This topic is
that ritual's first pass, not a separate mechanism; skill:sister-repo-consent
carries the full mechanism for adding a source later and for re-asking when the
purpose changes.

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
the default roster has no seat for, skill:init carries the one-command
seat-packaging step that covers it.

**If deferred:** the seats run on their default charters, which is the shipped
state and is safe.

Source: .claude/skills/init/SKILL.md Topic 3 - Your businesses and projects |
Topic 4 - Where else your context lives | Topic 5 - How you already work
(moved into this skill 2026-09-16)
