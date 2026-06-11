# Claude Code — Worked Examples

A curated gallery of Claude Code projects and supporting workshop materials from the **"Claude for Teaching, Course Development, and Research"** workshop series run by Marlon Kuzmick at Harvard's Bok Center Learning Lab.

## What's here

- **[examples/](examples/)** — two projects built live in this series, plus **[more-examples/](examples/more-examples/)**, a gallery of self-contained worked examples from earlier series. Each is meant to be opened as its own Claude Code project. Pick the one closest to your task; read its `summary.md` for the move it demonstrates and how to translate it.
- **[resources/](resources/)** — workshop-recap material: per-day handouts, the AI glossary (in both HTML and Markdown), and session takeaways.

### This series' projects

- **[handout-formatting](examples/handout-formatting/)** — turns rough course materials (a messy `.docx`, scanned PDFs, pasted text), in any subject, into clean, consistent, print-ready handouts via LaTeX. Packaged as a reusable skill that splits the house style into a `look` layer and a `behaviour` layer, so one source compiles to student, answer-key, and teacher versions with accessibility built in. Proven on both a Spanish reading/vocab sheet and a differential-equations course.
- **[admin-email-drafter](examples/admin-email-drafter/)** — drafts an administrator's reply to a student's questions about program requirements, answering each strictly from authoritative source material, citing every claim, and flagging anything the sources don't settle. The `/draft-reply` skill enforces a three-tier source hierarchy (College policy, department operational materials, student-perspective guides) so it never improvises policy. Claude drafts; the administrator reviews and sends.

See [CLAUDE.md](CLAUDE.md) for the full repo layout, conventions, and the table of all the examples.

## Using an example

Each example is standalone. To run one:

```bash
cd examples/<example-name>            # e.g. handout-formatting, admin-email-drafter
# or: cd examples/more-examples/<example-name>   # the earlier gallery
claude
```

The example's `CLAUDE.md` is loaded automatically and tells Claude Code what the project is, how to work in it, and what skills (if any) it ships.

## License

See [LICENSE](LICENSE).
