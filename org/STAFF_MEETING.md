# STAFF_MEETING - the convening protocol
<!-- file-class: DOCTRINE -->

*How your intent becomes a debated plan, how a debated plan becomes your ruling, and
how your ruling becomes mission packets that agents execute. This file is
self-contained. A reader who has only this file can convene and run a full meeting
end to end; the cross-references in §10 are pointers, not prerequisites.*

---

## 1. What a Staff Meeting is

A Staff Meeting is the ritual this organization uses to turn a new intent into work
that is safe to hand to agents. It exists because the expensive mistakes are almost
never execution mistakes. They are plan mistakes: the wrong thing built well, a
number nobody re-derived, a question the plan quietly answered on your behalf.

Four properties define it.

**Disk, not conversation, is where a meeting actually happens.** Every step of it
lands in a file at a fixed path. Two things follow from that: a convening can be
abandoned halfway and picked up days later by a session that remembers none of the
first half, and a year on you can still read why a decision went the way it did and
who argued against it.

**A second intent gets a second meeting.** The intent on the table is chaired through
to one ruling and no further, so anything that surfaces alongside it waits for a
convening of its own. Widening the agenda mid-debate is how a meeting ends up with a
plan that fits neither intent well.

**Once a packet is written, nothing inside it is up for debate again.** Executing
agents run the charge as ruled; they do not reopen it. That makes this ritual the last
room in the system where a decision is genuinely contestable, and it is also where
your rulings come from: apart from the status moves a mission logs against itself,
nothing else in this system produces one.

**A meeting cannot waive a gate.** The consequence gates in the constitution
(`CLAUDE.md`) bind every meeting, every plan, and every ruling below your own word.
In particular: no plan this ritual produces contains a send step or a deploy step,
because no send path and no deploy path exist in this system at all. A meeting can
rule that a message should be drafted and put in your hands. It cannot rule that the
message goes out. If a proposed plan needs a gate relaxed to work, the meeting stops
and surfaces the conflict to you instead of routing around it.

**When to convene one.** New intent that has real consequences, more than one
defensible approach, or money, liability, or public exposure attached. **When not
to.** Mechanical work with an obvious method and a small blast radius. Convening a
meeting for a ten-minute task is a real cost with no return; so is skipping one for a
decision you will live with for a year. When in doubt, ask for the meeting - the
ritual is cheap next to the class of mistake it catches.

---

## 2. Directory layout

Every meeting lives at `meetings/<date>-<slug>/`, in exactly this shape:

```
meetings/<date>-<slug>/
  00-intent.md      your intent, verbatim (or transcribed and marked so); names the
                    convened domain seats and the standing advisory attendees on
                    two separate lines
  01-briefs/        one position brief per convened seat and per advisory function,
                    written independently and in parallel
  02-debate.md      the chair's synthesis: agreements, live disagreements, pressure
                    tests. Never smoothed.
  03-plan.md        the proposed plan: missions, owners, cost envelope, and the
                    rulings-needed table with a type and a recommended default on
                    every row
  04-ruling.md      your word. The only file a human writes.
  05-missions/      one packet per mission, written once you have ruled
```

Nothing on this list is optional, and none of these names change. The numbering is the
order of operations; a stranger reading the directory should be able to follow the
decision from raw intent to fanned packet without asking anyone what happened.

`05-missions/` does not exist until `04-ruling.md` exists. However finished a plan
reads, it has produced no mission until your word sits above it in the ruling file.

---

## 3. The six files, one at a time

### 3.1 `00-intent.md` - your words, kept as your words

This file is your intent written down as you gave it. If you typed it into the file
yourself, it stands as is. If it came from a chat message, a voice note, or a live
conversation, the chair transcribes it and marks the top of the file:
`(transcribed from chat, verbatim, <date>)`. It is never paraphrased into the chair's
own words without that flag.

