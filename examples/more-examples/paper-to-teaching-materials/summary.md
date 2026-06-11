# Paper to teaching materials

A worked example of using Claude Code to **build and run teaching material** for a philosophy session, grounded in a single source paper:

> Grant, D. G., Behrends, J., & Basl, J. (2025). "What we owe to decision-subjects: beyond transparency and explanation in automated decision-making." *Philosophical Studies* 182, 55–85. (Open access, CC BY 4.0.)

Built for the *Summer of Claude* faculty workshop at Harvard's Bok Center. Jeff Behrends is among the workshop participants, so the design choices throughout are made to align with **his** paper's framework and its careful hedges — not with a generic "AI ethics" take.

The companion landing page that previously sat at the top of the folder is folded into the relevant sections below; the produced version of it is now at [outputs/case-study.html](outputs/case-study.html). The plan and the brainstorm that scheduled the build are folded into "how we built it."

---

## The self-referential point (read this first)

The workshop is teaching faculty to lean on an AI tool. Behrends' paper is precisely about the **limits of relying on AI for consequential decisions about people.** That tension is the lesson, not a problem to hide. So this project models the relationship the paper *prescribes*:

- Claude **augments the instructor's own reasoning** and generates teaching material.
- Claude **never makes the consequential call** — it surfaces candidates for human judgment, drafts cases, maps arguments. The human stays the moral agent.
- That is exactly the "human-in-the-loop with genuine agential consideration" the paper contrasts (§7.3) with blind deference and automation bias.

If a skill or output ever positions Claude as the *decider* about how a person should be treated, it has violated the paper it is built on.

---

## What it is

Four Claude Code skills, scoped to this project's `.claude/skills/` directory, plus the source paper in `inputs/` and the published landing page in `outputs/`.

- **`/teaching-case`** generates a student-facing case (a system dossier or a thought experiment) plus separate instructor notes that name the target move, tie it to a section of the paper, and flag the trap. Given a target move (accuracy §5.1, ignoring-evidence §5.2, inadmissible-evidence §5.3, decision-rules §7.1, or agential-consideration §7.2–7.3) and optionally a domain (bail, hiring, lending, admissions, medicine), it produces a case a seminar can read cold and instructor notes that defend every claim by section. Offers to generate a "decoy" variant (a case that should *pass* the audit — the construct-validity stress test) when asked.
- **`/discussion-plan`** generates a Socratic sequence for a given case or section of the paper: warm-up that elicits the intuitive transparency answer, the core dilemma, the positions students will likely take (anticipating S1–S3), the objection to steer toward (one of the three named Problems), the move in the paper that addresses it, and an honest note on what the case can and cannot show. Walks students *from* transparency *to* due consideration rather than asserting the destination.
- **`/objection-audit`** takes a student argument and **steelmans it first**, then diagnoses it against the framework: which distinction it misses or which Problem it falls to, with section citations, and a closing prompt for the student to push back on. Always "right about X, misses Y," never a flat "wrong." Genuine steelman; specific diagnosis; ends by inviting the student's response, not closing the question.
- **`/quiz`** generates a short-answer comprehension check on the core argument, with a student version and an instructor answer key.

The corpus the skills operate on lives in `inputs/`:

- [inputs/grant_behrends_basl.pdf](inputs/grant_behrends_basl.pdf) — the source paper.
- [inputs/grant_behrends_basl.md](inputs/grant_behrends_basl.md) — markdown digest of the paper for fast reading and citation lookup.

The published landing page that walks a visitor through the whole project — what it is, what we're teaching and why, the skills, the cases and student arguments they operate on, the constraints, the build story — is at [outputs/case-study.html](outputs/case-study.html). It is the artifact for sharing the project with a colleague who is not going to clone the folder.

### The framework these skills apply

The paper defends the **Explainability Thesis**: in many contexts, decision-makers are morally obligated *not* to base decisions about people on the outputs of black-box AI systems. It grounds this not in **duties of transparency** (the standard "you must be able to explain it" defense, which the paper argues is too narrow — the *Grounding Problem*) but in the duty to show **due consideration** to decision-subjects.

