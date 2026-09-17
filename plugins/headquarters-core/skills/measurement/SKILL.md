---
name: measurement
description: Before trusting, reporting, or acting on any number: prove the arms differ, label its provenance, reproduce before announcing, distrust a clean instrument.
---

# Measurement - the discipline for any number a session reports or acts on
<!-- file-class: DOCTRINE -->

*File class DOCTRINE: upstream owns this discipline the way it owns `doctrine/`
and `ops/`. Pull improvements to it; hand-edit it and the copy is yours to
merge by hand from then on, per `EXTENDING.md` section 6.*

*Purpose: any number a session writes into a record, quotes to the operator, or acts
on carries a discipline of its own, separate from whatever produced it. This skill
states that discipline once so every seat, every mission, and every fleet applies the
same bar to a measurement instead of inventing one per occasion.*

---

## 1. Why this skill exists

A wrong number is worse than no number, because a wrong number gets trusted. It
travels into a decision, a ruling, or an operator's own plan, and by the time it is
found wrong, whatever was built on it has to be found and unwound too. This skill is
the set of habits that keep a number honest between the moment it is produced and the
moment someone acts on it.

None of this replaces judgment about what to measure. It is the craft of measuring
whatever you have already decided matters, so that the number you hand up is one you
would stand behind if asked how you got it.

---

## 2. The record

A measurement is written down with what produced it before it is quoted anywhere
else. That means the instrument or method, the exact input, and the result, filed
together as one unit. A number separated from what produced it stops being a
measurement and becomes a claim someone has to take on faith.

Write the record at the moment you take the measurement, not afterward from memory.
A number reconstructed after the fact tends to acquire the shape the writer expected
it to have.

---

## 3. Where a number came from

A figure does not get to travel light. Before it moves from one session, seat, or
record to another, attach three things to it: what was measured, the thing it was
measured on, and when that happened. Strip that trail off and the number is no
longer safe to treat as settled once it has left the hands that produced it.

Distinguish three kinds of numeric claim, and never let one pass as another:

- **Measured.** Someone actually ran the thing and read the result.
- **Inferred.** Someone reasoned from logic or documentation without running
  anything. Sound reasoning still is not a measurement, and it is labelled as
  inferred wherever it travels.
- **Unchecked.** Nobody has looked. Say so plainly rather than letting silence read
  as confidence.

When a ratio or a percentage can be reported in more than one direction, report
whichever direction actually reveals the exposure, or give both. The same two
numbers can read as modest one way and severe the other; defaulting to the flatter
framing understates the real risk and is a form of dishonesty even when every digit
is correct.

---

## 4. One probe before escalating

An alarming finding earns one cheap observation that would settle it before anyone
is alarmed. Before a surprising or frightening result goes to the operator or into a
report, name the single cheapest check that would confirm or dissolve it, and run
that check first. Many alarming findings dissolve entirely on one cheap look, and an
alarming wrong result costs far more than a boring one, because it gets acted on
faster and more anxiously.

If a claim is later withdrawn, withdraw it to the same audience and at the same
visibility it was shared with, and keep the original claim visible alongside the
correction rather than quietly editing it away.

---

## 5. Reproduce before you announce

Reproduce a result in isolation before it leaves your hands. If two sources disagree
about something directly observable, go observe it yourself rather than reasoning
about which source seems more authoritative. Never apply a fix to something that has
not been confirmed broken; verify the problem exists in the current, real state
before spending any effort on it.

Do not assume that source code or a documented rule matching an expected pattern
means the running behavior actually matches it. Some pipelines silently fail to
apply what looks correct in source. Verify by observing the real output, not by
reading the logic that is supposed to produce it.

A bug found in a smaller or lower-stakes copy of something is often already present,
under a different name, wherever that code path is shared. After diagnosing any
defect, check whether a higher-stakes copy shares the path, and treat porting the fix
back as urgent when it does.

Work that is expensive if wrong is checked by someone other than whoever produced it,
every time. Name one reviewer, in the plan, who is responsible for re-deriving every
published figure from its own stated inputs, not for reading the producer's arithmetic
and nodding. That reviewer works from the sources, and having found one defect, sweeps
the whole deliverable for the same pattern rather than for the one string that
happened to be caught. A producer who marks their own work verified has not verified
it.

