# token-audit
<!-- file-class: DOCTRINE -->

*Four read-only scripts that measure token burn from your own local Claude
Code transcripts. They read `~/.claude/projects/<project-dir>/**/*.jsonl`,
never write anything, and never make a network call. Every number comes from
files already on your disk.*

---

## What each script measures

All four take `--since YYYY-MM-DD` and `--until YYYY-MM-DD` (default: the
last 21 days, ending today) and an optional `--projects SUBSTRING` that
limits which project directories get scanned - a substring match against the
raw directory name as it appears under `~/.claude/projects`, not against any
derived label. Run `<script>.py --help` for the exact default and every flag.

- **`token_audit.py`** - per-project and per-day totals, per-turn effective
  context size (median and p90), the top sessions by a cache-read-plus-output
  score, and a per-model-bucket breakdown. Pass `--extended` for three more
  sections: per-model totals again alongside turn counts, a main-chain vs
  subagent-chain split per project, and counts of main-chain turns above two
  effective-context thresholds.
- **`permodel.py`** - the same turns, sorted into a model family and a chain
  (main vs subagent), then priced against the table in `prices.py` (or your
  own override file - see below) to give one API-equivalent dollar total,
  broken into input, cache-write, cache-read, and output.
- **`rewarm.py`** - cache re-warm events: main-chain turns whose
  `cache_creation_input_tokens` exceeds 40,000 in one shot, meaning a cache
  that should have been warm got rebuilt from scratch. For each one it
  reports how long since the previous turn on that chain, and whether it
  followed an incoming cross-session message.
- **`read_audit.py`** - which tool calls produce the biggest transcript
  payloads: `Read` calls by the file basename read, `Bash` calls grouped by
  a configurable set of marker substrings (`--markers`), and every other
  tool call by name - each with a count, how many used a limiting flag, and
  total and max characters returned. Also reports `SendMessage` payload
  sizes and incoming cross-session message sizes.

None of the four read message text as content. `read_audit.py` is the one
exception worth naming precisely: it reads a `tool_result`'s text only to
take its length, and checks a fixed literal (`<cross-session-message`) as a
substring match on a user record's text to flag it as a cross-session
delivery. Neither operation prints, stores, or returns the text itself -
every field that reaches output is a count, a length, or a boolean.

## Taking a baseline and comparing after a change

1. Pick a window and run all four with the same `--since`/`--until` before
   you make the change you're trying to measure. Save the output - a
   redirected file is enough, there's nothing here that regenerates itself
   from a saved state.
2. Make the change.
3. Run all four again with an **equal-length** window that starts after the
   change (or the same historical window on a system that has since
   accumulated more data past it - what matters is comparing like-length
   periods, not raw dates).
4. Compare specific numbers, not just the totals:
   - `token_audit.py` section B's per-project median and p90 effective
     context - did the typical turn get lighter or heavier.
   - `rewarm.py`'s rewarm-turn count and the carried-token percentage per
     project - did the change reduce how often a cache gets rebuilt from
     scratch, or just move the rebuilds around.
   - `permodel.py`'s cache-write vs cache-read dollar split - a real fix to
     re-warm behavior should show up as cache-write dollars falling relative
     to cache-read dollars, not just the grand total moving (a total can
     fall because a project went quiet, which is not the same thing as the
     mechanism you changed actually working).
5. A number that didn't move when you changed something aimed at it is a
   result, not a failure of the script - report it as "no change measured",
   not silently drop the run. See `ops/MEASUREMENT_CRAFT.md` on why an
   unmoved number needs the same scrutiny as one that moved the way you
   expected.

A baseline and a comparison run pulled from a live, still-being-written
transcript set will differ by a small amount even with nothing else
changed, because new turns keep landing on disk between the two runs. That
drift is expected and is not the same thing as the change you're measuring;
if it matters, run both passes back to back and treat anything within that
drift's rough size as noise.

## What the numbers mean

- **Effective context** (`token_audit.py` sections B and C, and the H2
  thresholds) is `input_tokens + cache_creation_input_tokens +
  cache_read_input_tokens` for one assistant turn - everything that had to
  be in the model's context window to produce that turn, regardless of
  whether it came in fresh or from cache. Output tokens are excluded because
  they don't weigh down the *next* turn's input the way everything else on
  this list does.