The reason is narrow and load-bearing: every downstream file interprets this one. If
the intent is already an interpretation, nobody downstream can tell where your
thinking ended and the chair's began. Transcribe first, interpret second, and put the
interpretation in a clearly separate section headed as the chair's notes.

`00-intent.md` also carries, below your words:

- **The design constraints the intent itself names.** If you said the thing must be
  public, or must be free, or must work without a particular dependency, those are
  constraints - the briefs argue *how*, not *whether*. Listing them here stops a seat
  from spending its brief relitigating something you already settled.
- **Which domain seats are convened, and why** (§5).
- **Which standing advisory attendees are attached** - on a separate line, because
  they need no justification and should not read as a convening decision.
- **The two board reads** from the convening checklist (§7), stated plainly even when
  the answer is "nothing relevant."

### 3.2 `01-briefs/` - independent positions, written in parallel

One brief per convened domain seat, plus one per standing advisory function. They are
written **in parallel and independently**: a seat does not read another seat's brief
before writing its own.

This is the single most important mechanic in the ritual. Briefs written in sequence
converge - the second author reads the first and unconsciously argues inside its
frame. Independence is what makes the disagreement in `02-debate.md` real
disagreement rather than one seat echoing another it already read. If you take one
thing from this file into your own practice, take this.

Each brief follows the same four-part shape, which makes them comparable:

1. **POSITION** - what this seat would actually do, in its own voice and its own
   interest, with the real trade-off named rather than hidden.
2. **WHAT THIS SEAT NEEDS** - from you, or from another seat, before it can proceed.
3. **RISKS** - including the risks to its own preferred position. A brief that lists
   only the risks of the alternatives is advocacy, not a brief.
4. **RULINGS WORTH ASKING** - the open questions this seat cannot settle alone, each
   typed `[fact]` or `[judgment]` per §4, each with a recommended default.

A brief from an advisory **function** is marked advisory at the top of the file. It
carries no agenda of its own and frames its position as gates and constraints - what
would block a seal, what provenance or metadata it needs - rather than as a plan for
the intent.

**Execution note.** Briefs are the natural place to fan out to parallel agents, and
they run at the building tier per `org/models.yml`. Two rules apply. First, project
the cost before launching: estimated tokens, estimated wall-clock, and your current
usage headroom, stated at the launch moment, not reconstructed afterward. Second,
whatever tier you have designated as interactive-only - the seat you talk to
directly - never joins a fanned-out run. That rule is about cost and about
supervision, and it holds no matter which model happens to occupy that seat.

### 3.3 `02-debate.md` - the chair's synthesis, never smoothed

Written after all briefs land, by the chair, and it must surface three things:

- **Agreements** - where independent briefs converged without prompting. This is
  strong evidence, precisely because the authors could not see each other.
- **Live disagreements** - named plainly and attributed to the seat that holds each
  position. If one seat wants to ship before the underlying rework lands and another
  says the rework must come first, both positions appear here by name, and the
  tension is carried forward into `03-plan.md` as a rulings-table row. It is not
  resolved by the chair quietly picking a side.
- **Pressure tests** - the chair's own probing of the weakest point in each position,
  stated as questions and challenges, and left unanswered on the seats' behalf.

**Never smooth.** A debate document that reads as unanimous when the briefs were not
is a defect in the ritual, not a convenience. The smoothing instinct is strong and it
is always wrong here: it converts information you needed into prose you enjoyed
reading. If the chair genuinely believes one side is right, that belief belongs in
`03-plan.md` as a recommended default you can overrule - not in `02-debate.md` as a
disappeared disagreement.

### 3.4 `03-plan.md` - the proposed plan

Drafted by the chair at the reasoning tier, because this is the document whose errors
are most expensive. It contains:

- **The missions** the intent fans out into, each with **one owning seat**. Shared
  ownership means nobody owns it.
- **The sequencing** - what runs first, what gates on what, what waits on you.
- **The cost envelope** - a projection per phase, a total, and a hard cap. Every
  number is either derived in the document or labeled as a judgment call with the
  chair's name on it. An unlabeled invented number is a defect; it reads to you like
  an estimate when it is a guess.
