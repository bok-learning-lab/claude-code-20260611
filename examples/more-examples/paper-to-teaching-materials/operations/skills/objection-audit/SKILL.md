---
name: objection-audit
description: >-
  Stress-test a student argument against the framework of Grant, Behrends & Basl, "What we
  owe to decision-subjects." Steelmans the argument first, then diagnoses which distinction
  it misses or which objection (Definition / Double Standard / Grounding) it falls to, with
  section citations, and ends by inviting the student's reply. Use when the user runs
  /objection-audit, asks to evaluate, stress-test, or respond to a student's argument or a
  proposed position on the paper, or wants a "right about X, misses Y" memo.
---

# /objection-audit — stress-test a student argument

Produce a memo a TA could hand back: a genuine steelman, then a specific diagnosis against
the paper, then an opening for the student to push back. Never a flat "wrong."

## Inputs

- **Argument** (required): a student-argument ID (S1–S3), a path, or pasted text.

## Process

1. **Steelman.** State the strongest honest version and name what it gets *right* — there
   is almost always a real duty or intuition in the vicinity.
2. **Diagnose.** Identify the distinction missed or the Problem it falls to, with the
   section that addresses it. Be specific; "it's biased" is not a diagnosis.
3. **Open it back up.** End with a question or reformulation challenge that hands the next
   move to the student.

## Output

One markdown file per argument, with three labeled parts — **Steelman**, **Where it falls
short**, **Back to you**. Write audits to the skill's `examples/` (for demos) or to
`output/objection-audits/`.

## Hard constraints (inherited — see ../../../prompts/CLAUDE.md)

- **Claude does not grade or rule on the student.** It produces the analytic memo; the
  instructor owns marks and final judgment.
- **Steelman before diagnosis, always.** No verdict-without-steelman; no strawmanning.
- **Don't deny true premises.** For S2, do not deny that humans are opaque — deploy the
  interpretable third option instead.
- **Keep transparency vs. due consideration distinct. Cite by section; never invent a
  page number. No emojis.**

## Worked examples

Audits of all three corpus arguments (also promoted to `output/objection-audits/`):

- [examples/audit-S1.md](examples/audit-S1.md) — accuracy-is-all (§5).
- [examples/audit-S2.md](examples/audit-S2.md) — double standard (§6).
- [examples/audit-S3.md](examples/audit-S3.md) — human-in-the-loop (§7.3).