- **p50 / median and p90** describe the distribution of that per-turn
  context size across all turns in the window, not a single average. p50 is
  the typical turn; p90 is what the heaviest 10% of turns look like. A
  median that looks fine while p90 is very high usually means a small
  number of turns are dragging a huge amount of context along, which a
  single average would hide.
- **Cache write** (`cache_creation_input_tokens`) is a fresh write into the
  prompt cache - normally priced above the base input rate (`prices.py`
  defaults to 2x, a common list rate for a 1-hour TTL) because the provider
  also has to serve it back out again later. A high cache-write count
  relative to cache-read means the cache keeps getting rebuilt instead of
  reused.
- **Cache read** (`cache_read_input_tokens`) is a cache hit - context served
  from what was already warm. It's priced well under the base input rate
  (`prices.py` defaults to 0.1x, or 0.025x for one fast model family) because
  serving a hit is cheap. A high cache-read share relative to cache-write is
  the healthy shape: pay once to warm it, then read it cheaply many times.
- **Re-warm event** (`rewarm.py`) is one turn crossing the 40,000-token
  cache-write threshold. A cluster of these with a long idle gap beforehand
  usually means the provider's cache TTL simply expired between turns; a
  cluster right after an incoming cross-session message usually means the
  message itself forced a rebuild mid-conversation. The script reports both
  so you can tell which is driving a given project's re-warm rate.
- **API-equivalent dollars** (`permodel.py`) are what the counted tokens
  would cost at the list rates in `prices.py`, priced consistently so two
  runs compare on one scale. This is not a bill and is never checked against
  one - a subscription plan's own metering rarely charges strictly per
  token the way a list-rate table does. Read the ratio between two runs, or
  between cache-write and cache-read within one run; don't read the total in
  isolation as an amount you were actually charged.

## Price table and overrides

`prices.py` holds `model_bucket()` (which sorts a model name into a family
by substring match) and the default price table (`DEFAULT_PRICE_TABLE` and
the `OTHER_PRICE` fallback for anything `model_bucket()` doesn't recognize).
Only `permodel.py` uses pricing.

To use your own rates instead of editing `prices.py`, pass `permodel.py
--prices path/to/your-rates.json`. The file is a JSON object keyed by family
name, each value a dict overriding any subset of `input`, `output`,
`cache_write_multiplier`, and `cache_read_multiplier` (US dollars per
million tokens for the first two; multipliers on the input rate for the
other two). A family you don't mention keeps its default; the key `"other"`
overrides the fallback the same way. For example, to reprice just `opus`
and leave everything else at the default:

```json
{
  "opus": { "input": 15.0, "output": 75.0 }
}
```

## Known limits

- `permodel.py` divides its per-day figure by the real length of the `--since/--until` window, not a fixed 21 days, so that one number will not match an older fixed-window run even when every total does.
- `prices.py` buckets any model whose id contains `fable` into the top tier (the original per-model script matched `fable-5-1` exactly); widen or narrow the substring in `model_bucket()` if a future top-tier model should price differently.

- **Live drift.** A baseline and a comparison run against a still-being-
  written transcript set will never match to the exact token if anything
  else was actively running on the same machine between the two runs. See
  above.
- **`--since`/`--until` are dates, not instants.** The window is
  day-granular in UTC: `--since 2026-08-26` includes the entire UTC day of
  2026-08-26, from midnight. A tool that needs sub-day precision isn't this
  one.
- **`read_audit.py`'s marker list is a starting point, not a discovery
  mechanism.** `--markers` groups a `Bash` command under a label only when
  the command string contains one of the substrings you gave it (default:
  `HANDOFF,DECISIONS.md,TASKS.md,SPEND.md,SESSION_LOG,VENTURES.md`);
  anything else, including a marker you use in your own setup that isn't in
  that list, falls into `bash:other` until you add it with `--markers`.
- **`model_bucket()`'s family list is fixed at four names plus `other`.** A
  model your transcripts call something `model_bucket()` doesn't match
  (see `prices.py`) is priced at the `other` fallback and printed as a
  warning by `permodel.py`; it is never silently mispriced as a family it
  isn't.