- **The rulings-needed table** - every open question the plan cannot resolve on its
  own, each row typed and defaulted per §4.
- **A launch discipline line** for any fan-out the plan proposes: projected tokens,
  projected wall-clock, and required usage headroom. Long runs do not launch into
  thin headroom; they park to the next window.

A plan that hides a question is worse than a plan that asks too many. The table is
where the plan admits what it does not know.

### 3.5 `04-ruling.md` - your word, and the only file a human writes

You rule here. Everything else in this repository can be produced by an agent; this
file cannot. That is deliberate - it is the structural guarantee that the system
never decides on its own behalf.

You can write directly in the file, or rule in chat, in which case the chair
transcribes your words into this file verbatim and marks it so: `(chat ruling,
transcribed verbatim, <date>)`. No session paraphrases a ruling. Where the chair must
interpret a terse ruling to act on it, the interpretation goes in a clearly separate
section - "chair's interpretation record" - mapped row by row to the plan, so that a
misreading is visible and correctable rather than buried in the work.

The same ruling replicates to `DECISIONS.md` in the same session it is given, as the
next numbered entry, dated. A ruling that lives only in `04-ruling.md` is not fully
recorded: the meeting directory is where the decision was made, and `DECISIONS.md` is
where every session goes to find out what the standing rules are.

### 3.6 `05-missions/` - the fan-out

Populated only after `04-ruling.md` exists. Each mission the plan named - as ruled,
including any amendment you made in the ruling - gets a packet fanned out per §8.

---

## 4. Row typing: `[fact]` vs `[judgment]`, and proceed-on-default

This is the mechanic that makes a single "go" from you safe. Read it once carefully;
everything else in the ritual is scaffolding around it.

Every row in the rulings table is typed as exactly one of two kinds.

**`[fact]` rows ask for information only you hold.** Your actual floor price. Which
client relationship is fragile. Whether you have the capacity next month. Whether
that contract was ever signed. No amount of reasoning produces a fact you have not
supplied - an agent that "defaults" a fact is fabricating it.

So a `[fact]` row's recommended default is never an answer. It is always the **safe
provisional behavior**: draft against a clearly flagged placeholder, and publish
nothing, send nothing, spend nothing, and commit nothing that depends on the fact
until you supply it. The work continues; the exposure does not.

**`[judgment]` rows carry a real recommendation the chair is willing to stand
behind.** Approach, sequencing, structure, trade-offs - questions where the reasoning
is on the page and you are being asked to accept or overrule it. Here the default is
the chair's actual position, argued for, and proceeding on it is exactly what it
sounds like.

**Proceed-on-default** means the plan states, up front, that it assumes every row's
recommended default. Consequently you have three ways to rule and all three are
cheap: say "go" and approve the whole table at its defaults; rule row by row; or
overrule individual rows and accept the rest. The typing is what makes "go" safe -
you are trusting the chair's judgment on judgment calls only, never letting it invent
a fact about your own business.

A worked example of two rows, one of each kind:

| # | Type | Ask | Recommended default |
|---|---|---|---|
| 1 | `[judgment]` | Ship the new service page before the pricing rework, or after? | **Before.** The page earns nothing sitting in draft, and pricing can be revised under it later without re-authoring the page. |
| 2 | `[fact]` | What is the lowest price you will actually accept for this service? | Safe provisional: draft the page against a clearly flagged placeholder. Nothing publishes and no quote is prepared until you supply the number. |

**A rulings table with an untyped row, or a row with no recommended default, is an
incomplete plan.** Send it back rather than ruling on it.

**The characteristic failure, named so you can watch for it:** a chair converts a
`[fact]` into a `[judgment]` so the plan can keep moving. It looks like diligence -
the row now has a confident recommendation - and it is the single most dangerous
thing that happens in this ritual, because you approve it believing a real question
was answered when a real question was invented. The adversarial pass in §6 exists
substantially to catch this, and it does catch it.

