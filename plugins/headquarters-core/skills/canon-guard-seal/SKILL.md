---
name: canon-guard-seal
description: Before sealing any deliverable through standards-guard in this org: load the rule files fresh, run fail-closed checks, log the seal, never override a hard fail.
---

# The standards-guard seal ritual

Invoke this before any deliverable clears the seal: standards-guard runs on
every deliverable a mission produces, before that mission can move to sealed.
Full governing procedure: `org/functions/standards-guard/CHARTER.md`, "Guard
procedure" - this skill restates it as a session-runnable ritual.

1. **Load the rule files fresh.** Read every rule file this function owns at
   the start of the check, never from an earlier read or a cached impression
   of what they said (this product ships five:
   `org/functions/standards-guard/rules/vocabulary.yaml`, `banned-terms.yaml`,
   `style.yaml`, and two further rule files covering the judged categories in
   step 3). A file that will not parse is a guard error: stop, fail closed,
   surface to the operator, log the error row.

2. **Run the deterministic fast-path pass** against the deliverable's full
   text: vocabulary reserved-term and banned-inversion matches, retired-term
   and cliche matches, and style's two deterministic rows. Record every hard
   hit but do not short-circuit - the deliverable still gets a full pass, so
   every finding arrives at once rather than one block per resubmission.

3. **Make exactly one judgment call**, at this product's building tier
   (`org/models.yml` duty `standards-guard-judge`), covering every judged rule
   across the loaded rule files together rather than one call per rule. The call
   must return strict structured output, one verdict object per rule. A
   response that is not valid structured output, or that omits any rule it was
   asked about, is a guard error: fail closed, and do not partial-credit the
   rules that did parse.

4. **Aggregate the findings.** Any hard fail - fast-path or judgment-side -
   blocks the seal. A soft fail warns but does not block; carry it forward
   into the mission's after-action note. A clean pass on every rule clears
   this gate for the deliverable - General Counsel and any other required gate
   still apply before the mission itself seals.

5. **Write the row.** Append exactly one entry to `ledgers/STANDARDS_LOG.md`,
   every time, regardless of outcome: date, the deliverable's path or mission
   identifier, the seat of origin, and each rule's verdict and severity. A
   guard-error row (from step 1 or step 3) takes its own shape, distinct
   enough that nobody mistakes it for a content verdict, stating plainly that
   this is the guard's deliberate fail-closed design.

6. **Surface a hard fail or a guard error to the operator, and stop.** This is
   the one rule in the whole procedure with no exception: when the guard
   blocks, the correct move is always to surface the block and wait - never
   override it, retry it silently, or reason past it to seal anyway. A
   stalled seal costs the operator a few minutes of attention; a violation
   that ships under a clean-looking verdict costs more, precisely because
   nobody saw it happen. A soft-only outcome seals normally, its warnings
   sitting in the log for the next after-action review.

Source: generalized from the operator's private doctrine (moved into this skill 2026-09-16)
