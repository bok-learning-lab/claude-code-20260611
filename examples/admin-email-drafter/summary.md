# admin-email-drafter

A worked example for the June 2026 series, built for Day 4. It drafts an administrator's
reply to a student's questions about undergraduate program requirements — answering each question
strictly from authoritative source material, citing every claim, and flagging anything the
sources don't settle. Claude drafts; the administrator reviews, edits, and sends.

## The move it demonstrates

Routine advising email is high-volume and high-stakes at once: the answers must be *correct*
(a wrong course count or pass/fail rule misleads a student) and they must sound like the person
sending them. The move here is **grounded drafting with a source hierarchy** — Claude locates the
governing passage in the official requirements, answers in the administrator's own voice, and is
explicit about the line between "the requirements say X" and "this is the kind of thing to confirm
at an advising meeting." It never improvises policy.

## How it works

The skill [`/draft-reply`](.claude/skills/draft-reply/SKILL.md) takes the student email in the live
inbox, `inputs/emails/`, whose final message is an unanswered question. It:

1. Reads the email — pulls the concentration, the student's name, the open questions (in order),
   and any follow-up the administrator already promised. For the voice and sign-off it uses the
   most recent admin reply in the thread, or — for a first-contact email with no prior reply — the
   exemplar threads in `inputs/sample-emails/`.
2. Locates the governing passage for each question in the **authoritative** sources, respecting a
   source hierarchy (see below).
3. Drafts a clean, sendable reply in the administrator's voice.
4. Appends a "Sources and open items" section — a citation for each answer and a list of anything
   the human must confirm before sending.

The worked run on the demo email ([inputs/emails/secondary-field.md](inputs/emails/secondary-field.md))
lives in [outputs/](outputs/); its voice is drawn from the sample threads.

## The source hierarchy (the heart of the example)

The interesting design problem is that `inputs/` mixes authoritative and non-authoritative
material — even within a single folder. `inputs/department/` holds both official department
materials and a student-written guide. The skill sorts everything into three tiers:

- **Authoritative — College policy:** the official **Fields of Concentration** entries
  (`inputs/college/fields-of-concentration/primary` and `secondary`) and the **Harvard College
  Student Handbook**. The canonical statement of what a requirement is.
- **Authoritative — department operational materials** (Office of Undergraduate Studies in
  Chemistry / FAS CCB): the research-for-credit page, the advanced-lab petition guidelines and
  form, the advanced-lab course descriptions, and the term course offerings. These supply the
  *mechanics* the Fields entry only gestures at (how CHEM 98R is graded, how the advanced-lab
  petition works).
- **Supplementary — student perspective:** `inputs/department/guide-to-chemistry.md`, the
  **Harvard Chemistry Club's** student-written *Guide to Chemistry*, accurate only "as of
  September 5, 2025." Useful for soft, experiential questions but never a source of policy.

The skill cites department materials for mechanics, defers to College policy on what a requirement
is, treats the club guide as a peer perspective it attributes as such, and flags anything that
depends on stale or person-specific facts for human confirmation. That sorting — and being honest
in the draft about what is settled versus what needs an advising conversation — is the transferable
lesson.

## What you can translate this to

- Any office that answers recurring policy questions from a stable rule set: registrar, financial
  aid, study-abroad, graduate program requirements, HR benefits.
- Swap the `inputs/` requirements files for your own canonical sources, keep the source-hierarchy
  discipline, and the skill drafts grounded, in-voice replies that a human signs off.
- The pattern generalizes beyond email: any "answer faithfully from an authoritative corpus, cite
  it, and flag the gaps" task.

## Adapting this folder for your department

The demo is Chemistry, but nothing in the skill is Chemistry-specific except the source map. The
division of labor is simple: **you supply the documents, Claude does the sorting and the
re-mapping.** You don't have to understand the tier system or edit the source map yourself.

**Your job — gather good sources.** Replace the demo content in `inputs/` with your office's
authoritative documents: your program's official requirements and your institution's handbook,
your office's operational materials (forms, grading rules, course offerings), and any
student- or third-party-authored material you'd want cited only as perspective (PDFs are fine).
Put a few prior threads that show your office's house voice in `inputs/sample-emails/`, and the
student email you actually want answered in `inputs/emails/`. You just need the documents to be the
*right, current* ones — don't worry about organizing them.

**Claude's job — sort and re-map.** Open the folder and ask Claude to set it up for your context.
Working from the documents you added, Claude will:

- **Sort each source into the three tiers** (see "The source hierarchy" above) — canonical policy,
  operational materials, perspective-only — and record that tiering in `SKILL.md`.
- **Convert the frequently-read documents to Markdown**, keeping the original PDF in the folder as
  the source of record (as the Chemistry demo keeps `chem-adv-lab-petition.pdf` alongside
  `chem-adv-lab-petition.md`), because `.md` is cheaper and more reliable for the skill to read and
  cite.
- **Rewrite `reference/source-map.md` for your context** — the file-to-question mapping and the
  quick-reference of your most-asked answers — which is what lets the skill find the governing
  passage instead of guessing.

Then **review what Claude proposed** — especially the tiering (is this document really
authoritative?) and the source map — and run `/draft-reply inputs/emails/<your-email>.md`. As
always, you are the one who reviews the draft and sends it.

## How to run it

The skill lives in `.claude/skills/draft-reply/`, so a session rooted in this folder picks it up
automatically — no install step. Point it at the email in the inbox:

```
/draft-reply inputs/emails/secondary-field.md
```

Drafts land in `outputs/`.
