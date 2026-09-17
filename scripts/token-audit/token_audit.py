#!/usr/bin/env python3
# token_audit.py
# <!-- file-class: DOCTRINE -->
"""Per-project, per-model, per-day token audit over local Claude Code transcripts.

Read-only over ``~/.claude/projects/<project-dir>/**/*.jsonl``. Reads usage
and structural metadata only - never message text: the fields this script
looks at are ``type``, ``timestamp``, ``sessionId``, ``isSidechain``, and
``message.id`` / ``message.model`` / ``message.usage``.

The window defaults to the last 21 days; pass --since/--until to audit any
other range, and --projects to limit to project directories whose raw name
(as it appears under ~/.claude/projects) contains a given substring. See
_common.py for exactly how the window and the project filter are resolved,
and README.md in this directory for what each printed section means and how
to use this script to take a baseline and compare a later run against it.

Sections A, B, D, E, F and the parse-meta footer print with a plain run;
pass --extended for sections G (per-model-bucket totals again, alongside
turn counts), H (main-chain vs subagent-chain totals per project) and H2
(main-chain turns above two effective-context thresholds, across whichever
projects the --projects filter selected).
"""
import argparse
import glob
import json
import os
import statistics
import sys
from collections import defaultdict

from _common import (
    DEFAULT_PROJECTS_DIR,
    add_common_args,
    fmt_row,
    label_for_project_dir,
    list_project_dirs,
    parse_ts,
    pctl,
    resolve_window,
    window_label,
)
from prices import model_bucket


def build_turns(projects_dir, since_dt, until_dt, projects_filter):
    project_dirs = list_project_dirs(projects_dir, projects_filter)

    files_parsed = 0
    total_lines = 0
    skipped_lines = 0        # no usage / not assistant / parse error
    out_of_window_lines = 0  # had usage, timestamp outside the window
    duplicate_blocks = 0     # extra content-block lines for an already-seen message id

    global_min_ts = None
    global_max_ts = None

    turns = []
    seen_keys = set()

    for dirname in project_dirs:
        proj_path = os.path.join(projects_dir, dirname)
        label = label_for_project_dir(dirname)
        jsonl_files = glob.glob(os.path.join(proj_path, "**", "*.jsonl"), recursive=True)
        for fpath in jsonl_files:
            files_parsed += 1
            is_main_file = (os.path.dirname(fpath) == proj_path)
            try:
                fh = open(fpath, "r", errors="replace")
            except Exception:
                continue
            with fh:
                for line in fh:
                    total_lines += 1
                    if '"type":"assistant"' not in line:
                        skipped_lines += 1
                        continue
                    try:
                        d = json.loads(line)
                    except Exception:
                        skipped_lines += 1
                        continue
                    if d.get("type") != "assistant":
                        skipped_lines += 1
                        continue
                    msg = d.get("message") or {}
                    usage = msg.get("usage")
                    if not usage:
                        skipped_lines += 1
                        continue
                    ts = parse_ts(d.get("timestamp"))
                    if ts is None:
                        skipped_lines += 1
                        continue
                    if global_min_ts is None or ts < global_min_ts:
                        global_min_ts = ts
                    if global_max_ts is None or ts > global_max_ts:
                        global_max_ts = ts
                    if ts < since_dt or ts >= until_dt:
                        out_of_window_lines += 1
                        continue

                    session_id = d.get("sessionId")
                    mid = msg.get("id")
                    key = (session_id, mid)
                    if mid is not None and key in seen_keys:
                        duplicate_blocks += 1
                        continue
                    if mid is not None:
                        seen_keys.add(key)

                    it = int(usage.get("input_tokens") or 0)
                    cc = int(usage.get("cache_creation_input_tokens") or 0)
                    cr = int(usage.get("cache_read_input_tokens") or 0)
                    ot = int(usage.get("output_tokens") or 0)
                    is_side = bool(d.get("isSidechain")) or (not is_main_file)

                    turns.append({
                        "project": label,
                        "session": session_id,
                        "ts": ts,
                        "model": msg.get("model"),
                        "input": it,
                        "cc": cc,
                        "cr": cr,
                        "output": ot,
                        "ctx": it + cc + cr,
                        "sidechain": is_side,
                        "main_file": is_main_file,
                        "file": fpath,
                    })

    turns.sort(key=lambda t: t["ts"])

    meta = {
        "files_parsed": files_parsed,
        "total_lines": total_lines,
        "skipped_lines": skipped_lines,
        "out_of_window_lines": out_of_window_lines,
        "duplicate_blocks": duplicate_blocks,
        "global_min_ts": global_min_ts,
        "global_max_ts": global_max_ts,
    }
    return turns, meta


