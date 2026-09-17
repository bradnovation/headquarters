# Measurement - reference

Read this file when the moment at hand is one of the two below. Everything else
the measurement discipline requires is in `SKILL.md`.

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

Source: ops/MEASUREMENT_CRAFT.md §11, §12 (moved into this skill 2026-09-16)
