# class-processor — folder index

A worked example of turning the raw materials of a live course — transcripts, board work, audio, papers — into the teaching artifacts faculty hand out, in one house style. Start with [summary.md](summary.md); everything else is here for browsing.

The transcript → key-takeaways path (folded in from the former `class-summarizer`) is fully worked; the other modalities are scaffolded and waiting on real inputs.

## Top-level

- [summary.md](summary.md) — what this project is, how we built it, what you can translate it to
- [CLAUDE.md](CLAUDE.md) — project instructions and the output contract
- [index.md](index.md) — this file

## inputs/ — by modality

Each modality folder has a `README.md` describing what goes there and how it's processed.

- [inputs/transcripts/](inputs/transcripts/) — diarized session transcripts. **Populated:** `day_1_transcript.md` (8 June), `day_2_transcript.md` (9 June)
- [inputs/board-work/](inputs/board-work/) — photos/scans of board work, read with vision *(staged)*
- [inputs/audio/](inputs/audio/) — raw session recordings, transcribed into `transcripts/` *(staged)*
- [inputs/papers/](inputs/papers/) — assigned readings that ground generated materials *(staged)*
- [inputs/zettelkasten/](inputs/zettelkasten/) — slips fetched from the open Luhmann Archiv API (sample: `zk-9-8-sample.json`); used by the APIs-and-vision capstone

## operations/

- [operations/key-takeaways-prompt.md](operations/key-takeaways-prompt.md) — the reusable distillation prompt. Forces exactly 10 takeaways with bold one-sentence headlines, an italic provenance opening, and a secondary-points section
- [operations/board-vision-prompt.md](operations/board-vision-prompt.md) — stub: turn a board photo into structured text *(staged)*
- [operations/apis-and-vision/](operations/apis-and-vision/) — the **APIs capstone**: `fetch_zettels.py` (open Luhmann data API, no key) and `transcribe.py` (image → text via the Gemini and Claude vision APIs, key in `.env`). Its [README](operations/apis-and-vision/README.md) walks the two kinds of API. The only operation that ships scripts
- .claude/skills/
  - [handout-house-style/](.claude/skills/handout-house-style/) — renders a markdown artifact as a self-contained, print-ready HTML page in the Learning Lab house style (Inter, white background, red #c8102e accent, 11x17 tabloid). A small, no-script project copy of the global house-style skill

## outputs/ — by artifact type

- [outputs/key-takeaways/](outputs/key-takeaways/) — `day-1-key-takeaways.md` / `.html`, `day-2-key-takeaways.md` / `.html`
- `outputs/board-notes/`, outlines, study guides — *coming as more inputs arrive*

---

*To run the worked path on a new session: drop the transcript at `inputs/transcripts/day_N_transcript.md`, invoke [operations/key-takeaways-prompt.md](operations/key-takeaways-prompt.md), then run the `handout-house-style` skill on the resulting markdown to produce the portable HTML companion.*
