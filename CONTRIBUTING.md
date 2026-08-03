# CONTRIBUTING
<!-- file-class: DOCTRINE -->

This project ships as a chartered staff that other people run their own
businesses on. Contributions are welcome, and this file states the posture
plainly so nobody guesses at it: what a contribution has to do to land, what
it can never carry, and what happens when a proposed change touches the
doctrine layer rather than the mechanical one.

---

## How a contribution lands

There is exactly one path in: a pull request. Nothing else is read as a
contribution, however it arrives.

There is no service-level agreement on review time. This is maintained on
one person's own tempo, not a support contract, and a PR sitting unreviewed
for a while is not a signal that it was rejected or ignored. Batches get
reviewed when the maintainer sits down to review them.

The maintainer's own hand merges every pull request. Nothing merges itself,
however small the change looks, and a passing check is not the same thing
as an approval.

---

## Sign your work

Every commit in a pull request carries a Developer Certificate of Origin
sign-off, added with `git commit --signoff` (or `-s`), which appends a line
like:

```
Signed-off-by: Your Name <your.email@example.com>
```

That line is your certification that you wrote the change, or otherwise
have the right to submit it under this project's license, and that you
understand it will be distributed under that same license (see `LICENSE`).
It is a lightweight sign-off, not a separate contributor agreement: you keep
your own copyright in what you write, and no additional paperwork is asked
of you beyond the line itself. Pull requests carrying unsigned commits are
not merged.

---

## Doctrine changes get extra scrutiny

`EXTENDING.md` section 5 sorts every file in this repository into one of
three classes: DOCTRINE, GENERATED, or PERSONAL. A pull request that touches
a DOCTRINE file, meaning a file every downstream user eventually pulls into
their own copy, is read more slowly and more skeptically than one that adds
a template or fixes a typo, because a mistake there does not stay local to
this repository.

The constitution wins over every charter, and that rule binds contributions
exactly as it binds this project's own sessions. A change that would loosen
one of the five consequence gates, widen a function's read scope past what
the doctrine core allows, or add a send or deploy path where none exists
today does not land, regardless of how well-argued the case for it is. Where
a proposed change and the doctrine core disagree, the doctrine core wins,
and the pull request gets that reasoning back rather than a silent close.

---

## What must never appear in a pull request

- No proprietary or confidential material of any kind: not another
  business's real contract, not a counterparty's negotiated terms, not
  internal material from a company you work for or with.
- No personal data belonging to a real person who has not agreed to see it
  published, yours included. If a worked example needs a name, a company, or
  a number, invent one and say plainly that it is invented.
- No content copied from another project whose license or origin you cannot
  state. An adapted idea, credited honestly, is welcome; someone else's
  written work, uncredited or unlicensed, is not.

A pull request carrying any of the above is closed without merging, and the
closure is not a judgment on the rest of the change, only on that content.

---

## What a good first contribution looks like

A fixed bug in a script, a clarified paragraph in a template, a new worked
example under `examples/` that teaches one thing well, or a proposed seat
charter written against `org/SEAT-TEMPLATE.md`. Small, self-contained, and
reviewable in one sitting is easier to land than a large change bundling
several ideas at once, and splitting a large idea into smaller pull requests
usually gets it merged faster, not slower.
