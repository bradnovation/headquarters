---
name: local-model-rails
description: Use before loading a local model, when the preflight hook denies a command, after a reboot or ollama update, or when the machine freezes under a model.
---

# Local model rails

Apple Silicon shared memory means the GPU and macOS compete for the same pool.
Three independent guards keep a local model load from starving WindowServer and
freezing the machine. Each resets or vanishes on its own trigger, not all on the
same one — check all three fresh before any load; never trust what a prior
session set.

## What the rails are

1. **Wired GPU memory limit** (`iogpu.wired_limit_mb`) — an Apple Silicon sysctl
   that reserves GPU memory instead of leaving the OS default (0, unbounded
   contention with macOS). Resets to 0 on every true reboot.

2. **Four `OLLAMA_*` environment rails** — `OLLAMA_KEEP_ALIVE`,
   `OLLAMA_MAX_LOADED_MODELS`, `OLLAMA_FLASH_ATTENTION`, `OLLAMA_KV_CACHE_TYPE`.
   They bound how long a model stays resident, how many load at once, and how
   much the KV cache costs. Set with `launchctl setenv` (user-level, no sudo) —
   but that only writes the launchd domain. A server process already running
   keeps its OLD environment and silently ignores all four, even though
   `launchctl print` reports them as set. The only proof is the running
   server's OWN environment (check below). These vanish on GUI-session
   respawn, logout, reboot, or an Ollama auto-update — anything that restarts
   the server without the setenv having already happened.

3. **Reclaimable-memory floor** — a hard-abort threshold on free + reclaimable
   RAM, from `vm_stat`:
   `reclaimable_GiB = (pages_free + pages_inactive + pages_speculative + pages_purgeable) × 16384 / 1073741824`
   Below the floor, a load either gets refused or, if it slips through, runs at
   a fraction of its benched speed — one measured case ran ~35x slower with no
   crash. This is a throughput guard as much as a crash guard.

## Check each, one command

- Wired limit: `sysctl -n iogpu.wired_limit_mb`
- OLLAMA rails, from the SERVER PROCESS env (not `launchctl print` or
  `launchctl getenv` — both can lie):
  `ps eww $(pgrep -f 'ollama serve' | head -1) | tr ' ' '\n' | grep ^OLLAMA_`
- Reclaimable floor:
  `vm_stat | awk '/Pages (free|inactive|speculative|purgeable)/{v=$NF; sub(/\./,"",v); s+=v} END{printf "%d GiB\n", s*16384/1073741824}'`

This plugin ships `scripts/check-rails.sh`, which runs all three checks above
and prints the result in one pass. It only checks and prints — no sudo, no
restarts, no writes — so it's safe to run any time, whether or not a model is
loaded.

## Restore each

- **Wired limit** — the operator types this himself, every time (no TTY in an
  agent session, and it's their machine to authorize):
  `sudo sysctl iogpu.wired_limit_mb=<value>`

- **OLLAMA rails** — write a small rails-fix script for your own machine that
  does three things, in order:
  1. Sets the four `OLLAMA_*` rails with `launchctl setenv` (user-level, no
     sudo), so future logins and session starts pick them up.
  2. Restarts the `ollama serve` process. This step is required, not optional
     — a server already running keeps its OLD environment, so `setenv` alone
     never reaches it.
  3. Verifies the rails from the RESTARTED server's own environment (the
     one-liner above), not from `launchctl print` or `getenv`, since both can
     report a rail as set when the live server process never inherited it.
  After running it, use `scripts/check-rails.sh` to confirm independently —
  it reads the same server-environment truth without trusting the fix
  script's own exit code.

- **Reclaimable floor** — free memory, don't wait it out. See "never quit the
  operator's apps" below — this is never a Claude-initiated quit.

## What the preflight hook refuses

`ollama-preflight.sh` (this plugin's `hooks/ollama-preflight.sh`, a
PreToolUse `Bash` hook via `hooks/hooks.json`) intercepts commands that can
LOAD a model — `ollama run|serve|create|pull`, a direct call to
`:11434/api/generate|chat|embed`, `--local-provider ollama|lmstudio`, or
`codex ... --oss`. Inspection (`ollama ps`, `list`, `show`) passes through.

It checks all three rails above and denies with one message per failing rail,
concatenated. The fix line for each (as printed, with the live numbers filled
in):
- `iogpu.wired_limit_mb=<current>, need <required> (operator: sudo sysctl iogpu.wired_limit_mb=<required>)`
- `<n>/4 OLLAMA rails in the SERVER env (run your rails-fix script)`
- `ollama server not running (run your rails-fix script)`
- `reclaimable memory <n> GiB < <floor> GiB floor (free memory first: quit memory-heavy apps; no model until then)`

Thresholds are env vars (`PREFLIGHT_WIRED_MB`, `PREFLIGHT_FLOOR_GIB`) — each
machine sets its own. The shipped defaults (20480 MB / 17 GiB) are tuned for
a 24 GB Apple Silicon machine; scale both for your own hardware's total RAM
and typical model size. See the header comment in `hooks/ollama-preflight.sh`
for where to set the overrides.

## Fan-out cap while a model is resident

Cap Claude Code subagent parallelism at **2–3** while any local model is
GPU-resident — pick the conservative end when headroom is thin. Unthrottled
fan-out plus a wired-memory model is the exact combination that starves
WindowServer. Drop the cap before the fan-out starts, not after — checking
post-freeze is too late to matter.

## What the freeze actually is, and recovery order

A black screen that dumps you back to the login/redraw screen, with kernel
uptime unbroken, is a **WindowServer watchdog kill from memory starvation** —
not a reboot, not a panic. Confirm before acting on it:
- `last reboot` — if the boot time predates the freeze, nothing actually
  rebooted.
- `/Library/Logs/DiagnosticReports/` — look for a `*watchdog_timeout*` entry
  timestamped at the freeze.

Recovery order:
1. Confirm watchdog kill vs. true reboot (above) — this decides which rails
   are even suspect. A true reboot kills the wired limit AND the OLLAMA rails;
   a watchdog kill alone may leave both intact.
2. Find the memory holders: `top -l 1 -o mem -stats pid,mem,cmprs,command`.
   Check the CMPRS column too, not just resident size — a compressed hog
   (idle containers, a stale server, many browser tabs) can outweigh resident
   size and hide from a resident-only sort.
3. Show the holders to the operator. Don't guess which one caused it from
   process name alone.
4. Once memory is freed (or after any confirmed true reboot), run your
   rails-fix script, then re-check the wired limit — hand the operator the
   sudo line if it's still 0.
5. Re-run the one-command checks above (or `scripts/check-rails.sh`) before
   loading anything; the preflight hook re-checks on every attempt too.

## Never quit the operator's apps

Claude never quits the operator's applications to free memory, no exceptions
— not under a refused preflight, not during a live freeze. Show the memory
holders (step 2 above) and name what's using what; the operator decides what
to close, from the menu bar or by typing the quit command themself. This
holds even when the fix looks obvious and safe: an idle app holding gigabytes
for nothing currently connected to it is still their call, not an autonomous
one.
