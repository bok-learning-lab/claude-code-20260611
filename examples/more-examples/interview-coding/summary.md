# Interview coding with Claude Code

A worked example of LLM-assisted qualitative interview coding, built to align with Mary Waters' "flexible coding" approach as set out in Deterding & Waters (2018, *Sociological Methods & Research*). The project ships a four-respondent synthetic corpus, three Claude Code skills, and the prompts and audit trail that produced them. Open the folder, read this document, and you can either run the demo end-to-end against the included transcripts or translate the same pattern to your own corpus.

The companion docs that previously sat in `overview/` — a longer summary, a piece on the qualitative-methods tradition behind flexible coding, and a piece on what LLMs change about it — are folded into the relevant sections below. The brainstorm, plan, and conversational walkthrough that produced the artifacts are folded into the "how we built it" section.

---

## What it is

Three Claude Code skills, scoped to this project's `operations/skills/` directory, each implementing one move from Deterding & Waters' three-stage workflow.

- **`/index-transcript`** applies broad index codes to a single transcript, anchored to the interview protocol's sections. Produces an indexed copy of the transcript and a coverage report flagging where the conversation drifted away from the protocol. This is Waters' Stage 1 — scaffolding, not analysis.
- **`/find-negative-cases`** takes a claim and the indexed corpus and returns respondents whose evidence cuts against the claim, with verbatim excerpts, line references, and reasoning. Closes with an "implications for the theory" recommendation: narrow, abandon, or keep-but-report. This is Waters' Stage 3 validation move, drawing on Katz, Luker, and Blee.
- **`/methods-paragraph`** reads the project's actual state — what indexing was done, which claims were audited, what was *not* done — and writes a 250–500 word methods paragraph suitable for a journal article. It refuses to fabricate procedure that the project state does not support.

Each skill includes a worked example output, run against a synthetic four-respondent corpus modeled on Deterding's (2015) study of low-income mothers planning their children's college paths. The corpus is designed to surface a specific demo move at each stage: a clear instrumental case (R001), a clear expressive case (R002), a mixed case (R003), and a construct-validity stress test (R004) where surface vocabulary and underlying reasoning point in different directions.

The three skills line up with the three structural complaints Deterding & Waters make about the field: that coding does not scale, that negative cases are honored more in citation than in practice, and that methods sections are opaque. Indexing addresses scale, negative-case hunting addresses rigor, and the methods paragraph addresses transparency.

### The tradition this sits in

Glaser and Strauss published *The Discovery of Grounded Theory* in 1967 as a response to mid-century social science's dismissal of qualitative work as "biased, impressionistic, and anecdotal." Their open–axial–selective coding pipeline — read transcripts line by line, attach interpretive labels, cluster into broader categories, identify the organizing concepts — has structured qualitative-methods training for nearly sixty years. The workflow was designed for paper and index cards; NVivo, ATLAS.ti, MAXQDA, and Dedoose rebuilt the dining-room table in software rather than rethinking the affordances. Loïc Wacquant called the rhetorical convention that wraps this practice — researchers entering the field as theoretical blank slates so categories can "emerge" — the "epistemological fairytale" of grounded theory.

Deterding and Waters' diagnosis is empirical: contemporary interview practice has drifted decisively from the 1967 template. Sample sizes have grown well past the point at which line-by-line open coding by a single researcher remains tractable. Coding is increasingly done by teams. Interview studies are increasingly nested inside mixed-methods designs. Their redesign has three stages — **indexing** applies broad protocol-anchored topical codes; **analytic coding** applies interpretive codes *within* indexed sections rather than across the entire corpus; **validation** refines the typology against the indexed corpus with particular attention to negative cases. Construct validity comes from iterative typology refinement; theoretical validity from exhaustive engagement with negative cases; transparency from reportable, replicable indexing decisions. The proposal is to stop performing emergence and start documenting reasoning.

### What LLMs change about it

