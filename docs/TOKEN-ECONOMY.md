# TOKEN ECONOMY - where the spend goes, and what actually moves it
<!-- file-class: DOCTRINE -->

*A multi-session staff - several seats, each holding state across many turns
over many days - spends differently than a single short chat does. This page
says where that spend concentrates and orders the levers that move it by
structural effect, largest first. It names no dollar figure and no
operator's own measurement: `scripts/token-audit/` and
`scripts/usage-meter-tally.py` exist so you re-derive your own numbers
against your own transcripts, and a lever's rank here holds regardless of
what any one operator's mix of seats and models happens to cost.*

---

## 1. Where the money goes

Three classes of token make up almost all of it: cache reads, cache writes,
and output. A cache read is cheap - a fraction of a fresh input token - and a
cache write is not: at the one-hour retention window a provider's own
pricing typically bills a cache write at twice a fresh input token's rate,
against a lower rate at a shorter window. Output tokens cost the most per
token of the three, and are usually the smallest share of the total, because
most of what a long-lived session spends on is re-reading context it
already had, not generating new text.

That arithmetic makes one pattern the most expensive thing a multi-session
staff can do to itself: a session carrying a large context sits idle past
the cache's retention window, then gets woken - by a status ask, a mesh
message, anything - and its entire accumulated context is rewritten into
cache at the write rate before a single new word comes back. The cost is not
what woke the session. It is how much context existed to be rewritten, and
how long the session had been sitting on it un-refreshed. A small session
woken cold is cheap. A session that has been left to grow for hours before
anyone checks on it is not, and the growing, not the checking, is the
mistake.

File sizes and message payloads are usually not where the money is. A
handoff or a decision ledger read by slice, the way this repository's own
read order reads them, costs a bounded, small amount per orientation no
matter how large the file has grown, and a short cross-session message costs
close to nothing next to the context it might wake. Measure before assuming
otherwise - `scripts/token-audit/` is what settles it for your own repo -
but do not spend a rewrite pass shrinking a file before you have checked
whether shrinking it would move anything.

---

## 2. The levers, in order of effect

**1. Context ceiling and park-before-idle.** The largest lever, and the one
every other item on this list is secondary to: keep a session from living
far above the context it actually needs for its current work, and park it
- committing state to disk in a form the next session can pick up cold -
before an idle stretch is expected to cross the cache's retention window,
rather than leaving a large session sitting unrefreshed for someone to wake
later. This is `ops/MULTI-SESSION.md`'s doctrine in full: wake cadence,
durability across a session wall, and compaction insurance are all argued
there and not repeated here. `autoCompactWindow` in
`examples/settings/settings.json` is the mechanical half of the same idea -
it bounds how far a single session's context grows before compaction forces
the question, rather than leaving that to whenever the harness's own default
happens to trigger.

**2. Per-model effort.** `effortLevel` and `modelSettings` set how hard a
model reasons before it answers, independent of which model it is. A relay,
a status ask, or a ledger edit does not need the same effort a genuinely
hard judgment call does, and setting effort per model rather than leaving
every turn at the top setting is a lever you pull once, in a settings file,
rather than one you have to remember to invoke on every turn.
`examples/settings/settings.json` and its companion `README.md` are a worked
block.

**3. The judge / run / execute split.** Not every turn belongs on the same
model. A top-tier model reserved for judgment - rulings, audits, the calls
that are genuinely hard to get back if wrong - costs the most per token and
should run the fewest turns. A mid-tier model runs a seat's ordinary
day-to-day work: the volume of turns any staff actually produces most of.
A worker-tier model, reached through a fan-out's own subagents, executes the
mechanical and scanning-tier pieces of that work - fetches, searches,
scoped edits - at a fraction of the mid tier's cost per turn. **Workers never
nest.** A worker that could itself convene a worker turns one delegation
into an unbounded tree nobody projected the cost of; keeping delegation to
one level is what `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` in the settings
example enforces mechanically, and what `EXTENDING.md` section 3 already
says in words - a sub-agent is a hand, not a seat, and holds no standing of
its own to convene further hands. `org/models.yml` is where your own roster
maps onto this shape; `ops/FLEET_CRAFT.md` §2 is the doctrine on why the
building tier is the default every fan-out role starts from.

**4. Concurrency caps.** How many agents may run at once bounds how fast a
fan-out can spend, independent of how much any single agent costs.
`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` in the settings example is the
harness-level cap; `ops/FLEET_CRAFT.md` §3's agent-count brake is the same
idea built into a fleet script itself, as the second threshold of its budget
guard, because a live spend figure a harness reports is often a lower bound
that misses cache-write and input cost, where a count of convened agents is
exact.

**5. Explore on the small model.** A lookup - find the file, find the
function, confirm something exists - does not need the seat's own model or
its own effort level. Routing that class of work to the cheapest capable
model at the lowest effort, with a return contract that hands back paths and
short summaries rather than whole files, keeps the caller's own turn from
paying full price for work a small model does just as well.
`examples/settings/agents/explore.md` is a worked override.

**6. Doctrine as invoke-loaded skills instead of always-on imports.** A file
`@`-imported into a `CLAUDE.md` is read into every turn of every session
that opens there, whether or not that turn ever touches what it says. The
same material, packaged as a skill whose body loads only when a session
actually invokes it, costs a short description in the prefix instead of the
whole file, every turn that never needed it. This repository's own
`.claude/skills/` already ships the session rituals this way; the same move
is worth making for any other doctrine file that has grown long enough that
most turns never open it.

**7. Connectors and skills you do not use, kept out of the prefix.** Every
enabled MCP connector and every discoverable skill's description loads into
every session's prefix and every subagent's, whether or not that session's
work ever touches it. `disableClaudeAiConnectors` and `deniedMcpServers`
turn off connectors a given setup never calls; a project-scoped
`skillOverrides` does the same for skills that belong to one line of work and
not another. Small per turn, and it compounds over every turn of every
session that carries it for no reason.

**8. Shell output filtering.** Full, unfiltered command output that lands in
a transcript is written into cache once at the write rate and then re-read
on every later turn of that session for as long as the session lives.
Filtering a verbose command down to what actually answers the question -
before it enters context, not after - keeps a single noisy command from
becoming a standing tax on every turn that follows it.

---

## 3. How to measure

Nothing above is worth acting on from its description alone. `scripts/
token-audit/` reads your own local transcripts and reports the numbers that
settle whether a lever actually moved anything for your own mix of seats and
models: per-turn context size, how often a main chain re-warms a large
context after an idle gap, and a before-and-after comparison once you have
made a change. `scripts/usage-meter-tally.py` is the coarser companion
already in this repository - a weekly tally by model and by lane, useful for
checking a meter reading against the work actually done. Run either against
a baseline window before changing anything, make one change, and run it
again against the same window length going forward; a lever's rank on this
page is about which kind of change tends to matter most, not a promise about
what it will save in your own repository.
