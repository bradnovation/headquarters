# dream-run - reference

Read this once a dream run is actually underway (for the memlog's exact file
shapes) or when you want the reasoning behind the ritual rather than just its
steps (for the failure classes). Nothing here is needed to decide whether to
invoke dream-run in the first place - see SKILL.md for that.

---

## 5. Step four: the memlog, which makes a dead run resumable

*Adapted pattern: the generation-from-selection split and the resumable log carrying
it follow BMAD-METHOD. See `ATTRIBUTIONS.md`.*

Each run gets a directory: `inbox/dream-runs/<date>-<short-name>/`. Mark every file in
it `<!-- file-class: PERSONAL -->`; these hold the operator's own material and upstream
has no business with them.

Three files:

**`RUN.md`** - the run card, written at launch and updated at each transition. It
carries the cap that was read, the projection as filed, the lens set, and a status line
a resuming session can act on without reading anything else:

```
status: diverging | diverged | converging | filed | halted
lenses: 7 named, 4 complete
last-write: [DATE, time]
```

**`MEMLOG.md`** - the divergent record. Append-only, written continuously as
generation happens rather than assembled at the end. Every candidate carries its lens,
the order it arrived in, and whatever the agent wrote about where it came from. Nothing
is ever removed from this file, and nothing in it is ever rewritten. Not during
convergence, not when a candidate turns out to be wrong, not when a later run finds a
better version of the same thought. Corrections and second thoughts are appended, and
they say what they are correcting.

**`CONVERGENCE.md`** - written in step five, in a separate file for exactly this
reason. Selection lives here so that selection cannot touch the record it is selecting
from.

**Why continuous writing rather than a tidy write at the end.** Background work does
not survive the session that started it, but files do. A run that dies at the seventy
percent mark with everything still in context has lost seventy percent of a paid run.
The same run writing as it goes has lost the last thirty and can be resumed. On resume,
read `RUN.md` for the status line, read `MEMLOG.md` for what already exists, and
restart only the lenses that never finished. Do not re-run a completed lens for
tidiness. Do not start convergence on a partial record without saying plainly that the
record is partial and which lenses are missing from it.

---

## 9. The failure classes this ritual is built against

Each of these has a step above (in SKILL.md) that exists solely to prevent it.

- **The inline critic.** Scoring bleeds into generation, the run produces a clean list
  of reasonable ideas, and the seam nobody was looking at was killed at the moment it
  was least able to defend itself. Prevented by section 4 and by keeping convergence in
  a separate file.
- **The tidied record.** Convergence rewrites the memlog while it is in there anyway,
  and next year's version of this run reads a record that has already agreed with the
  judgment made about it. Prevented by the append-only rule in section 5, above.
- **The cheerful overrun.** A run that looked inexpensive costs several times its
  projection and nobody finds out until the meter says so. Prevented by projecting
  against the remaining cap in section 3 and reconciling in section 7.
- **The lost run.** Generation was excellent, the session died, and none of it was on
  disk. Prevented by writing the memlog continuously.
- **The interrupt.** One genuinely exciting row arrives between meetings, the surfacing
  discipline bends for it, and within a month the inbox is a notification stream.
  Prevented by section 7 holding absolutely.
- **The armed-by-drift run.** No cap was ever written, but the conversation was warm
  and the run went anyway. Prevented by section 2 refusing on the file rather than on
  the mood.

Source: .claude/skills/dream-run/SKILL.md §5, §9 (moved into this skill 2026-09-16)
