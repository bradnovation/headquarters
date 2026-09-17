---
name: init-tiers-and-caps
description: Mid-init, after context sources are set: the operator's values line, model tiers, and the dream-run spend cap.
---

# init-tiers-and-caps

Part of the init interview ritual (see skill:init for the full sequence, its
conduct rules, and the show-before-write discipline). These three topics are
asked mid-init, after context sources are recorded and before the ritual
closes. Ask one at a time, read each answer back before moving on, and write
nothing until the write pass.

### Topic 6 - Your values line

**Ask:** how they want work done in their name, in their own words. One line or
a short list. Not a mission statement - the sentence a colleague would recognize
as theirs.

**Why:** it is quoted into seat charters and it is what the standards guard
measures a draft against when it asks whether something sounds like the
operator. Left blank, the staff has no standard to hold work to beyond plain
competence, and it will say so honestly rather than inventing one.

**Lands in:** the generated layer of `CLAUDE.md`, section (f), transcribed
exactly as given.

**If deferred:** the placeholder stands and the guard runs without a voice
standard. Worth revisiting; not worth pressing for in the moment, because a
values line produced under mild pressure is nobody's values line.

### Topic 7 - Your model tiers

**Ask:** which models their own plan actually grants them, and let
`org/models.yml` do the sorting into reasoning, building, and scanning. That
file is the single source of truth for tier assignment and its comments explain
each tier's shape.

**Three things to state plainly while asking:**

- If their plan grants exactly one usable model, all three pins get that model.
  `org/models.yml` names this collapse case as a supported configuration and
  says what is lost by it. Configure it deliberately rather than leaving two
  pins blank.
- If they have a premium or interactive-only tier they reserve for their own
  keyboard, it is never pinned into a duty row. That rail is constitutional, and
  this product assumes nothing above the ordinary reasoning tier anywhere.
- Never set a global environment override for the subagent model. It wins
  silently over every pin in the file and nothing in a run's output records that
  it did.

**Lands in:** the three pins in `org/models.yml`. The duty map below them
already ships filled and needs no interview answer.

**If deferred:** the pins stay bracketed and the first fan-out has no tier to
read. File it as an open item; a missing model tier is one of the gaps the
founding handoff entry is written to surface.

### Topic 8 - Your dream cap

**Ask:** whether off-cycle generative work is worth spending on, and if so, what
ceiling they want on it, in whatever unit they meter in, over whatever period
they think in. Offer a conservative figure **as a starting point and say that is
what it is**: something small enough that a surprise is an annoyance rather than
an event. Then take whatever number they actually give.

**Never assume one.** Dreaming ships disarmed for exactly this reason: no
default figure is safe on somebody else's meter, and the number that governs has
to be one they typed.

**Say what the number does and does not do.** Recording a cap is one of three
conditions in `org/functions/innovation-desk/CHARTER.md`. The other two are a
confirmed read scope - public and internal material, with any external source's
consent already recorded under topic 4 rather than re-asked here - and a kill
switch they have verified they can operate. Until all three hold, dreaming does
not run by hand or otherwise, and setting the figure alone has not armed
anything.

**Lands in:** the dream cap line in `CLAUDE.md` section (f), which is the
governing figure; `ledgers/SPEND.md` is where each run is projected and
reconciled against it afterward.

**If deferred:** the line stays `[UNSET]`, router item 4 declines and says why,
and the item goes on the open list. This is a fully supported state, not a
half-finished setup.

Source: .claude/skills/init/SKILL.md Topic 6, Topic 7, Topic 8 (moved into this skill 2026-09-16)
