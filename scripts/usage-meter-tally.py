#!/usr/bin/env python3
# usage-meter-tally.py
# <!-- file-class: DOCTRINE -->
"""Read-only tally of recorded API usage, by week, model family, and lane.

This script never writes anything and never calls out to a network. It reads
the local Claude Code transcript files under ~/.claude/projects/**/*.jsonl
(the journal file, journal.jsonl, is skipped: it is an index, not a record of
API responses) and sums the token usage each "assistant" record carries.

Each assistant record is expected to carry message.model (a string) and
message.usage (a dict with input_tokens, cache_creation_input_tokens,
cache_read_input_tokens, and output_tokens), plus a timestamp field. Records
are de-duplicated by message.id: a session can persist the same message more
than once as it streams or resumes, and the safe rule is to keep whichever
copy of a given id carries the largest output_tokens, on the reasoning that a
partial write undercounts and a complete write never shrinks a prior one.

Usage is grouped into week windows on a configurable boundary (see the
constants below), then broken out two ways inside each week: by model family
(the model name with its date suffix stripped) and by lane. Lane is decided
purely from the path a transcript file lives at: a file whose path contains
"/subagents/" is counted as the subagents lane; everything else is counted as
the main keyboard lane. That split exists because the two lanes tend to carry
very different token shapes, and folding them into one number hides which
one actually moved.

Every period is also priced against the list-price table below, so that two
weeks compare on one scale even when the mix of models or the mix of lanes
between them changed. The price table is a set of constants you maintain
yourself; it is never fetched or inferred from anything in this repository.

Read the ratios, not the absolute total. A subscription plan's own metering
almost never charges strictly per token the way this script's price table
does; the provider's own weighting of a plan-included run belongs to the
provider, and this script does not attempt to reproduce it. What this script
is good for is comparing periods, models, and lanes against each other on a
single, consistent yardstick, so a change in the ratio between two weeks (or
between the main lane and the subagents lane) is visible even when the
provider's own dashboard reports a single blended number.
"""

import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover - stdlib fallback for very old builds
    ZoneInfo = None

# --------------------------------------------------------------------------
# CONSTANTS - edit these to match your own setup. Nothing here is read from
# the environment or from any other file in this repository.
# --------------------------------------------------------------------------

# Where to look for transcripts. This is the standard location; change it if
# your own install keeps transcripts somewhere else.
TRANSCRIPTS_ROOT = Path.home() / ".claude" / "projects"

# The journal file is an index of sessions, not a record of API responses,
# and is always skipped regardless of this constant.
JOURNAL_FILENAME = "journal.jsonl"

# Local timezone used to decide which week window a record falls into, and
# to print week labels a person can read without converting from UTC. Change
# the key to your own IANA zone name.
LOCAL_TIMEZONE_NAME = "America/New_York"

# A week starts on this weekday (0 = Monday .. 6 = Sunday) at this local
# hour. The default (Monday, 00:00) is an ordinary calendar week; change
# both if your own billing or reporting cadence starts elsewhere.
WEEK_BOUNDARY_WEEKDAY = 0
WEEK_BOUNDARY_HOUR = 0

# Above this many input tokens (including cache-read and cache-creation
# tokens) in a single record, some providers charge a higher long-context
# rate. Set to None to disable the long-context tier entirely and always
# price at the base rate.
LONG_CONTEXT_THRESHOLD_TOKENS = 200_000

# List-price table, in currency units per token (not per million tokens), by
# model family. "family" is the model name with any trailing date or build
# suffix stripped (see model_family() below). Fill in your own provider's
# published list price for each family you actually see in your transcripts;
# an unrecognized family is priced at UNKNOWN_FAMILY_PRICE and flagged in the
# printed table so it is never silently mispriced as something else.
#
# Each entry is a dict of per-token rates. The "long_" rates are used only
# when LONG_CONTEXT_THRESHOLD_TOKENS is set and a record's input tokens
# exceed it; omit them (or leave the threshold as None) if your provider
# does not price a long-context tier.
PRICE_TABLE = {
    "opus": {
        "input": 15.00 / 1_000_000,
        "cache_write": 18.75 / 1_000_000,
        "cache_read": 1.50 / 1_000_000,
        "output": 75.00 / 1_000_000,
    },
    "sonnet": {
        "input": 3.00 / 1_000_000,
        "cache_write": 3.75 / 1_000_000,
        "cache_read": 0.30 / 1_000_000,
        "output": 15.00 / 1_000_000,
        "long_input": 6.00 / 1_000_000,
        "long_cache_write": 7.50 / 1_000_000,
        "long_cache_read": 0.60 / 1_000_000,
        "long_output": 22.50 / 1_000_000,
    },
    "haiku": {
        "input": 0.80 / 1_000_000,
        "cache_write": 1.00 / 1_000_000,
        "cache_read": 0.08 / 1_000_000,
        "output": 4.00 / 1_000_000,
    },
}
UNKNOWN_FAMILY_PRICE = {
    "input": 0.0,
    "cache_write": 0.0,
    "cache_read": 0.0,
    "output": 0.0,
}

