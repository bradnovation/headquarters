# MEASUREMENT CRAFT - the discipline for any number a session reports or acts on
<!-- file-class: DOCTRINE -->

*This file ships with the product and is upstream-pullable. Edit it
only if you intend to own your own copy of it forever.*

*Purpose: any number a session writes into a record, quotes to the operator, or acts
on carries a discipline of its own, separate from whatever produced it. This file
states that discipline once so every seat, every mission, and every fleet applies the
same bar to a measurement instead of inventing one per occasion.*

---

## 1. Why this file exists

A wrong number is worse than no number, because a wrong number gets trusted. It
travels into a decision, a ruling, or an operator's own plan, and by the time it is
found wrong, whatever was built on it has to be found and unwound too. This file is
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

## 10. Testing is measurement too

A test is a measurement of behavior, and it earns the same discipline as any other
number.

- A test deliberately built to fail first, to prove a defect exists before it is
  fixed, must confirm that its intended failure actually occurred, not merely that
  some failure happened. A red-first test that silently exercises the wrong path is
  more dangerous than having no such test.
- A test or a guard whose output would look the same whether or not the thing it
  checks for is true is not checking anything. Before trusting a negative result, ask
  what the check would have shown if the thing it rules out were actually present. A
  ruling-out earns more scrutiny than a ruling-in, because it removes something from
  everyone's future attention.
- A guard or safety interlock is tested as hard as the thing it protects: every
  branch fired, including the refused path under genuine concurrent use, not merely
  written and assumed to work. Decide explicitly who runs the check and how often as
  part of designing it; a check nobody ever schedules protects nothing, however well
  it was designed, and a safeguard verified once at build time is not verified going
  forward.
- A test that hardcodes a fixed date, timestamp, or specific record identifiers from
  a one-off setup will silently break, or falsely pass, as time moves forward. Write
  dates relative to the moment the test runs, and have a test create or look up its
  own fixtures. A test that starts passing again only because time has moved past a
  hardcoded date is not evidence anything was actually fixed.
- Set pass and fail criteria for a review by deriving them fresh from the actual
  specification or code at hand, never by recalling what a similar-looking prior
  review used. A wrong criterion is more dangerous than a wrong command, because it
  succeeds and gets believed.
- A green, passing suite proves nothing about a path it never exercises. Require at
  least one true end-to-end execution per distinct action, and do a real manual
  walkthrough of any visible or structural change before it ships, however large the
  green suite behind it. "Verified in code" and "verified live" are different claims;
  before anything a person will act on goes out, run one more human-verifiable live
  check rather than trusting that a code-level fix implies the visible behavior
  changed. Treat a rollback that a walkthrough triggers as the process working, not
  as a failure of whoever built the change.
- A merge or a re-pin reporting no conflicts is not proof the result compiles or
  behaves correctly. After any merge, run a full build and test pass and specifically
  re-run the check for every previously fixed defect; a clean merge can silently
  resurrect an old bug by reintroducing code that shadows a prior fix.
- Whenever you quote a test result, state whatever special environment variables,
  flags, or stubbed configuration it ran under, or say none. A suite that silently
  inherits values from whoever is running it can have its real coverage reshaped, or
  reach a real external service, without anyone noticing. Pin test environment values
  explicitly.

---

## 11. Cross-check lower-tier output

Before fully trusting a fast or cheap model on a genuinely hard judgment task,
spot-check its output against a stronger reader or against ground truth on one hard
example early in the run, not after the whole batch finishes. A systematic error
caught early costs a fraction of what it costs once the whole run has spent its
budget on the same mistake.

Any claim a lower-tier or spawned agent produces (a quote, a citation, a fact about
whether something already exists) is cross-checked against the live or primary
source by default before it reaches a person or a decision. Fabricated quotes and
citations from a lower-tier pass are common enough to expect as routine, not as an
exceptional failure.

---

## 12. Numbers that have to survive a sanity check

A demonstration, a benchmark, or a synthetic dataset's own internal numbers must
survive quick mental arithmetic by someone who actually works in that field. If an
expert would spot the ratios as implausible on sight, the artifact undermines its own
story no matter how polished it otherwise looks.

---

## 13. What a harness's token figure counts, and what a meter charges

A running spend figure a harness shows you and the amount a subscription meter
actually charges are not the same measurement, and confusing them produces false
alarms and false confidence in both directions.

The rough shape: a request's cost is the context carried into it, multiplied by the
number of requests, multiplied by the model's price per unit of context. Under a
fleet, the model pinned to each role is usually the factor that moves the total, far
more than the number of requests does. A harness's own reported figure for a run is
typically dominated by cache-write input rather than freshly generated output, so
comparing two figures across runs or periods only means something when the units
match.

The full reasoning behind this, and the budget-guard consequences of it, live in
`ops/FLEET_CRAFT.md` section 9. This section exists so a session reading measurement
doctrine does not have to already know to look there.

---

## 14. The usage tally instrument

`scripts/usage-meter-tally.py` is a read-only instrument that sums the API responses
recorded in the local transcripts, grouped by week, by model family, and by lane, and
prices them against a list-price table so different periods compare on one scale.

Run it whenever the meter reading and the amount of work actually done seem to
disagree, or before reporting a savings figure from a cheaper-model policy that
someone downstream might rely on. Read the ratios it produces, not a single absolute
figure, since the provider's own dashboard weighting is theirs and may not match the
comparison you are trying to make.

---

## 15. Honest limits

- This discipline catches what gets measured and recorded. A number nobody thought to
  write down is invisible here, the same way an unrecorded decision is invisible to
  `ops/COLD_RESUME.md`.
- None of this substitutes for deciding what is worth measuring in the first place.
  A rigorously provenanced measurement of the wrong thing is still the wrong thing.
- A probe that becomes routine stops being cheap. Revisit which checks still earn
  their place as the systems they watch change shape.
