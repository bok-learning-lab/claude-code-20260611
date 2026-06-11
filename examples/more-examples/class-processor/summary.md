# Class processor

A worked example of turning the **raw materials of a live course** into the **teaching artifacts faculty hand out** — automatically, and in one consistent house style. The premise: a course generates a stream of messy source material as it runs — a session gets recorded and transcribed, the board fills with derivations and diagrams, papers get assigned, audio piles up. Each of those is an *input*. On the other end faculty need *outputs*: a five-minute key-takeaways doc, a printable handout, a session outline, a study guide. This project is the pipeline between the two.

It folds in the former `class-summarizer` example as its first fully worked path (transcript → Top 10 Key Takeaways → portable house-style handout), and sets the stage for the other modalities — board work read with vision, audio transcribed to text, papers used to ground generated materials.

---

## What it is

Inputs organized by **modality**, operations that process them, outputs organized by **artifact type** — all rendered through a single house-style skill.

- **The inputs** (in `inputs/`, one folder per modality, each with a `README.md`):
  - [transcripts/](inputs/transcripts/) — diarized session transcripts. **Populated:** Day 1 (8 June) and Day 2 (9 June).
  - [board-work/](inputs/board-work/) — photos/scans of whiteboard and blackboard work, read with vision. *Staged.*
  - [audio/](inputs/audio/) — raw session recordings, transcribed into `transcripts/`. *Staged.*
  - [papers/](inputs/papers/) — assigned readings that ground the generated materials. *Staged.*

- **The operations** (in `operations/`):
  - [key-takeaways-prompt.md](operations/key-takeaways-prompt.md) — the reusable distillation prompt. Forces exactly 10 takeaways with bold one-sentence headlines, an italic provenance opening, and a secondary-points section. Voice: tight, concrete, faculty-facing.
  - [board-vision-prompt.md](operations/board-vision-prompt.md) — a stub for turning a board photo into structured text (transcribe equations and labels, describe the teaching sequence). *To be refined when board images arrive.*
  - skills/
    - [handout-house-style/](.claude/skills/handout-house-style/) — renders any markdown artifact as a self-contained, print-ready HTML page in the Learning Lab house style (Inter, white background, red `#c8102e` accent, 11x17 tabloid). A small, no-script, project-scoped copy of the global house-style skill: font and CSS are inlined by hand.

- **The outputs** (in `outputs/`, one folder per artifact type):
  - [key-takeaways/](outputs/key-takeaways/) — `day-1-key-takeaways.md` / `.html` and `day-2-key-takeaways.md` / `.html`.
  - `board-notes/`, session outlines, study guides — *coming as more inputs arrive.*

### The capstone: APIs and vision

The final operation, [apis-and-vision/](operations/apis-and-vision/), introduces the concept of an **API** — a URL you ask for data or hand a piece of work — using Niklas Luhmann's *Zettelkasten* as the vehicle. Two kinds: an **open data API** (`fetch_zettels.py` pulls scanned slips from the Luhmann Archiv as JSON — no key) and **vision APIs** (`transcribe.py` sends an image to **Gemini** and/or **Claude** and gets the text back — key in a folder-scoped `.env`). The transference is the point: the same image-to-text move reads a Luhmann slip, a blackboard photo, or a student's in-class exercise. This is the one operation that ships **scripts** — they appear only because calling an external API needs code; the rest of the project is prompts and a no-script skill.

### The move worth noticing

The instruction *"capture the teaching point, not just the fact — why it mattered to faculty"* is what turns this from a transcript summary into a teaching artifact. A generic LLM summary produces accurate but inert prose: "the instructors discussed prompt engineering, CLAUDE.md files, and the use of skills." That summary is *true* and *useless*. The prompts here are structured to force the second layer — the headline mantra, the analogy that landed, the demo, the line worth quoting. The artifact is meant to *re-create* the room, not describe it.

The bigger move is the **pipeline shape itself**: many input modalities, a small set of operations, many output artifacts — but **one house style** at the end, so everything a faculty member produces from their own course looks like it belongs to the same set. The provenance opening on every artifact keeps it auditable: a reader can trace any claim back to a named speaker in a named hour, or to a specific board photo.

---

## How we built it

The build is a set of operations applied per input, then a single rendering skill.

**The worked path (transcripts):**

1. Capture the session transcript as markdown and drop it in `inputs/transcripts/` (transcribe from `inputs/audio/` if starting from recordings).
2. Invoke `operations/key-takeaways-prompt.md`, pointing it at the day's transcript.
3. Claude writes `outputs/key-takeaways/<day>-key-takeaways.md` — title shape, italic provenance, ten numbered takeaways with bold headlines, secondary points.
4. Invoke the `handout-house-style` skill to render the portable HTML companion next to it.

**The staged paths:** board work runs through `board-vision-prompt.md` (vision → structured text) into `outputs/board-notes/`; papers ground generated handouts and outlines. Same render step at the end.

### The discipline the prompts enforce

- **Exactly 10 takeaways.** The number is a constraint, not a guideline — it forces ranking.
- **Bold one-sentence headline,** then 1–3 sentences of grounded explanation.
- **Specific to the room.** Name the demos, analogies, turns of phrase. Generic phrasing is the failure mode.
- **Quote memorable lines** — the receipts that prove it came from the room.
- **Voice: tight, concrete, faculty-facing.** No preamble.
- **Secondary points worth keeping** — a two-tier structure that keeps the top 10 tight without losing the small things.

---

## What you can translate this to

The pattern is **messy live source material (in several modalities) + a small set of forced, grounded operations + one portable house-style renderer**. It applies wherever a course or event generates raw material that needs to become reusable artifacts:

- **Course session catch-up** for students who missed class — transcript or board photos in, a "what you missed" doc out.
- **Lecture-to-notes** — a blackboard-heavy session photographed and transcribed into structured notes.
- **Conference or seminar series** — per-session takeaways across a multi-track program.
- **Reading-grounded handouts** — assigned papers in, discussion guides or study sheets out.
- **Department meeting recaps** — a transcript in, a defensible record of decisions and follow-ups out.

The constant across all of them: named sources, a forced count or structure, verbatim quotes as receipts, and one house style so the whole set looks coherent.

---

## Alignment constraints (the hard ones)

- **Forced count, not "key takeaways."** The model must rank to comply.
- **Provenance is part of the artifact.** The italic opening names the source, the range, and the speakers. Floating claims are not allowed.
- **Specific, not generic.** Name the demos, analogies, turns of phrase. Quote the memorable lines.
- **Two-tier structure.** Top stays tight; secondary points catches the rest.
- **One house style.** Inline CSS, no external assets; every rendered artifact survives email and print and looks like the rest.
- **No preamble.** Just the artifact.