---

## 6. The rig itself can be what you're actually measuring

A clean result, a test that reports no difference, or a check that finds nothing, is
not evidence of correctness on its own. It is evidence only once the instrument has
been shown able to see the effect it is meant to catch. Break the control once, on
purpose, and confirm the instrument reports the failure; if it stays green with the
control broken, every earlier green it produced is unread, not passed. Two conditions
that return identical measurements are a flag on the instrument first, and only after
that a statement about the thing being measured.

A result that reproduces only alongside certain other operations, and not in
isolation, is telling you the harness itself, its sequencing or its shared state, is
the cause. It is not telling you anything about the thing you meant to test.

Before trusting a measured difference between two conditions, prove, inside the same
run, that the thing you meant to vary actually varied. Measure a claim on the real
scale and shape it is actually about; a simplified or co-located setup can look
identical whether or not the underlying claim is true. Build any fixture the same way
real data would arrive, and confirm a data store actually holds meaningful history
before trusting a plan or a recommendation it produces.

When two runs on identical inputs disagree by more than the effect you are trying to
detect, that disagreement is the finding. Do not average the two together;
investigate the instrument instead. Any benchmark that shares a busy resource with
other concurrent work either refuses to run while that resource is busy, or flags its
own result as suspect.

A check's logic can be correct while still pointed at the wrong scope, the wrong
baseline, or the wrong frame in time, and reading a stored label instead of the real
instant. Before trusting an automated check, name the frame it measures in, confirm
that is the frame the actual claim is about, and prove the answer by testing right at
the edge of that frame, where a wrong frame would visibly fail.

---

## 7. Bound the unknown before you ask the operator for anything

A single data point never confirms or refutes a claim about how something scales or
trends. A growth claim needs at least two measurements, with the second taken far
enough out that the underlying thing had a genuine reason to move.

When a decision depends on a fact nobody has measured yet, compute the outcome at
both ends of its plausible range before asking anyone anything. If the decision comes
out the same at both ends, the unknown does not matter and there is nothing to ask.
Measure, or ask, only when the outcome actually flips somewhere inside that range.
When you do publish a figure drawn from a range rather than a direct measurement,
say plainly which end of the range you used.

---

## 8. Don't recruit the operator as your test equipment

Do not hand the operator the job of taking a technical reading for you: opening
developer tools, wiring up their own device, capturing a trace, or relaying back
anything that only exists on their machine. If a report's final ask is for the
operator to go instrument something on their end, the report itself is broken, and
dressing that same ask up more gently does not fix it.

Build whatever you are diagnosing or fixing to hold correctly across the plausible
range of conditions instead of needing that one measurement. If something genuinely
cannot be validated without a reading only the operator can take, say so plainly as a
limitation of the work, rather than converting it into a question back to them.

---

## 9. Clock reads, never guessed timestamps

Every time written into a record comes from the clock at the moment of writing,
never estimated and never carried forward from memory. A guessed timestamp can drift
by hours, and every later reader treats the record as ground truth without
suspecting the drift.

Render a time shown to the operator in the operator's own timezone. A raw machine
timestamp read as local time can appear to be from the future, or otherwise confuse a
reader who is not tracking the offset. Keep raw machine time in logs and cross-record
references; convert it for anyone reading it as a wall-clock time.

---

## 15. Honest limits

- This discipline catches what gets measured and recorded. A number nobody thought to
  write down is invisible here, the same way an unrecorded decision is invisible to
  the cold-resume skill.
- None of this substitutes for deciding what is worth measuring in the first place.
  A rigorously provenanced measurement of the wrong thing is still the wrong thing.
- A probe that becomes routine stops being cheap. Revisit which checks still earn
  their place as the systems they watch change shape.

---

Read `reference.md` when the moment is specifically about cross-checking a fast or
cheap model's output against a stronger reader or ground truth (§11), or about
sanity-checking a demonstration's, benchmark's, or synthetic dataset's own internal
numbers before it ships (§12).

Source: ops/MEASUREMENT_CRAFT.md §1-9, §15 (moved into this skill 2026-09-16)
