# class-summarizer — folder index

A worked example of turning a long workshop session transcript into a Top 10 Key Takeaways doc faculty can read in five minutes — markdown and HTML, ready for email and print. Start with [summary.md](summary.md); everything else is here for browsing.

## Top-level

- [summary.md](summary.md) — what this project is, how we built it, what you can translate it to
- [index.md](index.md) / [index.html](index.html) — this file

## inputs/

Session transcripts. One markdown file per day, with speaker tags.

- [inputs/day_1_transcript.md](inputs/day_1_transcript.md) — Day 1 of the workshop
- [inputs/day_2_transcript.md](inputs/day_2_transcript.md) — Day 2 of the workshop
- [inputs/day_3_transcript.md](inputs/day_3_transcript.md) — Day 3 of the workshop (takeaways not yet generated)

## operations/

- [operations/key-takeaways-prompt.md](operations/key-takeaways-prompt.md) — the reusable distillation prompt. Forces exactly 10 takeaways with bold one-sentence headlines, an italic provenance opening, and a secondary-points section. Voice: tight, concrete, faculty-facing, favoring the instructors' own language
- operations/skills/
  - [md-to-deepthoughts-html/](operations/skills/md-to-deepthoughts-html/) — converts a markdown takeaways doc into a self-contained "Deep thoughts" style HTML page (cream/serif Dario layout, Newsreader font, screen + mobile + print styles, Print and Copy MD buttons)

## outputs/

One markdown and one HTML per session.

- [outputs/day-1-key-takeaways.md](outputs/day-1-key-takeaways.md) / [.html](outputs/day-1-key-takeaways.html)
- [outputs/day-2-key-takeaways.md](outputs/day-2-key-takeaways.md) / [.html](outputs/day-2-key-takeaways.html)

---

*To run on a new session: drop the transcript at `inputs/day_N_transcript.md`, invoke the prompt at [operations/key-takeaways-prompt.md](operations/key-takeaways-prompt.md), then run the `md-to-deepthoughts-html` skill on the resulting markdown to produce the portable HTML companion.*
