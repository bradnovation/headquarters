#!/bin/bash
# agent-cap.sh — Claude Code PreToolUse hook (matcher: Agent).
# Asks the operator, with the agent's stated purpose, once a session fans out past the cap
# inside a rolling window. Cap 5 (his ruling 2026-09-16: five by default, more on request with
# a reason), lowered to 3 while a local model is GPU-resident (factory doctrine M-010).
# Workflow-tool fleets do not pass through this hook; their brake is the projection ritual.
CAP="${AGENT_CAP:-5}"; CAP_RESIDENT="${AGENT_CAP_MODEL_RESIDENT:-3}"; WIN="${AGENT_CAP_WINDOW_SEC:-900}"
command -v jq >/dev/null || exit 0
INPUT=$(cat)
SID=$(printf '%s' "$INPUT" | jq -r '.session_id // "unknown"')
DESC=$(printf '%s' "$INPUT" | jq -r '.tool_input.description // ""')
note=""
if ollama ps 2>/dev/null | awk 'NR>1 && NF>0{f=1} END{exit !f}'; then CAP="$CAP_RESIDENT"; note=", lowered while a local model is resident"; fi
F="${TMPDIR:-/tmp}/claude-agent-spawns-$SID"; now=$(date +%s); touch "$F"
awk -v c=$((now-WIN)) '$1>=c' "$F" > "$F.tmp" 2>/dev/null && mv "$F.tmp" "$F"
echo "$now" >> "$F"; N=$(wc -l < "$F" | tr -d ' ')
if [ "$N" -gt "$CAP" ]; then
  jq -n --arg r "Subagent $N in the last $((WIN/60)) min (cap $CAP$note). Purpose: ${DESC:-unstated}. Approve this fan-out?" \
    '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"ask",permissionDecisionReason:$r}}'
fi
exit 0
