#!/usr/bin/env python3
"""resume-guard / window_boundary.py

Reconstructs the CURRENT Claude Code 5-hour usage window (start, end) from
local session transcripts, and prints the one-shot cron expression to arm
for the CHECK turn, at end + 1 minute.

Read-only, python3 standard library only, no network. Reads only the
'timestamp' and 'type' fields of each JSONL line -- never message content.
Skips every file under a 'subagents/' directory: those are subagent /
sidechain transcripts, not main-chain requests, and are not what the
account-wide usage window counts against (harness fact 2026-09-16/17: a
429 cuts every request INCLUDING background subagents, but the window
itself is opened by main-chain turns).

ALGORITHM (harness facts observed 2026-09-16/17, cited in SKILL.md):
  - The 5-hour window is account-wide (all projects share one clock), so
    every top-level */*.jsonl across ~/.claude/projects is in scope.
  - Collect every assistant-message timestamp from the last LOOKBACK_DAYS.
  - Walk the sorted timestamps: a window starts at the first timestamp
    on/after the previous window's end (start + 5h); repeat to build the
    full chain through "now". This directly encodes "the window starts at
    the first request after the previous window ended and resets exactly
    5 hours later."
  - PIN CORRECTION: once resume-guard is armed, its own CHECK cron is
    deliberately pinned to fire at boundary + 1 minute, never at the
    boundary itself (a :00/:30 pin can fire up to ~90s early and would
    eat a 429; +1 dodges that -- see SKILL.md section 2). When nothing
    else happens in a window's first minute, that pinned cron becomes the
    ONLY visible anchor, so a raw walk lands the window's start (and thus
    its end) about a minute late.

    Gap magnitude alone is NOT a safe detector of this: an audit, observed
    on one operator's machine (walking this file's own build_chain()
    output over that operator's real ~/.claude/projects history), found
    that organic window-to-window gaps land within PIN_TOLERANCE of an
    exact 5h multiple by pure chance often enough -- not just once -- that
    gap magnitude alone cannot be trusted, alongside a smaller number of
    genuine pin artifacts. An earlier version of this docstring trusted
    gap magnitude alone as the detector; that undercounted the coincidence
    rate and was replaced by this recomputation.

    What DOES separate the genuine pin artifacts from the coincidences:
    a real armed CHECK cron fires at the SAME minute-of-hour every single
    window transition (ARM always computes end-minute + 1, and the
    underlying boundary minute is stable), so it shows up as a REPEATING
    minute among near-multiple anchors. Every organic coincidence in that
    audit was a singleton -- its minute never recurred anywhere else in
    the history. depin() therefore only corrects an anchor when its
    minute has ALSO shown the near-multiple signature at least once
    earlier in the chain, not on gap magnitude alone. This produced zero
    false corrections in that audit, at the cost of leaving the very
    first post-arm transition uncorrected each time a new pin cadence
    starts (no prior repeat to confirm against yet) -- that only delays
    that one CHECK by ~1 minute, the safe direction (never early, never
    risks eating a 429). See SKILL.md Costs section for this as a known,
    accepted limitation. Only the CURRENT (last) anchor is ever corrected;
    historical anchors used purely to build the chain are left as
    reconstructed.

Verified working, observed on one operator's machine, against that
operator's real ~/.claude/projects data, matching that operator's own
usage screen and the reconstructed chain cited in the harness facts.
"""

import os
import json
import datetime

HOME = os.path.expanduser("~")
PROJECTS_DIR = os.path.join(HOME, ".claude", "projects")
LOOKBACK_DAYS = 7
CONFIDENCE_LOOKBACK_HOURS = 24
WINDOW = datetime.timedelta(hours=5)
PIN_TOLERANCE = datetime.timedelta(seconds=20)


def iter_jsonl_files(root):
    """Every top-level session transcript under each project dir. Never
    descends into a 'subagents/' directory."""
    if not os.path.isdir(root):
        return
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != "subagents"]
        for fn in filenames:
            if fn.endswith(".jsonl"):
                yield os.path.join(dirpath, fn)


def collect_assistant_timestamps(root, cutoff_utc):
    """usage/timestamp fields only -- never message text. Fast substring
    pre-check before json.loads, same pattern as tools/token-audit/."""
    out = []
    files_read = 0
    for path in iter_jsonl_files(root):
        files_read += 1
        try:
            fh = open(path, "r", errors="replace")
        except OSError:
            continue
        with fh:
            for line in fh:
                if '"type":"assistant"' not in line or '"timestamp"' not in line:
                    continue
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                if d.get("type") != "assistant":
                    continue
                ts = d.get("timestamp")
                if not ts:
                    continue
                try:
                    t = datetime.datetime.fromisoformat(ts.replace("Z", "+00:00"))
                except Exception:
                    continue
                if t >= cutoff_utc:
                    out.append(t)
    out.sort()
    return out, files_read


def build_chain(timestamps):
    """A window starts at the first timestamp on/after the previous
    window's end. Returns every anchor (window-opening timestamp) found."""
    if not timestamps:
        return []
    start = timestamps[0]
    end = start + WINDOW
    anchors = [start]
    for t in timestamps[1:]:
        if t >= end:
            start = t
            end = start + WINDOW
            anchors.append(start)
    return anchors


