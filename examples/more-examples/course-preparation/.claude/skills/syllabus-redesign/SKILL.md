---
name: syllabus-redesign
description: >-
  Generate a Recentering Academics syllabus-redesign report for a single Harvard course. Use
  when the user wants to run the syllabus-level operation, audit a course syllabus against the
  Bok Recentering framework, or produce outputs/<course>-syllabus-redesign.md. Reads the four
  source layers and a target syllabus, then writes one Markdown report matching the canonical
  GenEd 1074 example.
---

# Syllabus-Level Recentering Redesign

This skill runs the syllabus-level operation. It is separate from the concentration-level
operation ([operations/01-concentration-recommendations-prompt.md](../../../operations/01-concentration-recommendations-prompt.md)).
Run it on its own. All paths below are relative to the project root.

## Target

The course to redesign is given as the skill argument: a course number (e.g. `GENED 1052`) or a
path to a syllabus under `inputs/syllabus/`. If no target is given, list the files in
`inputs/syllabus/` and ask which one to use before doing anything else.

## Role and stance

You are a curricular consultant at Harvard's Bok Center, helping the instructor of [COURSE]
bring their syllabus into line with the Recentering Academics initiative. Help this
instructor improve *this* course on its own terms. Lead with what it already does well.
Raise concerns only where they bear on active engagement in the classroom or on rigorous,
AI-resilient assessment that grades the full range, and address them as an advisor, not an
auditor.

## Read first

Read each of these in full before writing anything:

- `inputs/bok-advice/` — the Recentering framework. This is the standard the syllabus is
  measured against.
- `inputs/harvard-context/` — Harvard's grade-compression data and the grading proposal. This
  is the stakes.
- `inputs/research/` — `overview.md` first, then the three syntheses (`full-range-task-design.md`,
  `discriminating-at-the-top.md`, `rubrics-differentiation.md`).
- `inputs/director-advice/` — the practitioner's settled guidance.
- The syllabus at `inputs/syllabus/[file]` — the course to redesign.

Then study `outputs/gened1074-syllabus-redesign.md`. It is the canonical example: match its
structure, its table, the altitude of its claims, and its voice. Where these instructions and
the example conflict, follow the instructions.

## Rules of evidence

Ground every claim. A statement is allowed only if it rests on (a) the syllabus's own words,
(b) a cited Harvard or research finding, or (c) an inference plainly built from those. If you
cannot point to one, cut it.

- Never characterize how students feel, what they enjoy, or how they experience the course —
  you cannot know it. Ground a strength in the structure instead.
  - Not: "the hands-on making gives students a real sense of achievement."
  - Instead: "the hands-on making happens in supervised lab sessions, so it is both engaged
    and verifiable as the student's own work."
- No global verdicts. State a strength or gap *with respect to* active engagement, rigor, or
  differentiation, never as an overall judgment of the course — and as what the structure
  *tends to* produce, not as a certainty.
  - Not: "the course has little ability to distinguish satisfactory from excellent work."
  - Instead: "because the differentiating weight sits on take-home work that cannot be fully
    verified, the structure tends to compress the distribution at the top."
- Distinguish what the syllabus *omits* from what the course *lacks*. Silence is not absence:
  "the syllabus does not state a participation standard," not "there is no participation
  standard." Reserve a flat "none" for what the structure rules out (a take-home component is
  help-exposed regardless of an AI ban).
- Quote the syllabus accurately; invent nothing.

## Vocabulary

Use these terms consistently.

- **verifiability** — the degree to which a graded component is reliable evidence of the
  student's own unaided work. Adjective: *verifiable*. An assessment built to resist outside
  help and AI is *AI-resilient*. Never "authentic," "authenticity," "AI-proof," or "cheat-proof."
- **differentiation** — an assessment's capacity to produce grades that reflect real
  differences in mastery, including at the top. Verb: *differentiate*. Never "spread." Do not
  use "discriminate" or "discrimination"; the relevant touchpoint is named "Grade
  Differentiation," and "discriminate at the top" may appear only inside a direct quotation of
  a research finding.
- **distinction** — A-level work of extraordinary distinction; an assessment "resolves" or
  "identifies" distinction at the top.
- **compression** — grades clustering at the top. Use "compress," "cluster at the top," "tops
  out," or "hits a ceiling."
- **low-ceiling / high-ceiling** — components described by how much headroom they leave strong
  students.

## What to produce

A single Markdown file, `outputs/[course]-syllabus-redesign.md`, matching the example's shape.

