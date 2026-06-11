# Class summarizer

A worked example of turning a long session transcript into a **Top 10 Key Takeaways** doc faculty can read in five minutes. The project hands Claude a markdown transcript of a workshop session and asks it to distill the substance into ten numbered takeaways, each leading with a bold one-sentence headline (the mantra or claim itself) and grounded in what *actually happened* in the room — the demos used, the analogies the instructors reached for, the memorable turns of phrase, quoted directly. A separate "secondary points" section catches the smaller details that did not make the top 10.

The project also ships the `md-to-deepthoughts-html` skill, used to convert each markdown takeaways doc into a printable, portable HTML page styled in the workshop's reading layout.

---

## What it is

One prompt, one HTML-rendering skill, two transcripts processed.

- **The transcripts** (in `inputs/`):
  - [day_1_transcript.md](inputs/day_1_transcript.md) — Day 1 of the workshop.
  - [day_2_transcript.md](inputs/day_2_transcript.md) — Day 2 of the workshop.

- **The prompt** at [operations/key-takeaways-prompt.md](operations/key-takeaways-prompt.md) — the reusable distillation prompt. Reconstructed from the Day 1 output, designed to be pointed at any session's transcript. Specifies the doc's title shape, an italic provenance opening (what was distilled from, chunk/time range covered, instructors present), exactly 10 numbered takeaways with bold one-sentence headlines, a secondary-points section, and a voice constraint: tight, concrete, faculty-facing, favoring the instructors' own language over generic AI-explainer prose.

- **The rendering skill** at [operations/skills/md-to-deepthoughts-html/](operations/skills/md-to-deepthoughts-html/) — converts a markdown file into a self-contained HTML page styled like the "Deep thoughts" essay layout (cream/serif Dario-style, Newsreader font, scoped to the article view, with screen + mobile + print styles plus Print and Copy MD buttons). The skill is invoked after each takeaways markdown is produced.

- **The outputs** (in `outputs/`):
  - [day-1-key-takeaways.md](outputs/day-1-key-takeaways.md) / [.html](outputs/day-1-key-takeaways.html)
  - [day-2-key-takeaways.md](outputs/day-2-key-takeaways.md) / [.html](outputs/day-2-key-takeaways.html)

The HTML files are portable — inline styling, self-contained — so a faculty member who missed the session can email the page to themselves and read it on any device, print it, or copy the markdown back out.

### The move worth noticing

The instruction *"capture the teaching point, not just the fact — why it mattered to faculty"* is what turns this from a transcript summary into a teaching artifact. A generic LLM summary of a workshop session produces accurate but inert prose: "the instructors discussed prompt engineering, CLAUDE.md files, and the use of skills." That summary is *true* and *useless*. The takeaways prompt is structured to force the second layer — the headline mantra, the analogy the instructor used, the demo that landed, the line worth quoting. The artifact is meant to *re-create* the room, not describe it.

The provenance opening is doing a small but important job: the italic note states what was distilled from, the chunk or time range, and who was teaching. This makes the doc auditable. A faculty member who wants to know whether a takeaway was their colleague's or the instructor's can trace it back to the named speaker in the transcript.

---

## How we built it

The build is the prompt and the skill, applied per session.

**Per session:**

1. Capture the session transcript as markdown and drop it in `inputs/`.
2. Invoke the prompt at `operations/key-takeaways-prompt.md`, pointing it at the day's transcript.
3. Claude writes `outputs/<day>-key-takeaways.md` directly — title shape, italic provenance, ten numbered takeaways with bold headlines, secondary points.
4. Invoke the `md-to-deepthoughts-html` skill to produce the HTML companion at `outputs/<day>-key-takeaways.html`.

**The discipline the prompt enforces:**

- **Exactly 10 takeaways.** The number is a constraint, not a guideline. Ten forces the model to prioritize.
- **Bold one-sentence headline.** The headline is the *mantra* — the claim a faculty member would tell a colleague. Then 1–3 sentences of grounded explanation.
- **Specific to the room.** Name the demos, the analogies, the turns of phrase. Examples from the Day 1 output: the limerick CLAUDE.md, the recipe metaphor, the Memento/context-window image. Generic phrasing is the failure mode the prompt is designed to prevent.
- **Quote memorable lines.** Direct quotes are the receipts. They tell the reader this came from the room, not from the model's general knowledge of AI workshops.
- **Voice: tight, concrete, faculty-facing.** Favor the instructors' own language. No preamble. No "here's your summary."
- **Secondary points worth keeping.** A short bulleted section for the details that did not make the top 10 but matter. The two-tier structure is what lets the takeaways stay tight without losing the small things.

### Things this approach taught us

The forcing function on the count matters. Asking for "the key takeaways" produces a long list. Asking for "exactly ten" produces ranking. The act of choosing which thing to leave out is the act of distilling.

The provenance opening is small but load-bearing. The italic note names the source transcript, the chunk covered, and who was teaching. Without it, the takeaways are floating claims; with it, they are tied to a specific hour in a specific room with named people. A reader can audit any claim by going back to the transcript.

The bold-headline / explanation structure mirrors how a faculty member would tell a colleague about the session. *"Bold claim. Then a sentence or two of what actually happened that made the claim land."* The format is the form of the conversation a faculty member would want to be able to have after reading.

---

## What you can translate this to

The pattern is **a long-form transcript or document + a forced-count distillation prompt + a portable HTML renderer**. It applies wherever a busy reader needs to catch up on substance without reading the full source.

Domains where the same shape applies almost without modification:

- **Conference session summaries.** Drop a transcript or recorded-talk transcript; produce a Top 10 doc per session. Especially useful for multi-track conferences where attendees only see a slice.
- **Faculty meeting recaps** for absent members. The same prompt, applied to a meeting transcript, produces a defensible record of what was decided and what was discussed.
- **Course session catch-up for students who missed class.** Drop the lecture-capture transcript; produce a "What you missed" doc with the day's key concepts, examples, and any announcements.
- **Department retreat or strategy session distillations** — long, often unstructured conversations boiled down to a ranked list of decisions, open questions, and named follow-ups.
- **Interview transcript summaries** for research teams — top takeaways from a 90-minute interview, with verbatim quotes from the participant on each.
- **Podcast / long-form-conversation summaries** for readers who want the substance but not the full hour.

The pattern in all of these is the same: a transcript with named speakers, a forced count, headline-plus-explanation structure, verbatim quotes as receipts, and a portable HTML companion that survives email and print.

---

## Alignment constraints (the hard ones)

These survive translation to other domains:

- **Forced count, not "key takeaways."** Ten is a constraint. The model must rank to comply.
- **Provenance is part of the artifact.** The italic opening names the source, the range, and the speakers. Floating claims are not allowed.
- **Specific, not generic.** Name the demos, analogies, and turns of phrase. Quote the memorable lines. Generic prose is the failure mode.
- **Two-tier structure.** Top 10 stays tight; secondary points catches the rest.
- **Portable HTML companion.** Inline CSS, no external assets. The artifact survives email, print, and offline reading.
- **No preamble.** Just the doc.