def _near_multiple_over(a, b):
    """(gap - WINDOW) if the gap a-b is within PIN_TOLERANCE of an exact 5h
    multiple, else None. Shared by depin()'s current-anchor check and its
    same-minute history scan so both use one definition of 'near'."""
    gap = a - b
    if gap < WINDOW:
        return None
    over = gap - WINDOW
    if datetime.timedelta(0) <= over <= PIN_TOLERANCE:
        return over
    return None


def depin(anchors):
    """Correct the boundary+1 pinned-check-cron artifact on the CURRENT
    (last) anchor only. Returns (start, evidence_note_or_None).

    Gap magnitude within PIN_TOLERANCE of an exact 5h multiple is NOT
    sufficient on its own -- see the module docstring's PIN CORRECTION
    section: observed on one operator's machine, a meaningful share of
    real organic gaps hit that band by coincidence. What is reliable is
    repetition: a genuinely armed CHECK cron fires at the same minute-of-
    hour every transition, so only apply the correction when this
    anchor's minute has ALSO shown the near-multiple signature at least
    once earlier in the chain -- a lone coincidence never repeats, a real
    pinned cron always does. This misses the first transition of a new
    pin cadence (no prior repeat to confirm against yet); that only
    delays that one CHECK by ~1 minute, never early -- the safe
    direction. Known, accepted limitation; see SKILL.md Costs section.
    """
    start = anchors[-1]
    if len(anchors) < 2:
        return start, None
    over = _near_multiple_over(start, anchors[-2])
    if over is None:
        return start, None

    minute = start.minute  # UTC minute; whole-hour tz offsets (EDT/EST) match local
    prior_hits = 0
    for i in range(1, len(anchors) - 1):
        o = _near_multiple_over(anchors[i], anchors[i - 1])
        if o is not None and anchors[i].minute == minute:
            prior_hits += 1
    if prior_hits < 1:
        return start, None

    corrected = start - datetime.timedelta(minutes=1)
    note = (
        f"anchor {start.isoformat()} sits {over.total_seconds():.1f}s past an exact 5h "
        f"multiple from its predecessor AND shares its minute-of-hour with {prior_hits} "
        f"earlier near-multiple anchor(s) in this chain -- the boundary+1 pinned-cron "
        f"signature confirmed by repetition, not gap magnitude alone (harness fact "
        f"2026-09-16/17: the check fires at boundary+1, never at the boundary); backed "
        f"out 1 minute to {corrected.isoformat()}"
    )
    return corrected, note


def main():
    now = datetime.datetime.now(datetime.timezone.utc)
    cutoff = now - datetime.timedelta(days=LOOKBACK_DAYS)

    timestamps, files_read = collect_assistant_timestamps(PROJECTS_DIR, cutoff)
    if not timestamps:
        print(f"no assistant timestamps found in the last {LOOKBACK_DAYS} days "
              f"({files_read} files scanned); cannot reconstruct a window.")
        return

    anchors = build_chain(timestamps)
    start, pin_note = depin(anchors)
    end = start + WINDOW

    if now >= end:
        raw_end_str = end.astimezone().strftime("%Y-%m-%d %H:%M %Z")
        print("next request opens a new window; arm after your first turn.")
        print(f"(last reconstructed window ended {raw_end_str}, now is past it)")
        return

    local_end = end.astimezone()
    local_start = start.astimezone()
    cron_time = local_end.replace(second=0, microsecond=0) + datetime.timedelta(minutes=1)
    cron_expr = f"{cron_time.minute} {cron_time.hour} {cron_time.day} {cron_time.month} *"

    recent_cutoff = now - datetime.timedelta(hours=CONFIDENCE_LOOKBACK_HOURS)
    recent_anchors = [a for a in anchors if a >= recent_cutoff]
    if len(recent_anchors) >= 2:
        confidence = "HIGH"
        why = f"{len(recent_anchors)} anchors in the trailing 24h"
    else:
        confidence = "LOW"
        if not recent_anchors:
            gap_h = (now - anchors[-1]).total_seconds() / 3600
            last_str = anchors[-1].astimezone().strftime("%Y-%m-%d %H:%M %Z")
            why = (f"no anchor in the trailing 24h (most recent {last_str}, {gap_h:.1f}h ago) "
                   f"-- chain may be broken by a plan change or reset; take the reset time "
                   f"from the operator's usage screen instead")
        else:
            why = ("only 1 anchor in the trailing 24h -- current window not yet confirmed "
                   "by a second transition; take the reset time from the operator's usage "
                   "screen instead")

    print(f"window start: {local_start.strftime('%Y-%m-%d %H:%M %Z')}")
    print(f"window end:   {local_end.strftime('%Y-%m-%d %H:%M %Z')}")
    print(f"cron (end+1min, minute hour dom month *): {cron_expr}")
    print(f"requests anchored the chain: {len(anchors)} (lookback {LOOKBACK_DAYS}d, "
          f"{len(timestamps)} timestamps, {files_read} files scanned)")
    print(f"confidence: {confidence} ({why})")
    if pin_note:
        print(f"evidence: {pin_note}")
    else:
        print(f"evidence: current anchor {start.isoformat()} is the first assistant "
              f"timestamp on/after the previous window's end")


if __name__ == "__main__":
    main()