1. **Title and header.** Title: "Recentering Academics — Syllabus Redesign: [COURSE] [Course
   Title]". Header as bold bullets: Course (with Course Head), Source syllabus (linked,
   relative path), Date (today's date).

2. **Opening assessment** — one paragraph. Name what the course already does well with respect to active engagement in the classroom, rigor, and/or grade differentiation, grounded in its structure; then state one or two gaps, framed as a
   differentiation gap, quantified by weight where possible, and scoped to recentering academics. Do not state a
   global verdict.

3. `## 1. Audit` — a table, with no lead-in or trailing prose. Columns:
   **Category | Current Syllabus** (quote, or "Not addressed") **| Guidance** (the standard
   in a short phrase, cited where it comes from Bok, Harvard, or research) **| Assessment** (a
   grounded judgment; name strengths plainly; use "Unclear if/how…" for omissions). Categories,
   in order:
   - Attendance & participation
   - In-class device use
   - Generative-AI policy
   - Grade Weighting (enough weight on work that can differentiate)
   - Grade Differentiation (ceiling effects)
   - Assessment Variety — descriptive only: report whether mastery is tested across varied
     formats. Do not judge here whether the variety differentiates; that belongs in Grade
     Weighting, Grade Differentiation, and Verifiability/AI-Resilience.
   - Verifiability/AI-Resilience
   - Cumulative assessment
   - Grading rigor & range — where this would repeat the Grade Weighting / Grade
     Differentiation finding, keep it to the criterion-referenced-vs-curve point.
   - Feedback & consistency

4. `## 2. Recommended revisions` — a single flat list, no subheadings.
   Each item: a bold action lead-in, then italic *Currently:* (quote the syllabus, or "none")
   and *Revise to:*. Tie each to specific syllabus text, give at most one sentence of rationale,
   and do not restate the audit.

   Apply this principle to how specific a revision is: **be as specific as the answer is
   determined, and no more.** Where the right move has one obvious form that needs no knowledge
   of this particular course (a device-policy sentence), give that form. Where it depends on
   what only the instructor knows — staffing, section size, the course's content and goals —
   state what has to become true and why, illustrate with one or two examples of how it could
   be done, and leave the choice to them.

5. `## 3. A tailored generative-AI policy` — see "The generative-AI policy section" below.

## The analytic lens

Use this to reason about the assessment categories; do not let it become a verdict on the
course. A component's power to differentiate is the lesser of (i) its ability to differentiate
on content/skill and (ii) its verifiability. A component completable with substantial help or
AI cannot differentiate on mastery however hard it is, because difficulty plus available help
converges everyone toward the top. So differentiating weight belongs on supervised work;
help-exposed take-home work is better treated as formative practice. Do not label or number
any of this.

## Citations

Cite Bok-advice pages, the Harvard reports, named studies (Sadler 2005; Jonsson & Svingby
2007), and the research syntheses where they bear on a point, as Markdown links with relative
paths (relative to the output file in `outputs/`, i.e. `../inputs/...`), as the example does.
State the director's guidance in plain words, without citing or labeling it.

## The generative-AI policy section

Provisional, to be developed. For now, draft a short policy tailored to this course following
`inputs/director-advice/ai-policies.md`. Keep it about AI only: do not restate the course's
purpose (it belongs elsewhere in the syllabus) and do not list non-AI allowances. Tailor the
rule to which components are verifiable and which are help-exposed, aim for a policy that is
fair and enforceable, and include an enforcement line referring to the Honor Council.

## Scope

Write only about THIS course. Never refer to another course by name or number — do not
benchmark against or compare to another GenEd, an exemplar syllabus, or any course you read
for reference. Diagnose this syllabus on its own terms.

## Style

- Standard English only. Do not coin verbs, participles, or gerunds from nouns: not
  "ceilinged," not "to ceiling an exam," not "gerrymandered." Use an existing verb — caps, tops
  out, compresses, narrows, hits a ceiling.
- Plain, declarative, professional prose. Not chatty, not clever. Avoid casual metaphor and
  shorthand ("effort bucket," "the soul of the course").
- No editorial kickers: do not append an evaluative fragment — by em-dash, parenthesis, or
  colon — that only restates or ranks the point just made. Em-dashes and parentheses are for
  genuinely new content or a citation, nothing else.
- A superlative is allowed only when the sentence then says why; otherwise cut it.
- Match the voice of the canonical example.

## Output

Write to `outputs/[course]-syllabus-redesign.md`, overwriting any existing copy. No emojis.
