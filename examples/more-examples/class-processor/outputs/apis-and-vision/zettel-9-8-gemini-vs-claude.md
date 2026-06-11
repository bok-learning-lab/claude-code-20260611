# Vision API comparison — Luhmann slip 9/8 (Gemini vs. Claude)

A real run of `operations/apis-and-vision/scripts/transcribe.py --provider both`
on one Zettelkasten card. The point: two vision APIs read the *same* handwritten
image and return *different* text — and the open Luhmann API hands us the
archive's own transcription as an answer key.

- **Card:** ZK II 9/8 ("Zettelkasten als kybernetisches System")
- **Facsimile:** [`inputs/zettelkasten/facsimiles/ZK_2_15_52_047_V_N_NB_9-8.jpg`](../../inputs/zettelkasten/facsimiles/ZK_2_15_52_047_V_N_NB_9-8.jpg) (downloaded from the open API, `?size=2`)
- **Models:** Gemini `gemini-2.5-flash` · Claude `claude-opus-4-8`

---

## Ground truth — the archive's own transcription

> 9/8 Zettelkasten 1 — als kybernetisches System. Kombination von **Unordnung und Ordnung**, von Klumpenbildung und unvorhersehbarer, im ad hoc Zugriff realisierter Kombination. Vorbedingung: Verzicht auf festgelegte Ordnung. Die vorgeschaltete Differenzierung: Suchhilfen vs. Inhalt; Register, Fragestellungen, Einfälle vs. Vorhandenes überformt und macht z.T. entbehrlich, das, was an innerer Ordnung vorausgesetzt werden muss.

(from the `transcriptionPreview` field returned by `fetch_zettels.py`)

## Gemini (`gemini-2.5-flash`)

```
3/8 Zettelkasten 1
als Kybernetisches System
Kombination von Umordnung w Ordnung
von Neucombildung und unvorhersehbare
im ad hoc zugriff realistische Kombination!
Unterscheidung: Verzicht auf festgelegte Ordnung
Die vorgeschaltete Differenzierung: Suchhilfen
vs. Inhalt ; Repisto, Fragesteller, Entfälle
vs. Vorhandenes überfordert w (nicht z.T.)
entstehen das vor in innerer Ordnung
vorausgesetzt werden muß.
```

## Claude (`claude-opus-4-8`)

```
9/8  Zettelkasten  1

a) Kybernetisches System
Kombination von Unordnung und Ordnung,
von Klumpenbildung und Unvorhersehbar-
keit, also der Zugriff realistische Kombination.

Verbindung: Verzicht auf festgelegte Ordnung
Die vorgeschaltete Differenzierung: Suchhilfen
vs. Inhalt; Register, Fragestellung, Einfälle
vs. Vorhandenes überschritten und macht z.T.
unlöslich, den man als inneres Ordnung
vorausgesetzt werden muss.
```

---

## What the comparison teaches

- **Two APIs, two readings.** Same image, same prompt — different output. An API
  is a service, not an oracle; the model behind it has a point of view.
- **Both are imperfect on hard handwriting, in different ways.** Gemini misreads
  the slip number ("3/8") and "Unordnung" → "Umordnung"; Claude gets the slip
  number and "Unordnung und Ordnung" right and even flags its own uncertainty,
  but invents line breaks and a couple of words ("unlöslich").
- **The open API is the answer key.** Because `fetch_zettels.py` also returns the
  archive's human transcription, you can *grade* a vision model's output instead
  of trusting it — the same discipline as checking a board-work transcription
  against what the instructor actually wrote.

Run it yourself: `python3 operations/apis-and-vision/scripts/transcribe.py --image inputs/zettelkasten/facsimiles/ZK_2_15_52_047_V_N_NB_9-8.jpg --provider both`