# --------------------------------------------------------------------------
# End of constants.
# --------------------------------------------------------------------------


def local_tz():
    if ZoneInfo is not None:
        try:
            return ZoneInfo(LOCAL_TIMEZONE_NAME)
        except Exception:
            pass
    return timezone.utc


def model_family(model_name):
    """Strip a trailing date or build suffix off a model name.

    "claude-sonnet-5-20260101" and "claude-sonnet-4-5" both fold to
    "sonnet"; anything that matches none of the known family words is
    returned lowercased and unchanged, so it still groups consistently and
    still shows up (priced at UNKNOWN_FAMILY_PRICE) rather than vanishing.
    """
    name = (model_name or "unknown").lower()
    for family in ("opus", "sonnet", "haiku"):
        if family in name:
            return family
    return name


def lane_for_path(path):
    return "subagents" if "/subagents/" in str(path).replace("\\", "/") else "main"


def parse_timestamp(raw):
    """Parse an ISO-8601 timestamp string into an aware UTC datetime."""
    if not raw:
        return None
    text = raw.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def week_start(dt_utc, tz):
    """Return the local-time start of the week window a UTC instant falls in."""
    local_dt = dt_utc.astimezone(tz)
    days_since_boundary = (local_dt.weekday() - WEEK_BOUNDARY_WEEKDAY) % 7
    candidate = local_dt.replace(
        hour=WEEK_BOUNDARY_HOUR, minute=0, second=0, microsecond=0
    ) - timedelta(days=days_since_boundary)
    if candidate > local_dt:
        candidate -= timedelta(days=7)
    return candidate


def iter_transcript_files():
    if not TRANSCRIPTS_ROOT.exists():
        return
    for path in TRANSCRIPTS_ROOT.glob("**/*.jsonl"):
        if path.name == JOURNAL_FILENAME:
            continue
        yield path


def iter_assistant_records():
    """Yield (path, record_dict) for every assistant record found."""
    for path in iter_transcript_files():
        try:
            with path.open("r", encoding="utf-8", errors="replace") as handle:
                for line in handle:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(record, dict):
                        continue
                    if record.get("type") != "assistant":
                        continue
                    yield path, record
        except OSError:
            continue


def extract_usage_row(path, record):
    """Pull the fields this script cares about out of one assistant record."""
    message = record.get("message")
    if not isinstance(message, dict):
        return None
    usage = message.get("usage")
    if not isinstance(usage, dict):
        return None

    message_id = message.get("id") or record.get("uuid")
    if not message_id:
        return None

    timestamp = parse_timestamp(record.get("timestamp"))
    if timestamp is None:
        return None

    def as_int(value):
        try:
            return int(value)
        except (TypeError, ValueError):
            return 0

    return {
        "message_id": message_id,
        "model": message.get("model", "unknown"),
        "timestamp": timestamp,
        "lane": lane_for_path(path),
        "input_tokens": as_int(usage.get("input_tokens")),
        "cache_creation_input_tokens": as_int(usage.get("cache_creation_input_tokens")),
        "cache_read_input_tokens": as_int(usage.get("cache_read_input_tokens")),
        "output_tokens": as_int(usage.get("output_tokens")),
    }


def dedupe_by_message_id(rows):
    """Keep, per message_id, the row with the largest output_tokens."""
    best = {}
    for row in rows:
        existing = best.get(row["message_id"])
        if existing is None or row["output_tokens"] > existing["output_tokens"]:
            best[row["message_id"]] = row
    return list(best.values())