def dominant_model(turns_subset):
    mc = defaultdict(int)
    for t in turns_subset:
        mc[(t["model"] or "?").replace("claude-", "")] += 1
    if not mc:
        return "?"
    dom = max(mc.items(), key=lambda kv: kv[1])[0]
    extra = len(mc) - 1
    return dom if extra <= 0 else f"{dom}+{extra}"


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    add_common_args(parser)
    parser.add_argument("--projects-dir", default=None, help=argparse.SUPPRESS)
    parser.add_argument(
        "--extended", action="store_true",
        help="also print sections G, H, and H2 (per-model totals, main-vs-subagent "
        "chain totals per project, and context-threshold counts)",
    )
    args = parser.parse_args()

    projects_dir = args.projects_dir or DEFAULT_PROJECTS_DIR
    since_dt, until_dt = resolve_window(args)

    turns, meta = build_turns(projects_dir, since_dt, until_dt, args.projects)
    files_parsed = meta["files_parsed"]
    total_lines = meta["total_lines"]
    skipped_lines = meta["skipped_lines"]
    out_of_window_lines = meta["out_of_window_lines"]
    duplicate_blocks = meta["duplicate_blocks"]
    global_min_ts = meta["global_min_ts"]
    global_max_ts = meta["global_max_ts"]

    out = []

    def add(s=""):
        out.append(s)

    # ---------- A ----------
    proj_stats = defaultdict(lambda: {
        "sessions": set(), "turns": 0, "side_turns": 0,
        "input": 0, "cc": 0, "cr": 0, "output": 0,
    })
    for t in turns:
        ps = proj_stats[t["project"]]
        ps["sessions"].add(t["session"])
        ps["turns"] += 1
        if t["sidechain"]:
            ps["side_turns"] += 1
        ps["input"] += t["input"]
        ps["cc"] += t["cc"]
        ps["cr"] += t["cr"]
        ps["output"] += t["output"]

    add(f"-- A. PER PROJECT TOTALS, tokens in millions ({window_label(since_dt, until_dt)}, sorted by cache_read desc) --")
    add(fmt_row([("project", 22, "l"), ("sess", 4, "r"), ("turns", 7, "r"), ("side%", 5, "r"),
                 ("input_M", 9, "r"), ("cachecr_M", 10, "r"), ("cacherd_M", 10, "r"), ("out_M", 8, "r")]))
    rows = sorted(proj_stats.items(), key=lambda kv: -kv[1]["cr"])
    for proj, s in rows:
        sidepct = (s["side_turns"] / s["turns"] * 100) if s["turns"] else 0
        add(fmt_row([
            (proj, 22, "l"), (len(s["sessions"]), 4, "r"), (s["turns"], 7, "r"),
            (f"{sidepct:.0f}%", 5, "r"),
            (f"{s['input']/1e6:.2f}", 9, "r"), (f"{s['cc']/1e6:.2f}", 10, "r"),
            (f"{s['cr']/1e6:.2f}", 10, "r"), (f"{s['output']/1e6:.2f}", 8, "r"),
        ]))
    add("")

    # ---------- B ----------
    add("-- B. PER-TURN EFFECTIVE CONTEXT = input+cache_creation+cache_read (tokens) --")
    add(fmt_row([("project", 22, "l"), ("turns", 7, "r"), ("median", 10, "r"), ("p90", 10, "r")]))
    proj_ctx = defaultdict(list)
    for t in turns:
        proj_ctx[t["project"]].append(t["ctx"])
    for proj, s in rows:  # keep same order as A
        vals = sorted(proj_ctx[proj])
        if not vals:
            continue
        med = statistics.median(vals)
        p90 = pctl(vals, 90)
        add(fmt_row([(proj, 22, "l"), (len(vals), 7, "r"), (f"{med:,.0f}", 10, "r"), (f"{p90:,.0f}", 10, "r")]))
    add("")

    # ---------- C ----------
    add("-- C. OPENING-LOAD CONTEXT SIZE PER PROJECT (main chain only, ctx=in+cc+cr) --")
    add(fmt_row([("project", 22, "l"), ("sessions", 9, "r"), (">=30 turns", 10, "r"),
                 ("turn1 median", 13, "r"), ("turn30 median", 14, "r")]))
    proj_sessions = defaultdict(lambda: defaultdict(list))
    for t in turns:
        if t["main_file"] and not t["sidechain"]:
            proj_sessions[t["project"]][t["session"]].append(t)
    for proj, s in rows:  # keep same order as A
        sessions = proj_sessions.get(proj, {})
        first_vals, t30_vals = [], []
        for sess, ts_list in sessions.items():
            ts_list.sort(key=lambda t: t["ts"])
            first_vals.append(ts_list[0]["ctx"])
            if len(ts_list) >= 30:
                t30_vals.append(ts_list[29]["ctx"])
        if not sessions:
            continue
        med_first = statistics.median(first_vals) if first_vals else 0
        med_30 = statistics.median(t30_vals) if t30_vals else 0
        add(fmt_row([(proj, 22, "l"), (len(sessions), 9, "r"), (len(t30_vals), 10, "r"),
                      (f"{med_first:,.0f}", 13, "r"),
                      (f"{med_30:,.0f}" if t30_vals else "-", 14, "r")]))
    add("")

    # ---------- D ----------
    add("-- D. DAILY TOTALS, ALL PROJECTS (turns, cache_read, output in millions) --")
    day_stats = defaultdict(lambda: {"turns": 0, "cr": 0, "output": 0})
    for t in turns:
        day = t["ts"].date().isoformat()
        ds = day_stats[day]
        ds["turns"] += 1
        ds["cr"] += t["cr"]
        ds["output"] += t["output"]
    days_sorted = sorted(day_stats.items())
    heavy_order = sorted(day_stats.items(), key=lambda kv: -(kv[1]["cr"] + kv[1]["output"]))
    heavy_days = set(d for d, _ in heavy_order[:3])
    add(fmt_row([("date", 12, "l"), ("turns", 7, "r"), ("cache_rd_M", 11, "r"), ("output_M", 9, "r"), ("", 6, "l")]))
    for day, ds in days_sorted:
        flag = "HEAVY" if day in heavy_days else ""
        add(fmt_row([(day, 12, "l"), (ds["turns"], 7, "r"), (f"{ds['cr']/1e6:.2f}", 11, "r"),
                      (f"{ds['output']/1e6:.3f}", 9, "r"), (flag, 6, "l")]))
    add("")

    # ---------- E ----------
    add("-- E. TOP 8 SESSIONS BY SCORE = cache_read + 5*output --")
    sess_stats = defaultdict(lambda: {
        "project": None, "turns": 0, "cr": 0, "output": 0,
        "models": set(), "model_counts": defaultdict(int), "peak_ctx": 0, "min_ts": None, "max_ts": None,
    })
    for t in turns:
        s = sess_stats[t["session"]]
        s["project"] = t["project"]
        s["turns"] += 1
        s["cr"] += t["cr"]
        s["output"] += t["output"]
        s["models"].add(t["model"])
        s["model_counts"][(t["model"] or "?").replace("claude-", "")] += 1
        s["peak_ctx"] = max(s["peak_ctx"], t["ctx"])
        if s["min_ts"] is None or t["ts"] < s["min_ts"]:
            s["min_ts"] = t["ts"]
        if s["max_ts"] is None or t["ts"] > s["max_ts"]:
            s["max_ts"] = t["ts"]
    scored = []
    for sess, s in sess_stats.items():
        score = s["cr"] + 5 * s["output"]
        scored.append((score, sess, s))
    scored.sort(key=lambda x: -x[0])
    add(fmt_row([("project", 22, "l"), ("date", 11, "l"), ("turns", 6, "r"),
                 ("model", 14, "l"), ("peak_ctx", 10, "r"), ("score_M", 8, "r")]))
    for score, sess, s in scored[:8]:
        date = s["min_ts"].date().isoformat() if s["min_ts"] else "?"
        mc = s["model_counts"]
        dom = max(mc.items(), key=lambda kv: kv[1])[0] if mc else "?"
        extra = len(mc) - 1
        model_disp = dom if extra <= 0 else f"{dom}+{extra}"
        add(fmt_row([(s["project"], 22, "l"), (date, 11, "l"), (s["turns"], 6, "r"),
                      (model_disp, 14, "l"), (f"{s['peak_ctx']:,}", 10, "r"), (f"{score/1e6:.2f}", 8, "r")]))
    add("")

    # ---------- F ----------
    add("-- F. PER MODEL BUCKET --")
    model_stats = defaultdict(lambda: {"turns": 0, "output": 0})
    for t in turns:
        b = model_bucket(t["model"])
        ms = model_stats[b]
        ms["turns"] += 1
        ms["output"] += t["output"]
    add(fmt_row([("model", 20, "l"), ("turns", 10, "r"), ("output_tokens", 16, "r")]))
    for b in ["fable", "opus", "sonnet", "haiku", "other"]:
        ms = model_stats.get(b, {"turns": 0, "output": 0})
        add(fmt_row([(b, 20, "l"), (f"{ms['turns']:,}", 10, "r"), (f"{ms['output']:,}", 16, "r")]))
    add("")

    # ---------- meta ----------
    add("-- PARSE META --")
    add(f"jsonl files parsed: {files_parsed}")
    add(f"lines read total: {total_lines:,}")
    add(f"lines skipped (no usage/not-assistant/parse error): {skipped_lines:,}")
    add(f"lines outside the window (had usage, out of range): {out_of_window_lines:,}")
    add(f"duplicate content-block lines collapsed into their turn: {duplicate_blocks:,}")
    add(f"unique assistant turns counted in tables: {len(turns):,}")
    if global_min_ts and global_max_ts:
        add(f"date range of ALL usage lines found on disk: {global_min_ts.date()} to {global_max_ts.date()}")
    if turns:
        add(f"date range covered by tables (windowed): {turns[0]['ts'].date()} to {turns[-1]['ts'].date()}")
    add(f"window applied: {window_label(since_dt, until_dt)}")
    if args.projects:
        add(f"project filter applied: {args.projects!r}")

    if args.extended:
        add("")
        # ---------- G ----------
        add("-- G. PER MODEL BUCKET, tokens in millions --")
        add(fmt_row([("model", 18, "l"), ("turns", 8, "r"), ("input_M", 9, "r"),
                     ("cachecr_M", 10, "r"), ("cacherd_M", 10, "r"), ("out_M", 8, "r")]))
        bucket_stats = defaultdict(lambda: {"turns": 0, "input": 0, "cc": 0, "cr": 0, "output": 0})
        for t in turns:
            b = bucket_stats[model_bucket(t["model"])]
            b["turns"] += 1
            b["input"] += t["input"]
            b["cc"] += t["cc"]
            b["cr"] += t["cr"]
            b["output"] += t["output"]
        for name in ["fable", "opus", "sonnet", "haiku", "other"]:
            b = bucket_stats.get(name, {"turns": 0, "input": 0, "cc": 0, "cr": 0, "output": 0})
            add(fmt_row([(name, 18, "l"), (f"{b['turns']:,}", 8, "r"),
                          (f"{b['input']/1e6:.2f}", 9, "r"), (f"{b['cc']/1e6:.2f}", 10, "r"),
                          (f"{b['cr']/1e6:.2f}", 10, "r"), (f"{b['output']/1e6:.2f}", 8, "r")]))
        add("")

        # ---------- H ----------
        add("-- H. PER PROJECT: MAIN CHAIN vs SIDECHAIN, tokens in millions --")
        add(fmt_row([("project", 22, "l"), ("chain", 6, "l"), ("turns", 7, "r"), ("dom.model", 14, "l"),
                     ("input_M", 8, "r"), ("cachecr_M", 10, "r"), ("cacherd_M", 10, "r"), ("out_M", 7, "r")]))
        project_labels = [proj for proj, _ in rows]
        for proj in project_labels:
            for chain_name, want_side in [("main", False), ("side", True)]:
                subset = [t for t in turns if t["project"] == proj and t["sidechain"] == want_side]
                if not subset:
                    continue
                input_ = sum(t["input"] for t in subset)
                cc = sum(t["cc"] for t in subset)
                cr = sum(t["cr"] for t in subset)
                output = sum(t["output"] for t in subset)
                dom = dominant_model(subset)
                add(fmt_row([(proj, 22, "l"), (chain_name, 6, "l"), (f"{len(subset):,}", 7, "r"),
                              (dom, 14, "l"), (f"{input_/1e6:.2f}", 8, "r"), (f"{cc/1e6:.2f}", 10, "r"),
                              (f"{cr/1e6:.2f}", 10, "r"), (f"{output/1e6:.2f}", 7, "r")]))
        add("")

        # ---------- H2 ----------
        main_turns = [t for t in turns if t["main_file"] and not t["sidechain"]]
        over_200k = sum(1 for t in main_turns if t["ctx"] > 200_000)
        over_500k = sum(1 for t in main_turns if t["ctx"] > 500_000)
        add("-- H2. MAIN-CHAIN TURNS ABOVE EFFECTIVE-CONTEXT THRESHOLDS (all selected projects) --")
        add(fmt_row([("threshold", 12, "l"), ("turns", 7, "r"), ("of", 4, "l"), ("total_main", 10, "r")]))
        add(fmt_row([("> 200K", 12, "l"), (f"{over_200k:,}", 7, "r"), ("of", 4, "l"), (f"{len(main_turns):,}", 10, "r")]))
        add(fmt_row([("> 500K", 12, "l"), (f"{over_500k:,}", 7, "r"), ("of", 4, "l"), (f"{len(main_turns):,}", 10, "r")]))

    print("\n".join(out))
    sys.stderr.write(f"\n[stats] total output lines: {len(out)}\n")


if __name__ == "__main__":
    main()
