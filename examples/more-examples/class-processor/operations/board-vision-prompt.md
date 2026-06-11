# Prompt — describe board work from an image

_The vision path is live (see below); the structured-description prompt is refined once real board-work images land in [inputs/board-work/](../inputs/board-work/)._

---

There are two ways to get the text off a board image, depending on what you need:

- **Quick raw transcription via a vision API** — run the vision code in
  [operations/apis-and-vision/scripts/transcribe.py](apis-and-vision/scripts/transcribe.py)
  (`--provider gemini|claude|both`). That is the same script the APIs capstone uses
  on Zettelkasten slips; a board photo is just another image. Use it when you want a
  fast, scriptable text dump (or to compare two models on hard handwriting).
- **A structured reading by Claude in this session** — for the richer
  layout-and-teaching-sequence description below, just point Claude at the image
  with the Read tool and the prompt that follows (no script, no key needed).

Read the image(s) at `inputs/board-work/<file>` and produce a structured markdown
description that the rest of the pipeline can use as text. For each image:

- **Transcribe** every legible element — equations (as LaTeX or plain math), labels,
  diagram captions, lists, and arrows together with what they connect.
- **Describe** the layout and the apparent teaching sequence: what was written first,
  what was boxed or underlined for emphasis, how the regions relate.
- **Flag** anything illegible or ambiguous rather than guessing — mark it `[unclear]`.
- Capture the *teaching point* the board work was building toward, not just its contents.

Write the result to `outputs/board-notes/<session>-board-notes.md`. Keep the project's
voice: tight, concrete, faculty-facing, no preamble.
