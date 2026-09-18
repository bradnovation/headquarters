#!/bin/bash
# agent-cap.sh — Claude Code hook, two events (see hooks.json):
#   UserPromptSubmit : reset this session's counter (the cap is PER INSTRUCTION, not per session).
#   PreToolUse/Agent : count the spawn; at the (cap+1)th spawn of one instruction ASK ONCE, with the
#                      agent's stated purpose; then again every CAP spawns after that (11th, 16th, ...) as a runaway check.
# Cap 5 (five by default, more on the operator's word with a reason), lowered to 3 while a
# local model is GPU-resident (local-model doctrine). The hard concurrency ceiling is
# CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS in settings.json; this hook is the checkpoint, not the ceiling.
# Workflow-tool fleets do not pass through this hook; their brake is the projection ritual.
# Shape after Aaron McGowan's finding (claude-ops PR #1, 2026-09): a per-session cumulative counter
# turns into a toll gate on every spawn past the cap; scope it to the instruction and ask once.
CAP="${AGENT_CAP:-5}"; CAP_RESIDENT="${AGENT_CAP_MODEL_RESIDENT:-3}"
command -v jq >/dev/null || exit 0
INPUT=$(cat)
SID=$(printf '%s' "$INPUT" | jq -r '.session_id // "unknown"')
EVENT=$(printf '%s' "$INPUT" | jq -r '.hook_event_name // ""')
F="${TMPDIR:-/tmp}/claude-agent-spawns-$SID"
if [ "$EVENT" = "UserPromptSubmit" ]; then : > "$F"; exit 0; fi
DESC=$(printf '%s' "$INPUT" | jq -r '.tool_input.description // ""')
note=""
if ollama ps 2>/dev/null | awk 'NR>1 && NF>0{f=1} END{exit !f}'; then CAP="$CAP_RESIDENT"; note=", lowered while a local model is resident"; fi
touch "$F"; echo "$(date +%s)" >> "$F"; N=$(wc -l < "$F" | tr -d ' ')
if [ "$N" -gt "$CAP" ] && [ $(( (N - CAP - 1) % CAP )) -eq 0 ]; then
  jq -n --arg r "This instruction is fanning out past $CAP subagents$note (this is number $N). Purpose: ${DESC:-unstated}. Approve the fan-out? (asked at the 6th spawn of an instruction and every 5 after; the hard concurrency ceiling stays at CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS)" \
    '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"ask",permissionDecisionReason:$r}}'
fi
exit 0