---

## 5. Who is convened

**The Chief of Staff convenes and chairs.** The chair's job is procedural: convene
the right seats, protect brief independence, synthesize honestly, draft the plan, ask
for the ruling, fan the packets. The chair holds no domain agenda of its own in a
meeting it chairs, except where the intent genuinely touches its own charter - and
when that happens, it is stated in `00-intent.md` as a dual role.

**Convene only the domain seats the intent actually touches.** A meeting about a
technical backlog convenes the engineering and marketing-side seats; it does not need
the seat that owns outbound relationships. Over-convening is its own failure mode:
more briefs, diluted debate, real cost, and a chair tempted to smooth because there
are now nine positions to reconcile. The chair states in `00-intent.md` which domain
seats are convened and why.

**Three duties attend every meeting whether or not the intent mentions them.** They
are standing attendees because a plan that ignored any of the three would be one
nobody can seal, fund, or track:

- **standards-guard** decides whether finished work is classified right and reads
  consistently, and nothing seals without that verdict;
- **Finance** carries the plan's cost envelope: the projection, the total, and the cap
  the work may not exceed;
- **Operations** maintains the registers that any convening ends up disturbing.

They attend by right, so `00-intent.md` justifies none of them the way it has to
justify each domain seat. Write the three on a line of their own, so that a meeting
with two domain seats and five briefs total reads as the ordinary shape rather than
as a chair who over-convened.

**Seat names are defaults, not law.** Rename any seat to match how you actually think
about your organization. The ritual keys on the *duty* - who gates, who owns spend,
who owns the registers - never on the label. Renaming is a documented edit to
`org/ORG_CHART.md` and the seat's own charter, and nothing in this protocol breaks
when you do it.

---

## 6. The pre-ruling adversarial pass

`03-plan.md` does not reach you straight from the chair. It goes first to a set of
agents whose entire charge is to find what is wrong with it. Run them at the building
tier, keep the number small, and hand each one the whole document set: intent, every
brief, the debate, the plan. None of them is asked whether the plan is any good.

**Three skeptics is the floor, one question each:**

1. **Fidelity.** Does the plan still say what the seats said? A position a brief
   actually took should survive into the plan intact or be visibly overruled, never
   trimmed or softened on the way through. Watch for a live disagreement that
   resolved itself somewhere between `02-debate.md` and `03-plan.md`, and for a
   `[fact]` row that has quietly become a `[judgment]` row. Here the briefs are the
   evidence and the plan is the claim on trial.
2. **Numbers and coverage.** Rebuild every figure in the plan from its inputs.
   Anything that will not rebuild is relabeled as the chair's judgment call or
   struck. Then run the check the other way around: every deliverable the plan
   promises needs a named vehicle that produces it, and every phase the plan names
   needs an output.
3. **Gates.** Test the plan against the consequence gates and against the standing
   rulings in `DECISIONS.md`. Look for a step that assumes an authority nobody handed
   over, and for anything scheduled to happen before your ruling makes it legitimate.

**Every finding carries a severity: BLOCKING, MATERIAL, or MINOR.** The fix lands in
the plan, or in `02-debate.md` where the defect belongs there instead, with the
finding named at the spot it was applied so a later reader can see both the edit and
its cause. **Nothing BLOCKING survives to the ruling ask.** Attaching a known
blocking defect to the plan as a caveat does not manage the problem; it moves the
problem to you.

What the pass costs is small against a plan and negligible against a build aimed at
the wrong thing. The honest argument for it is not that seats write sloppy briefs.
It is that every other participant in this ritual gets read by somebody, and the
chair does not, so a chair's error arrives on your desk wearing the same finished
surface as the rest of the document.

---

## 7. The convening checklist

The chair walks this list at the start of every Staff Meeting, before writing
`00-intent.md`:

