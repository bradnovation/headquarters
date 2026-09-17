#!/usr/bin/env python3
# _common.py
# <!-- file-class: DOCTRINE -->
"""Shared, read-only helpers for the token-audit scripts.

Every script in this directory reads the same on-disk shape - Claude Code
transcript files under ``~/.claude/projects/<project-dir>/**/*.jsonl`` - and
needs the same three things done the same way: turn a ``--since``/``--until``
pair into a UTC time window, list the project directories that fall inside an
optional ``--projects`` substring filter, and turn one project directory's
raw name into a short label for print output. This module is that shared
code, so the four scripts agree with each other on what a "project" and a
"window" mean instead of each reimplementing it slightly differently.

Nothing here reads message text. The functions below only ever look at a
record's ``type``, ``timestamp``, ``sessionId``, ``isSidechain``, and
``message.id`` / ``message.model`` / ``message.usage`` fields - never
``message.content``.
"""

import argparse
import os
from datetime import datetime, timedelta, timezone

HOME = os.path.expanduser("~")
DEFAULT_PROJECTS_DIR = os.path.join(HOME, ".claude", "projects")
DEFAULT_WINDOW_DAYS = 21


def parse_ts(ts):
    """Parse a transcript record's ISO-8601 timestamp into an aware UTC datetime."""
    if not ts:
        return None
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except Exception:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _parse_date_arg(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "expected a date as YYYY-MM-DD, got {!r}".format(value)
        )


def add_common_args(parser):
    """Add --since, --until, and --projects to an argparse parser in place."""
    parser.add_argument(
        "--since",
        type=_parse_date_arg,
        default=None,
        metavar="YYYY-MM-DD",
        help="start of the window, inclusive (default: {} days before --until, "
        "or before today if --until is also omitted)".format(DEFAULT_WINDOW_DAYS),
    )
    parser.add_argument(
        "--until",
        type=_parse_date_arg,
        default=None,
        metavar="YYYY-MM-DD",
        help="end of the window, inclusive (default: today, in UTC)",
    )
    parser.add_argument(
        "--projects",
        default=None,
        metavar="SUBSTRING",
        help="only include project directories whose raw directory name "
        "(as it appears under ~/.claude/projects) contains this substring; "
        "comma-separate several substrings to match any of them. Default: "
        "all project directories.",
    )
    return parser


def resolve_window(args):
    """Turn parsed --since/--until into (since_dt, until_dt_exclusive).

    since_dt is midnight UTC on the --since date (inclusive). until_dt is
    midnight UTC the day AFTER the --until date, so a half-open comparison
    ``since_dt <= ts < until_dt`` covers the --until date through its last
    instant.

    --until alone defaults to today (UTC); --since alone defaults to
    (--until minus 21 days), i.e. "since X" without an end means "from X
    through today", not an arbitrary 21-day window starting at X.
    """
    if args.until is not None:
        until_date = args.until
    else:
        until_date = datetime.now(timezone.utc).replace(
            hour=0, minute=0, second=0, microsecond=0
        )

    if args.since is not None:
        since_date = args.since
    else:
        since_date = until_date - timedelta(days=DEFAULT_WINDOW_DAYS)

    since_dt = since_date.replace(hour=0, minute=0, second=0, microsecond=0)
    until_dt_exclusive = until_date.replace(
        hour=0, minute=0, second=0, microsecond=0
    ) + timedelta(days=1)
    return since_dt, until_dt_exclusive


def window_label(since_dt, until_dt_exclusive):
    last_included = until_dt_exclusive - timedelta(days=1)
    return "{} to {}".format(since_dt.date(), last_included.date())


def list_project_dirs(projects_dir=DEFAULT_PROJECTS_DIR, projects_filter=None):
    """Return sorted raw directory names under projects_dir, filtered by substring.

    projects_filter, if given, is a comma-separated list of substrings; a
    directory is kept if its raw name contains ANY of them. Matching is
    against the directory name exactly as it appears on disk - never against
    a derived label - per the tool's --projects contract.
    """
    if not os.path.isdir(projects_dir):
        return []
    names = sorted(
        d for d in os.listdir(projects_dir)
        if os.path.isdir(os.path.join(projects_dir, d))
    )
    if not projects_filter:
        return names
    needles = [n.strip() for n in projects_filter.split(",") if n.strip()]
    if not needles:
        return names
    return [d for d in names if any(n in d for n in needles)]


def label_for_project_dir(dirname, home=HOME):
    """Shorten a raw ~/.claude/projects directory name into a print label.

    The raw name is the project's absolute path with "/" turned into "-"
    (Claude Code's own encoding). This strips the encoded home-directory
    prefix and, if present, one leading path segment literally named
    "Claude" or "claude" (a common one-level parent folder for grouped
    projects) so the label reads as a short project name instead of a full
    encoded path. If neither strip applies, the raw directory name is
    returned unchanged - the label is cosmetic, never required for
    filtering or joins.
    """
    prefix = "-" + home.strip("/").replace("/", "-") + "-"
    name = dirname
    if name.startswith(prefix):
        name = name[len(prefix):]
    else:
        name = name.lstrip("-")
    for p in ("Claude-", "claude-"):
        if name.startswith(p):
            name = name[len(p):]
            break
    return name or dirname


def fmt_row(cells):
    """cells: list of (text, width, align) with align 'l' or 'r'; space-joined."""
    parts = []
    for text, width, align in cells:
        text = str(text)
        parts.append(text.rjust(width) if align == "r" else text.ljust(width))
    return " ".join(parts)


def pctl(sorted_vals, p):
    """p in [0,100]; sorted_vals must already be sorted ascending and non-empty."""
    n = len(sorted_vals)
    if n == 1:
        return sorted_vals[0]
    k = (p / 100) * (n - 1)
    f = int(k)
    c = min(f + 1, n - 1)
    if f == c:
        return sorted_vals[f]
    d = k - f
    return sorted_vals[f] + (sorted_vals[c] - sorted_vals[f]) * d
