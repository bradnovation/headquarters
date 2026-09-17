#!/bin/bash
# ollama-preflight.sh — Claude Code PreToolUse hook (matcher: Bash).
# Refuses any command that can LOAD a local model unless the memory rails are in force.
# Why: on Apple Silicon the GPU and macOS share one memory pool. Loading a large
# local model with no enforced wired-memory limit, no live OLLAMA_* rails, and no
# reclaimable-memory floor can starve WindowServer and freeze the machine. Doctrine
# says "preflight first"; this hook is what enforces it.
# Defaults below (PREFLIGHT_WIRED_MB=20480, PREFLIGHT_FLOOR_GIB=17) are tuned for a
# 24 GB Apple Silicon machine. Override per machine with environment variables set
# wherever Claude Code launches (shell profile, or "env" in settings.json), e.g.
# PREFLIGHT_WIRED_MB=12288 PREFLIGHT_FLOOR_GIB=9 for a 16 GB machine. See
# skills/local-model-rails/SKILL.md for how to size both for your own hardware.
WIRED_MB="${PREFLIGHT_WIRED_MB:-20480}"      # iogpu.wired_limit_mb required (Apple Silicon)
FLOOR_GIB="${PREFLIGHT_FLOOR_GIB:-17}"       # reclaimable memory floor, GiB (hard abort)
RAILS="KEEP_ALIVE|MAX_LOADED_MODELS|FLASH_ATTENTION|KV_CACHE_TYPE"
command -v jq >/dev/null || exit 0
INPUT=$(cat); CMD=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // empty'); [ -z "$CMD" ] && exit 0
# Only commands that can load a model. Inspection (ps/list/show) passes.
printf '%s' "$CMD" | grep -Eq '(^|[^[:alnum:]_])ollama[[:space:]]+(run|serve|create|pull)([[:space:]]|$)|(localhost|127\.0\.0\.1):11434/api/(generate|chat|embed)|--local-provider[[:space:]]+(ollama|lmstudio)|codex[^|]*--oss' || exit 0
r=()
wl=$(sysctl -n iogpu.wired_limit_mb 2>/dev/null || echo 0)
[ "${wl:-0}" -ge "$WIRED_MB" ] || r+=("iogpu.wired_limit_mb=$wl, need $WIRED_MB (operator: sudo sysctl iogpu.wired_limit_mb=$WIRED_MB)")
sp=$(pgrep -f 'ollama serve' | head -1)
if [ -n "$sp" ]; then
  n=$(ps eww "$sp" 2>/dev/null | tr ' ' '\n' | grep -Ec "^OLLAMA_($RAILS)=")
  [ "$n" -eq 4 ] || r+=("$n/4 OLLAMA rails in the SERVER env (run your rails-fix script)")
else r+=("ollama server not running (run your rails-fix script)"); fi
recl=$(vm_stat 2>/dev/null | awk '/Pages (free|inactive|speculative|purgeable)/{v=$NF; sub(/\./,"",v); s+=v} END{printf "%d", s*16384/1073741824}')
[ "${recl:-0}" -ge "$FLOOR_GIB" ] || r+=("reclaimable memory ${recl} GiB < ${FLOOR_GIB} GiB floor (free memory first: quit memory-heavy apps; no model until then)")
if [ ${#r[@]} -gt 0 ]; then
  msg="LOCAL-LLM PREFLIGHT FAILED, load refused: $(IFS=';'; echo "${r[*]}")"
  jq -n --arg m "$msg" '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:$m}}'
fi
exit 0