The reason Deterding and Waters' proposal maps onto LLM affordances with unusual cleanliness is that the moves it proposes are precisely the moves that scale poorly under human-only labor at *N*>50. Indexing — assigning protocol-anchored topical codes to passages — is what instruction-tuned models are reliable at when given a clear codebook; recent studies (Tai et al. 2024; Qiao et al. 2024; Than et al. 2025) have begun to verify this empirically. Analytic coding remains under researcher control, with the LLM applying — not discovering — the codebook. Negative-case hunting, the move that is most honored in citation and least performed in practice at scale, becomes tractable: the LLM searches the indexed corpus exhaustively for evidence that cuts against a stated claim. Methods reporting, which usually requires reconstructing a process from memory weeks after the analysis, becomes a matter of reading the artifacts the pipeline already produced.

Five things to refuse, in any conversation with a senior methodologist: LLMs do not "discover themes" (the themes are what the researcher brings); they do not replace the immersive first read; quantification is not validation; reproducibility against shifting model versions is a real problem; and "false fluency" — plausible-sounding methods text not supported by the data — is the failure mode to design against. Every model-produced claim should be traceable to a specific passage; every methods paragraph auditable against the log of coding decisions. The skills in this project enforce that discipline.

---

## How we built it

The whole sequence — domain brief, brainstorm, drill-down, sample corpus, plan, parallel build, audit — took one conversation, about an hour, five prompts of substance. The prompts were short. None of them told Claude exactly what to write. They named a goal, one or two alignment constraints, and trusted Claude to produce the artifact.

**Step 1 — Brief Claude on the domain.** A single prompt that points Claude at the source paper, names the methodological frame, and explicitly names the senior methodologist in the room whose views matter: *"Can you read this PDF... help me think of a whole bunch of ways to make use of LLMs and Claude Code in particular for disciplinary work of this sort... Mary is at our workshop so we want to think of things that really align with her views and approach."* The dense methodological source acts as one constraint; the named expert acts as a second. The result was a thirty-item brainstorm, organized around Waters' three-stage workflow, with explicit flags for moves to avoid in front of Mary (no "LLM discovers themes," no replacing the immersive first read).

**Step 2 — Capture the thinking in a document.** *"Can you put all of these in a claude-thoughts doc so I can read more easily?"* Brainstorming in chat is fast but ephemeral. Asking Claude to commit the thinking to a markdown file turns it into a durable artifact future sessions can read.

**Step 3 — Drill into a specific affordance.** *"Can you also think of Claude SKILL.md files that would be useful?"* The brainstorm now has a skills catalog of about twenty candidates, each tied to a specific page or move in the paper. Closing with a recommended three-skill demo trio — `/index-transcript` (scale), `/find-negative-cases` (rigor), `/methods-paragraph` (transparency).

**Step 4 — Build a sample corpus.** *"Can you also generate some sample transcripts, or find some online?"* Claude explained why generating is better than finding — real transcripts are IRB-restricted or stripped of conversational texture — then produced four synthetic transcripts engineered to surface specific demo moves: textbook instrumental, textbook expressive, mixed, and a construct-validity stress test where reasoning and vocabulary diverge.

**Step 5 — Convert the brainstorm into a parallelizable plan.** *"Also add the three skill ideas to PLAN.md so I can get different Claudes working in parallel."* PLAN.md became three self-contained task sections, each copy-pasteable into a fresh Claude session, with shared context up top (required reading, hard constraints, output conventions) and per-task scope (skill behavior, what good output looks like, what to avoid, where to build, how to validate).

**Step 6 — Run three Claudes in parallel.** Three short prompts (~200 words each) pointed at PLAN.md rather than repeating its contents. The plan is the durable artifact; the prompts are the trigger. The three sessions ran independently; no shared writes.

**Step 7 — Make this folder a project with its own CLAUDE.md.** A project-level CLAUDE.md that loads automatically when Claude Code starts here, points new participants at the right reading order, names the hard constraints, and clarifies that `.claude/skills/<name>/` resolves under this folder so skills travel with the project.

