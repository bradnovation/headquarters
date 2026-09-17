# examples/settings/ - a worked user-level settings block

<!-- file-class: DOCTRINE -->

*`settings.json` alongside this file is plain JSON, which cannot carry a
file-class comment of its own; treat it as part of this DOCTRINE bundle. It
is a demonstration, not something this product writes for you: nothing in
the init interview touches `~/.claude/settings.json`, because that file lives
outside this repository, on your own machine, and applies to every project
you open with it - not only this one. Copy the keys you want into your own
copy of that file, at whatever scope your harness supports (user, project, or
local settings all accept the same keys; see the scope note on each key
below). `docs/TOKEN-ECONOMY.md` is the one-page explanation of why these
particular keys are the ones worth setting; this file is the block itself,
key by key.*

---

## `effortLevel: "high"`

**Scope: any settings file.** The default reasoning effort for any model that
does not have its own saved level. `high` balances token usage and
intelligence; `xhigh` reasons deeper at a real token-spend cost, and is worth
turning on for a specific hard problem rather than leaving on as the floor
under every relay, status ask, and ledger edit a session makes in a day. Drop
this to `medium` if your own mix of work is mostly routine and you want the
cheaper floor; raise a single turn to `xhigh` with `/effort xhigh` instead of
raising this line.

## `modelSettings`

**Scope: any settings file.** A per-model effort level, which overrides the
top-level `effortLevel` for that model wherever it runs. This block pins two
models at `high`: substitute whatever models your own plan actually gives
you a seat's standing model and the model you reach for judgment on. A model
with no entry here falls back to the top-level `effortLevel` above it, so you
do not need a row for every model you might ever use, only the ones you want
to hold at a level different from the default.

**A note on `maxEffortLevel`, not shipped here.** If you want a hard ceiling
a session cannot exceed even from `/effort` or a subagent's own frontmatter,
add `maxEffortLevel` next to a model's `effortLevel` in its `modelSettings`
entry (or at the top level to cap every model). This block leaves that unset
because it is a stricter choice than most operators want on day one; add it
once you know which model tends to run away with effort it does not need.

## `env`

**Scope: any settings file.** Three variables, read by Claude Code itself
rather than by anything in this repository:

- `CLAUDE_CODE_SUBAGENT_MODEL: "sonnet"` - the model a subagent runs on when
  nothing more specific names one. Per-call and per-agent-frontmatter model
  choices both outrank this variable, so pinning a subagent to a different
  model in its own definition still works; this is only the floor under
  whatever does not say otherwise. Set it to whatever your own middle tier
  is - the model that runs day-to-day work well without reasoning-tier cost.
- `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS: "5"` - how many subagents a single
  fan-out may run at once. Lower this if your machine also runs anything else
  memory- or CPU-hungry while a fan-out is in flight; raise it only after
  `ops/FLEET_CRAFT.md`'s budget guard and agent-count cap are actually in the
  script doing the launching, not before.
- `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH: "1"` - a worker may not itself
  convene a worker. This is the mechanical form of `EXTENDING.md` section 3's
  "sub-agents are hands, not seats": one level of delegation, never a tree of
  them running up a bill nobody projected.

Environment values are strings, including the two numbers, because that is
the type this key accepts across every setting in it.

## `autoCompactWindow: 150000`

**Scope: any settings file.** How full a session's context gets before Claude
Code compacts it automatically, in tokens. `150000` is the mechanical form
of `ops/MULTI-SESSION.md` section 14's own ceiling - "compact or park at
about 150K", with 200K as the hard line no seat should ever run above - so a
session compacts itself at the same point that doctrine already asks a
seat to stop, rather than at the harness's own per-model default, which is
sized to that model's full window and can sit far past 200K before it ever
fires. Raise this only for the specific, ruled long run section 14 itself
carves out for a wide-context model variant, never as a seat's everyday
setting; the pattern `docs/TOKEN-ECONOMY.md` §1 names as the single largest
cost driver it found in a real multi-session staff is exactly a session
left to grow for hours past this point before anyone checks on it.

## The model default line is not shipped here, on purpose

Nothing in this file sets a top-level `"model"` key. Which model a session
opens on is the operator's own choice - it depends on your plan, which
models you actually have seats for, and which one you want a fresh session
to land on before you say otherwise - and this template does not guess at
it. Add `"model": "<your-default>"` yourself once you know what that is.

**Whatever you set it to, re-check this file after you use the `/model`
picker.** Switching models interactively does not just change the session in
front of you: Claude Code saves the model you picked as your new default and
saves that model's effort level under `modelSettings`, writing both into
this same settings file, silently, the next time you use the picker. A
`/model` switch made for one session's convenience can quietly become the
standing default and overwrite the effort level this block set on purpose.
After using the picker, open this file again and confirm it still says what
you meant it to.

## Where this file installs

`~/.claude/settings.json` for a setting that should apply to every project
you open on this machine (the usual home for everything in this example).
The same keys work in a project's own `.claude/settings.json`, checked into
version control and shared with everyone who clones it, or in
`.claude/settings.local.json` for a machine-specific override that never
gets committed. Pick the scope that matches who else should see the change:
a personal effort preference belongs at user scope; a subagent-model floor
the whole team should share belongs at project scope.
