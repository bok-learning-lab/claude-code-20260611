# texts-and-translation — folder index

A scaffolded demonstration of LLM-assisted close work for disciplines whose primary sources are not in English. Start with [summary.md](summary.md); everything else is here for browsing.

## Top-level

- [summary.md](summary.md) — what this project is, how we built it, what you can translate it to
- [CLAUDE.md](CLAUDE.md) — project-level instructions loaded by Claude Code on session start
- [index.md](index.md) / [index.html](index.html) — this file

## inputs/

Two demo corpora, each set up as a standalone target.

- inputs/the-odyssey/
  - [odyssey_homeric_greek.xml](inputs/the-odyssey/odyssey_homeric_greek.xml) — Homeric Greek in TEI/XML (PerseusDL, Murray edition)
  - inputs/the-odyssey/translations/ — 14 translations across 6 languages:
    - English: [Bryant](inputs/the-odyssey/translations/odyssey_bryant_book1.txt), [Butcher/Lang](inputs/the-odyssey/translations/Odyssey_Butcher_Lang.txt), [Butler](inputs/the-odyssey/translations/Odyssey_translated_by_Samuel_Butler.txt), [Cotterill](inputs/the-odyssey/translations/odyssey_cotterill.txt), [Cowper](inputs/the-odyssey/translations/The-Odyssey-William_Cowper_J_Johnson.txt), [Merry/Riddell](inputs/the-odyssey/translations/Odyssey_Merry_Riddell.txt), [Monro](inputs/the-odyssey/translations/Odyssey_David_Monro.txt), [Pope](inputs/the-odyssey/translations/odyssey_pope.txt), [Alford hendecasyllable](inputs/the-odyssey/translations/Odyssey_hendecasyllable_alford.txt)
    - Greek: [Polylas (Modern Greek)](inputs/the-odyssey/translations/odyssey_greek_Iakovos_Polylas.txt)
    - Latin: [odyssea-latin](inputs/the-odyssey/translations/odyssea-latin.txt)
    - French: [Calbet](inputs/the-odyssey/translations/lodyssee_french_calbet.txt)
    - Spanish: [Segala Estalella](inputs/the-odyssey/translations/la_odisea_spanish_Segala_Estalella.txt)
    - Swedish: [Sjöström](inputs/the-odyssey/translations/Odysseia_swedish_sjostrom.txt)
- inputs/early-modern-sanskrit/
  - [jagannatha-rasagangadhara.htm](inputs/early-modern-sanskrit/jagannatha-rasagangadhara.htm) — Ānana 1 of Jagannātha Paṇḍitarāja's *Rasagaṅgādhara* (17th c.) in Devanāgarī from GRETIL, edited by Timothy C. Cahill

## operations/

Prompts and skills.

- [operations/deep-research-prompt.md](operations/deep-research-prompt.md) — prompt that commissioned the background research at `outputs/research-result.md`
- .claude/skills/
  - [split-into-books/](.claude/skills/split-into-books/) — utility: pre-splits translation files into per-book files
  - [show-passage/](.claude/skills/show-passage/) — display a passage (by primary coordinate) with Greek original + chosen translations
  - [identify-figures-greek/](.claude/skills/identify-figures-greek/) — identify rhetorical figures in a Homeric Greek passage
  - [identify-figures-sanskrit/](.claude/skills/identify-figures-sanskrit/) — identify candidate *alaṃkāras* in a *Rasagaṅgādhara* passage

## outputs/

Produced artifacts. Skill outputs preserve the corpus nesting used in `inputs/`.

- outputs/the-odyssey/
  - figures-greek/ — figure-identification outputs against the Homeric Greek corpus
  - passages/ — `/show-passage` outputs
- [outputs/research-result.md](outputs/research-result.md) — background research on the project's place in the philological / translation-theory traditions

---

*To run end-to-end: open this folder in Claude Code, run `/split-into-books all` once to pre-split the translation files, then `/show-passage 1.1-10` on the proem to see Wilson next to Lattimore next to Pope; then `/identify-figures-sanskrit` on an illustrative verse from the *Rasagaṅgādhara* whose alaṃkāra Jagannātha himself names.*
