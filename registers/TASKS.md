<!-- file-class: PERSONAL -->

# TASKS - the cross-project task ledger

*Owned by the Operations seat (`org/seats/operations/CHARTER.md`).
Append-only: one H2 dated section per task, newest on top. When a task's
status changes, append a new dated section referencing the same task rather
than editing the old one - the old section is the history of how it got
here, the newest section is the current truth.*

*Status values, exactly these five words:*

- ***proposed*** - *named as work, not yet ruled on.*
- ***ruled*** - *you have approved it; it has not started.*
- ***in-flight*** - *a mission packet exists and work is happening under it.*
- ***blocked*** - *cannot proceed without something only you can supply; also
  filed on `registers/BLOCKED_ON_OPERATOR.md`, cross-linked by task name so
  the two registers never drift apart.*
- ***sealed*** - *done, passed its gates, nothing further expected.*

*Cross-reference `registers/PROJECTS.md` for which project a task belongs to,
and `registers/BLOCKED_ON_OPERATOR.md` for the operator-facing subset of what
is blocked here. A mission packet's own `STATE.md` (see
`ops/OPERABILITY.md` §4) is the authoritative live account of an in-flight
task; this register's row is a pointer to it, not a replacement for reading
it.*

---

No tasks recorded yet. Add the first one in this shape - copy it, fill every
bracket, delete this line:

## [DATE] - [Task name] - [one-line description of the work]

**Status:** proposed. **Owner:** [seat name]. **Project:** [name, from
`registers/PROJECTS.md`]. **Packet:** [path, once a mission exists - e.g.
`missions/<project>/<task-slug>/PACKET.md`].
