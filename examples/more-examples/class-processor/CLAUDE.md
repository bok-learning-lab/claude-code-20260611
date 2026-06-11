# CLAUDE.md — Class processor

Project-level instructions loaded when Claude Code starts in this folder.

## What this project is

A worked example of turning the **raw materials of a live course** — session transcripts, board work, audio recordings, assigned papers — into the **teaching artifacts** faculty actually hand out: key-takeaways docs, handouts, outlines, study materials. Materials in one end, finished artifacts out the other, on one consistent house style.

This folder is meant to be opened as a standalone Claude Code project — `cd` into it, run `claude`, and everything you need is here. See [summary.md](summary.md) for the move worth noticing and what you can translate it to; [index.md](index.md) maps the folder.

The transcript → key-takeaways pipeline (folded in from the former `class-summarizer` example) is the **fully worked** path today. The other modalities — board work, audio, papers — are scaffolded and waiting on real inputs; treat them as the shape the project grows into, not finished work.

## The shape: inputs (by modality) → operations → outputs (by artifact)

| Input modality | Operation | Output |
|---|---|---|
| `inputs/transcripts/` | [operations/key-takeaways-prompt.md](operations/key-takeaways-prompt.md) → [handout-house-style](.claude/skills/handout-house-style/) skill | `outputs/key-takeaways/<day>-key-takeaways.md` + `.html` |
| `inputs/board-work/` (images) | [operations/board-vision-prompt.md](operations/board-vision-prompt.md) — vision description | `outputs/board-notes/` *(staged)* |
| `inputs/audio/` | transcribe (external) → `inputs/transcripts/` | feeds the takeaways path |
| `inputs/papers/` | ground generated materials in assigned readings | handouts / outlines / study guides *(staged)* |
| any image (board work, a student exercise, a Zettelkasten scan) | [operations/apis-and-vision/](operations/apis-and-vision/) — call a vision **API** (Gemini or Claude) to read it | text transcription |

Each `inputs/` modality has a `README.md` describing what goes there and how it's processed. Generated artifacts go in `outputs/`, one subfolder per type.

## APIs and vision (the capstone)

Everything above is text and files. The [operations/apis-and-vision/](operations/apis-and-vision/) operation adds the last idea: an **API** — a URL you ask for data or hand a piece of work. It meets two kinds, using Niklas Luhmann's *Zettelkasten* (slip-box) as the vehicle:

1. **An open data API (no key)** — `fetch_zettels.py` fetches scanned slips from the Luhmann Archiv as JSON (metadata + the archive's own transcription + an image id).
2. **Vision APIs (need a key)** — `transcribe.py` sends an **image** to **Gemini** and/or **Claude** and gets the text back.

The transference: the same `transcribe.py` reads a Luhmann slip, a **blackboard photo**, or a **student's in-class exercise**. Keys live in this example's own `.env` (see [`.env.example`](.env.example)) — folder-scoped, never the repo root, never committed. This is the one operation that ships **scripts** (the rest of the project is prompts and skills); scripts appear here because calling an external API genuinely needs code. See its [README](operations/apis-and-vision/README.md).

## How to work in this project

You are acting as a careful note-taker and materials-builder for the Director of Harvard's Bok Center Learning Lab. Faculty who missed a session — or who want their live teaching turned into reusable materials — are the audience. Every artifact does two jobs: (1) it names the *teaching point* — the mantra a faculty member would tell a colleague — and (2) it grounds that point in what *actually happened*: the demos, the analogies, the board work, the lines worth quoting.

For the takeaways pipeline specifically, two passes, in order:

1. **Read the source fully before writing anything.** Mark candidates as you go, but don't write the doc until the whole transcript (or board-work set) has been read.
2. **Rank ruthlessly to exactly ten.** Ten is a constraint, not a guideline. Choosing what to leave out is the act of distilling. Everything else worth keeping goes in the secondary-points section.

## Conventions

- **Inputs are organized by modality** (`transcripts/`, `board-work/`, `audio/`, `papers/`); **outputs by artifact type** (`key-takeaways/`, `board-notes/`, …).
- **Skills live in `.claude/skills/<skill-name>/`** — project-scoped, so they travel with this folder.
- **Scripts only where genuinely needed.** Most work here is prompts and skills (no code). The one exception is [operations/apis-and-vision/](operations/apis-and-vision/), whose scripts call external APIs. Its API keys live in a folder-scoped `.env` (this example's folder, not the repo root); `.env` is git-ignored, `.env.example` is the tracked template.
- **Source materials in `inputs/` are read-only.** Don't modify them. Generated artifacts go in `outputs/`.
- **One house style for everything rendered.** The [handout-house-style](.claude/skills/handout-house-style/) skill (Inter / white / red `#c8102e` accent, 11x17 tabloid) is the single formatting layer — no second visual vocabulary.
- **No emojis** in any file (workshop-wide convention).
- **Markdown link syntax** for file references — `[Day 1](inputs/transcripts/day_1_transcript.md)`.
- **Speaker initials are stable** — `MW = Madeleine`, `MK = Marlon`, plus any faculty/guests named in the source. Preserve them in the provenance opening.

## Output contract (hard rules — for the takeaways doc)

- **Title** in the shape `# <Day> (<date>) — Top 10 Key Takeaways`.
- **One-line italic provenance note** as the opening: what was distilled from (linked), the chunk/time range, and the instructors present.
- **Exactly 10 numbered takeaways**, each led by a **bold one-sentence headline** (the mantra), then 1–3 sentences of grounded explanation.
- **Specific to the room.** Name the demos, analogies, turns of phrase. Quote memorable lines verbatim. Generic phrasing is the failure mode.
- **Secondary points** section at the end — bulleted, for the smaller details that did not make the top 10.
- **Voice: tight, concrete, faculty-facing.** Favor the instructors' own language over generic AI-explainer prose. No preamble.
- **Portable HTML companion** in house style — self-contained (font + CSS inlined), no external assets, survives email and print.

## Alignment constraints (the hard ones)

These survive translation to other course-processing tasks:

- **Forced count, not "key takeaways."** Ten is the constraint that forces ranking. Without it, the model produces a long list and nothing is distilled.
- **Provenance is part of the artifact.** The italic opening makes every claim auditable — a reader can trace a takeaway back to a named speaker in a named hour (or to a specific board photo).
- **Quote verbatim.** Direct quotes are the receipts — they tell the reader it came from the room, not from the model's general knowledge.
- **Two-tier structure.** Top 10 stays tight; secondary points catches the rest.
- **One house style.** Every rendered artifact looks like it belongs to the same set.
