# joyce — folder index

A worked Claude Code example built around a single research task in Prof. Natasha Sumner's territory: *where does Fionn mac Cumhaill actually appear in James Joyce's* Finnegans Wake? The hero arrives in misspellings, puns, avatars, body-as-landscape, and mythic attributes with no letters in common with his name — so `grep` can't find him. The project breaks the book into 48 chunks, points one Claude subagent at each as a close reader, and pools the structured findings. Start with [summary.md](summary.md); everything else is here for browsing.

## Top-level

- [summary.md](summary.md) / [summary.html](summary.html) — what this project is, the research question, the method (48 close-readers in parallel), and what it shows about literary work an LLM can and cannot do
- [index.md](index.md) / [index.html](index.html) — this file

## inputs/

- [inputs/finnegans_wake.md](inputs/finnegans_wake.md) — the OCR'd full text of *Finnegans Wake* (~28,500 lines), with stable line numbers used throughout the operations and outputs

## operations/

- operations/chunks/ — 48 ~600-line slices of the source text (`chunk_00` through `chunk_47`), each sized so a single subagent can read it word-by-word. Each chunk preserves a known line offset so findings map back to the source text by global line number

## outputs/

One JSON per chunk plus an aggregate.

- outputs/finn_chunk_00.json through outputs/finn_chunk_47.json — one close-reader's structured findings per slice. Each finding is `{global_line, matched_text, snippet, variant_type, reasoning}` — a small structured judgment, not just a location
- [outputs/finn_references_aggregated.json](outputs/finn_references_aggregated.json) — all 48 files merged into one master list of Finn-references across the book

---

*To re-run: invoke a close-reading subagent on each chunk (`operations/chunks/chunk_NN`) with the instruction to read every word, judge candidates with its Joyce knowledge, and write findings as JSON to `outputs/finn_chunk_NN.json`. Then concatenate into `finn_references_aggregated.json`.*
