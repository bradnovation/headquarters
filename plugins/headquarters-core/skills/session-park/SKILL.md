---
name: session-park
description: Mid-session, approaching the context ceiling or an idle stretch past the cache window, or a session wall may land: checkpoint, write the resume recipe, park before the gap starts.
---

# Session Park

A session wall is not a pause. When a shared usage pool resets on its own clock, or a
session simply runs out of room, the wall ends the current turn outright — nothing on
the other side of it resumes itself, and whatever wasn't written to disk before the
wall did not survive it. This skill covers the durability discipline that survives a
wall (§7), the hard ceiling that should trigger a park before one is even in sight
(§14), and the economics that say park early rather than let a seat go idle (§15).

## §7. Durability across a session wall

Build every long piece of work assuming a wall can land at any point, not just at the
end:

- **The resume recipe lives on disk before the wall, not after.** Write down what is
  running, what a resuming session must verify on disk before touching anything, and
  what must never be re-run blindly. Do this while you still can, not as a postmortem
  once the wall has already landed.
- **Checkpoint commits land at material points**, not only when the work is finished.
  A session that has done an hour of real work and written none of it down has
  produced nothing durable, no matter how good the work was.
- **Size remaining work against the time actually left**, and do not launch new work
  in the final stretch before a wall you can see coming. Starting something you
  cannot finish just before a wall guarantees exactly the kind of half-written state
  the resume recipe exists to avoid.
- **The spend-limit stop protocol, on any hard usage-limit error: stop, record what
  happened, and never retry into the same wall.** Retrying against a limit you have
  already hit spends whatever is left of the budget on failures and buys nothing.
  Resume only after the limit resets, and resume small: inventory what is already on
  disk before deciding what still needs doing.

## §14. The context ceiling

**No seat runs above 200K tokens of context.** Compact or park at about 150K, and
before any idle stretch expected to run past 45 minutes — whichever comes first. The
number is not a token-counting exercise for its own sake: it is the point past which
a wake gets expensive under §15, and past which a session is running on a compacted
memory of its own reasoning rather than the record it actually wrote down.

**A model variant with an extended context window does not move this ceiling; it
changes what enforces it.** Some model variants offer a window far past 200K. An
auto-compact setting that triggers as a fraction of the model's own window will not
fire until a seat on the wider variant is deep past this ceiling, because it is sized
to that variant's much larger window, not to this number. A seat that keeps the wide
variant as its everyday default gets no help from auto-compact at the point that
actually matters here, and has to watch its own context and compact or park by hand.
The narrower default window keeps auto-compact's own trigger point comfortably under
200K on its own, which is why it is the standing default; the wide variant stays
reachable by an explicit model switch for one specific, ruled long run, never as a
seat's everyday setting.

## §15. Park before idle, and the cache-window wake rule

**The mechanism:** a live seat whose context sits at several hundred thousand tokens
costs a full re-write of that context at the cache-write rate when it is woken after
the provider's cache window (one hour) has lapsed; a parked seat costs almost nothing
to wake. The expensive event is not the message that wakes a seat — it is what waking
a large, idle context costs once the cache backing it has gone cold.

**The rule this produces: park, don't idle.** If a seat expects to sit idle past the
cache window, it parks before the gap starts, not after. §14's 45-minute mark is
deliberately short of the one-hour window on purpose, so the decision to park is made
with margin, not discovered once the window has already lapsed. A parked seat's next
wake starts from its own written state, at whatever context that costs to re-open —
not from a stale, multi-hundred-thousand-token conversation waiting to be re-warmed
at the expensive rate.

Source: ops/MULTI-SESSION.md §7, §14, §15 (moved into this skill 2026-09-16)
