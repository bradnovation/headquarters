# Standards-guard (function)

<!-- file-class: DOCTRINE -->

*The gate every deliverable clears before a mission seals, and it fails closed.
It carries no agenda of its own and arrives with no opinions in it: you supply
the standards it enforces before it can do anything for you.*

## Mandate

Any organization that operates for a while accumulates a voice, a working
vocabulary, and a list of things it has decided it will not say. A chartered
org is no different. What is different is that nothing here enforces any of it
by default, so enforcement falls to whichever session happened to touch the
deliverable last, which is another way of saying it falls to nobody.

This function is how enforcement stops depending on who was paying attention.
Every deliverable about to be sealed is checked against rules you wrote, cheap
mechanical checks running first and exactly one judgment call running second,
and every verdict it reaches, clean or otherwise, is written into a log that
outlasts the mission that produced it.

It carries no agenda. It proposes no content, drafts no copy, chairs no debate,
and holds no view about what your standards ought to be. Its whole job is
measuring what a seat has already written against what you have already
declared. Before you declare anything it has nothing to measure, which is
precisely why it arrives empty (below) instead of arriving with somebody else's
preferences installed under your name.

**Before anything else about this function, the property that matters most:
it fails closed.** Should a rule file refuse to parse, should the judgment call
time out or hand back something that is not valid structured output, should
anything at all break inside the guard itself, the deliverable is blocked and
the breakage is put in front of you. A bad day for the checker is not a reason
to let work through. A guard that fails open is a guard that goes silently
offline at the exact moment something has gone wrong, which is the moment you
needed it most. A stalled seal costs little and is impossible to miss. A
standards violation shipping under a verdict that looked clean costs more and
nobody sees it happen.

## Convening

This is a standing advisory function: it attaches to every meeting ritual as a
matter of course rather than waiting to be named in a convening intent. It
holds no seat and chairs nothing. It speaks when a rule question is genuinely
live, and it runs mechanically at the seal step of every mission whether or not
anyone thought to call for it.

It runs at two speeds by design:

- **A deterministic fast path.** Pattern and substring matching against the
  rule files listed below. No model call, no judgment, no cost. Your private
  denylist (below) is always checked this way and never handed to judgment,
  because matching a name needs no judgment and because a probabilistic pass
  over your own sensitive names is not something you should ever be relying on.
- **A single judgment call per deliverable, at this product's building tier.**
  The few rules that genuinely require judgment (voice, tone, whether something
  reads as a violation without matching any literal string) are evaluated in
  one call rather than one call per rule. Judgment is costly enough to be worth
  bounding on purpose and cheap enough, bounded, to run on every seal without
  turning into a spend question.

This function never convenes at the reasoning tier, and it never runs inside
the unattended context of a seat that exists only for interactive use. The rule
stated elsewhere in this product holds here as well: anything whose whole
purpose is to be talked to in real time does not get to run unsupervised.

## Owns

- `org/functions/standards-guard/rules/vocabulary.yaml`, holding reserved terms
  and banned inversions: the phrases you never want turned around or misapplied.
- `org/functions/standards-guard/rules/banned-terms.yaml`, holding retired
  terms and language you have decided to stop using, split into hard (never
  ships) and soft (flag it, blocking optional).
- `org/functions/standards-guard/rules/style.yaml`, holding voice and style
  rules, split between the ones a pattern check settles and the few that go to
  the one judgment call.
- `org/functions/standards-guard/rules/private-denylist.yaml`, holding your own
  sensitive names: people, clients, financial counterparties, internal project
  names, anything that must never appear in work leaving your hands. This file
  is yours alone. It never ships with content in it, nothing outside your own
  instance ever references it, and if you fork or hand your setup to somebody
  else, it is the one file that stays behind.
- `ledgers/STANDARDS_LOG.md`, the append-only verdict log: one row for every
  deliverable checked, clean or not, including the guard-error rows the
  fail-closed behavior above produces.

## Read scope

Public and internal-business material only. What it reads is the deliverable in
front of it, the rule files it owns, and whatever source-of-truth material you
pointed it at during onboarding (below). Anything you have classified as
restricted or third-party-sourced under this product's classification scheme is
out of reach; that tier belongs to a single seat working in live, attended
sessions, and this function is not that seat.

Restricted material found inside a deliverable under review is treated as an
anomaly and flagged as one, because a deliverable should never have been
carrying it, rather than being run through as an ordinary verdict.

Attended or unattended makes no difference to how this function runs, since it
never touches anything above the internal-business tier.

## Deliverables and gates

The verdict is the deliverable: a structured pass or fail for each rule file,
with the judgment call constrained to strict structured output for the rules it
covers. Every verdict, whether clean, soft-fail, hard-fail, or guard-error,
appends exactly one row to `ledgers/STANDARDS_LOG.md`.

- This is the gate every deliverable clears before its mission seals. A
  deliverable carrying money or liability weight clears this product's counsel
  function as well. This function is not a substitute for that pass and does
  not clear anything that function would still need to look at.
- It sends nothing anywhere. It reaches a verdict and appends a row. Its only
  write path, ever, is that row and the rule files it owns.
- A hard fail from either speed blocks the seal. A soft fail warns: the
  deliverable may still seal, the warning is recorded, and it carries into the
  after-action note the agent-quality function writes for that mission.
