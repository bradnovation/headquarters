# Multi-session - durability commits for a running record, batched

The churn this section answers is a specific one, not checkpoint commits in
general: a single running record - a HANDOFF top entry, a status line,
anything section 17 says gets pointed at rather than copied - gets
hand-edited many times over a session, and each edit becomes its own commit.
Measured on one busy day: a HANDOFF top entry rewritten 32 times, each
rewrite a full paragraph resent through the same edit, for one seat's
ordinary work. That is not the session-park skill's durability discipline
across a session wall; it is the same fact restated over and over.

**For that class of commit only - a still-being-drafted record accumulating
its own incremental edits - batch: at most two an hour**, unless a session
wall is close enough that the next batch point might not be reached before it
lands - in that case, commit what is durable now rather than holding it for
the batch window. Append the dated one-line update (section 19's shape) as it
happens, and let the commit that carries it wait for the batch window;
nothing is lost in the meantime because the line is already written to disk,
only not yet committed.

**This never defers a checkpoint commit for a genuine, distinct material
point** - a ruling landed, a phase completed, a spend authorised, a finding
that changes what happens next - as the checkpoint-discipline skill's
sections 2 and 3 already require: write the file, then commit it, on that
point's own occurrence, the same as the session-park skill's own durability
discipline already requires for a session wall. A session that clears three
real material points in one hour commits three times in that hour; the
two-per-hour figure caps how often the same record gets re-committed for
restating itself, not how many different things a session is allowed to get
durably right.

Source: ops/MULTI-SESSION.md §18 (moved into this skill 2026-09-16)
