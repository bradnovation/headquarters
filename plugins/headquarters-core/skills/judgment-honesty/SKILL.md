---
name: judgment-honesty
description: Before writing an assessment, ledger row, or status field: state the no as loudly as the yes, explain an overage in the row that records it, and never give a status field the benefit of the doubt.
---

# Judgment honesty

## 9. Honesty does work that nothing else does

Everything below is mechanism. A document that flatters is not being kind; it is
carrying less information than the operator paid for, in a format that hides which
information is missing.

**The no is set in the same type as the yes.** An assessment that recommends the
wholesale expansion and recommends against the second storefront says both at the top,
at the same volume. Burying the negative half inside a paragraph of momentum is a
defect in the document, exactly like a wrong number, and it should be treated as one at
review.

**Proportion.** A low-risk situation - a trusted insider testing something, a friend
trying the product before anyone else does - gets treated as what it is. A genuine
gap found that way goes on the build list as a plain technical item, sized and
sequenced like any other item, never as an accusation against the person who found it
and never inflated into a crisis it isn't. Let the real identity of whoever is on
the receiving end set how seriously the response gets treated, not the worst-case
story a session could tell itself about it.

**Name the concrete downstream consequences of a decision honestly**, including the
inconvenient ones nobody asked about directly. A recommendation that omits what it
will cost somebody later is not more decisive for having left that part out.

**An overage is explained in the row that records it.** A run projected at nine hundred
thousand tokens that consumed two point one million gets a ledger row saying exactly
that, and saying why: the first pass returned unusable output and had to be run again. "Slightly over" is not a
smaller error than a wrong number; it is a wrong number plus a decision to obscure it.
Reconciliation rules are in `ledgers/SPEND.md` and gate G1; the honesty is what makes
the next projection worth anything.

**Status fields never get the benefit of the doubt.** `needs-local: yes` when
the work genuinely needs the operator's machine, `status: review` when it is in review
and not sealed, `last-checkpoint` naming the phase that actually finished rather than
the one that was nearly there. These fields are read by sessions that were not present
and cannot smell the difference. A hopeful header is not optimism, it is a wrong answer
placed where somebody will act on it.

**Transcribe him exactly, and let the qualifiers live.** He says to hold the
subscription boxes for now. "For now" is half the ruling. Recording it as a decline turns a
pause into a kill, and the next session, reading the ledger in good faith, will never
reopen it. Transcribe what was said, exactly, and let the qualifiers survive into
`DECISIONS.md`; paraphrase is where a decision quietly becomes what the session wished
had been decided.

**Some rulings arrive as acts rather than sentences.** When the operator books the
delivery van's service for every Thursday, the standing question about which day the
second route runs has been answered, whether or not anyone said so. Recognise it, write
it down as a ruling with its source named as conduct, and close the open ask. An
unrecorded answer keeps costing attention every time the question comes back around.

**A finding resting on an assumption never stated as one gets withdrawn and corrected
on the record.** Do not let "probably not achievable" ship as fact when the honest
version was "not achievable if X, and X was never checked." When you reverse an
earlier default against your own preference even though the evidence points the
other way, have whoever executes the reversal state the contrary evidence back to
you before you rule, and keep that evidence on file, annotated with the ruling that
overrode it.

**A ruling about a replaceable or versioned artifact states explicitly which
generation it governs.** Otherwise the version currently shipping can be left
silently ungoverned by a ruling that was really meant for its successor.

Source: ops/JUDGMENT_CRAFT.md §9 (moved into this skill 2026-09-16)
