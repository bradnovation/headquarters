---
name: mission-lifecycle
description: A mission has a packet and needs resuming or advancing: move proposed to ruled to in-flight to review to sealed one step at a time, never edit the packet, log redirects instead.
---

# Mission Lifecycle

Full governing procedure: the org's Staff Meeting doctrine, §4. Run this to
resume or execute an already-fanned-out mission packet (the router's
session-open item for an existing mission).

1. Read the mission's `STATE.md` first, then `FINDINGS.md` if present, before
   touching the packet. `STATE.md` tells you which of the five states you're
   in; `FINDINGS.md` tells you what has actually been discovered or produced
   so far.
2. **Packet immutability.** The packet is a snapshot from the ruling that
   fanned it out. Never edit it in place. If the operator redirects the
   mission mid-flight, append a dated entry to `STATE.md` recording the
   redirect (what changed, why), plus a `DECISIONS.md` entry if the redirect
   amounts to a new ruling; either supersede specific lines with a visible
   amendment block, or, for a large enough change, close the mission and open
   a new one referencing it. A packet rewritten silently in place is a
   protocol violation regardless of how sensible the edit seemed.
3. **Advance the status machine, one state at a time, never skipped, never
   moved backward except via a logged redirect:**
   ```
   proposed -> ruled -> in-flight -> review -> sealed
   ```
   - `proposed`: named in the plan document, not yet ruled.
   - `ruled`: the operator approved it; packet fanned out, no work started.
   - `in-flight`: a seat is actively executing. Move here the moment work
     starts and append the dated transition line (newest on top, same ledger
     format as everything else).
   - `review`: work is done, awaiting the canon-guard-seal skill (and General
     Counsel, if money or liability is present) before it can seal.
   - `sealed`: canon-guard has passed (and General Counsel, where required).
     Closed.
4. Do the actual work at the tier the model-tier duty map assigns the owning
   seat for that duty (e.g., a content seat's building-tier duty, an
   engineering seat's build duty at building tier, that same engineering
   seat's plan duty at reasoning tier). Record what the mission discovers or
   produces in `FINDINGS.md`, separate from `STATE.md` bookkeeping — this is
   where a successor session reads to understand the substance.
5. When work is done, move `STATE.md` to `review` and run the canon-guard-seal
   skill. If money or liability is present, also route through the
   counsel-drafting skill before sealing.
6. **Seal only after every required gate has passed.** On seal: post any
   operator-only items to `registers/BLOCKED_ON_OPERATOR.md` immediately, not
   held until later; write the after-action note to the owning seat's
   `LEDGER.md` (a standing habit for the Agent Quality function — required
   for the seal to be complete, though it does not itself block the `sealed`
   transition). Move `STATE.md` to `sealed`.
7. Update the COO's registers (`registers/TASKS.md`, `registers/PROJECTS.md`
   if a project's state changed) and, before the session's final commit, run
   the session-close skill's `HANDOFF.md` and session-log update.

Source: generalized from the operator's private doctrine, §2.3 (moved into
this skill 2026-09-16).
