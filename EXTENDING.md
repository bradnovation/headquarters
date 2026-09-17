<!-- file-class: DOCTRINE -->

# EXTENDING

*How to add your own seats, functions, and sub-agents without breaking the thing
that makes this work. File class DOCTRINE - upstream owns this file; read it
before you change anything under `org/`.*

---

## 1. What extending means here

This product ships an organization: an operator above it, a Chief of Staff
chairing, five other default seats, four functions, and a small set of gates that
never move. It is meant to be extended. Your business has shapes this default
roster does not name - development agents that need an engineering seat watching
them, a delivery or project-management seat, a support seat, a research seat -
and adding them is a normal act, not a fork.

Extending means **adding domain rules**. It never means loosening a gate. A new
seat can be stricter than the constitution, narrower in scope, slower to declare
work done. It cannot grant itself a send path, a deploy path, wider read scope
than the constitution allows, or the right to seal without passing the
standards-guard. Where a charter and `doctrine/CONSTITUTION-CORE.md` disagree,
the constitution wins, and the session surfaces the conflict to you rather than
choosing for itself.

That rule is what keeps a growing organization safe to run. Everything below is
mechanics.

---

## 2. Adding a seat: four acts

1. **Copy the template.** `org/SEAT-TEMPLATE.md` to
   `org/seats/<your-seat>/CHARTER.md`, short lowercase directory name. Fill every
   bracketed placeholder; delete the italic guidance lines.
2. **Register it in the chart.** Add a row to section 2 of `org/ORG_CHART.md`
   with the seat's one-line mandate, default tier, and the paths to its charter
   and ledger. An unregistered charter is a document, not a seat: the meeting
   ritual convenes from the chart.
3. **Add a duty row.** `org/models.yml` maps duties to model tiers. Give the seat
   at least one duty row - more if its work splits, the way plan-shaped work and
   execution-shaped work usually split. Building tier is the default; reasoning
   tier is claimed on a stated reason written next to the row.
4. **Create the ledger.** An empty `org/seats/<your-seat>/LEDGER.md` with two
   lines of format prose. The after-action note has to have somewhere to land on
   the day the first mission seals, or it will not be written.

Removing a seat is the same four acts in reverse, with a line in `DECISIONS.md`
recording why. Renaming a seat is a rename plus the chart row plus the duty row -
nothing in the constitution keys off a seat's label, which is exactly why the
default names are safe to change.

**Two worked shapes**, because these are the two most people want first:

- *Development agents under your own engineering seat.* The seat is the charter;
  the agents are its hands. The charter names the build-plan shape they execute,
  the verification bar they must clear before anything is called done, and the
  repos they may read. The agents inherit the seat's read scope exactly, and its
  gates exactly.
- *A delivery or project-management seat.* Owns the schedule view across active
  work, the handoff between a sealed mission and whoever consumes it, and the
  standing judgment on what is actually blocked versus merely slow. It writes to
  the registers the operations seat owns only through that seat, or it takes over
  a named register outright - decide which, and write it in both charters, so two
  seats never both own one file.

---

## 3. Sub-agents under a seat

A seat may convene as many sub-agents as the work needs. They are hands, not
seats: they hold no charter, no standing state, and no chair at the meeting. Four
rules bind them, and a seat charter may tighten them but never relax them.

- **Inheritance, not expansion.** A sub-agent's read scope is its seat's read
  scope, and its gates are its seat's gates. A convened agent that needs
  something outside that scope stops and asks, rather than reaching.
- **Unattended runs read less.** An agent running without you watching reads
  public and internal material only - never the vault, never anything classed
  sensitive that a specific ruled mission has not put in front of it.
- **No interactive-only tier ever runs unattended.** If you have a model tier you
  treat as your own thinking seat - the expensive one you sit with - it stays out
  of every fan-out. This is a rule about the role, not about any particular
  model: whichever tier plays that part in your setup is excluded from
  unattended work, and `org/models.yml` is where you say so.
