---
name: init-close
description: Mid-init, after model tiers and the dream cap are set: the first proving-ground mission, the show-before-write discipline, deferrals/rerun rules, and the handoff into the router.
---

# init-close - the last topic, the write pass, and the close

Part of the init interview ritual (see skill:init for the full sequence, its
conduct rules, and the show-before-write discipline). This skill carries the
interview's last topic, the rules for turning nine topics of answers into
files, what happens to anything deferred or interrupted, and the three
sentences that close the ritual and hand the new organization to its own
router.

### Topic 9 - Your first proving ground

**Ask:** what the first real mission should be. Genuinely useful, small enough
to finish, concrete enough that they will know whether it worked. Nothing
urgent and nothing expensive, because the point of the first run is watching
the machinery work end to end rather than betting on it.

**Then ask the falsifiable question:** what observable result settles whether
it worked? One sentence. "It felt useful" is not an answer, and accepting it
here is how a first mission ends without anyone able to say whether it
succeeded.

**Lands in:** the first proving ground section of `MISSION.md`, and a first
dated row in `registers/TASKS.md` with status `proposed`.

**If deferred:** the section stays bracketed and the first session picks a
starting point instead. Harmless.

If any topic along the way surfaced a role the roster does not name, see
reference.md for the one-command seat-packaging offer before moving on to the
write pass below.

## 6. SHOW BEFORE WRITE

Everything above produced answers. Nothing above produced a file. This is
where writing happens, and it happens one artifact at a time.

For each artifact: draft it in full, show it in full, and stop. Two live
options, always: keep it as written, or change it. Silence is not the first
option. If the operator wants a change, work it through in conversation and
show the revision - never replace a shown draft with a second guess they did
not ask for, and never write the revision straight to disk on the strength of
the comment that prompted it.

reference.md carries the full artifact table - every file this ritual can
write, its file class, and what lands in it - plus three write-pass details
that are easy to miss. Read it now, before drafting the first artifact.

## 7. Deferrals, interruption, and running it again

**Every deferred answer becomes a visible row**, not a note in someone's
memory. One entry on `registers/BLOCKED_ON_OPERATOR.md` per deferral, saying
what is missing and what stays unavailable until it is settled - an unset cap
keeps dreaming disarmed, unpinned tiers block the first fan-out, an unanswered
posture question keeps everything at the private standard and unpublished.

**An interrupted sitting parks like any other session.** Write the artifacts
already approved, leave the rest bracketed, and record in `HANDOFF.md` exactly
which topics were covered and which are still open. State captured in the
middle survives; state carried in conversation to the end does not, and this
ritual is long enough for that difference to matter.

**Running it again is normal and is not destructive.** A re-run reads what is
already filled, asks only about placeholders and about anything the operator
names for revisiting, and shows a diff before touching a field that already has
a value. It never silently overwrites a filled field. Changing something
previously ruled - the cap, the posture - is a new ruling in `DECISIONS.md`
first, and only then an edit to the file it governs.

## 8. What this ritual never does

- Never asks a business question before init-identity-and-scope's quarantine
  checks pass.
- Never opens, lists, or samples the vault, in setup or afterward.
- Never reads an external source before its consent entry is written and
  approved, and never runs a version-control command against one.
- Never fills a bracket by inference, by plausible default, or because the
  answer seemed obvious from something else the operator said.
- Never arms dreaming. It records a figure; the desk's three conditions are
  what arm anything.
- Never sends, publishes, or deploys anything. Gates G3 and G4 have no switch
  to find here.
- Never edits a doctrine file to accommodate an answer.
- Never treats a chat reply as approval to write.

## 9. The close

Close in three sentences, and no more than three.

Your first session starts the way every session does: the read order at the
top of `CLAUDE.md`, then the router. When you have something real to decide,
convene the first meeting through `org/STAFF_MEETING.md` and let the seats
argue it before you rule. Whatever you do in that session, park it through the
close ritual in `ops/OPERABILITY.md`, so the next session inherits a true
picture instead of reconstructing one.

Source: .claude/skills/init/SKILL.md Topic 9, §6, §7, §8, §9 (moved into this skill 2026-09-16)