1. **Read the blocked-on-operator board** (`registers/BLOCKED_ON_OPERATOR.md`).
   Anything already waiting on you that touches this intent's domain belongs in the
   agenda - as context for the briefs, or as a row in the rulings table. Two
   unrelated asks arriving at you separately is a failure of this step.
2. **Read the innovation inbox** (`inbox/INNOVATION.md`). Ranked proposals surface
   here and only here; they never interrupt you. If a banked proposal is relevant to
   the intent at hand, it enters the agenda through this reading.
3. **State which seats are convened, and why**, in `00-intent.md`. Convene only what
   the intent touches. List the standing advisory attendees separately.
4. **Project the cost before any fan-out.** Estimated tokens, estimated wall-clock,
   and your current usage headroom, stated at the launch moment. Long runs do not
   launch into thin headroom; they park to the next window. This applies to the
   briefs fleet and to the adversarial pass alike.
5. **Run the ritual**: briefs in parallel and independent → debate synthesized
   honestly → plan with a typed rulings table at recommended defaults → adversarial
   pass with blocking findings resolved → your ruling → ruling replicated to
   `DECISIONS.md` → packets fanned to `05-missions/` and `missions/<slug>/`.
6. **Close the session properly.** Update `HANDOFF.md` and `SESSION_LOG.md` before
   the session's final commit, never after. The meeting is not parked until
   `HANDOFF.md` says where it landed - ruled and fanned out, or parked mid-debate
   awaiting your word. *Exception:* when the meeting runs as a fan-out beneath an
   orchestrating session, the orchestrator may seal `HANDOFF.md` instead of the
   chair. The chair still writes `SESSION_LOG.md` unconditionally and states there,
   in plain words, that `HANDOFF.md` was deliberately left for the orchestrator - so
   that a successor session does not read the gap as a dropped close.

A meeting that skips any of these six steps has not actually convened, even if every
file from `00-intent.md` to `05-missions/` exists on disk.

---

## 8. Mission packet discipline

A mission packet is the unit of work this ritual produces. Its discipline is what
keeps executing agents from drifting away from what you ruled.

**Immutable once fanned out.** A packet, once written from `04-ruling.md`, is a
snapshot of the charge as ruled. Nothing inside `missions/<slug>/PACKET.md` changes
by silent edit. If the packet is wrong, that is a fact to record, not a file to
quietly fix.

**Changed only by your redirect, and the change is itself recorded.** If you change
your mind mid-mission, a dated entry is appended to the mission's `STATE.md` noting
the redirect, what changed, and why - plus a `DECISIONS.md` entry if the redirect
amounts to a new standing rule. The original `PACKET.md` is never rewritten in place.
Small redirects supersede specific lines with a visible amendment block; a large
enough change closes the mission and opens a new one that references it.

**Per-mission `STATE.md` tracks a status machine:**

```
proposed -> ruled -> in-flight -> review -> sealed
```

- `proposed` - the mission exists in `03-plan.md` but has not been ruled.
- `ruled` - your ruling approved it and the packet has been fanned out, but no work
  has started.
- `in-flight` - a seat is actively executing against the packet.
- `review` - work is done and awaiting the classification-and-consistency gate (and
  General Counsel, if money or liability is present) before it can seal.
- `sealed` - the gates passed; the mission is closed.

`STATE.md` never skips a state and never moves backward except through a logged
redirect. Each transition is a dated line, newest on top. The header of `STATE.md`
also carries machine-readable status so an automated resume can tell, without reading
prose, whether a mission is live and whether it needs a particular environment to
continue.

**Per-mission `FINDINGS.md` is separate from `STATE.md`, deliberately.** `STATE.md`
is bookkeeping: where the mission is, what moved it, what it is waiting on.
`FINDINGS.md` is substance: what the mission actually discovered, produced, or
decided along the way. Keeping them apart is what lets a successor session read the
substance in one file without reconstructing it from a status log, and lets a status
check stay cheap. The moment findings start appearing in `STATE.md`, both files stop
being useful.