Due consideration decomposes into **duties of consideration**:

- **Evidential consideration** (§5, constrains fact-finding). Black-box reliance fails three ways: degraded field **accuracy** / overfitting (§5.1, the "Jared" screener); **ignoring readily available evidence** a human wouldn't (§5.2, COMPAS + the excised brain-tumor neurologist); relying on **morally inadmissible evidence** (§5.3, redundantly-encoded race/gender, the Amazon "women's" résumé tool, proxies).
- **Practical consideration** (§7, constrains decision-making). Prohibited **decision rules** / the Kantian injunction against treating people as mere things (§7.1); and **agential consideration** (§7.2–7.3) — some decisions (jury verdicts, lethal force, punishment) must be made by full-blown moral agents who take responsibility. The **Juror Substitution** thought experiment carries this; HITL doesn't escape it if the human merely defers.

Two framing problems the paper also solves: the **Definition Problem** (what "black box" means: high flexibility + high dimensionality + limited **rule transparency**, §4) and the **Double Standard Problem** (why hold machines to a higher bar than human experts, §6 — partly it generalizes to humans, but **interpretable models** are the safer third option and humans have agential capacities).

The three Problems (Definition, Double Standard, Grounding) are the objection-handling exercises the skills walk students through.

---

## How we built it

The brainstorm-and-build sequence mirrors the [interview-coding](../interview-coding/summary.md) shape (Mary Waters' paper there; Jeff Behrends' paper here) but in a teaching register rather than a research register. The arc a teacher actually runs — make the material, plan the conversation, anticipate the pushback — became the demo trio: `/teaching-case`, `/discussion-plan`, `/objection-audit`. `/quiz` was added because the paper's clean taxonomy is unusually well-suited to a comprehension check.

**Step 1 — Brief Claude on the paper and the audience reality.** A single prompt that points at the source paper, names the framework, and explicitly names the workshop participant whose framework it is: *"Jeff Behrends is among the workshop participants, so the design choices throughout should align with his paper's framework and its careful hedges."* The paper acts as one constraint; Jeff's presence acts as a second.

**Step 2 — Capture the brainstorm.** The result was a working brainstorm: what the paper gives a teacher to work with (a headline thesis with careful hedges, a reframing move from transparency to due consideration, a clean taxonomy that maps onto discussion structure, memorable cases already in the text, three named Problems that are ready-made objection-handling exercises), a menu of teaching use cases, a skills catalog with each skill tied to a section, and an explicit "what to avoid in front of Jeff" section — the analog of the Mary-Waters "never pitch LLMs as discovering themes" rule.

**Step 3 — Convert the brainstorm into a parallelizable plan.** Three self-contained skill-build tasks, each copy-pasteable into a fresh Claude Code session, with shared context (required reading, hard constraints, output conventions) and per-task scope (skill behavior, what good output looks like, what to avoid, how to validate).

**Step 4 — Run parallel sessions, audit, promote.** Each session built its skill at `.claude/skills/<name>/` with a `SKILL.md` and a `examples/` directory of validated runs. After the returns, an audit pass against the corpus — the most common failure mode for these skills is plausible-but-overclaimed citations (page numbers given without verification against the PDF). Every section/page reference verified before promotion.

**Step 5 — Build a synthetic corpus to demo against.** Four cases (C1–C4) and three student arguments (S1–S3), each engineered to surface a specific move in the framework. C3 in particular is the construct-validity stress test — a case designed to *pass* the audit, so the skill is forced to discriminate. The three student arguments are designed to be instructively wrong in ways the paper diagnoses, so `/objection-audit` has clean targets.

**Step 6 — Build the published landing page.** The case-study HTML at `outputs/case-study.html` walks a visitor through the project end-to-end — what it is, what we're teaching, the skills, what they produce, the corpus they operate on, the constraints they obey, the build story, and a one-screen summary of the paper. The audience is the colleague who is not going to clone the folder.

### Things this approach taught us

Naming the methodological author in the room is half the alignment work. *"Jeff is in the room"* is a stronger constraint on the design than any abstract "respect the paper's hedges" instruction. The presence of the author makes the model conservative in the right way.

