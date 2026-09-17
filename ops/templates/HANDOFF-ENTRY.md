<!-- file-class: DOCTRINE -->

# HANDOFF-ENTRY (template)

*The structured shape a HANDOFF entry uses. Referenced from
`ops/MULTI-SESSION.md` section 19. File class DOCTRINE - leave this file alone
so upstream can improve it; nothing here carries operator content, so there is
nothing of yours to fork by using it. What it shapes - `HANDOFF.md` itself -
stays PERSONAL, exactly as `EXTENDING.md` section 5 already has it.*

---

## How to use this template

The whole entry - the STATE table, OWED, and RESUME - stays under 2KB. That
limit is deliberate: a HANDOFF entry gets read far more often than it gets
rewritten, and a reader should get the live picture from one screen, not a
scroll through a paragraph that grew all day.

Write the STATE table, OWED, and RESUME block once, when the entry is opened.
After that, **nobody re-edits that block.** Anything that changes before the
entry is next rewritten wholesale gets appended below it as a new, dated,
one-line entry - never folded back into the block above by editing it in
place. A block that gets hand-edited on every small change is exactly the
churn this shape exists to stop; see `ops/MULTI-SESSION.md` section 18 on
batching the commits that carry those edits.

Per `ops/MULTI-SESSION.md` section 17, a row in this table points at a seat's
own ledger, ruling, or commit rather than re-narrating it. "Last commit" names
a commit; it does not summarize what that commit did.

---

## The template - copy everything below this line

```
### STATE

| Seat | Tier | In flight | Last commit |
|---|---|---|---|
| [seat] | [reasoning \| building \| scanning] | [mission/phase, or "nothing"] | [short hash] |

**OWED:** [what this seat owes the next reader, or another seat, before either
one can move - one or two lines, or "nothing"]

**RESUME:** [the obvious next step, and what must NOT move until the operator
rules - or "nothing blocked"]

<!-- Mid-session updates append below this line, oldest first.
     Never edit the block above. -->
```

---

## A filled example

Seat names below are neutral placeholders, not a real roster - substitute
whichever seats and tiers your own copy actually runs.

```
### STATE

| Seat | Tier | In flight | Last commit |
|---|---|---|---|
| seat-a | reasoning | mission M-9, phase 2 of 3 | a1b2c3d |
| seat-b | building | nothing | 9e8d7c6 |

**OWED:** seat-a owes seat-b the schema decision from M-9 phase 2 before
seat-b's next build step.

**RESUME:** seat-a resumes M-9 phase 2 from its own STATE.md. Do not start
phase 3 until the operator rules on the open scope question logged against
M-9.

<!-- Mid-session updates append below this line, oldest first.
     Never edit the block above. -->
2026-09-16 11:40 - seat-a - phase 2 checkpoint committed, see a1b2c3d
2026-09-16 14:05 - seat-b - parked; idle expected past the cache window
```
