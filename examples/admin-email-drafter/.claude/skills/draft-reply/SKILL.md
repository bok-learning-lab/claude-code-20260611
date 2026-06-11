---
name: draft-reply
description: >-
  Draft an administrator's reply to the final unanswered student email in a thread, answering
  each question about undergraduate program requirements (concentration and secondary-field
  requirements, courses, tutorials, pass/fail, thesis, honors, research) strictly from the
  authoritative source files in inputs/, citing each claim and flagging anything the sources
  do not settle. Use when the user runs /draft-reply, points at an email in
  inputs/emails/, or asks you to draft a reply answering a student's questions about program
  requirements. Claude drafts; the administrator reviews and sends.
---

# /draft-reply — draft an administrator's reply to a student's requirements question

Given a student–admin email thread whose most recent message is an unanswered student
question, draft the administrator's reply. Answer every open question about undergraduate
program requirements, grounded **only** in the authoritative source files, in the voice of the
administrator who has been answering the thread. The draft is for a human to review, edit, and
send — never to send automatically.

This skill does not decide policy and does not improvise it. It locates the governing passage,
states the answer in plain language, and tells the administrator exactly where it came from and
what (if anything) still needs a human to confirm.

## Inputs

- **Email to answer** (required): a path to a message or thread in `inputs/emails/`
  (e.g. `inputs/emails/secondary-field.md`). This is the live inbox — the student email whose
  final unanswered message you draft a reply to. The user passes it in the invocation
  (`/draft-reply inputs/emails/secondary-field.md`). If they didn't, ask once: "Which email
  should I draft a reply to? (e.g. `inputs/emails/secondary-field.md`)"
- **Voice reference** (always consult): `inputs/sample-emails/` holds prior threads that
  exemplify the office's house voice — its greeting, register, and sign-off block, and which
  administrator signs. Read them to match that voice. This matters most when the email to answer
  is a first contact with **no prior administrator reply** in its own thread: there is no in-thread
  signature to copy, so the voice and sign-off come from the samples.

All paths in this skill are relative to the project root (the folder containing `inputs/`).

## The source hierarchy (read this before drafting)

Not every file in `inputs/` is authoritative, and `inputs/department/` is **mixed** — it holds
both official department materials and a student-written guide. Treat sources in this order, and
**never let a lower tier override a higher one**:

1. **Authoritative — College policy.** The canonical statement of what a degree requires.
   - `inputs/college/fields-of-concentration/primary/<slug>.md` — the concentration's
     requirements (basic and honors).
   - `inputs/college/fields-of-concentration/secondary/<slug>.md` — the secondary field.
   - `inputs/college/harvard-college-student-handbook.pdf` — College-wide policy (e.g.
     drop/withdraw rules, credit requirements) when the concentration file defers or is silent.
2. **Authoritative — department operational materials.** Issued by the Office of Undergraduate
   Studies in Chemistry / FAS Chemistry & Chemical Biology. These give the operational detail the
   Fields entry only gestures at — use them for the *mechanics* of a requirement, but defer to
   tier 1 on what the requirement *is*. (Cite the `.md` files below; they are faithful text
   extractions of the department PDFs, which remain in the folder as the originals of record.)
   - `inputs/department/chem-91r-98r-99r.md` — research-for-credit (CHEM 91R/98R/99R): eligibility,
     SAT/UNS grading, the credit-vs-pay rule, workload expectations.
   - `inputs/department/chem-adv-lab-petition.md` — guidelines + petition form for using two
     consecutive semesters of research-for-credit to fulfill the Advanced Laboratory requirement.
   - `inputs/department/adv-chem-lab-courses.md` — descriptions and prerequisites of the four
     advanced lab courses (CHEM 100R/135/145/165).
   - `inputs/department/chemistry-course-offerings.md` — which courses run which term, with
     instructors and prep. Term-specific; carries a "double-check My.Harvard" caveat — cite as
     *current offering*, not permanent rule.
3. **Supplementary — student perspective, not policy.** `inputs/department/guide-to-chemistry.md`
   is the **Harvard Chemistry Club's** student-written *Guide to Chemistry*, accurate only "as of
   September 5, 2025" and explicitly liable to go stale. Use it **only** for soft, process
   questions tiers 1–2 don't cover (e.g. how students approach professors about research), and
   **always attribute it as student advice**, never as a requirement. If it conflicts with a
   higher tier, the higher tier wins and the guide is ignored.

If a question can't be answered from tiers 1–2 and is only touched by tier 3, the answer must say
so and point the student to the office of record — do not present club advice as policy.

See [reference/source-map.md](reference/source-map.md) for which file and section answers each
common question type, and for how a `concentration:` slug maps to a requirements file.

## Procedure

### Step 1 — Read the thread

1. Read the thread file. From the YAML frontmatter, note `concentration:` (the slug) and
   `topic:`. If absent, infer the concentration from the body.
