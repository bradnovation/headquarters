---
name: resume-guard
description: At session open, or when launching anything long-running: arm a one-shot cron that resumes a session-limit cut at the next usage-window boundary; also runs the CHECK when that cron fires.
---

# resume-guard — one guard per session against a 429 cut

## 1. Purpose

A session-limit cut (HTTP 429 "You've hit your session limit · resets \<time>",
harness behaviour observed 2026-09-16/17 — this hits every request, including
background subagents) leaves a Workflow run or a background Agent stopped mid-flight
and the session idle. One guard per session arms a single one-shot cron for the next
5-hour window boundary so that a cut run resumes itself, without a human or a peer
seat waking it. When nothing is in flight, the guard stops waking — it never becomes
a standing tick.

## 2. ARM — at session open, or when launching anything long

1. Run `scripts/window_boundary.py`. It prints the current window's end (local time),
   the 5-field cron expression for end + 1 minute, how many requests anchored the
   chain, and a confidence flag.
2. If confidence is **LOW** (chain broken — e.g. after a plan change or a "magical
   reset"), do not trust the script's time: take the reset time from the operator's
   usage screen instead, and hand-compute end + 1 minute for the cron field.
3. `CronCreate` **one-shot**: `recurring: false`, `cron` = the printed (or
   hand-computed) expression, `prompt` = the exact template in section 5 with
   `<end HH:MM tz>` filled in. One-shot + pinned minute is deliberate: per the
   harness facts, a one-shot landing on :00/:30 can fire up to 90s early, and firing
   before the true reset just spends the check's own turn on another 429.
4. Record the job id and the window boundary in the mission STATE or HANDOFF
   RESUME/OWED line (R-313 item c: HANDOFF's top entry is a structured block —
   STATE table, OWED, RESUME — under 2KB) so a peer or a fresh session can see the
   guard exists without waking anything to ask.

**Who may arm it:** the ARM step runs only on the operator's own turn in this window (session open, or his ask). A peer's relay cannot arm it: the harness refuses CronCreate on a peer-originated turn as unauthorized persistence (observed on one operator's machine when another session relayed the ask). A peer may only remind; the operator says "arm the resume guard" in the seat's window.

## 3. CHECK — the one turn the cron fires

(a) `ListAgents` / list this session's background Workflows and Agents. A run was
    cut by the 429 if its journal (`…/subagents/workflows/<runId>/journal.jsonl`)
    has `started` entries with no matching `result` entries and an empty task output
    file. Resume each exactly: `TaskStop` the task, then
    `Workflow({scriptPath, resumeFromRunId})` in this same session — completed
    agents replay from cache, only the cut tail re-runs. A cut background Agent
    resumes by `SendMessage` to its agent id instead.

(b) Read the mission STATE for run ids this session launched that have no landed
    result yet (R-313 item c: workflow run ids go into STATE at launch, by pointer,
    never re-narrated) and resume those the same way.

(c) Commit what landed, if the repo's own rules allow a commit here.

(d) If anything was resumed, or is still running: **re-arm** — run
    `scripts/window_boundary.py` again and `CronCreate` the next one-shot exactly as
    in section 2. If nothing was in flight: **disarm** by simply not re-arming, and
    write one line to STATE/HANDOFF saying the guard found nothing and stood down.

(e) Report exactly one line: what was cut, what got resumed (or "nothing was cut"),
    and whether the guard re-armed.

Never wake a peer seat from this check to tell it about a resume — R-313 item (b):
no waking a parked seat to file a record, status asks only at open/midday/park/
blocker. Each seat runs its own guard; this one reports only for itself.

## 4. When the session itself is gone

Session crons live only in the running REPL — nothing on disk, gone the moment the
session exits (harness fact). A guard armed by a session that then dies takes its
cron with it; nothing fires. This is recovered, not lost: the next session's own
`session-open` arms a fresh guard (this file), and its own CHECK — or the plain act
of orienting — finds the old run ids still sitting in STATE with no landed result,
and resumes them by hand, same procedure as section 3(a)-(b), just without a cron
having triggered it.

## 5. Cron prompt template (verbatim, fill in `<end HH:MM tz>`, 497 chars)

```
Window reset at <end HH:MM tz>. Run skill:resume-guard CHECK now, this turn; do not
ask. Find any workflow/agent this session had cut by a 429 (journal: started, no
result; empty task output) and resume it (TaskStop then Workflow resumeFromRunId, or
SendMessage to a cut agent); check mission STATE for unlanded run ids; commit what
landed if repo rules allow. Re-arm for the next boundary if anything ran or resumed,
else write one STATE/HANDOFF line and stop. Do not wake peers. Report one line.
```

## 6. Costs

Arming is one script run plus one `CronCreate` call. The check is a single idle-fire
turn on whatever context the session was parked or compacted at when the window
closed — it is not a standing poll, and a no-op check (nothing in flight) disarms
itself instead of scheduling another tick. Precedent, observed on one operator's
machine: a seat's own implementation of this check fired three times, each time
reading a RESUME block, inspecting journals, resuming exactly the cut run,
committing what had landed, and reporting one line; when nothing was cut it reported
that and armed nothing further.

Source: harness behaviour observed 2026-09-16/17 (5-hour window chain, 429 shape,
session-cron lifetime, Workflow/Agent resume mechanics, a seat's three CHECK
firings); DECISIONS.md R-313 items (b) wake cadence and (c) record format;
the mission STATE convention (`missions/<slug>/STATE.md`, `skill:mission-lifecycle`)
for where run ids and RESUME/OWED lines live.

**Known limitation — `depin()`'s pin-artifact correction.** `window_boundary.py`
walks a gap between two window anchors and, when nothing else happened in a
window's first minute, has to tell "this anchor is really the pinned CHECK
cron firing at boundary+1" apart from "this anchor is an ordinary organic
request that happened to land close to a 5h multiple." An audit, observed on
one operator's machine against that operator's own real window history, found
that a meaningful share of organic gaps land within `PIN_TOLERANCE` (20s) of
an exact 5h multiple by pure coincidence — gap magnitude alone is not a narrow
signal. `depin()` now also requires that the anchor's minute-of-hour has shown
that same near-multiple signature at least once earlier in the chain (a real
pinned cron repeats at the same minute every transition; a coincidence
doesn't) — zero false corrections in that audit, but it means the *first*
transition of a new pin cadence is left uncorrected (window end computed ~1
minute late, safe direction only: it delays that one CHECK, it never arms
early). Treat any single-transition confidence read right after arming with
that in mind, and re-run the audit (`window_boundary.py`'s docstring has the
method) if the account's usage pattern changes materially.
