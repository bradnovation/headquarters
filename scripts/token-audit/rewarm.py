#!/usr/bin/env python3
# rewarm.py
# <!-- file-class: DOCTRINE -->
"""Cache re-warm events on each project's main chain, with attribution.

Read-only over the TOP-LEVEL ``~/.claude/projects/<project-dir>/*.jsonl``
files only (a project's main chain - nested files such as a subagent's own
transcript are a different chain and are excluded here on purpose). Reads
usage and structural metadata plus one thing that is not strictly metadata:
to attribute a re-warm to an incoming cross-session message, it checks
whether a user record's text contains the literal marker
``<cross-session-message`` - a substring check, never printed, never stored,
and never used for anything but a yes/no flag alongside the timestamp.
Message text is otherwise never read.

A "re-warm" is defined here as one assistant turn whose
cache_creation_input_tokens exceeds 40,000: a fresh, expensive cache write
happening on a chain that should usually be reading a warm cache instead.
For each one found, this script reports how long it had been since the
previous turn on that chain (a long gap means the 1-hour cache TTL simply
expired) and whether the turn immediately followed an incoming cross-session
message (a plausible alternative cause: a message landing mid-conversation
can force a cache rebuild even inside the TTL window).

The window defaults to the last 21 days; pass --since/--until for any other
range, and --projects to limit to project directories whose raw name
contains a given substring.
"""
import argparse
import glob
import json
import os
import statistics

from _common import (
    DEFAULT_PROJECTS_DIR,
    add_common_args,
    label_for_project_dir,
    list_project_dirs,
    parse_ts,
    resolve_window,
    window_label,
)

REWARM_THRESHOLD_TOKENS = 40_000
LONG_GAP_MINUTES = 55
CROSS_SESSION_MARKER = "<cross-session-message"


def extract_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(b.get("text", "") for b in content if isinstance(b, dict))
    return ""


def build_project_turns(proj_path, since_dt, until_dt):
    """Return sorted (ts, cache_creation, cache_read, output, after_cross_session) tuples."""
    turns = []
    for fpath in sorted(glob.glob(os.path.join(proj_path, "*.jsonl"))):
        seen = set()
        last_was_cross_session = False
        try:
            fh = open(fpath, "r", errors="replace")
        except Exception:
            continue
        with fh:
            for line in fh:
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                ts = parse_ts(d.get("timestamp"))
                message = d.get("message") or {}
                if ts is None:
                    continue
                if ts < since_dt or ts >= until_dt:
                    continue
                if d.get("isSidechain"):
                    continue
                if d.get("type") == "user":
                    content = message.get("content")
                    text = extract_text(content) if isinstance(content, (str, list)) else ""
                    if CROSS_SESSION_MARKER in text:
                        last_was_cross_session = True
                    elif not any(
                        isinstance(b, dict) and b.get("type") == "tool_result"
                        for b in (content if isinstance(content, list) else [])
                    ):
                        last_was_cross_session = False
                    continue
                if d.get("type") != "assistant":
                    continue
                mid = message.get("id")
                usage = message.get("usage")
                if not usage or mid in seen:
                    continue
                seen.add(mid)
                turns.append((
                    ts,
                    usage.get("cache_creation_input_tokens", 0) or 0,
                    usage.get("cache_read_input_tokens", 0) or 0,
                    usage.get("output_tokens", 0) or 0,
                    last_was_cross_session,
                ))
    turns.sort()
    return turns


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    add_common_args(parser)
    parser.add_argument("--projects-dir", default=None, help=argparse.SUPPRESS)
    args = parser.parse_args()

    projects_dir = args.projects_dir or DEFAULT_PROJECTS_DIR
    since_dt, until_dt = resolve_window(args)

    print(f"rewarm.py - window {window_label(since_dt, until_dt)}"
          + (f", project filter {args.projects!r}" if args.projects else ""))
    print(f"re-warm threshold: cache_creation_input_tokens > {REWARM_THRESHOLD_TOKENS:,} in one turn")
    print()

    for dirname in list_project_dirs(projects_dir, args.projects):
        label = label_for_project_dir(dirname)
        proj_path = os.path.join(projects_dir, dirname)
        turns = build_project_turns(proj_path, since_dt, until_dt)
        if not turns:
            continue

        tot_cc = sum(t[1] for t in turns)
        big = [(i, t) for i, t in enumerate(turns) if t[1] > REWARM_THRESHOLD_TOKENS]
        big_cc = sum(t[1] for _, t in big)

        gaps = []
        after_cross_session = 0
        for i, t in big:
            if i > 0:
                gaps.append((t[0] - turns[i - 1][0]).total_seconds() / 60)
            after_cross_session += t[4]
        long_gaps = sum(1 for g in gaps if g >= LONG_GAP_MINUTES)

        print(
            f'{label:20s} main-chain turns={len(turns):6d} '
            f'cache_create total={tot_cc/1e6:6.1f}M | '
            f'rewarm turns(>{REWARM_THRESHOLD_TOKENS//1000}K cc)={len(big):4d} '
            f'carrying {big_cc/1e6:6.1f}M ({100*big_cc/max(tot_cc,1):.0f}%) | '
            f'of those: gap>={LONG_GAP_MINUTES}min={long_gaps:3d}, '
            f'after cross-session msg={after_cross_session:3d}, '
            f'median gap={statistics.median(gaps) if gaps else 0:.0f}min | '
            f'median cc on rewarm={statistics.median([t[1] for _, t in big]) if big else 0:,.0f}'
        )


if __name__ == "__main__":
    main()
