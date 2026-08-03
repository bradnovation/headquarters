# counsel/ - the drafting library
<!-- file-class: DOCTRINE -->

*Class note: EXTENDING.md section 5's table treats "counsel/ contents" as
PERSONAL as a directory-wide rule, and names this README as the stated
exception - it documents the shared templates/precedents convention every
instance of this product uses, not a user's own negotiated material.
Everything else under counsel/ (templates/ and precedents/ alike) stays
PERSONAL per that table.*

*DOCTRINE layer for the conventions below; the files you accumulate inside
`precedents/` are yours and personal. Governed by
`org/functions/general-counsel/CHARTER.md`, which wins wherever this file and
that one appear to disagree.*

---

## What this directory is

Two things, kept deliberately apart:

- **`templates/`** - the skeletons a draft is assembled from. Generic,
  jurisdiction-neutral, safe to share, safe to publish.
- **`precedents/`** - what you actually negotiated and ruled on. Specific, tied
  to real counterparties, private by convention, never published.

Everything under `counsel/` is a draft or an input to a draft. Nothing here is
legal advice, nothing here is executed paper, and nothing here leaves your hands
by any path an agent controls. If you have not read
`org/functions/general-counsel/CHARTER.md`, read it before you use anything in
this directory - the limits section in particular.

---

## `templates/`

The drafting skeletons. What ships is a small, generic set - the shapes most
businesses need first:

- a services or pilot agreement skeleton
  (`templates/services-agreement-skeleton.md`);
- a scope-of-work skeleton (`templates/scope-of-work-skeleton.md`);
- an engagement-letter skeleton (`templates/engagement-letter-skeleton.md`);
- a mutual non-disclosure skeleton (`templates/mutual-nda-skeleton.md`).

If the shape you need is not here, the General Counsel function drafts a fresh
one under the rules below. It does not import one.

**The rules, all inherited from the function's charter:**

1. **The standing header is baked in.** Every template file opens with it, so
   every copy carries it without anyone having to remember:

   ```
   DRAFT ONLY. Prepared by an AI General Counsel function. Not legal advice.
   Human legal review recommended before execution.
   ```

   A template that has lost its header is broken. Put it back before you use it.

2. **Governing law is an unfilled placeholder, always:**

   ```
   Governing law: [not specified - select with local counsel before execution]
   ```

   No jurisdiction default is ever filled in for you - not by a template, not by
   a drafting session. Venue, forum, and language-of-contract clauses follow the
   same rule.

3. **Every substantive blank is a visible placeholder.** Party names, dates,
   figures, notice periods, and terms in brackets, never invented to make a
   draft look complete. A filled-in number that nobody stated is the most
   dangerous thing a template can contain.

4. **Jurisdiction-dependent clauses carry an inline drafting note** saying so,
   and the draft carries the review flag.

5. **No legal citations.** No statutes, cases, or section numbers - see the
   charter's jurisdiction rules for why.

6. **Templates are authored fresh.** Never adapted from a counterparty's paper,
   a former employer's contract, a document found online with unclear licensing,
   or anything whose provenance you cannot state out loud. Someone else's
   agreement is their lawyer's work product and frequently their confidential
   material.

**Adding a template:** copy the closest existing skeleton, keep the header and
the governing-law placeholder, strip every clause you do not actually need, and
leave what remains in placeholders. Small and honest beats comprehensive and
guessed.

---

## `precedents/`

**What a precedent is:** a term you negotiated with a real counterparty on a
real engagement, and ruled on. What you proposed, what you conceded, what held,
and the context that made it reasonable. A firmly rejected term counts too - a
line you refused to cross is precedent about you.

**What a precedent is not:** a term you approved in a draft that never reached a
counterparty. That is template guesswork that survived one review. It does not
belong here.

**One file per ruled term-set.** The directory is its own index; there is no
separate log to keep in sync.

**No fabricated entries, ever.** Nothing in this directory is seeded with a
hypothetical, an illustration, or a guess at what you would probably accept. An
empty `precedents/` directory is the correct and honest state until your first
real engagement produces an entry. One invented entry destroys the only property
that makes the whole mechanism worth having.

**Assembly order: precedent first, template second.** When drafting, the
function checks whether a ruled term-set already answers a clause before falling
back to the template's default language. Your ruled terms outrank a generic
skeleton every time.

### `precedents/` is PRIVATE by convention

This directory fills with counterparty names, negotiated positions, fee figures,
and concessions - the exact material your own confidentiality agreements exist
to protect. A leak here is not embarrassment; it can be a breach of an
obligation you personally signed.

The convention, stated as rules because convention alone is not enough:

- **Never commit this directory to a public repository.** Not a fork you
  publish, not a gist, not an issue attachment, not a bug report.
- **Before your instance is ever published, add `counsel/precedents/` to
  `.gitignore` and confirm nothing from it is already in your history.** Git
  history is permanent - removing a file in a later commit does not remove it
  from what people can read.
- **The safest posture is a private instance.** If your instance holds real
  engagement material, keep the whole repository private and pull doctrine
  updates from upstream rather than pushing yours outward.
- **This is a convention, not a guarantee.** Nothing in this repo enforces it
  for you. It is a rule you keep, checked at every point where something of
  yours might become public.

---

## What never goes in this directory

- Raw third-party material of any kind - transcripts, recordings, forwarded
  correspondence. That belongs in `vault/` and never leaves it. See
  `vault/README.md`.
- Executed originals and signed copies. Those are records, not drafting inputs;
  keep them wherever you keep your real business records.
- A counterparty's own confidential documents, whatever your intention in saving
  them.
- Anything you would not be able to explain having, to the person it came from.
