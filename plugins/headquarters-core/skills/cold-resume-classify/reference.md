# Worked example: classifying a cold-resume stop point

*This example is invented, start to finish, to show the method applied. The
business, the projects, the numbers, and the dates are fictional. Read it for
the shape of the reasoning, not for its content.*

**The setting.** The operator runs a small coffee roastery: a retail
storefront and a growing wholesale line selling to cafes. A session opens
with no memory. The operator types nothing but "orient".

**Step 1-2, constitution.** `CLAUDE.md` establishes the gates in force, the
router, and that nothing sends, deploys, or spends beyond the session without
the operator. Nothing here has been amended in a way that changes the route.

**Step 3, the blocked board.** `registers/BLOCKED_ON_OPERATOR.md` shows two
open items, newest first:

- **B-6** - "Wholesale pricing plan landed, awaiting your ruling," naming
  `meetings/2026-03-09-wholesale-pricing/03-plan.md`.
- **B-5** - "Sign the second-location lease amendment." Real-world act, no
  dependency on anything in this repo.

One file, and the session already knows the org's live edge: a plan is
waiting on a human word, and it names the exact file.

**Step 4, tasks.** `registers/TASKS.md` shows:

- **T-11** *Wholesale pricing rebuild* - status `in-flight`, packet at
  `missions/wholesale/pricing-rebuild/`, owner Finance.
- **T-12** *Cafe onboarding pack* - status `proposed`, cross-linked to B-6; it
  cannot start until the pricing plan is ruled.
- **T-9** *Storefront signage refresh* - status `sealed`.

T-12's cross-link corroborates B-6 from the register side. Two independent
records agreeing is what "reconstructed" feels like.

**Step 5, projects.** `registers/PROJECTS.md` carries a wholesale section
naming the same pricing question as its top open risk, and a retail section
with nothing live. Consistent so far.

**Step 6, spend.** `ledgers/SPEND.md` shows a per-day cap set at onboarding,
two reconciled runs against the pricing mission this week, and no
unreconciled projection. The meter is clean; there is headroom for one more
modest run today.

**Step 7, meetings and missions.** One meeting directory,
`meetings/2026-03-09-wholesale-pricing/`, holds its intent, four briefs, a
debate, and a plan - and its ruling file is still the unfilled stub. That is
the meeting's live edge and it matches B-6 exactly.

One mission directory, `missions/wholesale/pricing-rebuild/`. Its `STATE.md`
header reads `status: in-flight`, `needs-local: no`, and the body records
**phase 2 of 4 complete** with a checkpoint line naming the file that phase 2
produced. `FINDINGS.md` holds two findings, one of them flagged as needing
the Finance seat's review before phase 3.

**Step 8, handoff.** `HANDOFF.md`'s topmost entry says the pricing mission is
"at phase 1, phase 2 launching next." That contradicts `STATE.md`, which says
phase 2 is complete. Per the trust order, `STATE.md` wins - it is the
mission's own role-owned record and the handoff is narrative. But before
acting on that, the session checks whether the state file is genuinely newer
or whether someone edited it optimistically.

**Step 9, the tie-breaker.** `git log` shows, most recent first: a commit
landing the phase 2 output file with a message naming phase 2 complete, and
*before* it, the commit that wrote the handoff entry. The sequence is
unambiguous: the last session finished phase 2 and ended without updating
its handoff. `STATE.md` is right, `HANDOFF.md` is stale, and the staleness
has a named cause - a session that closed without running its park ritual.

**Step 10, classify and propose.** Two live threads, classified separately:

- *Thread one, at the ruling gate.* The pricing meeting's plan is filed and
  its ruling file is a stub; B-6 and T-12 name the same gate. Safe next
  step: surface the plan and its rulings table to the operator and wait.
  Nothing downstream moves - no packet, no status flip, no resolved board
  item.
- *Thread two, mid-mission.* The pricing rebuild is complete through phase 2
  with one finding awaiting the Finance seat. Safe next step: read the
  finding, take it to the Finance seat, and resume at phase 3 - but only
  after the operator confirms this is where he wants the session's
  attention.

The session also reports the stale handoff as a finding rather than quietly
fixing it, because the operator should know that a prior session ended
without parking properly - that is a discipline problem, not a typo.

**What this example demonstrates.** The registers named the edge before any
narrative was read. The mission file beat the handoff. History settled the
contradiction in one look. And no file was written during any of it. That is
a complete cold resume: five minutes of reading, zero writes, one proposal,
and a halt.

Source: ops/COLD_RESUME.md §5 (moved into this skill 2026-09-16)
