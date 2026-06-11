# Workflow Prompt: Lecture Video → Lecture Notes

This document is a self-contained recipe for turning a single downloaded
lecture video into a finished, readable **lecture-notes** document (Markdown +
PDF). It is the prompt you would hand to an AI coding agent (e.g. Claude Code)
to run the whole pipeline end to end.

The instructor in this course (CS 1200, Harvard) teaches on a blackboard —
there are no slides. So "notes" are reconstructed from two sources: **what was
written on the board** (recovered from video frames) and **what was said**
(recovered from the transcript).

The worked example shipped with this operation shows every artifact the workflow
produces, for one real lecture (Lecture 1): the captured inputs live in
`inputs/lecture-recordings/` (deduped frames + transcript) and the deliverables
in `outputs/lecture-notes/` (slides + notes). All paths below are relative to the
`course-preparation/` project root.

---

## The pipeline at a glance

```
downloaded video (.mp4, camera/blackboard stream)
        │
        │  operations/lecture-notes/scripts/extract_frames.py   (ffmpeg: scene-change + interval frames)
        ▼
   inputs/lecture-recordings/frames/<lecture>/        (many near-duplicate JPGs)
        │
        │  operations/lecture-notes/scripts/dedupe_frames.py    (perceptual-hash dedupe)
        ▼
   inputs/lecture-recordings/frames_deduped/<lecture>/   (a handful of distinct board states)
        │
        │  SUBAGENT STEP 1: transcribe board  →  slides.md (+ pandoc PDF)
        ▼
   outputs/lecture-notes/slides.md   ── the captured board content (GROUND TRUTH)
        │
        │  + inputs/lecture-recordings/transcript.srt  (fetched separately)
        │
        │  SUBAGENT STEP 2: merge board + narration  →  notes.md (+ pandoc PDF)
        ▼
   outputs/lecture-notes/notes.md / notes.pdf  ── THE FINAL PRODUCT
```

Two inputs are gathered up front from the recording platform (Panopto, here):

- `operations/lecture-notes/scripts/fetch_videos.py` — downloads the **camera
  (`dv`) stream**, which frames the instructor + blackboard. (The composite
  stream is dominated by the laptop screen and is not used.)
- `operations/lecture-notes/scripts/fetch_transcripts.py` — downloads the
  auto-generated `.srt` transcript.

Both take a browser session cookie; see each script's docstring.

---

## Step 1 — Extract and dedupe frames (scripted, deterministic)

Run from the `course-preparation/` project root:

```bash
# 1. Pull frames: scene-change detection + a frame every 45s for coverage
python3 operations/lecture-notes/scripts/extract_frames.py \
  --videos inputs/lecture-recordings/videos/ --out inputs/lecture-recordings/frames/

# 2. Collapse near-identical consecutive frames into distinct board states
python3 operations/lecture-notes/scripts/dedupe_frames.py \
  --frames inputs/lecture-recordings/frames/ --out inputs/lecture-recordings/frames_deduped/
```

`--sensitivity` on the dedupe step controls aggressiveness (lower = fewer
frames kept). The 13 frames in `inputs/lecture-recordings/frames_deduped/` are
the deduped output for Lecture 1.

---

## Step 2 — Frames → captured board content (`slides.md`)

Spawn an agent with the following prompt. Substitute the bracketed fields.

> You are generating lecture slides for CS 1200: Introduction to Algorithms and
> their Limitations (Harvard). The instructor writes on a blackboard — no
> slides. Read the frames extracted from the lecture video, transcribe the board
> content, and produce a clean Markdown file suitable as lecture slides.
>
> **Output:** `outputs/lecture-notes/[LECTURE]-slides.md` (the worked example is
> `outputs/lecture-notes/slides.md`), then a PDF via the pandoc command below.
>
> 1. Read each frame image file (in time order) with the Read tool.
> 2. Group related board states into logical slides (a slide = a coherent topic
>    or step, not one frame per board state). Skip empty/transitional boards;
>    where consecutive frames show the same content, keep only the clearest.
> 3. Formatting: `##` for slide titles; `---` between slides; LaTeX math
>    (`$...$`, `$$...$$`); bullet lists and tables where useful; plain and
>    simple — no decoration; no timestamps or frame references in the output.
> 4. Course math conventions: arrays written
>    `A = {(K_0, V_0), ..., (K_{n-1}, V_{n-1})}` (keys `K_i`, values `V_i`);
>    asymptotics `O(·), Ω(·), Θ(·)`; pseudocode as a numbered/bulleted list, not
>    a code block.
> 5. After writing the Markdown, render the PDF:
>    ```
>    pandoc outputs/lecture-notes/slides.md -o outputs/lecture-notes/slides.pdf \
>      --pdf-engine=pdflatex -V geometry:margin=1in -V fontsize=12pt --standalone
>    ```
>
> **Frames to read (in time order):** [list the frame paths under
> `inputs/lecture-recordings/frames_deduped/`]

