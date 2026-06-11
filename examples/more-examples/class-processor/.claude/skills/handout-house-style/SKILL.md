---
name: handout-house-style
description: Render a Markdown takeaways doc (or any short reference) as a single, self-contained, print-ready HTML page in the Learning Lab "house style" — Inter typeface, white background, red (#c8102e) as the only accent, on an 11x17 tabloid portrait sheet. A small, no-script, project-scoped copy of the global handout-house-style skill: you inline the CSS and font by hand, no build step. Use when turning a key-takeaways .md into its portable HTML companion, or making any single-page house-style handout for this project.
---

# handout-house-style (project copy)

A trimmed, **no-script** version of the global `handout-house-style` skill, scoped to
this example so it travels with the folder. It makes single-page, print-ready handouts
that all look like they belong together. Output is **one self-contained HTML file**
(font + styles inlined, no network) — the portable companion to a takeaways markdown.

There is no build script and no PDF step here: the HTML companion is the deliverable.
You assemble the self-contained file by hand (see Workflow).

## The look (non-negotiables)

- **Typeface:** Inter. Body is bold (`font-weight:600`); headings extra-bold (`800`–`900`).
- **Color:** white background, near-black text (`#141414`), and **red `#c8102e` as the only
  accent** — kicker, list markers/counters, links, key terms. Use red sparingly.
- **Paper:** 11x17 tabloid, portrait (`11in 17in`), 0.5in margin.
- **Header/footer:** a red uppercase **kicker** ("DAY 1 · 8 JUNE 2026 · TOP 10 TAKEAWAYS"),
  a big `h1` with a grey `.sub`, and a footer reading
  `Summer of Claude · Faculty Workshop · <date>` / `Bok Center · Learning Lab`.

## Files in this skill

```
assets/
  house-style.css              component styles + design tokens (the heart of it)
  fonts-inter.css              Inter (latin 500–900 + italics) as base64 woff2
  template-portrait.src.html   starter — portrait 11x17, pre-wired for a Top-10 doc
```

## Workflow

1. **Copy the template** to a working `.src.html`, or start from the structure below.
2. **Write the content.** For a key-takeaways doc the structure is fixed:
   - `.kicker` — `Day N · DD Month 2026 · Top 10 Takeaways`
   - `h1` "Top 10 Key Takeaways" + `.sub` (chunk/time range · instructors)
   - `p.provenance` — one italic line, linking the source transcript in `../inputs/`
   - `ol.top10` — **exactly ten** `<li>`, each leading with `<b>headline</b>` then the
     grounded explanation. `<i>` for italics, `<code>` for code/paths.
   - `p.beat-h` "Secondary points worth keeping" + `ul.sec` bullets.
   - `.footer` with the date.
   Convert the markdown to literal HTML by hand: `**bold**`→`<b>`, `*italic*`→`<i>`,
   `` `code` ``→`<code>`, `[t](u)`→`<a href="u">t</a>`. Escape literal `<`,`>`,`&`
   (e.g. `git clone <url>` → `git clone &lt;url&gt;`).
3. **Inline the assets to make it self-contained.** Replace the two placeholders at the
   top of `<style>`:
   - `/*__FONTS__*/` → the full contents of `assets/fonts-inter.css`
   - `/*__HOUSE_STYLE__*/` → the full contents of `assets/house-style.css`
   Read both files and paste them in verbatim. The result must have **no external
   resources** — no `<link>` to Google Fonts, no CDN (those make print engines stall
   and render blank). Write the finished file to `outputs/<day>-key-takeaways.html`.
4. **Verify.** Open the HTML; confirm one page, Inter loaded (not a system serif), red
   accents present, and content clears the footer. If it overflows, tighten the
   `font-size` / `margin` on `ol.top10`/`ul.sec` rather than shrinking the page.

## Components (class reference)

Defined in `house-style.css`. The takeaways doc uses `.kicker`, `h1`+`.sub`,
`.provenance`, `ol.top10`, `.beat-h`, `ul.sec`, `.footer`. Also available for other
handouts: `.lede`, `.beat`/`.sub-h`, `ul.list`/`ul.sub` (red square / dash markers),
`.callout` / `.takehome`, `table.glance`, the fill-in `.card`, file-row `.ft`, and the
`.flow` diagram. (The global skill's segmented-bar / pattern fills are omitted from this
copy — they need `patterns.css`, which this no-script version doesn't ship.)

## Page setup

Portrait block (already in the template):

```css
@page { size: 11in 17in; margin: 0.5in; }
.sheet { width:10in; height:16in; padding:0.55in 0.6in 0.8in; display:flex; flex-direction:column; }
.footer { bottom:0.34in; }
```
