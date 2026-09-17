---
name: cold-resume
description: A session opens with no memory of what came before, or a stranger must reconstruct org state from files alone: why this holds, the trust order, and the read-only reconstruction procedure.
---

# cold-resume - reconstructing the state of this org from the repo alone
<!-- file-class: DOCTRINE -->

*File class DOCTRINE: upstream owns this procedure the way it owns `doctrine/`
and `ops/`. Pull improvements to it; hand-edit it and the copy is yours to
merge by hand from then on, per `EXTENDING.md` section 6.*

*Purpose: any session that opens this repo with no memory of anything that came
before must be able to work out exactly where the org stands, what is safe to do
next, and what it must not touch - using only the files in this repo. No prior chat,
no session transcript, no verbal recap from the operator is ever required. If a
reconstruction needs a human to explain it, the repo has failed, not the session.*

---

## 1. Why this skill exists

Sessions are disposable. The repo is not. Every session ends - by design, by
interruption, by a closed laptop - and the next one starts from nothing. An org that
only works when the same conversation continues is not an org; it is a habit living
inside one context window.

The whole of this system's operability rests on one bar: **a stranger, or a fresh
session, reading files in a fixed order, reaches the same picture of reality that the
last session had.** This skill states that order and explains why it runs in that
sequence.

An index entry that summarizes or points to a fuller file can go stale independently
of the file it points to. Because the index gets read first and fastest, a stale
index entry silently overrides current doctrine sitting underneath it. Update both
the index line and the file it points to in the same edit, and open the underlying
file before letting a recalled index entry drive a real decision.

Three things make it work together, and they are one mechanism, not three:

- the read order in `CLAUDE.md`, which every session runs at open;
- the trust order below, which decides who wins when files disagree;
- the session-close ritual in `ops/OPERABILITY.md`, which is what keeps the files
  worth reading in the first place.

Remove any one and the other two stop being trustworthy.

---

## 2. The trust order, and why it runs in this sequence

When two files describe the same situation differently, this is the order of
authority. Higher wins.

1. **`registers/` and `ledgers/` first.** Four files, and between them they answer
   the questions no session can move without: who or what is holding something up
   (`registers/BLOCKED_ON_OPERATOR.md`), which work items exist and what status each
   one carries (`registers/TASKS.md`), how each project or business stands right now
   (`registers/PROJECTS.md`), and where the meter sits (`ledgers/SPEND.md`). They rank
   at the top because a named seat keeps them as a standing duty - dated and
   append-only, maintained because the role requires it rather than because somebody
   sat down to summarise. A row here reading blocked is a property of the organization,
   entered by the seat that owns that duty. It is not one session's impression of how
   things looked on its way out the door.

2. **Mission and meeting artifacts next.** For anything fanned out as a packet,
   `missions/<name>/STATE.md` and its `FINDINGS.md` where one exists; for anything
   still mid-ritual, `meetings/<date>-<slug>/*`. Direction of travel is what earns
   these second place. Work lands in them first and reaches a register only afterwards,
   once the seat holding that duty gets to its sweep, and the gap between the two is
   frequently a matter of minutes: the packet can be right at the same moment the row
   summarising it is merely older. Resolution runs the same way. What a register
   compresses into a status word, these files still hold at full size - the argument as
   it was actually had, the open questions tabled for a human, the finding one phase
   handed to the next. When a summary is too coarse to act on, and it usually is, this
   is the layer that answers.

3. **`HANDOFF.md`, topmost entry only.** What the previous session wrote down, in its
   own words, about where it set the work down. It is usually the quickest read in the
   repo and often the single most useful paragraph in it. It still ranks below the
   artifacts above, for one structural reason: nothing keeps it honest. As soon as a
   later session touches files and skips its own close ritual, this entry is
   describing a repo that no longer exists. Read it to learn where to point your
   attention. Do not let it settle any question about what is actually so.

