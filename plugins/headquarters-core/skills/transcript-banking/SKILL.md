---
name: transcript-banking
description: A raw transcript export needs banking into the vault: the ritual is design-only — get the operator's explicit go-ahead before building any tooling; it touches the vault by definition (gate G5).
---

# Transcript Banking

*Design-only, not yet built. Do not build this ritual's tooling casually — confirm
with the operator before starting, since it touches `vault/` by definition (gate
G5).*

1. **Vault rules are absolute, not situational (gate G5).** Raw transcripts are C3.
   They live in `vault/raw/` (gitignored, local-only) and never commit, never push,
   never enter an unattended run's context, no exception, no matter how useful a
   single quote would be in a draft.
2. Only the Chief of Staff seat touches `vault/`, and only in a live, interactive
   session on the operator's explicit word. This never runs unattended, and no other
   seat or function reads `vault/` under any circumstance.
3. When run: the operator drops a raw transcript export into `vault/raw/`. A banking
   pass, at scanning tier (`org/models.yml` duty `research-and-indexing`), produces
   one index card per transcript into `transcripts/index/`: date, participants as
   role-plus-initials, ventures touched, commitments made by either side, follow-ups
   with owners, and pointers back into the vault by line range.
4. **Redaction rule:** a card never carries more third-party verbatim than the
   minimum needed to anchor its pointer. Cards are C1/C2; the raw source stays C3 in
   the vault, always.
5. Retrieval is grep-first over `transcripts/index/`. Any seat needing the raw
   source behind a card escalates to the Chief of Staff seat; no seat other than the
   Chief of Staff opens `vault/` directly to answer that escalation.
6. Commitments surfaced in a card feed General Counsel (contract triggers) and the
   CRO's follow-up list; decisions surfaced feed `DECISIONS.md`.

Source: generalized from the operator's private doctrine, §2.7 (moved into this
skill 2026-09-16).
