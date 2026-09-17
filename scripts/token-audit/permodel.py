#!/usr/bin/env python3
# permodel.py
# <!-- file-class: DOCTRINE -->
"""Priced token totals by model family and chain (main vs subagent).

Read-only over ``~/.claude/projects/<project-dir>/**/*.jsonl``. Reads usage
and structural metadata only - never message text: the fields this script
looks at are ``type``, ``timestamp``, ``sessionId``, ``isSidechain``, and
``message.id`` / ``message.model`` / ``message.usage``.

Every assistant turn in the window is sorted into a model family (see
prices.py) and a chain - "sub" if the record's own isSidechain flag is set or
its transcript file's path contains "/subagents/" (the on-disk layout Claude
Code subagent runs use), "main" otherwise - then priced against the table in
prices.py (or your own override file, via --prices). The window defaults to
the last 21 days; pass --since/--until for any other range, and --projects to
limit to project directories whose raw name contains a given substring.

The printed total is an API-EQUIVALENT dollar figure: what the same token
counts would cost at list rates if billed per token, priced consistently so
that two runs of this script compare on one scale. It is not a claim about
what you were actually billed - see README.md.
"""
import argparse
import collections
import glob
import json
import os

from _common import (
    DEFAULT_PROJECTS_DIR,
    add_common_args,
    list_project_dirs,
    parse_ts,
    resolve_window,
    window_label,
)
from prices import load_price_table, model_bucket, price_turn


def iter_jsonl_files(projects_dir, projects_filter):
    for dirname in list_project_dirs(projects_dir, projects_filter):
        proj_path = os.path.join(projects_dir, dirname)
        for fpath in glob.glob(os.path.join(proj_path, "**", "*.jsonl"), recursive=True):
            yield fpath


def build_aggregates(projects_dir, since_dt, until_dt, projects_filter):
    # (bucket, chain) -> [turns, input, cache_creation, cache_read, output]
    agg = collections.defaultdict(lambda: [0, 0, 0, 0, 0])
    seen = set()
    for fpath in iter_jsonl_files(projects_dir, projects_filter):
        try:
            fh = open(fpath, "r", errors="replace")
        except Exception:
            continue
        with fh:
            for line in fh:
                if '"usage"' not in line:
                    continue
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                if d.get("type") != "assistant":
                    continue
                message = d.get("message") or {}
                usage = message.get("usage")
                ts = parse_ts(d.get("timestamp"))
                if ts is None or not usage:
                    continue
                if ts < since_dt or ts >= until_dt:
                    continue
                key = (d.get("sessionId"), message.get("id"))
                if key in seen:
                    continue
                seen.add(key)
                chain = "sub" if (d.get("isSidechain") or "/subagents/" in fpath) else "main"
                a = agg[(model_bucket(message.get("model")), chain)]
                a[0] += 1
                a[1] += usage.get("input_tokens", 0) or 0
                a[2] += usage.get("cache_creation_input_tokens", 0) or 0
                a[3] += usage.get("cache_read_input_tokens", 0) or 0
                a[4] += usage.get("output_tokens", 0) or 0
    return agg


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    add_common_args(parser)
    parser.add_argument("--projects-dir", default=None, help=argparse.SUPPRESS)
    parser.add_argument(
        "--prices", default=None, metavar="PATH",
        help="JSON file overriding prices.py's default price table; "
        "see README.md for the file shape",
    )
    args = parser.parse_args()

    projects_dir = args.projects_dir or DEFAULT_PROJECTS_DIR
    since_dt, until_dt = resolve_window(args)
    table, other = load_price_table(args.prices)

    agg = build_aggregates(projects_dir, since_dt, until_dt, args.projects)

    print(f'{"model":7s} {"chain":5s} {"turns":>7s} {"in_M":>6s} {"ccreate_M":>10s} '
          f'{"cread_M":>9s} {"out_M":>7s} | {"$in":>5s} {"$write":>8s} {"$read":>7s} {"$out":>7s} {"$total":>7s}')

    T = collections.Counter()
    unpriced = set()
    for (bucket, chain), (n, i, cc, cr, o) in sorted(
        agg.items(), key=lambda kv: -(kv[1][2] * 2 + kv[1][3] * 0.1)
    ):
        d_in, d_cc, d_cr, d_out, known = price_turn(bucket, i, cc, cr, o, table, other)
        if not known:
            unpriced.add(bucket)
        tot = d_in + d_cc + d_cr + d_out
        T["in"] += d_in
        T["cc"] += d_cc
        T["cr"] += d_cr
        T["out"] += d_out
        T["tot"] += tot
        T["turns"] += n
        print(f'{bucket:7s} {chain:5s} {n:7d} {i/1e6:6.2f} {cc/1e6:10.1f} {cr/1e6:9.0f} {o/1e6:7.2f} '
              f'| {d_in:5.0f} {d_cc:8.0f} {d_cr:7.0f} {d_out:7.0f} {tot:7.0f}')

    days = max((until_dt - since_dt).days, 1)
    label = window_label(since_dt, until_dt)
    print(f'TOTAL {label} API-equivalent ({T["turns"]:,} turns): in ${T["in"]:.0f}  '
          f'cache-write ${T["cc"]:.0f}  cache-read ${T["cr"]:.0f}  output ${T["out"]:.0f}  '
          f'= ${T["tot"]:.0f}  (~${T["tot"]/days:.0f}/day)')
    if unpriced:
        print(f'WARNING: unpriced model bucket(s), priced at the "other" fallback: {", ".join(sorted(unpriced))}')
    if args.projects:
        print(f'project filter applied: {args.projects!r}')


if __name__ == "__main__":
    main()
