# headquarters - a chartered staff for your business, run in Claude Code

<!-- file-class: DOCTRINE -->

**headquarters is an independent open-source project. It is not affiliated with,
endorsed by, or sponsored by Anthropic. "Claude" and "Claude Code" are trademarks of
Anthropic, referenced here only to describe what this project is compatible with.**

---

## A constitution and a chartered staff for Claude Code

*The rituals, gates, and org shape that let you run a business at the level of
intent, not prompts.*

A capable model will do almost anything you ask, one prompt at a time, and remember
none of it tomorrow. What that costs you is not output quality, it is continuity:
decisions with no record, work that restarts from your own memory every session, and
irreversible acts (money spent, messages sent, someone else's repository written to)
sitting one confident sentence away. headquarters is the organization that goes
around the model instead of inside it: written charters, a session ritual, a small
set of gates that never move, and a repository that is the record.

### What this is not

- **Not a chatbot.** There is no interface here. You bring Claude Code; this
  repository tells the session what it is, what it may do, and what it owes you
  before it stops.
- **Not an autonomous swarm.** Nothing convenes itself. Nothing runs while you are
  away. Every fan-out states its cost before it starts and every one of them ends
  inside the session you opened.
- **Not a SaaS.** No account, no service, no hosted anything, no telemetry. You clone
  files onto your own disk and they stay there.
- **Not legal advice.** The General Counsel function drafts paper for you to take to
  a lawyer you hire. It has no send path and it is not a substitute for
  professional advice. Read the framing below before you use it.
- **Not a promise about your revenue.** This project makes no claim about what
  running it will earn you, save you, or automate away. It is a way of working, and
  the results are yours.

### What changed in 0.2

- **The building tier is now the default for every fan-out role**, with a boost line
  that names any proposed reasoning-tier escalation and a notify rule that surfaces
  the case for one mid-work instead of pinning up silently.
- **Two new doctrine files**: `ops/MULTI-SESSION.md`, for peer sessions working in
  parallel, and `ops/MEASUREMENT_CRAFT.md`, for instrument validity and verification
  discipline.
- **The budget guard gained a second brake**: a cap on how many agents may be
  convened at once, independent of the token guard.
- **Two new scripts**: a usage-meter tally read from your own transcripts, and a
  doctrine-diff helper for taking an upstream release.
- **An install-from-GitHub section**, right below, that a friend can follow cold.
- **This doctrine still runs fully with the reasoning tier at the keyboard.** A more
  capable interactive-only tier stays a luxury for particular days, never a pinned
  duty.

Full detail in `CHANGELOG.md`.

### What changed in 0.3

- **Doctrine is now invoke-loaded from `plugins/headquarters-core`** as skills,
  instead of being read whole out of `doctrine/CONSTITUTION-CORE.md` every
  session. It loads either in-repo (the `.claude/skills/headquarters-core`
  symlink this template ships with, auto-loaded once you trust the folder) or
  machine-wide, symlinked into your own `~/.claude/skills/` so it follows you
  across every project - see `plugins/README.md` for both routes. The
  `local-lane` plugin alongside it stays entirely optional: nothing here
  requires it, and you only see it if you enable it yourself.

---

## What you get

### An organization on paper, with a shape you can change

```
                          THE OPERATOR
            all intent starts here, all rulings end here, and
               nothing downstream moves without your word
                               |
              -------------------------------------
              |                                   |
       CHIEF OF STAFF                  DECISIONS.md / HANDOFF.md
     (chairs the meeting;               (your word and the live
      org/STAFF_MEETING.md)              state, written down)
              |
  ------------------------------------------------------------------
  |             |            |             |               |
OPERATIONS   MARKETING    REVENUE     ENGINEERING       FINANCE
 (seat)       (seat)       (seat)       (seat)           (seat)
                                             (the sixth seat, Chief of Staff,
                                              is drawn one row up)

      FUNCTIONS - nothing of their own to push; each stays quiet until
                  something inside its domain comes up
  ------------------------------------------------------------------
  |                  |                    |                   |
STANDARDS-GUARD  GENERAL COUNSEL     AGENT QUALITY      INNOVATION DESK
(gates every      (drafts only,       (notes work once   (ranked inbox;
 seal)             never sends)        it is done)        dreaming, disarmed)
```

Six seats hold state between sessions and take a chair when the staff convenes. Four
functions hold no agenda of their own and speak only when their domain is touched.
The names are defaults: rename them, drop the ones your business does not have, add
the ones it does. Nothing in the constitution keys off a seat's label. The full map
is `org/ORG_CHART.md`; the ritual those seats convene for is `org/STAFF_MEETING.md`.

### Five consequence gates, named once and never moved

The gates are the part a stranger can read in one sitting and know exactly what this
system will not do. They are stated in `CLAUDE.md` in short form and in
`doctrine/CONSTITUTION-CORE.md` in full, with the failure class behind each:

- **G1 - Spend.** Metered work needs you in the room, and a fan-out shows you its
  projected cost while refusing is still cheap.
- **G2 - Foreign repositories.** Other people's code is readable by opening files and
  nothing more. The version-control command line is never aimed at a repository you
  do not own, however harmless the command.
- **G3 - External communication.** Outbound anything stops with you. The staff
  composes; you release.
- **G4 - Deploys.** Nothing ships from here to any environment.
- **G5 - Sensitive material.** Third-party words, and whatever else you classify
  sensitive, stay in `vault/`: out of version control, out of any run you are not
  sitting with.

G3 and G4 are structural rather than configured: this product contains no mechanism
for sending and none for deploying, so there is nothing in it to switch on. That is a
real ceiling, named here rather than discovered later.

### Spend treated as a first-class feature, not a footnote

Cost discipline is built into the work, not bolted onto the end of it:

- **Projection before launch.** Nothing that convenes more than the current session
  starts until three figures have been said out loud in a form you can refuse: the
  projected tokens with the arithmetic shown, the projected wall-clock, and your
  meter position read fresh at the launch moment. A projection that lands over your
  ceiling reaches you as a written proposal instead of as a thing already in motion.
  Filing is the normal outcome of a high projection, not a failure of the run.
- **A budget guard inside the script.** Every fan-out carries a two-threshold guard:
  warn at 80% of its projection, stop launching at 100% of its cap, let in-flight
  work finish and write, then close out and report. Never retry into a wall.
- **A ledger that closes the loop.** `ledgers/SPEND.md` takes the projection before
  the launch and the actual afterward, with any overage attributed in plain language.
  An unreconciled projection blocks the next launch of the same shape.

The doctrine is `ops/FLEET_CRAFT.md`. The two-threshold guard is adapted from prior
art and credited in `ATTRIBUTIONS.md`.

### Dreaming, and it ships disarmed

Dreaming is the off-cycle generative pass: a run that reads your own repository state
and comes back with proposals for the seams you have not had time to see. It is a
governed ritual rather than a novelty script. Divergence is kept strictly apart from
selection, an interrupted pass resumes from its log instead of restarting, everything
it produces lands in a ranked inbox, and nothing it finds interrupts you between
meetings.

**It will not run until you type a spend cap.** There is no default figure, because
no default could be safe: what an idle run costs depends on your plan, your meter,
and your tolerance. Until you set one, the router declines and says why. Charter:
`org/functions/innovation-desk/CHARTER.md`.

### A General Counsel function that is propose-only by construction

This function drafts contract-shaped paper so you start from a working draft instead
of a blank page: agreements, scopes of work, engagement letters, notices. Read the
rails before you use any of it:

- **It is software, not a lawyer, and running it does not give you one.** Nothing it
  produces is legal advice.
- **Propose-only is structural.** The function holds no transmission mechanism of any
  kind, so there is no setting to find and switch off. Every document is a draft you
  carry to a qualified human, or it goes nowhere.
- **It never assumes a jurisdiction.** Governing law is left as an explicit unfilled
  placeholder that says it must be chosen with a local professional.
- **Fluent formatting is not evidence of correct substance.** A draft that reads
  finished is the easiest thing for a language model to produce and the weakest
  possible reason to sign it.

The same rail attaches by output shape, not by job title: any seat you add that
produces advice-shaped output inherits it, and `EXTENDING.md` section 7 says so in
terms you cannot opt out of by renaming the seat. Charter:
`org/functions/general-counsel/CHARTER.md`.

### Consent before anything outside this repository is read

Your other work lives somewhere. A second project, a notes system, a repository that
predates this staff entirely. headquarters can read those for context, and it asks
first, every time a new source is added, and records the answer in `SISTER-REPOS.md`
with the specific purpose consent was given for.

A location not listed there is not read. Not a directory sitting next to this one, not
a path that came up in conversation, not a quick look to see whether it would be worth
asking about. Reads are plain file reads only, nothing is ever written back, and no
version-control command is run against a source in the registry even when it would
only look.

### Built to be extended into your business, not around it

The default roster is six seats and four functions. Your business has shapes it does
not name: development agents that need an engineering seat watching them, a delivery
seat, a support seat, a research seat. Adding one is four small acts (copy the
template, register it in the chart, give it a duty row, create its ledger), and it is
a normal act rather than a fork.

Extending means adding domain rules. It never means loosening a gate. A new seat may
be stricter than the constitution and narrower in scope; it cannot grant itself a send
path, a deploy path, or wider read scope. `EXTENDING.md` is the procedure, and
`examples/adding-a-seat/` is one worked all the way through, including the chart diff
and the first ledger entry.

---

## Install from GitHub

Official quickstart, read 2026-09-12, is the authority behind the commands below:
<https://code.claude.com/docs/en/quickstart>. Check it yourself if anything here
looks out of date by the time you read it.

1. **Install Claude Code.** Native installer, on macOS, Linux, or WSL:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
   Windows PowerShell:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
   Homebrew: `brew install --cask claude-code`. WinGet: `winget install Anthropic.ClaudeCode`.
   Confirm it with `claude --version`. The first `claude`
   command prompts you to log in: a Claude Pro, Max, Team, or Enterprise
   subscription, or a Console account, all work.
2. **Get your own copy of this repository.** Three paths, in the order worth
   trying:
   - **The template button.** On the repository's GitHub page, click **Use this
     template**, name your copy, and leave it **private** (why, below). Then:
     ```
     git clone https://github.com/YOUR-NAME/headquarters.git
     ```
   - **The GitHub CLI, one line:**
     ```
     gh repo create YOUR-NAME/headquarters --template bradnovation/headquarters --private --clone
     ```
   - **A plain clone with detached history**, if you would rather not use either
     GitHub feature:
     ```
     git clone https://github.com/bradnovation/headquarters.git my-headquarters
     cd my-headquarters
     rm -rf .git
     git init
     git add -A
     git commit -m "headquarters v0.2, my copy"
     ```
     Then create a private repository on GitHub and push that commit to it.

   **Why private.** The fork-posture line in `CLAUDE.md` section (f) decides which
   defaults are safe: a private copy may hold internal business material in
   ordinary committed files, a public one may not. Start private, and change that
   answer deliberately later if you actually mean to run this in the open.
3. **Open a session inside it.** `cd` into the directory you cloned, then run
   `claude`. On a fresh clone the staff offers you the onboarding interview itself;
   if it does not, asking in plain words, "run the onboarding interview," always
   works. There is no slash command to remember.
4. **Your first orientation.** The orientation ritual reads the entry file, the
   constitution core, the top of `HANDOFF.md`, and your newest rulings, then reports
   where things stand and stops for your direction. Orienting is reading, not doing;
   nothing is written during it.
5. **Convene your first meeting.** Pick a genuine open question in your business,
   small enough to finish. The staff argues it through in briefs, the disagreements
   get carried rather than smoothed, and you rule. The ruling lands in `DECISIONS.md`
   and the work becomes a mission packet.
6. **Park.** Touch anything in the repository and the close ritual is owed before you
   stop: the handoff is rewritten, the session log gets its entry, and the commit
   carries both.

The narrated walkthrough is `docs/GETTING-STARTED.md`. A complete fictional meeting,
from intent through briefs and debate to a ruling and a sealed mission, is at
`examples/first-meeting/`, readable end to end in about fifteen minutes.

---

## The philosophy, in short

- **Propose-then-approve.** A session reads, orients, and proposes. You sign off
  before anything durable happens. Drafts are shown before they are kept, and a
  rejected draft is workshopped in conversation rather than silently overwritten.
- **No daemons.** Nothing is scheduled, nothing polls, nothing runs while you sleep.
  Work happens in sessions you open and the fan-outs those sessions launch, and it
  ends when they do.
- **The repository is the record.** A session with no memory of the last one must be
  able to reconstruct where things stand from the files alone. That is why the
  handoff is mandatory at close, why state is written down along the way rather than
  at the end, and why `ops/COLD_RESUME.md` states the trust order for reading it back.
- **Four security classes, decided before anything else.** C0 public, C1 internal
  business, C2 sensitive, C3 third-party words. The class decides where a thing may
  live: a private working copy may hold C0 and C1 freely and C2 where marked, a public
  one may hold C0 only, and C3 never leaves `vault/` in either case.
- **The constitution wins.** Where a charter and the doctrine core disagree, the
  doctrine core governs and the session surfaces the conflict to you instead of
  choosing for itself.
- **The clean-start promise.** You begin empty. There are no meetings, no missions,
  and no rulings in a fresh clone but the one format example that teaches the ledger
  shape and says so on its face. Everything demonstrative lives under `examples/` or
  `docs/`, headed as a worked example. Every line of history in your copy will be
  yours.

---

## How this differs

*Comparison state as of 2026-08. This landscape moves fast, several of the projects
below shipped code the same week these notes were written, and any of these lines can
go stale without anyone doing anything wrong. Check the sources yourself before you
decide on the strength of a paragraph in someone else's README.*

Four projects a reader is likely to have in mind already, what each ships, and where
headquarters is doing something different:

- **Paperclip.** A hosted control plane for AI agent employees: model-agnostic, a
  dashboard, a companies library, a skill studio, and genuinely shipped tiered budget
  stops that pause agents and cancel queued work at the limit. As of 2026-08 its
  budget mechanism acts on spend already incurred, and its published feature set
  includes no legal-drafting function and no ideation ritual. headquarters projects a
  run's cost before it launches and files it instead of launching when the projection
  lands over your ceiling.
- **BMAD-METHOD.** A fixed-role method with a Clarify, Plan, Build, Learn loop and a
  brainstorming skill that separates divergence from convergence and keeps a log an
  interrupted pass can resume from. As of 2026-08 that skill carries no spend ceiling
  or governing ritual around it. headquarters adapts the separation and the log into a
  dreaming ritual that ships disarmed behind a cap you type yourself, and credits the
  origin in `ATTRIBUTIONS.md`.
- **Agency Agents.** The broadest persona roster of anything in this comparison,
  including a titled chief of staff and a legal and compliance persona, packaged for
  one-command installation. As of 2026-08 that compliance persona's own file carries
  no draft-only or consult-a-professional language. headquarters writes the
  propose-only rail into the General Counsel charter itself, and makes it inherit by
  output shape to any seat you add.
- **Anthropic's chief-of-staff cookbook pattern.** A teaching example built on the
  Claude Agent SDK: a chief of staff delegating to subagents, with a plan-approval
  step. It is a pattern to build from rather than an organization to run.
  headquarters ships the surrounding organization: charters, a meeting ritual, named
  gates, ledgers, handoff discipline, and a cold-resume path.

The four things headquarters is actually built around, and the only claims here worth
weighing: a small named set of consequence gates a stranger reads in one sitting; cost
projected before a run rather than metered after it; dreaming as a capped, ranked,
governed ritual; a propose-only legal-drafting rail written into the artifact itself;
and consent recorded before anything outside this repository is read. A survey of
comparable public projects in 2026-08 found each of the individual pieces somewhere
and the combination nowhere, which is a snapshot rather than a standing claim.

**And the honest redirect.** Want a hosted dashboard, a web interface, and agents that
keep working while you are away, and you do not need a legal-drafting rail or a cost
gate that files a run instead of launching it? **Paperclip is a fine, actively
maintained choice. Use that instead.** Sending you somewhere that fits your problem
better is a good outcome of reading this page.

---

## License, contributing, credits

**License: Apache-2.0.** The full text is in `LICENSE` and the attribution notice
downstream redistributions must retain is in `NOTICE`.

**Contributing.** Pull requests only, sign-off by DCO rather than a contributor
licence agreement, and one honest posture stated up front: there is no service level
here. Review happens in batches at the maintainer's tempo, doctrine changes get extra
scrutiny because the constitution wins over everything downstream of it, and nothing
proprietary or confidential belongs in a pull request. Details in `CONTRIBUTING.md`,
with `CODE_OF_CONDUCT.md` alongside it.

**Credits.** Several mechanics here were adapted from open-source projects that solved
the same problem first. `ATTRIBUTIONS.md` is the one place that says which, and what
was adapted in each case is an idea rather than code: a shape, a threshold, a
separation of concerns. Any of them being wrong in this implementation is this
project's fault and not the original author's.