4. **`git log` last, and only to break a tie.** One situation calls for opening the
   history: two of the records above make incompatible claims and neither will yield.
   What settles it is a property no other layer has, which is that the log grows only
   by appending. Wording and position are fixed at the instant a commit lands, and no
   session afterwards can take either of them back, which is precisely what a session
   can do to any paragraph in any file. Its place at the bottom of this list is a
   separate point, about habit rather than about accuracy: on an ordinary day nothing
   in the log alters a picture the records above have already fixed, and a session that
   begins there tends to carry commit messages forward as though a line written three
   weeks ago were as live as this morning's register row.

The principle underneath: **role-owned, append-only records outrank narrative;
narrative outranks nothing; history breaks ties.** Anything you add to this repo later
should be filed into that hierarchy deliberately, not left for a future session to
guess at.

Two additions worth stating plainly, both about a session's own memory rather than
about the files. A peer session's own handoff file outranks any other session's
account of that peer; if a peer told you where it stood, and its own file since says
something else, its file wins. And after a compaction or any loss of context, a
session re-reads its own live state files before acting on what it remembers -
compacted memory of what it was doing is a summary, not the record, and a summary can
drop exactly the caveat that mattered.

---

## 3. The reconstruction procedure

Run this in order at the start of any session with no memory of what came before.

**Nothing gets written while it runs.** Orienting is an act of reading only: assemble
the picture, put a route in front of the operator, and stop there until a word comes
back. A session that starts editing during orientation has skipped the approval gate
that everything else in this system depends on.

1. **Read `CLAUDE.md`.** The constitution and router. Confirms which consequence gates
   are in force and what routes exist.
2. **Read `doctrine/CONSTITUTION-CORE.md`** if anything about the gates, the security
   classes, or the approval cadence is in question. Skip it only when you already know
   the rules cold.
3. **Read `registers/BLOCKED_ON_OPERATOR.md` in full.** Nothing on this board moves
   without the operator; that is what puts an item on it. Taken whole, the board
   answers two questions in a single pass: is the org standing at a gate right now, and
   if it is, which gate.
4. **Read `registers/TASKS.md` in full.** Every work item, with the status it currently
   carries. Tasks and board items are built to point at each other, so run the pairs
   against one another and see whether both tell the same story. A pair that disagrees
   is a finding in its own right.
5. **Read `registers/PROJECTS.md`.** Narrow it to the project in play when the session
   already has one; take every entry when it does not. What you are after is the
   inventory: which projects exist, how each one is standing, and what somebody has
   already written down as a risk against it.
6. **Read `ledgers/SPEND.md`** for the current spend posture: what caps are in force,
   what has been consumed, whether anything is projected but not yet reconciled.
7. **Enumerate `meetings/`, then `missions/`.** Inside a meeting directory the files
   are taken in the sequence the ritual sets, and **the reading stops the moment one of
   them turns up empty or absent altogether**; where it stops is the live edge of that
   meeting. Inside a mission directory, `STATE.md` comes first without exception, and
   `FINDINGS.md` follows it whenever the mission has produced one.
8. **Read `HANDOFF.md`, topmost entry only.** By this point the picture already exists;
   this entry is a check against it and never its source. Where the two line up, the
   reading is finished. Where they clash, the entry is the side that gives way, and the
   clash itself gets reported to the operator rather than quietly absorbed.
9. **Consult `git log` only if something still does not add up.** Recent commits, in
   order, with their messages. This settles which of two conflicting accounts is
   current.
10. **Classify the stop point** - see skill:cold-resume-classify for the
    stop-point table - then propose a route and halt. Do not act on the proposal
    without the operator's word. Keep the proposal itself short and structured - a
    compact table, one clear ask, well under a page - unless the operator has
    explicitly asked for more depth; a long, technically thorough update is often
    functionally illegible next to a short, structured one.

If the repo is large, steps 3-7 are still cheap: registers and ledgers are short by
design, and any register that has grown too long to read in full has stopped doing its
job and should be archived rather than skimmed.

Source: ops/COLD_RESUME.md §1-3 (moved into this skill 2026-09-16)