**Step 8 — Audit each Claude's return.** The parallel sessions returned out of order. For each return: read the SKILL.md, verify examples against the source corpus, spot-check verbatim quotes and line numbers. Notable findings — `/find-negative-cases` had one verbatim slip (a quote silently dropped its opening sentence); `/index-transcript` and `/methods-paragraph` were clean. Audit caught the slip. The most common failure mode for parallel-built skills is plausible-looking output with small honesty bugs; the audit pass is not optional.

After the audits, validated outputs were promoted from each skill's `examples/` into the project's shared `outputs/` tree; the methods-paragraph was regenerated against the now-populated state.

### Things this approach taught us

The hand-off from "Claude brainstorms" to "Claude builds" benefits from explicit constraints and validation steps. Without them, parallel sessions drift in different directions. With them, three Claudes building three skills in parallel produce work that fits together.

The five prompts above are short. They give Claude a goal, one or two alignment constraints, and trust it to produce the artifact. That delegation is the part that is hard to demonstrate in a slide. The way you learn it is by trying it, looking at what Claude produces, and adjusting the next prompt.

---

## What you can translate this to

The pattern in this project is portable to any domain where the substantive work is:

1. **A defined methodological source** — a paper, a manual, a senior practitioner's framework — that provides constraints against which Claude's outputs can be checked.
2. **A multi-stage workflow** with named artifacts at each stage. Skills work best when they implement *one specific move* in an established procedure, not "do qualitative analysis."
3. **A corpus the work operates on**, ideally with a few engineered edge cases so the skills can be validated against known-difficult instances rather than only easy ones.
4. **An audit step** that checks model output against the source material before it is used downstream.

Domains where the same shape applies almost without modification:

- **Course design from a teaching framework.** Replace Deterding & Waters with Wiggins & McTighe's *Understanding by Design*; replace the four transcripts with four course-design briefs from different disciplines. Skills become `/draft-essential-questions`, `/identify-misconceptions`, `/transfer-task-rubric`.
- **Literature review against a typology.** A senior researcher provides the typology; the corpus is a folder of PDFs; skills become `/classify-paper`, `/find-counter-evidence`, `/synthesis-paragraph`.
- **Grant proposal review against a funder's published criteria.** The criteria document is the methodological source; the corpus is a folder of draft proposals; skills become `/criterion-check`, `/missing-evidence`, `/reviewer-paragraph`.
- **Editorial review against a house style.** Style guide as source, manuscript corpus as inputs, skills along the lines of `/style-check`, `/queries-for-author`, `/copyedit-summary`.
- **Curriculum mapping against learning outcomes.** Outcomes document as source, syllabi as corpus, skills like `/outcome-coverage`, `/gap-analysis`, `/program-summary`.

The pattern in all of these is the same: source provides constraints, corpus provides material, skills implement specific moves, audit closes the loop, methods-paragraph-equivalent makes the work transparent. The skills travel with the project rather than living globally, so a colleague who clones the folder gets everything they need to reproduce or extend the work.

The portability question is not "can Claude do qualitative coding" — it is whether the move you are trying to make has a clear procedural form and a checkable artifact at the end. If it does, the pattern in this project gives you the skeleton.

---

## Alignment constraints (the hard ones)

These apply throughout the project and survive translation to other domains:

- Do not pitch LLM assistance as "discovering themes" (or "discovering" anything). Frame as "applying the researcher's concepts at scale," "surfacing candidates for human review," or "auditing for X." The alternative framing is empirically false and would not survive a serious methodological conversation.
- Do not replace the immersive first read. Skills augment human analysis; they do not substitute for it.
- Do not oversell quantification. Frequency counts are useful but they are not the proof of theoretical validity.
- Every model-produced claim must be traceable to a specific passage. Every methods paragraph must be auditable against the log of decisions. False fluency is the failure mode to design against.
- No emojis in any output. Respondent IDs and pseudonyms stable across artifacts. Markdown link syntax for file references.
