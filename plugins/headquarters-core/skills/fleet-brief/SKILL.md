---
name: fleet-brief
description: Authoring a new fan-out script or its per-agent prompts: the hard script-craft rules (files not returns, honest portability, house style in-prompt, ...).
---

# Fleet-brief: script-craft rules for a fan-out

Each rule below is stated with the failure class it exists to prevent. They are
hard rules: embed them in every fleet script you write, and treat a script that
skips one as unfinished rather than as a stylistic variant.

1. **Work travels through files, not through returns.** Every lane writes its
   output to disk at the moment it has it, not at the end when it hands something
   back. An agent that dies mid-run must have already left its value behind.
   Returns are for short digests the orchestrator uses to sequence the next step;
   they are never the only copy of anything.

2. **No single agent's failure kills the run.** Every awaited call outside a
   managed group catches its own error and continues. A dead lane costs one log
   line and whatever it had not yet written. This rule is only survivable because
   of rule 1: the two are one design, not two preferences.

3. **Reasoning-tier calls return prose, not schema-constrained structure.**
   Strict output formats and the most capable tier are a poor pairing: the
   retries pile up, and a retry cap reached mid-run can take the whole script
   down with it. Keep structured returns on the lighter tiers, where they
   behave, and let the reasoning tier answer in plain text the orchestrator
   parses loosely or not at all.

4. **A writer's first move is inspection, and production is what happens after
   it.** Every writer prompt carries an instruction to this effect, in these
   words or your own:

   > Look at the target path before you produce anything. Where something is
   > already sitting there, your assignment changes shape: find each place the
   > existing content falls short of this brief, close those specific gaps, and
   > leave whatever already satisfies the brief untouched. Producing the file
   > from nothing is the exception, and it needs a reason you can state.

   The economics are why this is a hard rule rather than a preference. Checking
   a file that turns out to be sound costs a fraction of producing that same
   file a second time, and the second copy is no better than the first. On a
   resume, where much of the target set is usually fine already, this one
   instruction decides most of the bill.

5. **Pin the tier, and the effort, on every call.** Each agent's tier comes from
   the operator's model-tier config, named explicitly at the call site, never
   inherited by accident. An unpinned call inherits whatever model sits at the
   keyboard, which may be the one interactive-only tier that must never run
   unattended. Set an explicit effort level per stage too: lower for extraction
   and drafting, higher for synthesis, adversarial review, judging, and final
   verification. The interactive seat you sit with never appears in a fan-out at
   all: that rail is stated in the model-tier config and no script may quietly
   override it.

6. **Prefer a pipeline to a barrier.** Stage work so that each piece proceeds as
   soon as its own input exists, rather than gathering everything at a
   checkpoint. A barrier concentrates risk: if a window closes or a limit trips
   while many agents are waiting at one, they all die together, whereas a
   pipeline loses only what was moving.

7. **Say honestly what the run needs.** If a fleet writes to a path that exists
   only on the operator's machine, or depends on a local tool or credential, the
   mission's `STATE.md` header says so plainly. A header that overstates
   portability wastes somebody's time later on a pickup that was never possible.

8. **Checkpoint while the fleet runs.** Commit output at material change points
   during the run, not at the end of it, per the operability doctrine. Insurance
   this cheap is worth buying every time, and it is what turns an interrupted
   run into an inconvenience rather than a loss.

9. **Close the source before drafting from it.** A writer producing distilled
   prose from source material reads the source for concepts, then closes it
   before it starts drafting. Drafting with the source still open tends to bleed
   through as near-verbatim text that survives a casual check. Treat any passage
   that must stay verbatim as a deliberate, named exception, never paraphrased;
   fixing a passage flagged as too close to its source needs a structural
   rewrite, not a synonym swap.

10. **Point a derived writer at a staged file, not at moving state.** When one
    run authors both a derived artifact and its own source material at the same
    time, give the derived writer a sibling file to open: the source's finished,
    staged copy, not the live document a parallel writer might still be editing
    underneath it.

11. **Embed house style in the prompt, not in a reference file.** State house
    style or format rules directly inside every writer's own prompt; a writer
    often will not go read a separate style file on its own. Any style sweep
    applies to outbound, public-facing copy only. Internal working files are
    exempt entirely.

12. **Capture verbatim material at the moment of fetch.** Any worker pulling
    quoted or verbatim material copies it exactly into a durable record before
    it does any summarizing. Downstream work reads only from that verified
    capture, never from a paraphrase dressed up as a quote.

13. **Give parallel builds their own namespace, and kill the stale one.** Give
    every worktree, sandbox clone, or parallel build a unique namespace before
    the first command touches it, and have each worker's first action confirm it
    is scoped to its own instance. Scope any teardown sweep to an explicit
    allowlist of what this run actually created, never to "everything of this
    class," which can remove a shared resource another concurrent run depends
    on; name shared infrastructure explicitly as off-limits to every worker.
    When more than one instance of a build ends up running, identify and kill
    the stale one, so review targets exactly one canonical build.

14. **Every example value is synthetic.** Every example or placeholder value
    inside a prompt or script is synthetic, never a real value drawn from the
    material being processed. Grep your own generated scripts and deliverables
    for leaked real values before committing either one.

15. **A scout confirms it is reading current state.** A scout, audit, or
    research agent reading a repository or resource it does not own confirms it
    is reading current state, not a stale local checkout, before it reports a
    finding. A scout many commits behind can surface a finding that is false or
    already fixed, which wastes a correction cycle.

16. **Dictate concrete lines, and cap the correction rounds.** Hand execution
    agents dictated, concrete lines to implement rather than free-form prose
    requirements. A vague spec invites the executor to invent structure nobody
    intended, which then has to be corrected by hand. Name the invariants that
    must not change explicitly, and cap the number of correction rounds before
    escalating to a higher tier rather than iterating indefinitely at the lower
    one.

Source: ops/FLEET_CRAFT.md § 4. Script-craft rules (moved into this skill 2026-09-16)