- **Cost is projected before launch, not discovered after.** Any fan-out states
  its projected spend and its projected wall-clock before it starts, and the
  actuals land in `ledgers/SPEND.md` at close. A seat that convenes agents
  without a projection is running your budget on hope.

Foreign code you do not own - a sister repository, a client project, a checkout
on your own disk - is read-only, by plain file reads, and only after you have
granted consent for that path. No agent runs a version-control command against a
repository it does not own, read-only commands included. Your hand does that
work, or it does not happen.

---

## 4. Seats versus functions

Add a **seat** when the thing has a domain agenda: work it wants to see happen,
artifacts it owns, a chair it would take at a meeting.

Add a **function** when the thing is a gate or a service with no agenda of its
own - it speaks when its domain is touched and is otherwise silent. Functions
live at `org/functions/<name>/CHARTER.md` and are registered in section 3 of
`org/ORG_CHART.md`.

A new function that gates must say exactly what it gates and what happens when it
errors. Copy the standards-guard's posture: **fail closed.** A gate that passes
work through when it breaks is not a gate, it is a delay. If your new function
records rather than gates - the way Agent Quality does - say that plainly in its
charter, so nobody waits on a pass that is never coming.

---

## 5. The three file classes

Every file in this repo is one of three classes. The class decides who may edit
it and whether an upstream update can ever touch it.

| Class | Who owns it | Upstream behaviour |
|---|---|---|
| **DOCTRINE** | Upstream. | Improved upstream and pullable into your copy. Do not hand-edit. |
| **GENERATED** | You, after the onboarding interview writes it once from your answers. | Never touched by an upstream pull. Re-running onboarding rewrites it, showing you the diff first. |
| **PERSONAL** | You, entirely. | Never read, never written, never pulled. Upstream does not know these files exist. |

Where the classes land in the shipped tree:

| Path | Class |
|---|---|
| `doctrine/`, `ops/`, `org/STAFF_MEETING.md`, `org/SEAT-TEMPLATE.md`, `EXTENDING.md`, `org/functions/*/CHARTER.md`, `README.md`, `docs/`, `examples/`, `scripts/`, `.claude/skills/`, `ATTRIBUTIONS.md`, `SISTER-REPOS.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `counsel/README.md` | DOCTRINE |
| `CLAUDE.md`, `MISSION.md`, `org/ORG_CHART.md`, `org/models.yml`, the six default seat charters, `NOTICE` (its copyright line is yours to fill) | GENERATED |
| `DECISIONS.md`, `HANDOFF.md`, `SESSION_LOG.md`, `registers/`, `ledgers/`, `meetings/`, `missions/`, `counsel/` contents other than its README and the shipped `templates/` skeletons (the skeletons are marked PERSONAL because your filled copies are yours; the shipped blanks pull like doctrine), `transcripts/index/`, `vault/`, every seat `LEDGER.md`, every seat you add | PERSONAL |
| `LICENSE` | unmarked by design: verbatim third-party license text, never edited |

Mark the class at the top of any file you create, on its own line, in the same
form this file uses:

```
<!-- file-class: PERSONAL -->
```

**Nothing enforces this.** The classes are convention plus review - a marker is a
note to the next reader and to the session that opens your repo cold, not a
permission system. Said plainly so you are not surprised later: a session can
write to a doctrine file if you tell it to, and the file will not stop it.

**As of 0.3, most of the DOCTRINE class ships as invoke-loaded skills** under
`plugins/headquarters-core` rather than as files a session reads whole. It loads
from the in-repo `.claude/skills/headquarters-core` symlink this template ships
with (automatic once you trust the folder), or you can symlink it into your own
`~/.claude/skills/` for a machine-wide install that follows you across projects -
`plugins/README.md` walks both routes. The `local-lane` plugin beside it is a
separate, optional add-on with no bearing on the doctrine above; leave it alone if
you don't run local models.

---

## 6. The upstream pull, honestly

The doctrine layer improves over time and you can take those improvements. Read
`CHANGELOG.md` first for what actually changed, and let `scripts/doctrine-diff.sh`
prepare step 3's diff for you. The mechanics, all of which are your hand rather than
a session's:

1. Add the public repository as a second remote in your own copy. Once, ever.
2. Fetch it. Never merge it blind - your history and its history are not the same
   organization.
3. Review a diff limited to the doctrine paths in the table above. A session can
   prepare that diff and explain it to you; approving and applying it is yours.
4. Apply only those paths, in your own commit, with a line in `DECISIONS.md` if
   the update changed how you work.

**The honest failure mode:** this holds only while you leave doctrine files
alone. Hand-edit one and every future pull becomes a merge conflict you own,
forever, with no mechanism helping you - the product cannot tell your improvement
from a stale copy. That is a real cost, and it is why the classes exist.

**What to do instead of editing doctrine**, in order of preference: put the rule
in your own seat's charter, where it binds the work and upstream never touches
it; or record it as a ruling in `DECISIONS.md`, which is the layer built for
exactly this; or propose the change upstream, so everyone gets it and you keep a
clean pull path. Only if none of those fit should you edit a doctrine file - and
then accept that you have forked that file and will merge it by hand from now on.

Your personal layer is never at risk from any of this. Upstream has no path to
your rulings, your registers, your ledgers, your meetings, your missions, or your
vault, by design.

---

## 7. The advice-shaped-extension rule

Some output is dangerous in a specific way: a stranger reading it could act on it
as though a professional produced it. Legal drafts, tax positions, compliance
answers, safety sign-offs, anything that looks like counsel.

**Any seat or function you add that produces output of that shape inherits the
same rail the General Counsel function carries. This is structural, not a style
preference, and you do not get to opt out by naming the seat something else.**

The rail, in full:

1. **Draft-only by structure.** No send path, no filing path, no submission path
   exists for that output. The operator carries it to a qualified human, or it
   goes nowhere.
2. **A standing header on every document**, saying it is a draft prepared for the
   operator's review and is not professional advice, in language a stranger
   understands on the first read.
3. **A recommend-human-review flag, applied conservatively.** When in doubt, the
   flag goes in. It is cheap to carry and expensive to have omitted.
4. **No jurisdiction assumed, ever.** Governing law, tax residency, regulatory
   regime: each stays an explicit unfilled placeholder that says it must be
   selected with a local professional before the document is used.
5. **The seat's charter states the rail out loud**, in its own words, in
   Deliverables and gates - because a convened agent reads the charter, and a
   rule it has to infer is a rule it will eventually miss.

The test to apply when you are unsure whether the rail attaches: *could a
reasonable person, reading this output without context, take it as the work of a
qualified professional and act on it?* If yes, the rail attaches. The mechanism
that makes this hold is that the rail is inherited by output shape rather than by
seat name - a bookkeeping seat that starts answering tax questions is inside the
rail from the first answer.

---

## 8. Checklist before your first run of a new seat

1. Charter filled from `org/SEAT-TEMPLATE.md`, all placeholders replaced, all
   guidance lines deleted.
2. Row added to `org/ORG_CHART.md`; duty row added to `org/models.yml`; empty
   `LEDGER.md` created.
3. Nothing in the charter loosens a gate, widens read scope, or creates a send or
   deploy path.
4. If the seat convenes sub-agents: their read scope, their unattended limits,
   and the projection-before-launch habit are named in the charter.
5. If the output is advice-shaped: the section 7 rail is written into the
   charter, not assumed.
6. File-class marker at the top of every new file.
7. A line in `DECISIONS.md` recording that the seat now exists and why - so the
   next cold session, yours or a successor's, can reconstruct the organization
   from the files alone.
