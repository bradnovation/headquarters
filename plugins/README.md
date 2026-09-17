# Plugins

This repo ships Claude Code plugins under `plugins/<name>/`, each a
self-contained directory with its own `.claude-plugin/plugin.json`, and
whatever mix of `skills/`, `hooks/`, `scripts/`, etc. it needs. Plugins here
are optional add-ons layered on top of the headquarters staff-and-doctrine
files — nothing in the core repo depends on any of them being enabled.

Currently shipped:

- **`local-lane`** — a local-model safety lane for Apple Silicon: a
  PreToolUse hook that refuses commands which would load a local model
  (`ollama run`, etc.) until three memory rails are confirmed sound, plus a
  `local-model-rails` skill documenting the rails and how to restore them.
  **Optional.** Operators who don't run local models never enable it and
  never see it — the hook only fires on `Bash` commands, and it exits
  immediately (no-op) on any command it doesn't recognize as a model-load.

- **`headquarters-core`** — this template's own operating doctrine, packaged
  as a plugin: invoke-loaded skills, a `worker` subagent for delegated
  building-tier work, and a PreToolUse hook that asks before a session fans
  out past its subagent cap. Skills land here as they're validated; the
  `skills/` directory ships empty until then.

## Enabling a plugin from this repo

There are three ways to turn a plugin on. None of them require anyone else's
opt-in — each operator or project chooses independently.

### (a) In-repo, automatic when this repo is your working directory

Claude Code auto-loads any folder under `.claude/skills/` that itself
contains a `.claude-plugin/plugin.json` as a **project-scope skills-directory
plugin**, named `<name>@skills-dir`, the next time you start a session in
this repo. To wire up `local-lane` this way, either symlink or copy it into
place:

```bash
# from the repo root
ln -s ../../plugins/local-lane .claude/skills/local-lane
# or, if you'd rather not symlink:
cp -r plugins/local-lane .claude/skills/local-lane
```

**The trust gate**: because this content is checked into a repository rather
than something you typed yourself, Claude Code only loads a project-scope
`@skills-dir` plugin after you've accepted the workspace trust dialog for
this folder. Trusting a parent directory doesn't count, and neither does
running in `-p`/non-interactive mode — you (or whoever clones this repo)
need to trust this specific folder in an interactive session first. This is
the same gate that governs project-level allow rules in
`.claude/settings.json`, and it's why a cloned repo can't silently run hooks
or MCP servers on your machine without you seeing and accepting it once.

Launch Claude Code from the repo root for this to take effect — a
project-scope `@skills-dir` plugin loads only from the `.claude/skills/` of
the session's primary working directory; it does not walk up from a
subdirectory to find one at the repo root.

### (b) Everywhere on your machine, regardless of working directory

Symlink the plugin into your personal (user-scope) skills directory instead
of the project one:

```bash
ln -s /path/to/this/repo/plugins/local-lane ~/.claude/skills/local-lane
```

Personal-scope skills-directory plugins carry none of the project-scope
restrictions above (no trust-dialog gate, hooks and MCP servers load
normally) because the content is something you deliberately linked in
yourself. Confirm it loaded with:

```bash
claude plugin list
```

which will show `local-lane@skills-dir` once Claude Code picks it up (next
session, or after `/reload-plugins`).

### (c) The marketplace route

This repo's `.claude-plugin/marketplace.json` is itself a plugin
marketplace. Add it and install from it like any other:

```bash
claude plugin marketplace add /path/to/this/repo
claude plugin install local-lane@headquarters
```

This is the right route when you want Claude Code's normal
install/update/uninstall lifecycle (versioning, `claude plugin update`,
per-scope enable/disable) rather than a hand-placed symlink.

## Live-reload notes

- Edits to a `SKILL.md` take effect immediately in the current session —
  no reload needed.
- Edits to anything else — `hooks/`, `.mcp.json`, `agents/`,
  `output-styles/` — need `/reload-plugins` (or a session restart) to take
  effect, whichever install route you used.

## local-lane is optional

Nothing in this repo requires `local-lane`. If you don't run local models
(Ollama, LM Studio, etc.) on your machine, there's no reason to enable it,
and if you never enable it, you never see it — no hook fires, no skill
loads, no prompt changes. It exists for operators who do run local models
on memory-constrained hardware and want the load-time safety check.
