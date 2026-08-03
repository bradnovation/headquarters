# ATTRIBUTIONS - the outside work this product's mechanics were adapted from
<!-- file-class: DOCTRINE -->

*Several mechanisms in this product were adapted from open-source projects that
solved the same problem first. This file is the one place that says so, so that a
reader of any single doctrine file can find out in one hop whether the mechanic in
front of them originated here or elsewhere. Individual files carry a short pointer
back to this list rather than repeating the credit in their own words.*

*What was adapted in every case below is an idea: a shape, a threshold, a
separation of concerns. No code was copied from any of these projects. The wording,
the gates each mechanism sits behind, the failure modes named around it, and every
implementation detail are this product's own, and any of them being wrong is this
product's fault rather than the original author's.*

---

## The list

- **Paperclip** (`paperclipai/paperclip`) - a tiered budget stop that lives inside
  the running script instead of in a document its author is meant to remember.
  Lands in the two-threshold budget guard, `ops/FLEET_CRAFT.md` section 3.
- **Kortix / Suna** (`kortix-ai/suna`) - agent sessions that run in isolation and
  reach the main line only through a change request a human approves. Lands in the
  branch-per-session landing mechanic, `ops/FLEET_CRAFT.md` section 6.
- **BMAD-METHOD** - generation kept strictly apart from selection, plus a running
  log that lets an interrupted pass be resumed rather than restarted. Lands in the
  divergence and convergence separation and the memlog, `.claude/skills/dream-run/SKILL.md`.
- **AI Team OS** - typing a failure by the kind of remedy it deserves instead of
  filing every failure the same way, and keeping a small script that mechanically
  re-checks the rules a set of documents states. The first lands in the lesson
  typing shared by `ops/FLEET_CRAFT.md` section 10 and
  `org/functions/agent-quality/CHARTER.md`, and in `ops/JUDGMENT_CRAFT.md`'s
  failure handling; the second lands in `scripts/check-invariants.sh`.
- **Agency Agents** - packaging a working persona in a single command so that
  standing up a new one is a short interview rather than a build. Lands in the
  onboarding interview, `.claude/skills/init/SKILL.md`.

---

## Keeping this file honest

Add a row here when you adapt an outside mechanism into your own copy, and put a
one-line pointer at the place it lands rather than an inline credit that drifts out
of step with this list. Where you are unsure whether something was genuinely
adapted or merely arrived at independently, write the row anyway: an unnecessary
credit costs a line, and a missing one is the kind of thing that is only ever
noticed by the person who deserved it.
