---
name: performance-run
description: Use when starting a performance run or audit: confirm the trigger applies, confirm the symptom with real users first, follow the fixed order of measurement, then judge worth-building.
---

# Performance Run

Measurement discipline comes first: most real performance errors turn out to
be measurement errors, not engineering ones. This skill governs how a
performance run gets started, how a symptom gets confirmed, the order
measurements get taken in, and how a finding gets judged worth building.

## §3.1 Trigger

A performance run happens when one of three things is true, and not
otherwise:

1. **A person who uses the surface reports a symptom.** This is the good
   trigger.
2. **A growth dimension crossed a value someone predicted would hurt**, and
   the prediction is on file with its arithmetic.
3. **Periodic**, at a standing review cadence, scoped to re-checking known
   numbers rather than hunting for new findings.

A run triggered by none of these produces a list nobody should build from.

## §3.2 Confirm the symptom with the people who use the surface, before optimizing

**Hard rule.** Before a single line is optimized, the symptom is confirmed
with the humans on that surface: which screen, which tap, what were they
doing, how often, and does it happen on their own device. Two failures this
rule exists to prevent:

- A slow demo number wore a venture's name for weeks because nobody asked
  whether anyone actually using that surface had ever felt it.
- A findings register can be entirely correct and entirely unbuildable,
  because "correct" and "someone is waiting" are different claims.

**And the operator is not an instrument.** Never ask them to run a profiler,
read a header, or time a request on their own phone. A report that ends by
asking them to instrument their own device is malformed. Ask what they FELT
and when; the seat gets the number.

## §3.3 Order of measurement

Cheapest and most re-ranking first. Do not proceed down this list until the
step above is answered.

1. **The topology facts.** Read `Content-Encoding` on one real response.
   Time one app-to-database round trip in the real deployment. These two
   numbers re-rank more of a findings list than any amount of code reading.
2. **The real row counts.** One read-only `SELECT COUNT(*)` per table any
   finding depends on. Replaces every ASSUMED scale figure with a MEASURED
   one, and kills fabricated ones.
3. **Server render time and database time**, on the actual surface, at the
   actual data volume, with a control that varies the dimension the claim is
   about.
4. **Query count**, filtered to the SPECIFIC query signature, asserted as an
   exact number, with the arms proven to differ.
5. **Wire bytes**, both compressed and uncompressed, on the real endpoint.
6. **Client-side cost** in a real browser on a real device: script time,
   render/diff time, paint. Often the least-instrumented step, and therefore
   commonly the largest blind spot.

## §3.5 Deciding whether a finding is worth building

A finding is worth building when it clears **all four**:

1. **It has file:line evidence.**
2. **It can name its own falsifying measurement,** with a control that can
   fail. A finding that cannot is not a finding; drop it.
3. **It has an honest expected win stated in the units the user feels,** at
   today's real volume, or an explicit "zero today, growth only" label.
4. **Its risk is proportionate to that win.** Additive indexes and swaps to
   existing parity-tested twins clear this on hygiene grounds alone. Shared
   write-path predicates, live payment surfaces, transactional-mail
   selection, and anything gated by a static gate file do not, until
   something is actually slow.

**Three standing rules on top:**

- **A refuted finding is a finding.** Record it with why it died, in a
  refuted-sub-claims table — it stops someone re-raising it.
- **A green audit honestly reported is worth more than a manufactured
  list.** If the surface is fast, the first line of the report says the
  surface is fast.
- **Findings that fire on one user action claim shares of ONE budget.**
  Their counts ADD. Verify them together, and a fix that does not restore
  the whole delta has not failed.

Source: generalized from the operator's private doctrine, §3.1, §3.2, §3.3,
§3.5 (moved into this skill 2026-09-16).