- A rule file that will not parse, a judgment call that times out, and a
  malformed response are all guard errors: fail closed, block, surface, and log
  as a guard-error row shaped distinctly from a content verdict so the two are
  never confused.

## Onboarding: point this at your own standards

**The rule files ship as documented empty schemas.** Each of the five artifacts
listed above is present in the tree with its shape written out and no content
inside it: the four rule files carry their keys and commented example entries,
and the verdict log carries its header and no verdict rows. That is the state
this function is meant to arrive in, because your standards are not this
product's to guess at. Filling them is onboarding work, done once by you and
revisited whenever your source material moves. Until that work happens the
guard runs, finds nothing to check, and says so honestly.

Rule shapes, documented so you know what goes in them:

```yaml
# rules/vocabulary.yaml
reserved_terms: []
  # - term: ""
  #   definition: ""
  #   source: ""        # where this term's meaning comes from
banned_inversions: []
  # - phrase: ""
  #   canonical_correction: ""
  #   source: ""
```

```yaml
# rules/banned-terms.yaml
retired_terms: []
  # - term: ""
  #   reason: ""
  #   severity: hard
banned_cliches: []
  # - phrase: ""
  #   reason: ""
  #   severity: soft
```

```yaml
# rules/style.yaml
deterministic_rules: []
  # - rule_id: ""
  #   pattern: ""
  #   severity: soft
judged_rules: []
  # - rule_id: ""
  #   description: ""
  #   severity: soft
```

```yaml
# rules/private-denylist.yaml  (never leaves your own instance)
denied_terms: []
  # - term: ""
  #   category: person | client | financial | internal-project | other
```

The onboarding step, in order:

1. **Name the source your standards come from.** A style guide, a brand
   document, a piece of your own past writing you would hold up and call the
   voice you want, whatever your actual true north for vocabulary and tone is.
   If nothing formal exists, your own plain description of how this should
   sound is enough to begin with.
2. **Mirror that source; do not fork it.** Its content gets copied into the
   rule files above rather than paraphrased from memory. The same fail-closed
   instinct applies: the rule files are a mirror of something you can point
   back at, not one session's private impression of your voice.
3. **Fill the private denylist before anything of yours is pushed publicly.**
   Every name that must never leave your hands goes into that file first. This
   step is neither optional nor deferrable. It is the one rule file whose
   omission has consequences the moment it is skipped.
4. **Re-mirror when the source moves.** A canon-of-truth document that changes
   leaves the rule files mirroring it stale, silently, until you run this step
   again. v1 has no drift detection behind that habit.

## Standing constraints

- Fails closed rather than open. Stated once already and restated here because
  it is the one property of this function that a future change must never
  assume away: an error inside the guard blocks and surfaces, every time.
- No agenda. It proposes no content, drafts no copy, and chairs no debate. It
  measures what already exists.
- No spend authority past the single bounded judgment call per deliverable, and
  no unattended-run exception of its own. It runs inside whatever session or
  fan-out already convened it.
- Judged rules are probabilistic by their nature. Holding them to one call per
  deliverable keeps both cost and behavior predictable, and you, at seal
  review, are the backstop for any verdict that reads wrong. A clean pass is a
  strong signal rather than a guarantee.
- Arrives with no opinions. Every rule file above stays empty until you fill
  it. A version of this shipping with somebody else's vocabulary already
  installed would be enforcing somebody else's standards on your work, which
  would defeat the whole reason it is yours.

## Guard procedure

A fixed order, so the cheap checks screen for the expensive one:

1. **Read the rules fresh.** Every rule file is read at the start of each
   check, never cached, because nothing here runs long enough for staleness to
   be a risk worth taking. A file that will not parse ends the check there:
   guard error, fail closed, surface, log.

2. **Run the deterministic pass.** Private-denylist matches go first and are
   always hard, never deferred to judgment. Then vocabulary reserved-term and
   banned-inversion matches (hard), then banned-terms retired-term matches
   (hard) and cliche matches (soft), then style's deterministic rows (soft). A
   hard hit at this stage is recorded but does not end the pass: the
   deliverable is checked all the way through so that every finding arrives at
   once, rather than the author receiving one block per resubmission.

3. **Make the one judgment call.** A single call takes every rule in style's
   `judged_rules` list and evaluates them together against the deliverable's
   full text. Back comes one verdict object per rule: the rule identifier, pass
   or fail, the severity that rule's file declared, and a short detail naming
   the passage and the reasoning. A response that is not valid structured
   output, or that leaves out a rule that was asked about, is a guard error.
   Fail closed; the rules that did parse earn no partial credit.

4. **Combine the findings into one outcome.** A hard fail from either stage
   blocks the seal. A soft fail warns and carries forward into the after-action
   note. Clean on every rule clears this function's own gate and nothing
   further: the other gates this product runs, for money and liability, still
   stand between the deliverable and the seal.

5. **Write the row.** One row per deliverable checked, every time, whatever the
   outcome: date, the deliverable's path or the mission identifier, the seat it
   came from, and each rule's verdict with its severity. A guard error takes a
   row shaped distinctly enough that nobody could mistake it for a content
   verdict, saying plainly that this is the deliberate fail-closed behavior and
   what triggered it.

6. **Put it in front of you.** A hard fail and a guard error both stop the seal
   and reach you in whatever channel the mission is running through. An outcome
   carrying only soft fails seals normally, its warnings sitting in the log for
   the next after-action review to pick up.
