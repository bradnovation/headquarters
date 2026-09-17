---
name: sister-repo-consent
description: Adding, widening, or revoking this staff's permission to read a location outside its own repository: the fixed five-step consent ritual.
---

# Sister-repo consent

The fixed procedure for adding, widening, or revoking a seat's permission to
read a location outside its own repository - another repository, a notes
directory, a second venture's own tree, anything living somewhere else on the
operator's disk. Every result lands as a shown-before-written entry in
SISTER-REPOS.md, the registry this ritual produces. SISTER-REPOS.md's own
format and standing rules live there, not here; this skill only walks the
steps that land entries in it.

## 1. When this runs

Three occasions, all landing in the same place:

- **During the onboarding interview**, topic 4 - where else your context lives
  (see skill:init for the full interview sequence). That topic is this
  ritual's first pass, not a separate mechanism - the same steps below apply,
  run once per source the operator names during setup.
- **Any time afterward**, the moment the operator names a new source directly.
  Nothing about this ritual is a one-time setup step; a source can be added in
  month six exactly the way one is added on day one.
- **Any time afterward**, when the org itself has a reason to ask whether a
  further source exists - because a task in front of it would clearly benefit
  from context it does not have, and naming that gap to the operator is more
  honest than working around it. Asking is always in bounds. Going looking for
  the answer without asking is not.

## 2. The ritual, in fixed order

**Step 1 - name the source.** Either the operator names it outright, or the
org asks the operator directly whether a further source exists and, if so,
where it sits. **The org does not go looking on its own.** It does not scan
the machine for plausible directories, does not infer a source from a name
mentioned in passing, and does not present a shortlist of candidates to choose
from. A source enters this process because a person named it, not because it
was found.

**Step 2 - state the ask, specifically.** Before anything is read, the org
says in plain terms what it wants to read this source **for**. "Context" is
not a purpose; "checking whether a pricing draft collides with an arrangement
already on record elsewhere" is one. A purpose vague enough to justify reading
anything is a purpose that cannot later be revoked meaningfully, because there
is nothing narrow to take away.

**Step 3 - consent, given explicitly.** The operator answers with an actual
yes, in their own words, to the actual purpose stated in step 2 - not to a
general sense that the source sounds useful. A path that came up while
discussing something else is not consent. Moving on to a different topic
without an answer is not consent either; an unanswered ask stays unanswered,
and the source stays unread.

**Step 4 - record before reading.** Draft the entry in the exact shape
SISTER-REPOS.md specifies, show it in full, and stop. Two live options: keep
it as drafted, or change it. The entry is written only once the operator has
looked at it and said yes to the entry itself, not only to the idea of the
source in conversation. **The read has not happened yet, and does not happen
until this step is done** - not to preview the source, not to confirm it is
the right directory, not for any reason at all.

**Step 5 - only then, read.** Once the entry is written and active, reads
against that source are plain file reads and nothing more. No version-control
command of any shape ever targets it, including one that only inspects and
changes nothing - that restriction holds exactly as written in
SISTER-REPOS.md and does not loosen here. Nothing is ever written back to the
source. A read stays inside the purpose recorded in step 2; a use that drifts
outside that purpose is the trigger for step 6, not a use of the existing
grant.

## 3. Scope changes re-ask, every time

An entry's purpose is a boundary, not a starting point to expand from
quietly. If a second reason turns up for reading a source already listed, or
the original reason shifts into something broader, that is a new pass through
steps 1 through 4, in full - not a hand-edit of the old entry's purpose line.
The result is a new dated entry in SISTER-REPOS.md, standing next to the old
one rather than replacing it. This is what keeps the registry an honest
record of what was actually asked for and when, rather than a single line
that quietly means more today than it did the day it was written.

The same re-ask applies going the other direction. If the operator wants a
source's permission narrowed, that narrowing is itself drafted, shown, and
confirmed the same way a widening would be - it is not assumed just because
narrower sounds safer.

## 4. Revoking a source

Revoking is one field, not a deletion. Change the entry's Status to `revoked`
with the date, and leave the rest of the entry exactly as written. The entry
stays in SISTER-REPOS.md afterward - a registry that erases what used to be
true cannot answer whether something was once allowed, and that question
comes up more often than it seems like it would. From the moment the status
changes, the source is not read again under that entry, full stop. No grace
period, no "just to finish this one task" exception.

## 5. What this ritual never does

- Never scans for candidate sources or nominates one on the org's own
  initiative. The operator names sources; this ritual does not go looking.
- Never treats a directory's existence, or its name surfacing in
  conversation, as consent by itself.
- Never reads a source before its entry is drafted, shown, and approved in
  the exact shape SISTER-REPOS.md specifies.
- Never runs a version-control command against a source, for any operation,
  read-only ones included.
- Never writes, creates, or modifies anything inside a source. The grant
  this ritual produces is a permission to read, and only that.
- Never widens a standing entry's purpose without running steps 1 through 4
  again in full and landing a new dated entry.
- Never treats a chat answer alone as the write. The shown entry, approved as
  itself, is what makes a source active.

## 6. The close

Once an entry lands, the source is available to any session or convened work
whose task genuinely falls inside that entry's stated purpose - nothing
further needs to be asked before each individual read. What still applies
every time, without exception, is the shape of the read itself: plain file
reads, nothing written back, and nothing beyond what the entry's own purpose
line covers. When in doubt about whether a use fits inside a standing entry's
purpose, that doubt is itself the signal to run this ritual again rather than
to stretch the entry that already exists.

Source: .claude/skills/sister-repo-consent/SKILL.md frontmatter, §1-6 (moved into this skill 2026-09-16)
