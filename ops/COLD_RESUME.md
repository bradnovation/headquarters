# COLD RESUME - reconstructing the state of this org from the repo alone
<!-- file-class: DOCTRINE -->

*This file ships with the product and is upstream-pullable. Edit it
only if you intend to own your own copy of it forever.*

*Purpose: any session that opens this repo with no memory of anything that came
before must be able to work out exactly where the org stands, what is safe to do
next, and what it must not touch - using only the files in this repo. No prior chat,
no session transcript, no verbal recap from the operator is ever required. If a
reconstruction needs a human to explain it, the repo has failed, not the session.*

---

## 1. Why this file exists

Sessions are disposable. The repo is not. Every session ends - by design, by
interruption, by a closed laptop - and the next one starts from nothing. An org that
only works when the same conversation continues is not an org; it is a habit living
inside one context window.

The whole of this system's operability rests on one bar: **a stranger, or a fresh
session, reading files in a fixed order, reaches the same picture of reality that the
last session had.** This file states that order, explains why it runs in that
sequence, and shows the procedure applied end to end.

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
10. **Classify the stop point** (section 4), then propose a route and halt. Do not act
    on the proposal without the operator's word.

If the repo is large, steps 3-7 are still cheap: registers and ledgers are short by
design, and any register that has grown too long to read in full has stopped doing its
job and should be archived rather than skimmed.

---

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

A session can sit in several rows at once - mid-mission on one thread while a separate
meeting waits at its ruling gate. Classify each thread separately. Never collapse them
into a single verdict; that is how live work gets forgotten.

---

## 5. Worked example

*This example is invented, start to finish, to show the method applied. The business,
the projects, the numbers, and the dates are fictional. Read it for the shape of the
reasoning, not for its content.*

**The setting.** The operator runs a small coffee roastery: a retail storefront and a
growing wholesale line selling to cafes. A session opens with no memory. The operator
types nothing but "orient".

**Step 1-2, constitution.** `CLAUDE.md` establishes the gates in force, the router, and
that nothing sends, deploys, or spends beyond the session without the operator.
Nothing here has been amended in a way that changes the route.

**Step 3, the blocked board.** `registers/BLOCKED_ON_OPERATOR.md` shows two open items,
newest first:

- **B-6** - "Wholesale pricing plan landed, awaiting your ruling," naming
  `meetings/2026-03-09-wholesale-pricing/03-plan.md`.
- **B-5** - "Sign the second-location lease amendment." Real-world act, no dependency
  on anything in this repo.

One file, and the session already knows the org's live edge: a plan is waiting on a
human word, and it names the exact file.

**Step 4, tasks.** `registers/TASKS.md` shows:

- **T-11** *Wholesale pricing rebuild* - status `in-flight`, packet at
  `missions/wholesale/pricing-rebuild/`, owner Finance.
- **T-12** *Cafe onboarding pack* - status `proposed`, cross-linked to B-6; it cannot
  start until the pricing plan is ruled.
- **T-9** *Storefront signage refresh* - status `sealed`.

T-12's cross-link corroborates B-6 from the register side. Two independent records
agreeing is what "reconstructed" feels like.

**Step 5, projects.** `registers/PROJECTS.md` carries a wholesale section naming the
same pricing question as its top open risk, and a retail section with nothing live.
Consistent so far.

**Step 6, spend.** `ledgers/SPEND.md` shows a per-day cap set at onboarding, two
reconciled runs against the pricing mission this week, and no unreconciled projection.
The meter is clean; there is headroom for one more modest run today.

**Step 7, meetings and missions.** One meeting directory,
`meetings/2026-03-09-wholesale-pricing/`, holds its intent, four briefs, a debate, and
a plan - and its ruling file is still the unfilled stub. That is the meeting's live
edge and it matches B-6 exactly.

One mission directory, `missions/wholesale/pricing-rebuild/`. Its `STATE.md` header
reads `status: in-flight`, `needs-local: no`, and the body records **phase 2 of 4
complete** with a checkpoint line naming the file that phase 2 produced.
`FINDINGS.md` holds two findings, one of them flagged as needing the Finance seat's
review before phase 3.

**Step 8, handoff.** `HANDOFF.md`'s topmost entry says the pricing mission is "at phase
1, phase 2 launching next." That contradicts `STATE.md`, which says phase 2 is
complete. Per the trust order, `STATE.md` wins - it is the mission's own role-owned
record and the handoff is narrative. But before acting on that, the session checks
whether the state file is genuinely newer or whether someone edited it optimistically.

**Step 9, the tie-breaker.** `git log` shows, most recent first: a commit landing the
phase 2 output file with a message naming phase 2 complete, and *before* it, the commit
that wrote the handoff entry. The sequence is unambiguous: the last session finished
phase 2 and ended without updating its handoff. `STATE.md` is right, `HANDOFF.md` is
stale, and the staleness has a named cause - a session that closed without running its
park ritual.

**Step 10, classify and propose.** Two live threads, classified separately:

- *Thread one, at the ruling gate.* The pricing meeting's plan is filed and its ruling
  file is a stub; B-6 and T-12 name the same gate. Safe next step: surface the plan and
  its rulings table to the operator and wait. Nothing downstream moves - no packet, no
  status flip, no resolved board item.
- *Thread two, mid-mission.* The pricing rebuild is complete through phase 2 with one
  finding awaiting the Finance seat. Safe next step: read the finding, take it to the
  Finance seat, and resume at phase 3 - but only after the operator confirms this is
  where he wants the session's attention.

The session also reports the stale handoff as a finding rather than quietly fixing it,
because the operator should know that a prior session ended without parking properly -
that is a discipline problem, not a typo.

**What this example demonstrates.** The registers named the edge before any narrative
was read. The mission file beat the handoff. History settled the contradiction in one
look. And no file was written during any of it. That is a complete cold resume: five
minutes of reading, zero writes, one proposal, and a halt.

---

## 6. Honest limits

- **This procedure reconstructs what was recorded, not what was known.** A decision the
  operator made verbally and nobody wrote down is invisible here and always will be.
  The rail is the close ritual, not this file.
- **Registers can be wrong.** Role-ownership makes them the best available record, not
  an infallible one. When a register contradicts the artifact it summarises, the
  artifact is usually closer to the truth, and the register needs a correcting entry -
  appended, not overwritten.
- **History is only as honest as the commits.** A session that lumps a week of unrelated
  work into one commit has degraded the tie-breaker for everyone after it. That is why
  commit-per-work-unit is doctrine, not taste.
- **This file goes stale too.** If you add a new kind of record to this repo, place it
  in the trust order here explicitly. An unranked record is a future disagreement with
  no rule to settle it.