def price_row(row):
    family = model_family(row["model"])
    table = PRICE_TABLE.get(family, UNKNOWN_FAMILY_PRICE)

    total_input_context = (
        row["input_tokens"]
        + row["cache_creation_input_tokens"]
        + row["cache_read_input_tokens"]
    )
    use_long = (
        LONG_CONTEXT_THRESHOLD_TOKENS is not None
        and total_input_context > LONG_CONTEXT_THRESHOLD_TOKENS
    )

    def rate(base_key):
        long_key = "long_" + base_key
        if use_long and long_key in table:
            return table[long_key]
        return table.get(base_key, 0.0)

    cost = (
        row["input_tokens"] * rate("input")
        + row["cache_creation_input_tokens"] * rate("cache_write")
        + row["cache_read_input_tokens"] * rate("cache_read")
        + row["output_tokens"] * rate("output")
    )
    return cost, family in PRICE_TABLE


def format_week_label(start_dt):
    end_dt = start_dt + timedelta(days=7)
    return "{} .. {}".format(start_dt.strftime("%Y-%m-%d %H:%M %Z"), end_dt.strftime("%Y-%m-%d"))


def format_tokens(n):
    return "{:,}".format(n)


def format_cost(n):
    return "{:,.2f}".format(n)


def main():
    tz = local_tz()
    rows = []
    for path, record in iter_assistant_records():
        row = extract_usage_row(path, record)
        if row is not None:
            rows.append(row)

    rows = dedupe_by_message_id(rows)

    if not rows:
        print("No assistant usage records found under: {}".format(TRANSCRIPTS_ROOT))
        return 0

    # week_start -> family -> lane -> aggregate dict
    buckets = {}
    unknown_families = set()

    for row in rows:
        wk = week_start(row["timestamp"], tz)
        family = model_family(row["model"])
        lane = row["lane"]
        cost, known = price_row(row)
        if not known:
            unknown_families.add(family)

        week_bucket = buckets.setdefault(wk, {})
        cell = week_bucket.setdefault(family, {}).setdefault(
            lane,
            {
                "input_tokens": 0,
                "cache_creation_input_tokens": 0,
                "cache_read_input_tokens": 0,
                "output_tokens": 0,
                "cost": 0.0,
                "records": 0,
            },
        )
        cell["input_tokens"] += row["input_tokens"]
        cell["cache_creation_input_tokens"] += row["cache_creation_input_tokens"]
        cell["cache_read_input_tokens"] += row["cache_read_input_tokens"]
        cell["output_tokens"] += row["output_tokens"]
        cell["cost"] += cost
        cell["records"] += 1

    print("usage-meter-tally.py - read-only, {} assistant records after de-duplication".format(len(rows)))
    print("transcripts root: {}".format(TRANSCRIPTS_ROOT))
    print("week boundary: weekday {} (0=Mon), hour {}, timezone {}".format(
        WEEK_BOUNDARY_WEEKDAY, WEEK_BOUNDARY_HOUR, LOCAL_TIMEZONE_NAME
    ))
    if unknown_families:
        print("WARNING: unpriced model families seen (priced at 0): {}".format(
            ", ".join(sorted(unknown_families))
        ))
    print()

    header = "{:<28} {:<10} {:<10} {:>10} {:>10} {:>12} {:>10} {:>12}".format(
        "week", "family", "lane", "input", "output", "cache_read", "records", "list_cost"
    )
    print(header)
    print("-" * len(header))

    for wk in sorted(buckets.keys()):
        for family in sorted(buckets[wk].keys()):
            for lane in sorted(buckets[wk][family].keys()):
                cell = buckets[wk][family][lane]
                print("{:<28} {:<10} {:<10} {:>10} {:>10} {:>12} {:>10} {:>12}".format(
                    format_week_label(wk),
                    family,
                    lane,
                    format_tokens(cell["input_tokens"]),
                    format_tokens(cell["output_tokens"]),
                    format_tokens(cell["cache_read_input_tokens"]),
                    cell["records"],
                    format_cost(cell["cost"]),
                ))

    print()
    print("Read the ratios between periods and between lanes, not the absolute")
    print("total: a subscription plan's own metering weighs a run its own way,")
    print("and that weighting belongs to the provider, not to this table.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
