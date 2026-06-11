# CLAUDE.md — Interview coding project

## What this project is

A worked example of LLM-assisted qualitative coding aligned with Mary Waters' "flexible coding" approach (Deterding & Waters 2018, *Sociological Methods & Research*). Built during the 4-day workshop "Claude for Teaching, Course Development, and Research" at Harvard's Bok Center. Mary Waters is among the workshop participants, so the design choices throughout this project are made to align with her methodological view rather than with grounded theory.

This folder is intended to be opened as a standalone Claude Code project — `cd` into it, run `claude`, and everything you need is here.

## If you just opened this folder

Read in this order:

1. [summary.md](summary.md) — what this project is, how it was built, and the patterns to translate elsewhere.
2. [index.md](index.md) — a map of the folder.
3. [inputs/README.md](inputs/README.md) — the synthetic corpus we demo against.

## What you might be here to do

- **Running the demo end-to-end** — `/index-transcript` on the four transcripts, then `/find-negative-cases` on the demo claim, then `/methods-paragraph`. Worked examples are already in each skill's `examples/` directory under `operations/skills/`, and validated outputs live in `outputs/`.
- **Reading the skills as references** — every skill in `operations/skills/<skill-name>/` ships its `SKILL.md`, supporting templates, and worked examples.
- **Translating the pattern** — see the "What you can translate this to" section of summary.md.

## Conventions for this project

- **Skills live in `operations/skills/<skill-name>/`** — project-scoped, not user-scoped, so they travel with this folder.
- **Sample data is read-only.** Don't modify files in `inputs/`. New artifacts go in `outputs/`.
- **Respondent IDs and pseudonyms are stable.** R001–R004 and their pseudonyms (Tasha, Marisol, Carla, Denise) must be preserved consistently across every skill output, memo, and report.
- **No emojis in any file.** Workshop-wide convention.
- **Markdown link syntax for file references** — `[R001](inputs/transcripts/R001-Transcript.md)` — so they're clickable in the IDE.
- **Filenames follow Deterding & Waters' p. 723 convention**: respondent ID first (`R001-Transcript.md`), so attributes auto-link by leading ID.

## Alignment with Waters (the hard constraints)

These come from the Deterding & Waters paper and apply to everything Claude does in this project:

- Do not pitch LLM assistance as "discovering themes." Frame as "applying the researcher's concepts at scale," "surfacing candidates for human review," or "auditing for negative cases."
- Do not start with line-by-line open coding. Index first (Stage 1), then apply analytic codes to indexed sections (Stage 2), then validate against negative cases (Stage 3).
- Do not replace the immersive first read. Skills augment human analysis; they don't substitute for it.
- Don't oversell quantification. Frequency counts are useful but they are not the proof of theoretical validity (Deterding & Waters 2021, p. 734).

## A note on the corpus

The four transcripts in `inputs/transcripts/` are **synthetic**, designed to showcase specific demo moves: a clear instrumental case (R001 Tasha), a clear expressive case (R002 Marisol), a mixed case where the respondent is self-aware about the tension (R003 Carla), and a case where surface vocabulary and underlying reasoning point in different directions (R004 Denise — the construct-validity stress test). They are modeled on Deterding's published study of low-income mothers planning their children's college paths (*Sociology of Education* 2015) but contain no real respondents. See [inputs/README.md](inputs/README.md) for design rationale.