The four skills mirror the four moves a careful teacher makes — make the material, plan the conversation, anticipate the pushback, check that the framework landed. The skills do not replace the teacher's judgment; they take the parts of the work that scale poorly (drafting cases that isolate one move, anticipating three positions a class might take, steelmanning a student paper) and make them cheap.

The audit step is not optional. The most common failure of skills like `/teaching-case` is plausible-but-overclaimed page citations — the model produces a confident "§5.2, p. 71" that turns out to be §5.3 or off by two pages. Verify every section reference and page number against the PDF before promotion. A confident wrong citation in front of the paper's author is the worst possible workshop outcome.

The decoy case (C3, the one designed to *pass*) is the single most useful piece of corpus discipline. Without it, the skills would have learned only to surface failures; with it, they have to discriminate. Construct-validity stress tests do for skill-building what negative-case analysis does for qualitative coding.

---

## What you can translate this to

The pattern is **a defining paper + a named author whose hedges matter + a multi-skill teaching toolkit that operationalizes the paper's moves**. It applies to any seminar or course that turns on a single dense source — and most graduate seminars do.

Domains where the same shape applies almost without modification:

- **Any seminar grounded in a single paper or book.** Replace the Grant–Behrends–Basl paper with the work you actually teach. Build `/teaching-case`, `/discussion-plan`, `/objection-audit`, and `/quiz` scoped to *that* framework. The four-skill pattern is invariant; the framework changes.
- **Course design from a methodological framework** — replace the paper with Wiggins & McTighe's *Understanding by Design*, or a clinical guideline, or a legal doctrine, and build skills that produce cases, plans, and audits against that framework.
- **Ethics-of-X teaching modules** — bioethics, business ethics, research ethics, AI ethics. The "what to avoid in front of [author]" section becomes "what to avoid in front of [the field's defining critic]."
- **Graduate-level argument-mapping projects** — every philosophy paper has a thesis, hedges, distinctions, and named problems. The toolkit ports almost verbatim.
- **Clinical reasoning case banks** built from a single framework paper or guideline — same `/teaching-case` shape, with the audit step calibrated to clinical specificity rather than philosophical citation.

Candidate operations the workshop attendee could implement against this corpus:

- `/map-argument` — render the paper's structure as a diagram or outline for lecture use.
- `/reading-guide` — pre-class questions keyed to sections.
- `/rubric-item` — exam/problem-set prompt with a rubric keyed to the paper's distinctions.
- `/structured-debate` — assign the three Problems as positions, with prep memos for each side.
- `/cross-domain-transfer` — take one case (bail) and reskin it into medicine and lending so students practice spotting the same duty.

The pattern in all of these is the same: a defining source, a small toolkit that operationalizes its moves, a corpus engineered to surface specific challenges, an audit step that catches plausible overclaims, and a published landing page that shares the work with colleagues who are not going to clone the folder.

---

## Alignment constraints (the hard ones)

These come from the Grant–Behrends–Basl paper and apply to everything Claude does in this project. They also survive translation to other domains:

- **Claude is never the decision-maker about a person.** Frame Claude as augmenting the instructor and generating material. Never as the adjudicator.
- **Don't collapse transparency into due consideration.** The paper's central move is that due consideration is *broader* than, and not reducible to, transparency. Cases and discussion plans must keep the distinction live.
- **The Explainability Thesis is not absolute.** The authors say "often," "prima facie," "potentially overridable," "context-sensitive." Never present it as "never use black boxes." Don't oversell.
- **Interpretable models are safer, not a panacea** (§6). They are *less* prone to the failures, not immune.
- **Keep the three Problems distinct** (Definition, Double Standard, Grounding) and tie claims to a section or page when you can. Defensible beats vibes.
- **Black-box ≠ "any AI."** The paper's target is high-flexibility, high-dimensional, low-rule-transparency systems (§4) — not all automation.
- **Cite by section** (§5.2) — page numbers only if verified against the PDF. The audit step is not optional.
- **Stable IDs.** C1–C4 (cases) and S1–S3 (student arguments) must be preserved consistently across every skill output.
- **No emojis.**