**Sealing.** A mission seals only after the classification-and-consistency gate
passes, and after General Counsel passes too where money or liability is present.
Sealing a mission that has not cleared its gates is a protocol violation regardless
of how confident the owning seat is in the work. On seal:

- Anything only you can unblock is posted to `registers/BLOCKED_ON_OPERATOR.md`
  **the moment it exists**, not held until the mission closes. A blocker discovered
  on day one and surfaced on day nine cost you eight days.
- The owning seat appends a short after-action note to its own ledger: what the
  charter got right, and where the agent fought its brief. This is how charters
  improve from lived sessions instead of staying as written on day one.

---

## 9. Running your first meeting

If this is your first time, work straight down this list. Nothing here requires
reading another file.

1. Create `meetings/<today>-<short-slug>/`.
2. Write `00-intent.md`. Paste your own words at the top under a verbatim marker.
   Below them, list the constraints you already consider settled.
3. Walk the checklist in §7. Read your blocked-on-operator board and your innovation
   inbox. Note both reads in `00-intent.md`, even if the answer is "nothing
   relevant."
4. Decide which seats the intent genuinely touches. Two or three is normal. Write
   them in `00-intent.md` with one line each on why. On a separate line, note that
   the three standing advisory attendees are attached by default.
5. Project the cost of the briefs run and state it. Then write the briefs - in
   parallel, independently, one file per attendee in `01-briefs/`, each following the
   four-part shape in §3.2. If you are running them as parallel agents, none of them
   may see another's output.
6. Write `02-debate.md` yourself, or have the chair seat write it. List agreements,
   then live disagreements attributed by name, then your own pressure tests on the
   weakest points. Resist every urge to reconcile.
7. Write `03-plan.md`: the missions, one owner each, the sequencing, the cost
   envelope, and the rulings table with a type and a recommended default on every
   single row.
8. Run the adversarial pass from §6 - fidelity, numbers, gates. Patch what it finds,
   citing each finding at the patch site. Resolve every BLOCKING finding.
9. Read the plan. Rule in `04-ruling.md` - "go" to take the table at its defaults, or
   row by row. Replicate the ruling to `DECISIONS.md` in the same session.
10. Fan the packets into `05-missions/` and `missions/<slug>/`, each with
    `PACKET.md`, `STATE.md` at `ruled`, and `FINDINGS.md`.
11. Update `HANDOFF.md` and `SESSION_LOG.md`, then commit.

**The smallest honest meeting** is two domain seats plus the three standing advisory
attendees: five briefs, one debate, one plan, one ruling. That is not a stripped-down
version of the ritual - it is the ordinary shape. Growth in a meeting's size should
come from the intent genuinely touching more domains, never from a wish to look
thorough.

---

## 10. Cross-references

None of these are required to run a meeting; they are where the surrounding system
is written down.

- `CLAUDE.md` - the constitution: the consequence gates every meeting operates
  inside, the session read-order, and the state discipline this protocol's close step
  inherits.
- `org/ORG_CHART.md` - the seats and functions this ritual convenes, and the gate
  rules (the consistency gate on every seal; General Counsel wherever money or
  liability appears) that §8 applies.
- `org/models.yml` - the tier scheme, and the rule that the interactive-only seat
  never joins an unattended run.
- `DECISIONS.md` - where every ruling from `04-ruling.md` replicates, in the same
  session it is given.
- `registers/BLOCKED_ON_OPERATOR.md`, `inbox/INNOVATION.md` - the two reads in the
  convening checklist.
- `ops/FLEET_CRAFT.md` - the fleet doctrine behind the projection-before-launch rule
  used in §3.2 and §7: the three numbers stated at every launch, the budget guard
  embedded in every fleet script, and how a fan-out's output lands for your approval.
- `ops/COLD_RESUME.md` - how a session with no memory reconstructs where a parked
  meeting or mission stands.
