#!/usr/bin/env python3
# read_audit.py
# <!-- file-class: DOCTRINE -->
"""Which sources get read in full vs with a limit, and payload sizes, per project.

Read-only over ``~/.claude/projects/<project-dir>/**/*.jsonl``. This one
script in the set does look at message text, but only ever to measure its
length or to check for the presence of one fixed marker - the actual text is
never printed, stored, or returned by any function here:

- A ``tool_result``'s content length (character count), attributed back to
  the ``Read``/``Bash``/other tool call it answers, to see which sources
  produce the biggest payloads.
- Whether a ``Bash`` command's ``command`` string contains a limiting flag
  (``head``, ``sed -n``, ``tail``, ``awk``, ``grep``) or one of the register
  filenames in --markers, purely to group bash reads by what they were
  reading.
- The character length of each ``SendMessage`` payload sent, and of each
  incoming cross-session message (detected by the literal marker
  ``<cross-session-message`` in a user record's text) received.

The window defaults to the last 21 days; pass --since/--until for any other
range, and --projects to limit to project directories whose raw name
contains a given substring.
"""
import argparse
import collections
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

# Bash commands mentioning one of these substrings are grouped under
# "bash:<marker>" instead of "bash:other" - a generic starter set of common
# operational register filenames. Override with --markers if your own setup
# uses different register names.
DEFAULT_MARKERS = ["HANDOFF", "DECISIONS.md", "TASKS.md", "SPEND.md", "SESSION_LOG", "VENTURES.md"]

LIMIT_WORDS = ("head", "sed -n", "tail", "awk", "grep")
CROSS_SESSION_MARKER = "<cross-session-message"
TOP_N_SOURCES = 14


def extract_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(b.get("text", "") for b in content if isinstance(b, dict))
    return ""


def audit_project(proj_path, since_dt, until_dt, markers):
    files = sorted(set(
        glob.glob(os.path.join(proj_path, "*.jsonl"))
        + glob.glob(os.path.join(proj_path, "**", "*.jsonl"), recursive=True)
    ))
    reads = collections.defaultdict(lambda: [0, 0, 0, 0])  # source -> [n, n_with_limit, total_chars, max_chars]
    pending = {}
    msgs_out = []
    msgs_in = []
    agents = 0
    workflows = 0
    sessions = set()
    turns = 0
    tool_total = 0

    for fpath in files:
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
                if ts is None or ts < since_dt or ts >= until_dt:
                    continue
                message = d.get("message") or {}
                content = message.get("content")
                if not isinstance(content, list):
                    continue

                if d.get("type") == "assistant":
                    sessions.add(d.get("sessionId"))
                    turns += 1
                    for block in content:
                        if block.get("type") != "tool_use":
                            continue
                        name = block.get("name")
                        tool_input = block.get("input") or {}
                        block_id = block.get("id")
                        if name == "Read":
                            source = "read:" + os.path.basename(tool_input.get("file_path", ""))
                            has_limit = ("limit" in tool_input or "offset" in tool_input)
                            pending[block_id] = (source, has_limit)
                        elif name == "Bash":
                            cmd = tool_input.get("command", "")
                            for marker in markers:
                                if marker in cmd:
                                    pending[block_id] = (
                                        "bash:" + marker,
                                        any(w in cmd for w in LIMIT_WORDS),
                                    )
                                    break
                            else:
                                pending[block_id] = ("bash:other", True)
                        elif name == "SendMessage":
                            msgs_out.append(len(tool_input.get("message", "")))
                        elif name == "Agent":
                            agents += 1
                            pending[block_id] = ("agent-return", True)
                        elif name == "Workflow":
                            workflows += 1
                        else:
                            pending[block_id] = ("tool:" + str(name), True)
                elif d.get("type") == "user":
                    for block in content:
                        if block.get("type") == "text" and CROSS_SESSION_MARKER in block.get("text", ""):
                            msgs_in.append(len(block["text"]))
                        if block.get("type") == "tool_result" and block.get("tool_use_id") in pending:
                            source, has_limit = pending.pop(block["tool_use_id"])
                            size = len(extract_text(block.get("content")))
                            r = reads[source]
                            r[0] += 1
                            r[1] += has_limit
                            r[2] += size
                            r[3] = max(r[3], size)
                            tool_total += size

    return {
        "files": files,
        "reads": reads,
        "msgs_out": msgs_out,
        "msgs_in": msgs_in,
        "agents": agents,
        "workflows": workflows,
        "sessions": sessions,
        "turns": turns,
        "tool_total": tool_total,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    add_common_args(parser)
    parser.add_argument("--projects-dir", default=None, help=argparse.SUPPRESS)
    parser.add_argument(
        "--markers", default=None, metavar="A,B,C",
        help="comma-separated substrings that group a Bash read under 'bash:<marker>' "
        "instead of 'bash:other' (default: {})".format(",".join(DEFAULT_MARKERS)),
    )
    args = parser.parse_args()

    projects_dir = args.projects_dir or DEFAULT_PROJECTS_DIR
    since_dt, until_dt = resolve_window(args)
    markers = [m.strip() for m in args.markers.split(",")] if args.markers else DEFAULT_MARKERS

    print(f"read_audit.py - window {window_label(since_dt, until_dt)}"
          + (f", project filter {args.projects!r}" if args.projects else ""))
    print()

    for dirname in list_project_dirs(projects_dir, args.projects):
        label = label_for_project_dir(dirname)
        proj_path = os.path.join(projects_dir, dirname)
        result = audit_project(proj_path, since_dt, until_dt, markers)
        if result["turns"] == 0 and not result["reads"]:
            continue

        print(
            f'\n##### {label}: {len(result["files"])} files, {len(result["sessions"])} sessions, '
            f'{result["turns"]} asst turns in window; tool-result chars total '
            f'{result["tool_total"]/1e6:.1f}M; Agent spawns {result["agents"]}; '
            f'Workflow runs {result["workflows"]}'
        )
        top = sorted(result["reads"].items(), key=lambda kv: -kv[1][2])[:TOP_N_SOURCES]
        print(f'{"source":42s} {"n":>4s} {"w/lim":>5s} {"totalMB":>8s} {"maxKB":>6s}')
        for source, (n, n_limited, total, mx) in top:
            print(f'{source[:42]:42s} {n:4d} {n_limited:5d} {total/1e6:8.2f} {mx/1e3:6.0f}')

        if result["msgs_out"]:
            vals = result["msgs_out"]
            svals = sorted(vals)
            p90 = svals[int(len(svals) * 0.9)]
            print(f'SendMessage OUT: n={len(vals)} median={statistics.median(vals):.0f} '
                  f'p90={p90:.0f} max={max(vals)} total={sum(vals)/1e3:.0f}K chars')
        if result["msgs_in"]:
            vals = result["msgs_in"]
            print(f'cross-session IN: n={len(vals)} median={statistics.median(vals):.0f} '
                  f'max={max(vals)} total={sum(vals)/1e3:.0f}K chars')


if __name__ == "__main__":
    main()
