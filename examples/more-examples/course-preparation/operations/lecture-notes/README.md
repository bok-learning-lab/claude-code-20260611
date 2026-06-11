# Lecture-notes pipeline (CS 1200)

The second prep operation in `course-preparation`: turning blackboard
**lecture recordings** for **CS 1200: Introduction to Algorithms and their
Limitations** (Harvard) into clean, readable **lecture-notes** documents —
materials you can hand students or reuse when you next teach the course.
Contributed by a collaborator from the larger CS 1200 project.

This is a common **before-class** move when a course is handed off between years
or instructors: take last year's recordings — even from a different professor —
and turn them into clean notes you can adapt for your own version of the course.

The instructor teaches entirely on a blackboard — no slides. This pipeline
reconstructs notes from two sources: **what was written on the board** (recovered
from video frames) and **what was said** (recovered from the transcript). The
two are merged into a three-layer notes document that visually distinguishes
captured board content from spoken narration from best-effort reconstructions of
boards the camera missed.

## How it maps into this project

The pieces live across the standard `inputs/ → operations/ → outputs/` folders
(paths relative to the `course-preparation/` project root):

```
operations/lecture-notes/
├── README.md            ← you are here
├── WORKFLOW_PROMPT.md   ← the end-to-end recipe: video → frames → board → notes
├── scripts/             ← the deterministic, scripted steps
│   ├── fetch_videos.py        download the camera/blackboard video stream
│   ├── fetch_transcripts.py   download the .srt transcript
│   ├── extract_frames.py      ffmpeg: scene-change + interval frames
│   └── dedupe_frames.py       perceptual-hash dedupe of consecutive frames
└── render-helpers/      ← pandoc helpers that draw the colored boxes in the notes PDF
    ├── _boxes.tex             blue "board" box, red dashed "GENERATED" box
    └── _divs.lua              maps ::: board / ::: guess fenced divs to those boxes

inputs/lecture-recordings/   ← the captured material for one worked lecture (Lecture 1)
├── frames_deduped/          13 distinct board states (the deduped frames)
└── transcript.srt           auto-generated lecture transcript

outputs/lecture-notes/       ← the artifacts the workflow produces
├── slides.md / .pdf         INTERMEDIATE: the transcribed board content
└── notes.md  / .pdf         FINAL PRODUCT: board + narration, three-layer format
```

## How to read the example

1. **`inputs/lecture-recordings/frames_deduped/`** — start here. These 13 JPGs
   are what the pipeline keeps after extracting frames from the video and
   discarding near-duplicates: the distinct states of the blackboard.
2. **`outputs/lecture-notes/slides.pdf`** — an agent read those frames and
   transcribed the board into clean Markdown. The captured board content, treated
   as ground truth.
3. **`inputs/lecture-recordings/transcript.srt`** — what the lecturer actually
   said (auto-generated ASR, somewhat garbled).
4. **`outputs/lecture-notes/notes.pdf`** — the deliverable. A second agent merged
   the board (blue boxes) with a structured summary of the narration (bullets),
   flagging reconstructed-but-uncaptured board content in red "GENERATED" boxes.

Open `outputs/lecture-notes/notes.pdf` and `WORKFLOW_PROMPT.md` together to see
the output and the process side by side.

## Reproducing it

The scripted steps need `ffmpeg`, `ffprobe`, Python 3 with `requests` and an
image-hashing library, and a session cookie for the recording platform (see each
script's docstring). The two agent steps are prompts you hand to an AI coding
agent — `WORKFLOW_PROMPT.md` has them verbatim. Rendering the PDFs needs `pandoc`
with a LaTeX engine (`pdflatex`).
