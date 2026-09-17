---
name: staff-meeting-convene
description: New intent needs debate, a plan, and a ruling: convene a Staff Meeting — pre-read blockers, fan out per-seat briefs in parallel, chair the debate, replicate the ruling to DECISIONS.md same session.
---

# Staff Meeting: Convene

Full governing procedure: the org's Staff Meeting doctrine. Run this when new
intent needs debate, a plan, and a ruling (the router's session-open item for
new intent).

1. **Convening checklist, before writing anything** (Staff Meeting doctrine
   §5): read the blocked-items register for anything already blocked that
   touches this intent; read the ranked-proposals inbox for any relevant
   proposal; decide which seats the intent actually touches (convening seats
   it doesn't touch is its own failure mode: bloat, diluted debate).
2. Create a dated meeting directory. Write the intent file: the operator's
   intent verbatim, or transcribed and marked so if it came from chat
   (`(transcribed from chat, verbatim, <date>)`). State which seats are
   convened and why, in this file.
3. **Fan out seat briefs with subagents, in parallel, at building tier**
   (the org's model-tier configuration, duty `seat-briefs`; or a reasoning-tier
   duty if a chartered executive seat such as a COO is convened — the one
   named exception to building tier). Launch one subagent per convened seat,
   each pointed at that seat's own charter and ledger plus the meeting's
   intent file, and nothing else from another seat's brief — briefs are
   drafted independently so that disagreement in the debate document is real,
   not one seat echoing another it already read. Each subagent writes one
   file: its seat's brief, its own honest position (what it would do, what it
   needs, what risks it sees).
4. **Chair at reasoning tier**, per the model-tier configuration's chair duty,
   for the two judgment-heavy steps that follow. Do not delegate these to a
   building-tier subagent; they are exactly the work reasoning tier is
   reserved for.
   - Write the debate document after all briefs land: agreements the briefs
     converge on without prompting, live disagreements named plainly and
     attributed to the seat that holds each position (never resolved by
     picking a side), and pressure tests (the chair's own probing questions,
     not answered on the seats' behalf). A debate document that reads as
     unanimous when the briefs were not is a defect, not a convenience.
   - Write the plan document: the missions this intent fans out into, an
     owning seat per mission, and a rulings-needed table where every row
     carries a recommended default (the proceed-on-default pattern) so a
     single "go" approves the whole table, or the operator can rule row by
     row. A row with no default is an incomplete plan.
5. **Stop. Wait for the operator's ruling.** The ruling file is the only file
   in the directory a human writes. If the ruling arrives in chat, transcribe
   it into the ruling file verbatim, marked `(chat ruling, transcribed
   verbatim, <date>)`. Do not paraphrase.
6. **Replicate the ruling to `DECISIONS.md`** in the same session it is
   given, as the next numbered ruling entry, dated, in the shared ledger
   format. A ruling that lives only in the meeting's own ruling file is not
   fully recorded.
7. **Fan out mission packets.** Only after step 6: for each mission the
   ruling approved (as ruled, including any amendment), create the mission's
   packet (an immutable snapshot of what was ruled), a state file set to
   `ruled`, and an empty findings file. Mirror the packet path into the
   meeting directory's own missions index per the Staff Meeting doctrine.
8. **Close.** Post any items only the operator can unblock to the
   blocked-items register immediately, update the handoff file and the
   session log. A meeting that skips this closing step has not actually
   convened, even if every file through the missions index exists on disk.

Source: generalized from the operator's private doctrine, §2.2 (moved into this skill 2026-09-16).
