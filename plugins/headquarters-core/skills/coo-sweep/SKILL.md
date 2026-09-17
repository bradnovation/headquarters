---
name: coo-sweep
description: Time to run a portfolio freshness sweep: read-only, scanning tier, file drift only — never touches the vault or edits a venture repo directly.
---

# COO sweep

Full governing procedure: the seat's own charter (`org/seats/coo/CHARTER.md`).
Run this for a freshness check across the portfolio (the router's
session-open item for portfolio freshness).

1. Convene at scanning tier (the org's model-tier configuration, duty
   `coo-sweeps`) — cheap, disposable, read-only.
2. Read across `registers/PROJECTS.md`, `registers/TASKS.md`, and, read-only,
   the venture repos named in `registers/PROJECTS.md`'s repo map. **The sweep
   is read-only outside this repository, full stop** (gate G2, foreign
   repositories): it never edits a venture repo directly, no matter how small
   or obviously-correct the fix looks.
3. Look for drift: a register that says "clean tree" when the tree isn't, a
   stale `HANDOFF.md` in a venture repo, a venture gone quiet without anyone
   noticing, a task whose state no longer matches reality.
4. File findings as one of two things, never silently corrected in place:
   - Routine drift: a new dated `registers/TASKS.md` entry.
   - Anything only the operator can unblock: a new dated
     `registers/BLOCKED_ON_OPERATOR.md` entry, filed the moment it exists,
     not batched for the next Staff Meeting.
5. A sweep never reaches into `vault/` under any circumstance, and never
   touches C2 content beyond noting that it exists and is pending (e.g.
   "pricing decision pending" is fine; drafting or holding the C2 content
   itself is General Counsel's and the CFO's territory, not the COO's).
6. There is no scheduled or cron-driven sweep — no daemons in this system.
   Every sweep is triggered inside an operator-initiated session. Run one now
   if none has run yet since the org's founding build sealed — the seat's own
   queued first work calls for a baseline sweep before any register can be
   called "live."

Source: generalized from the operator's private doctrine, §2.6 (moved into
this skill 2026-09-16).
