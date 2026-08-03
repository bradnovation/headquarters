# SISTER-REPOS - consent registry for external context sources
<!-- file-class: PERSONAL -->

*This file is yours. It ships empty, upstream never writes to it, and nothing in
it travels anywhere upstream. It answers one question and only one: which
locations outside this repository has this staff been given permission to read,
and for what. A location not answered by this file is not read, and that is true
regardless of how convenient it would be, how obviously related it looks, or how
many times its name has come up in conversation.*

*This registry is where gate G2 - foreign repositories, in
`doctrine/CONSTITUTION-CORE.md` - meets an actual path on your disk. The gate says
the version-control command line never goes near somewhere this staff does not
own. This file says which somewheres it may even open for a plain read, and why.*

---

## What belongs here

One entry per external context source: another repository, a notes directory, a
project folder, anything living outside this repository's own tree that you have
decided this staff may read for a stated reason. A source most people reach for
first is whatever separate place already holds context about their other work or
their life - a personal notes system, a second project's own repository, a
tracker that predates this staff entirely. There is nothing special about that
case; it follows the same rule as any other location you might name.

## The standing rules

1. **Consent is asked once and recorded, never re-asked as routine.** Once an
   entry exists and is active, a session does not re-confirm it before reading,
   the way it might re-check something genuinely uncertain. The entry is the
   record. Re-asking happens only when the purpose itself changes - see below.
2. **Consent is never assumed.** A directory sitting next to this one on the same
   machine, a path that happened to come up while you were talking about
   something else, a name this staff can guess at from context - none of that is
   consent. Consent is a specific yes, to a specific ask, written down here
   before anything is read.
3. **Reads are plain file reads, and nothing else.** No version-control command
   of any kind is ever run against a source in this registry, including one that
   only looks and changes nothing. That restriction does not soften because you
   own the source too, or because the command would be read-only, or because it
   would save a step. Opening a file and reading its text is the entire
   mechanism.
4. **Nothing is ever written back.** This registry grants permission to read.
   It never grants permission to write, to create, to modify, or to leave
   anything behind in a source it names. A sister repository's own state is not
   this staff's to touch, in any form, for any reason.
5. **A source not listed here is not read. Full stop.** There is no informal
   tier below this registry, no "just this once to check," no exploring a
   directory to see whether it would be worth asking about. If it is not an
   active entry below, this staff's world ends at its own repository boundary.

## Entry format

Copy this block for each source. Every field is required; write "none" rather
than leaving a field blank.

```
### [Source name] - consented [YYYY-MM-DD]

**Location:** [absolute path, or a plain description of where it sits and how
  to find it]
**What it is:** [one line - whose material this is and what kind of thing it
  holds]
**Read for:** [the specific, stated purpose consent was given for - not
  "context" or "background," a purpose narrow enough that granting it and
  later revoking it both mean something concrete]
**Consent given by:** [who said yes, and the circumstance - a named session,
  the onboarding interview, a direct instruction]
**Carve-outs:** [any part of the source that stays off limits even though the
  rest is readable, or "none"]
**Status:** active | revoked [date, if revoked]
```

## Widening scope is a new ask, not an edit

An entry's **Read for** line is the boundary of what was actually granted. When
the reason for reading a source changes, or a second purpose comes up for a
source already listed, that is a fresh ask handled by the ritual in
`.claude/skills/sister-repo-consent/SKILL.md`, landing as a new dated entry - not
a silent rewrite of the old one's purpose line. Keep the old entry standing
alongside the new one; the history of what was asked for and when is worth more
than a tidy single row.

To withdraw a source entirely, change its **Status** to `revoked` with the date,
and leave the rest of the entry as it was. Do not delete a revoked entry. A
registry that only ever shows what is currently true cannot answer whether
something used to be allowed.

---

## Registered sources

No sources are recorded yet. Until you add one, this staff's context is exactly
this repository: its own files, and nothing beyond them. That is a complete,
working configuration, not a gap waiting to be filled. Adding a source follows
the ritual in `.claude/skills/sister-repo-consent/SKILL.md`, which lands its
result here in the shape above.

---

## EXAMPLE - not a real source; delete this block once you have entries of your own

*Invented end to end, to show the shape and nothing more. The business, the
sister directory, the date, and the arrangement described are all fictional.*

### Roastery Notes - consented 2026-03-11

**Location:** `../roastery-notes` (a separate local repository on the same
  machine; not a subdirectory of this one, and not under this repository's own
  version control)
**What it is:** the operator's own long-running personal notes repository,
  predating this staff, where cafe-account relationships, delivery-schedule
  quirks, and general life logistics get tracked in the operator's own words.
**Read for:** checking existing wholesale-account context - standing
  arrangements, who asked for what and when - before a draft touching a named
  cafe account goes out, so this staff never proposes terms that collide with
  something already agreed and recorded there.
**Consent given by:** the operator, given directly during topic 4 of the
  onboarding interview.
**Carve-outs:** the notes repository's own `personal/` subdirectory (health,
  family, anything not business-related) stays off limits; it is never opened,
  for any purpose.
**Status:** active.