2. Identify the **student's name**. Then identify the **administrator's identity and full sign-off
   block**: from the most recent administrator message in the thread if there is one; otherwise
   (a first-contact email with no prior admin reply) from `inputs/sample-emails/`, which shows who
   signs for this office and in what form. Preserve names exactly; never re-spell.
3. Enumerate the **open questions** in the final (student) email as a numbered list. Answer
   them in the student's order.
4. Note any **promises the administrator already made** earlier in the thread (e.g. "I'll
   confirm the exact number in a follow-up"). These are must-answer items even if the student
   didn't repeat them.

### Step 2 — Locate the governing passages

For each open question, find the passage that settles it, using the source hierarchy and
[reference/source-map.md](reference/source-map.md):

- Open the primary (or secondary) requirements file by slug.
- For each answer, record the **citation**: file + the requirement item or heading (e.g.
  `chemistry.md` item 5b; `chemistry.md` "Honors Eligibility Requirements" item 1c).
- For the *mechanics* of a requirement — how research-for-credit is graded, how the advanced-lab
  petition works, what runs which term — consult the tier-2 department materials and cite them
  alongside the Fields entry they operationalize.
- If the concentration file defers to College-wide policy, consult the handbook PDF.
- Only if a question is purely procedural and unaddressed by tiers 1–2, check the student guide —
  and mark that answer as student-perspective, to be confirmed.

### Step 3 — Draft the reply

Write a clean, student-facing email:

- Open with a greeting matching the house register (from the thread, or from the samples),
  addressed to the student by name.
- Answer each open question **in the student's order**, in plain language. Lead with the
  bottom-line answer, then the necessary specifics (counts, course codes, grading basis).
- Resolve any earlier promise the administrator made.
- Where a question isn't fully settled by the authoritative sources, say what *is* known and
  name the next step (an advising meeting, the DUS office) rather than guessing.
- Close with the administrator's exact sign-off block — from the thread if present, otherwise the
  one the samples establish for this office.

The student-facing body carries **no citations and no bracketed notes** — it should read as a
sendable email. All sourcing goes in the appendix (Step 4).

### Step 4 — Write the draft file

Write to `outputs/<slug>-<topic-slug>-reply.md`. Use this structure:

```markdown
---
title: "Draft reply — <concentration>: <topic>"
type: email-draft
concentration: <slug>
in_reply_to: <thread filename>
status: draft-for-review
drafted: <date>
---

# Draft reply — <concentration>: <topic>

> Draft for review. Verify the flagged items below, then edit and send. Not auto-sent.

## Email body

<the student-facing reply, greeting through sign-off — clean, no citations>

---

## Sources and open items (not part of the email)

### Where each answer comes from

| Student's question | Answer in brief | Source |
|---|---|---|
| 1. ... | ... | `chemistry.md` item 5b |
| 2. ... | ... | `chemistry.md` items 1, 5a |

### Flag for you to confirm before sending

- <Anything not fully settled by the authoritative sources, or drawn from the student-run
  guide, or that depends on the student's specific record. If nothing, write "None.">
```

### Step 5 — Report back

In 3–6 lines: where the draft is (markdown link), which questions you answered and from which
source, and — most important — the single most consequential item the administrator should
verify before sending. Do not paste the whole draft into the reply.

## Hard constraints

- **Claude drafts; the administrator sends.** Every output is a draft for human review and
  signature. Never describe an email as sent, and never auto-send one.
- **Never invent policy.** Counts, course codes, grading bases, deadlines, names, and
  eligibility rules must each trace to a passage in an authoritative source. If the sources
  don't answer it, the draft says so and points to the office of record — it does not guess.
- **Respect the source hierarchy.** The student-run *Guide to Chemistry* is never a source of
  policy. Attribute anything drawn from it as student advice and mark it for confirmation; if it
  conflicts with a requirements file, the requirements file wins.
- **Cite every substantive claim** in the appendix, by file + requirement item or heading.
  Citations never appear in the student-facing body.
- **Answer every open question**, in the student's order, plus any follow-up the administrator
  already promised.
- **Match the administrator's voice and sign-off** — from the thread, or from
  `inputs/sample-emails/` when the email to answer has no prior admin reply. Don't impose a generic
  tone or invent a new signature.
- **Preserve names and course codes exactly** — students, administrators, advisors, courses.
- **No emojis.** Anywhere. Markdown links for any file references in the appendix.

## Worked example

The live email [inputs/emails/secondary-field.md](../../../inputs/emails/secondary-field.md) has
been run through this skill; the draft is at
[outputs/chemistry-secondary-field-reply.md](../../../outputs/chemistry-secondary-field-reply.md).
It is a first-contact message with no prior admin reply, so its voice and sign-off (the demo's
office signer, Dr. John Smith) are drawn from the threads in
[inputs/sample-emails/](../../../inputs/sample-emails/). The three
questions — course count and grading, whether a CHEM 91R research term counts, and study-abroad
credit — are answerable from the secondary-field requirements file, with the letter-grade
interaction and the study-abroad petition flagged for human confirmation.
