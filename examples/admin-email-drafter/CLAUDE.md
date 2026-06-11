# CLAUDE.md — admin email drafter

Project-level instructions loaded when Claude Code starts in this folder.

## What this project is

A worked example of using Claude Code to **draft administrative replies to students' questions
about undergraduate program requirements**, grounded strictly in authoritative source material.
A student emails the concentration office about requirements (courses, tracks, pass/fail, the
thesis, honors, research); this project drafts the administrator's reply, answering every question
from the requirements files in `inputs/`, citing each claim, and flagging anything the sources
don't settle. **Claude drafts; the administrator reviews, edits, and sends.**

The drafting move is captured as a project-scoped skill, `/draft-reply`, in
[.claude/skills/draft-reply/](.claude/skills/draft-reply/).

## If you just opened this folder

1. [summary.md](summary.md) — what this is, how it was built, what you can translate it to, and
   an "Adapting this folder for your department" guide for retargeting it to another office.
2. [.claude/skills/draft-reply/SKILL.md](.claude/skills/draft-reply/SKILL.md) — the skill,
   including the source hierarchy it relies on.
3. The live student email in [inputs/emails/](inputs/emails/), the voice-reference threads in
   [inputs/sample-emails/](inputs/sample-emails/), and the generated draft in [outputs/](outputs/).

## Running the skill

The skill lives in `.claude/skills/`, so a session rooted here picks it up automatically. Point it
at the email in the inbox:

```
/draft-reply inputs/emails/secondary-field.md
```

Drafts land in `outputs/`.

## The source hierarchy (the central design constraint)

Not everything in `inputs/` is authoritative, and `inputs/department/` is **mixed**. The skill —
and anyone drafting here — must keep these tiers straight and never let a lower tier override a
higher one:

1. **Authoritative — College policy.** `inputs/college/fields-of-concentration/primary/<slug>.md`
   and `secondary/<slug>.md` (the official Fields of Concentration entries), and
   `inputs/college/harvard-college-student-handbook.pdf`. The canonical statement of what a
   requirement *is*.
2. **Authoritative — department operational materials** (Office of Undergraduate Studies in
   Chemistry / FAS CCB): `chem-91r-98r-99r.md` (research-for-credit), `chem-adv-lab-petition.md`
   (advanced-lab petition), `adv-chem-lab-courses.md` (the four advanced lab courses),
   `chemistry-course-offerings.md` (term offerings). Cite the `.md` files (faithful extractions of
   the department PDFs, which stay in the folder as originals). Use for the *mechanics* of a
   requirement; defer to tier 1 on what the requirement is.
3. **Supplementary (student perspective, not policy).** `inputs/department/guide-to-chemistry.md`
   — the **Harvard Chemistry Club's** student-written guide, accurate only "as of September 5,
   2025." Use only for soft process questions tiers 1-2 don't cover, always attribute it as student
   advice, and defer to a higher tier on any conflict.

## Conventions

- **The skill lives in `.claude/skills/draft-reply/`** — project-scoped, so it travels with the
  folder and runs as a slash command without an install step.
- **`inputs/` is read-only.** Don't modify the requirements files, threads, or PDFs. Drafts go in
  `outputs/`; regenerating overwrites.
- **Two email folders, distinct roles.** `inputs/emails/` is the live inbox — the student email to
  answer. `inputs/sample-emails/` holds prior threads that exemplify the office's house voice and
  signature; the skill reads them to match tone and sign-off (essential for a first-contact email
  with no prior admin reply).
- **Never invent policy.** Counts, course codes, grading rules, names, and deadlines must each
  trace to an authoritative source passage. If the sources don't answer it, say so and point to
  the office of record.
- **Drafts are for human review and signature** — never auto-sent.
- **Preserve names and course codes exactly.** Match the administrator's voice and sign-off from
  the thread, or from `inputs/sample-emails/` when the email has no prior admin reply.
- **No emojis** in any file. **Markdown link syntax** for file references.
