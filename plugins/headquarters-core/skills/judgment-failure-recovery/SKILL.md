---
name: judgment-failure-recovery
description: Something just broke: inventory the output directory before forming a theory, salvage the gap not the whole, commit what survived before recovering.
---

# Judgment: when something breaks

Failure is ordinary and mostly cheap if it is handled in the right order. The order
matters more than the diagnosis.

**Inventory the output directory before forming any theory about what went wrong.**
Agents write their files before they return, so a run that ends in an error has
usually left most of its work sitting there. Look at what is on disk first. A run
reported as failed that produced four of its six files is not a failure, it is a run
with two gaps, and treating it as a failure means paying for four files twice.

**Salvage before rebuilding.** Once you know what actually landed, author a short run
aimed at exactly what is missing. Re-running the whole thing is the reflex, and it is
almost always the most expensive available option. Inventory, then write for the gap.

**Commit what survived before attempting recovery.** The salvage is state; a recovery
attempt is a new thing that can also fail. Landing the good files first means the next
attempt cannot take them with it. This is the same continuous-durability rule the
checkpoint-discipline skill sets, applied at the moment it is most tempting to skip.

**A second identical attempt is not a recovery.** Running the same thing into the same
failure spends the meter to learn nothing. Change one named variable, or stop and take
the problem to the operator.

**Patch the pattern, not the two prompts.** A pair of failed agents that both asked
for a table with a column the source data could not populate will both stall trying to
invent it, for the same one reason. Patching those two instructions fixes today.
Writing the pattern into the fleet doctrine, and typing the lesson into the owning
seat's `LEDGER.md` the way the Agent Quality function expects, is what makes it not
happen again to a seat that has never heard of this run.

**On a defect report, find the root cause before fixing.** Decide explicitly whether
the failure is a wrong-source problem - the data feeding the work was bad - or a
missing-write problem - something that should have been recorded never was. The fix
differs for each, and a patch aimed at the wrong one looks like a fix while leaving the
real cause untouched.

Source: ops/JUDGMENT_CRAFT.md §10 (When something breaks) (moved into this skill 2026-09-16)
