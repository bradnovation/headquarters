# Heartbeat - why the cycle marker exists

None of section 5's marker discipline in the heartbeat skill is theoretical caution
dressed up as procedure. Routines built exactly this way — resume-only and running
on a clock — have, in real operation, fired while a live session was already
mid-task on the very same piece of work, and the two runs collided: duplicate
output, a commit history that briefly disagreed with itself, spend that should have
counted once counted twice. That is not a scenario this doctrine is guessing might
someday happen. It is the entire reason the marker exists, the entire reason it gets
checked before anything else in the cycle runs, and the entire reason this routine
ships with `armed: false` rather than shipping ready to fire and trusting everyone
to remember to turn it off.

A routine that has never once been allowed to race a live session has never had
occasion to prove its guard actually works. Read that as a reason to keep the guard
exactly as strict as it is, never as a reason it has earned the right to be trimmed.

Source: ops/HEARTBEAT.md §6 (moved into this skill 2026-09-16)
