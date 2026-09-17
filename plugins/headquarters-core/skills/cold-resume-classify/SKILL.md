---
name: cold-resume-classify
description: After running cold-resume's reconstruction procedure: classify the stop point with the seven-row table, then state the honest limits of what files alone can tell you.
---

# cold-resume-classify

Use this skill once the cold-resume reconstruction procedure has already been
run and a picture of live state is on the table. Its job is the last move in
that procedure: name exactly what kind of stop point the org is sitting at,
propose the safe next step for it, and then say plainly what this method
cannot tell you.

## 4. Stop-point classification

| Signal on disk | What it means | Safe next step |
|---|---|---|
| A meeting directory has its intent, briefs, and plan filed, but the ruling file is still a stub or absent | **Mid-meeting, at the ruling gate.** A plan exists; no human has ruled on it. | Surface the plan and its rulings table to the operator. Do not fan out any packet, do not treat a recommended default as approved, do not flip any register status. |
| A mission `STATE.md` exists with status anything other than `sealed` | **Mid-mission.** A packet is in flight or paused. | Read `STATE.md`, then `FINDINGS.md`. Resume from the recorded phase and honour the packet's resume protocol. Packets are immutable once fanned out: change them only on an explicit operator redirect, logged, never by silent edit. |
| A ruling is recorded in a meeting's ruling file, but the decisions ledger has no matching entry | **Ruled but not replicated.** The operator has spoken and the record is incomplete. | Close the gap first: write the ruling into `DECISIONS.md` as the next number, then execute its consequences (status flips, board items resolved, packets fanned out) before starting anything new. |
| Files exist on disk that no register, ledger, or mission file accounts for | **Mid-build, uncaptured.** A prior session's work is sitting there unrecorded. | Verify the files against the deliverable list they were meant to satisfy before treating any of it as done. Do not assume partial work is either finished or safe to discard. Capture what is real; flag what is ambiguous. |
| `HANDOFF.md`'s topmost entry describes a state the registers and mission files no longer show | **Stale handoff.** The last session changed things after writing its account, or ended without updating it. | Trust the registers and mission files. Use `git log` to establish the true sequence. Report the staleness to the operator; do not quietly rewrite history to match. |
| A projected spend has no reconciled actual against it | **Unreconciled meter.** A run happened and nobody closed the loop. | Reconcile before authorising anything new. An unreconciled ledger makes every subsequent projection unreliable. |
| None of the above: no open meeting edge, no unsealed mission, no uncaptured work, no unreplicated ruling | **Clear.** The org is at rest between units of work. | Route from the pick-list in `CLAUDE.md`: convene a meeting, execute or resume a mission, run an operations sweep, run a dream (if a cap is set), or park. |

A session can sit in several rows at once - mid-mission on one thread while a
separate meeting waits at its ruling gate. Classify each thread separately.
Never collapse them into a single verdict; that is how live work gets
forgotten.

## 6. Honest limits

- **This procedure reconstructs what was recorded, not what was known.** A
  decision the operator made verbally and nobody wrote down is invisible here
  and always will be. The rail is the close ritual, not this skill.
- **Registers can be wrong.** Role-ownership makes them the best available
  record, not an infallible one. When a register contradicts the artifact it
  summarises, the artifact is usually closer to the truth, and the register
  needs a correcting entry - appended, not overwritten.
- **History is only as honest as the commits.** A session that lumps a week
  of unrelated work into one commit has degraded the tie-breaker for everyone
  after it. That is why commit-per-work-unit is doctrine, not taste.
- **This skill goes stale too.** If a new kind of record is added to the
  repo, place it in the trust order explicitly. An unranked record is a
  future disagreement with no rule to settle it.

Read `reference.md` when the invoker wants to see this classification step
applied to a full worked example end to end, rather than just the table in
the abstract.

Source: ops/COLD_RESUME.md §4, §6 (moved into this skill 2026-09-16)