The result is `outputs/lecture-notes/slides.md` (+ `slides.pdf`) — the verbatim
board, reorganized into logical sections. This is an **intermediate artifact**
and the ground truth for the next step.

---

## Step 3 — Board + transcript → finished notes (`notes.md`, the final product)

This is the payoff step. It merges the captured board with the spoken narration
into a three-layer notes document:

- **Captured board content** → a blue box (`::: board` fenced div). The slide md
  is the source of truth: reorganize and fix obvious formatting, but never
  invent or silently "correct" content.
- **What the lecturer said** → a *structured bullet* summary outside the boxes
  (intuition, motivation, emphases, asides, student Q&A, foreshadowing). Bullets
  and sub-bullets, not paragraphs.
- **Board the transcript clearly references but the camera missed** →
  a best-effort reconstruction in a red dashed "GENERATED" box (`::: guess`
  fenced div), only where the transcript makes it reasonably clear; otherwise
  just note in a bullet that the board wasn't captured.

The `::: board` / `::: guess` fenced divs are turned into the blue/red boxes by
the two render helpers in `operations/lecture-notes/render-helpers/`
(`_boxes.tex`, `_divs.lua`), which are passed to pandoc.

Spawn an agent with this prompt (substitute the bracketed fields):

> Generate a CS 1200 (Harvard) lecture-notes document for Lecture [N], [DATE].
>
> FIRST, read the approved template and MATCH its format EXACTLY (header, "How to
> read these notes." legend blockquote, three-layer box scheme, structured-bullet
> style, `##` headings, `---` separators): **`outputs/lecture-notes/notes.md`**
> (the worked example here is itself the canonical template). Skim the render
> helpers so you understand the boxes:
> `operations/lecture-notes/render-helpers/_boxes.tex` (blue `boardbox`, red
> dashed `guessbox`) and `operations/lecture-notes/render-helpers/_divs.lua`
> (`::: board` / `::: guess` map to those boxes).
>
> Read BOTH inputs IN FULL (the transcript is long and the Read tool truncates —
> page through the WHOLE file with offset/limit; it is auto-generated ASR, so
> infer meaning through garbled words using the board content as ground truth):
> - BOARD CONTENT (GROUND TRUTH): `outputs/lecture-notes/slides.md`
> - TRANSCRIPT (what was SAID): `inputs/lecture-recordings/transcript.srt`
>
> Write `outputs/lecture-notes/notes.md` with the THREE-LAYER scheme described
> above (captured board → `::: board`; spoken narration → structured bullets
> outside boxes; clearly-referenced-but-uncaptured board → `::: guess`).
>
> FORMAT: header `# Lecture [N]: <concise topic>` then
> `**CS 1200 | [DATE] | [LECTURER]**`; copy the legend blockquote from the
> template; LaTeX math (`$...$`, `$$...$$`); PDFLATEX-SAFE TEXT ONLY (no raw
> Unicode minus U+2212 — use `-` or math; no emoji; em-dashes/curly quotes/§/…
> are fine).
>
> RENDER (run after writing; verify exit 0 and the .pdf exists; if pandoc errors
> on a Unicode char, fix it — math→LaTeX, prose→ASCII — and re-run):
> ```
> pandoc outputs/lecture-notes/notes.md -o outputs/lecture-notes/notes.pdf --pdf-engine=pdflatex \
>   -H operations/lecture-notes/render-helpers/_boxes.tex \
>   -L operations/lecture-notes/render-helpers/_divs.lua \
>   -V geometry:margin=1in -V fontsize=11pt --standalone
> ```
>
> Do NOT edit the slide md. If you find a SUSPECTED ERROR in the captured board
> (something transcribed wrong vs. what the transcript or the math implies), do
> NOT change it — report it in your return message instead.

The result is `outputs/lecture-notes/notes.md` (+ `notes.pdf`) — the deliverable.

---

## Notes on scale and provenance

- One lecture is shown here; the real project runs Step 2 and Step 3 with **one
  agent per lecture, dispatched in parallel** across an entire semester (25
  lectures). When scaling, give each lecture its own subfolder under
  `inputs/lecture-recordings/` and name the outputs per lecture.
- The board content is always treated as ground truth; the transcript supplies
  meaning and motivation. Reconstructions are visually flagged (red box) so a
  reader never mistakes a guess for something that was actually on the board.
