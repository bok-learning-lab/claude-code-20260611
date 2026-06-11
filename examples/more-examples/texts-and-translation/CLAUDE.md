# CLAUDE.md — Texts and translation

Project-level instructions loaded when Claude Code starts in this folder.

## What this project is

A workshop project for faculty who work with texts in languages other than English — translation, close reading, comparative scholarship across editions and translations. See [summary.md](summary.md) for what the project ships, the tradition it sits in, and what LLMs change about it.

Two corpora bundled, each set up as a standalone demo target:

- [inputs/the-odyssey/](inputs/the-odyssey/) — Homer's *Odyssey* in 14 translations spanning Greek, Latin, Spanish, French, Swedish, and English (Bryant, Butcher/Lang, Butler, Cotterill, Cowper, Merry/Riddell, Monro, Pope), plus the Homeric original in TEI/XML (PerseusDL, Murray edition). Designed for *comparative translation*.
- [inputs/early-modern-sanskrit/](inputs/early-modern-sanskrit/) — Jagannātha Paṇḍitarāja's *Rasagaṅgādhara* (17th c.), Ānana 1, from the GRETIL etext archive. Designed for *close work on a non-Roman-script primary text*, including identifying figures of speech in a treatise that is itself about figures of speech.

Skills live under `.claude/skills/` so the project travels as a self-contained bundle.

## If you just opened this folder

Read in this order:

1. [summary.md](summary.md) — what this is, how we built it, what you can translate it to.
2. [index.md](index.md) — a map of the folder.
3. The skill SKILL.md files in [.claude/skills/](.claude/skills/) for the specific skill you want to invoke.

## The skills

| Skill | File | What it does |
|---|---|---|
| `/split-into-books` | [.claude/skills/split-into-books/SKILL.md](.claude/skills/split-into-books/SKILL.md) | Splits translation files into 24 per-book files for fast passage queries |
| `/show-passage` | [.claude/skills/show-passage/SKILL.md](.claude/skills/show-passage/SKILL.md) | Displays a passage with original Homeric Greek at top and chosen translations below |
| `/identify-figures-sanskrit` | [.claude/skills/identify-figures-sanskrit/SKILL.md](.claude/skills/identify-figures-sanskrit/SKILL.md) | Identifies candidate alaṃkāras in a passage from the *Rasagaṅgādhara* |
| `/identify-figures-greek` | [.claude/skills/identify-figures-greek/SKILL.md](.claude/skills/identify-figures-greek/SKILL.md) | Identifies rhetorical figures in a passage of Homeric Greek |

Run `/split-into-books all` once before using `/show-passage`.

## Audience modes

- **Faculty working with their own non-English texts.** May never have touched a code editor. Default to plain-English explanations; do not assume CLI fluency. Frame outputs in terms of the scholarly task (close reading, translation comparison, glossary work, figure identification), not in terms of "data" or "documents."
- **Marlon (or another collaborator) iterating on the project itself.** Terse responses.

If unsure which mode applies, ask one question to disambiguate.

## Conventions

- **Skills live in `.claude/skills/<skill-name>/`** — project-scoped, so they travel with this folder.
- **Source texts are read-only.** Don't modify files in `inputs/`. Generated artifacts go in `outputs/` (using the same sub-corpus nesting — `outputs/the-odyssey/`, `outputs/early-modern-sanskrit/`).
- **Preserve script and diacritics exactly.** Do not silently transliterate, romanize, or strip diacritics. If a transformation is needed, produce a separate file and label it explicitly (e.g. `passage-iast.txt`).
- **No emojis** in any file.
- **Markdown link syntax** for file references — `[Pope](inputs/the-odyssey/translations/odyssey_pope.txt)`.
- **Cite by edition and line/verse**, not by file line number. A passage exists at *Odyssey* 1.1–10 across every translation; that citation should be primary, with file paths secondary.

## Alignment with humanistic practice

Workshop participants here are likely to be skeptical of LLM-assisted text work, often for good reasons. Skills built here should:

- Frame the LLM as a *first-pass collaborator*, not a final arbiter. The scholar reads the primary source; the LLM surfaces candidates the scholar evaluates.
- Be honest about what the model can and cannot do. It can compare translations; it cannot make Sanskrit philological judgments at the level of a trained Sanskritist.
- Quote verbatim. Paraphrase is the scholar's job, not the LLM's.
- Cite by primary-source coordinates (book.line, verse number, sūtra number), not by file path.
- Never invent passages or translations. If asked for a translation that does not exist in the corpus, say so.
