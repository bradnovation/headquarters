#!/bin/bash
# check-rails.sh — read-only status check for the three local-model memory rails
# (see skills/local-model-rails/SKILL.md). Prints what it finds; makes no changes.
# No sudo, no restarts, no writes. Safe to run any time, loaded model or not.
#
# Exit code is informational only: 0 if all three rails look sound, 1 if any
# rail is missing or below its floor. Nothing here fixes anything — that script
# is machine-specific and yours to write; see "What a rails-fix script must do"
# in the SKILL for the shape of it.
#
# Thresholds, same env vars the preflight hook reads (defaults tuned for a
# 24 GB Apple Silicon machine; override per machine, see the hook's header):
WIRED_MB="${PREFLIGHT_WIRED_MB:-20480}"
FLOOR_GIB="${PREFLIGHT_FLOOR_GIB:-17}"
RAILS="KEEP_ALIVE|MAX_LOADED_MODELS|FLASH_ATTENTION|KV_CACHE_TYPE"

status=0

echo "== Wired GPU memory limit =="
wl=$(sysctl -n iogpu.wired_limit_mb 2>/dev/null)
if [ -z "$wl" ]; then
  echo "  iogpu.wired_limit_mb: not readable on this machine (not Apple Silicon macOS?)"
elif [ "$wl" -ge "$WIRED_MB" ]; then
  echo "  iogpu.wired_limit_mb=$wl  OK (>= required $WIRED_MB)"
else
  echo "  iogpu.wired_limit_mb=$wl  BELOW required $WIRED_MB"
  echo "  fix: sudo sysctl iogpu.wired_limit_mb=$WIRED_MB"
  status=1
fi

echo
echo "== OLLAMA_* rails (read from the running server process's own environment) =="
sp=$(pgrep -f 'ollama serve' | head -1)
if [ -z "$sp" ]; then
  echo "  ollama server: not running — nothing to check yet"
  echo "  (rails are set on the server process at start; they don't apply until one is running)"
else
  found=$(ps eww "$sp" 2>/dev/null | tr ' ' '\n' | grep -E "^OLLAMA_($RAILS)=")
  n=$(printf '%s\n' "$found" | grep -c "^OLLAMA_")
  echo "  ollama server: running (pid $sp)"
  for name in OLLAMA_KEEP_ALIVE OLLAMA_MAX_LOADED_MODELS OLLAMA_FLASH_ATTENTION OLLAMA_KV_CACHE_TYPE; do
    v=$(printf '%s\n' "$found" | grep "^${name}=" | head -1)
    if [ -n "$v" ]; then echo "  $v  OK"; else echo "  $name  MISSING from server env"; fi
  done
  if [ "$n" -lt 4 ]; then
    echo "  $n/4 rails present in the server's own environment."
    echo "  Note: launchctl setenv / getenv can both report a rail as set even when"
    echo "  the already-running server process never inherited it — this check reads"
    echo "  the server's actual environment instead, which is the only place that matters."
    status=1
  fi
fi

echo
echo "== Reclaimable memory vs. floor =="
recl=$(vm_stat 2>/dev/null | awk '/Pages (free|inactive|speculative|purgeable)/{v=$NF; sub(/\./,"",v); s+=v} END{printf "%d", s*16384/1073741824}')
if [ -z "$recl" ]; then
  echo "  vm_stat: not available on this machine"
elif [ "$recl" -ge "$FLOOR_GIB" ]; then
  echo "  reclaimable ${recl} GiB  OK (>= floor ${FLOOR_GIB} GiB)"
else
  echo "  reclaimable ${recl} GiB  BELOW floor ${FLOOR_GIB} GiB"
  echo "  fix: free memory first (quit memory-heavy apps yourself); no model load until above floor"
  status=1
fi

echo
if [ "$status" -eq 0 ]; then
  echo "All checked rails look sound."
else
  echo "One or more rails need attention before loading a local model."
fi
exit "$status"
