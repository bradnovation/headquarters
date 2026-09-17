#!/usr/bin/env python3
# prices.py
# <!-- file-class: DOCTRINE -->
"""Model-family bucketing and the price table used by permodel.py.

A "family" is a short string a model name is sorted into by substring match
(see model_bucket() below), so that turns from every dated build of, say,
Sonnet land in one "sonnet" row instead of one row per build string. Every
family in MODEL_FAMILIES needs an entry in the price table below or it prices
at the OTHER_PRICE fallback and gets flagged as unpriced in permodel.py's
output.

The default table holds list rates, in US dollars per million tokens, split
into:

- input: price per million ordinary input tokens.
- output: price per million output tokens.
- cache_write_multiplier: cache-creation (a fresh 1-hour-TTL cache write)
  tokens are priced at input-rate times this multiplier. Most providers price
  a cache write above the base input rate because it also has to be read
  back; 2x is the common list rate for a 1-hour TTL.
- cache_read_multiplier: cache-read (a cache hit) tokens are priced at
  input-rate times this multiplier, and is normally well under 1 since a
  cache hit is cheap to serve.

These are constants you maintain, not a live price feed: nothing here is
fetched from a network. Use --prices on permodel.py to point at your own
JSON file instead of editing this one - see README.md for the file shape.
"""

import json

MODEL_FAMILIES = ("fable", "opus", "sonnet", "haiku")

DEFAULT_PRICE_TABLE = {
    "fable": {
        "input": 10.0,
        "output": 50.0,
        "cache_write_multiplier": 2.0,
        "cache_read_multiplier": 0.025,
    },
    "opus": {
        "input": 5.0,
        "output": 25.0,
        "cache_write_multiplier": 2.0,
        "cache_read_multiplier": 0.1,
    },
    "sonnet": {
        "input": 2.0,
        "output": 10.0,
        "cache_write_multiplier": 2.0,
        "cache_read_multiplier": 0.1,
    },
    "haiku": {
        "input": 1.0,
        "output": 5.0,
        "cache_write_multiplier": 2.0,
        "cache_read_multiplier": 0.1,
    },
}

# Any model name that matches none of MODEL_FAMILIES buckets into "other" and
# prices here. The default guesses the most expensive known family's input
# and output rate (a conservative, over- rather than under-count default) but
# the standard 0.1x cache-read multiplier rather than a specific family's.
OTHER_PRICE = {
    "input": 10.0,
    "output": 50.0,
    "cache_write_multiplier": 2.0,
    "cache_read_multiplier": 0.1,
}


# Note: buckets on the bare substring "fable" (the original token_audit.py matched "fable-5-1");
# a superset today, deliberately widened so a newer top-tier id still prices at the top tier.
def model_bucket(model_name):
    """Sort a model name into one of MODEL_FAMILIES, or "other"."""
    m = (model_name or "").lower()
    for family in MODEL_FAMILIES:
        if family in m:
            return family
    return "other"


def load_price_table(path=None):
    """Return (table, other_price) with any overrides from a JSON file applied.

    The JSON file, if given, is a dict of {family: {field: value, ...}, ...}.
    A family present in the file replaces its fields over the default for
    that family (missing fields keep the default); a family not mentioned in
    the file is untouched. The key "other" overrides OTHER_PRICE the same
    way. Unknown families in the file are accepted as-is (a new family your
    own transcripts use that isn't one of MODEL_FAMILIES still needs
    model_bucket() taught to recognize it to ever be selected, but you can
    price it here ahead of that).
    """
    table = {family: dict(fields) for family, fields in DEFAULT_PRICE_TABLE.items()}
    other = dict(OTHER_PRICE)
    if not path:
        return table, other

    with open(path, "r") as fh:
        overrides = json.load(fh)
    if not isinstance(overrides, dict):
        raise ValueError("price override file must contain a JSON object")

    other_override = overrides.pop("other", None)
    if other_override:
        other.update(other_override)
    for family, fields in overrides.items():
        table.setdefault(family, dict(OTHER_PRICE))
        table[family].update(fields)
    return table, other


def price_turn(bucket, input_tokens, cache_creation_tokens, cache_read_tokens,
                output_tokens, table, other):
    """Price one turn's four token counts against a price table.

    Returns (input_$, cache_write_$, cache_read_$, output_$, known) where
    known is False if bucket fell back to `other`.
    """
    rates = table.get(bucket)
    known = rates is not None
    if rates is None:
        rates = other
    pin = rates["input"]
    pout = rates["output"]
    wmul = rates["cache_write_multiplier"]
    rmul = rates["cache_read_multiplier"]
    d_in = input_tokens / 1e6 * pin
    d_cc = cache_creation_tokens / 1e6 * pin * wmul
    d_cr = cache_read_tokens / 1e6 * pin * rmul
    d_out = output_tokens / 1e6 * pout
    return d_in, d_cc, d_cr, d_out, known
