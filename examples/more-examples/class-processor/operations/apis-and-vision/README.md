# APIs and vision — the capstone

Until now everything in this repo has been **text and files**. This operation
introduces the last piece: an **API** — a URL you can ask for data, or hand a
piece of work and get a result back. We meet two kinds.

## 1. An open data API (no key) — Luhmann's Zettelkasten

The Niklas Luhmann Archiv scanned the sociologist's entire **Zettelkasten** (his
famous paper slip-box) and serves it from an open API. You ask a URL for a branch
of slips and it answers with JSON — each slip's metadata, the archive's own
**transcription** of the handwriting, and an image id for the scan.

```bash
python3 scripts/fetch_zettels.py --branch 9/8 --rows 5 \
  --out ../../inputs/zettelkasten/zk-9-8.json
```

No key, no login — just a URL returning data. That is the whole idea of an API.
(A sample response is already saved at
[`inputs/zettelkasten/zk-9-8-sample.json`](../../inputs/zettelkasten/zk-9-8-sample.json).)

## 2. Vision APIs (need a key) — Gemini and Claude

The second kind of API takes *work*. `transcribe.py` sends an **image** to a
vision model and gets the **text** back. It can call two different providers —
**Gemini** and **Claude** — so you see the same task hit two endpoints:

```bash
cp ../../.env.example ../../.env      # then fill in your keys
pip install -r requirements.txt
python3 scripts/transcribe.py --image my-zettel.jpg --provider both
```

These need a **key**, kept in this example's own `.env` (never the repo root, never
committed). That is the practical difference between the two API kinds: the open
archive is a public reading room; a model API is a metered service you sign in to.

## The move worth noticing — transference

A Luhmann slip is just a handwritten card. So is a **photo of your blackboard**,
or a **scan of a student's in-class exercise**. The same `transcribe.py` turns any
of them into text:

```bash
python3 scripts/transcribe.py --image ../../inputs/board-work/lecture3.jpg --provider claude
```

And because the Zettelkasten API also returns the archive's *own* transcription,
you can close the loop: fetch a slip, transcribe its scan with a vision model,
and compare your output to the human transcription — a built-in answer key.

## Worked outputs (real runs)

- [`outputs/apis-and-vision/zettel-9-8-gemini-vs-claude.md`](../../outputs/apis-and-vision/zettel-9-8-gemini-vs-claude.md) — slip 9/8 read by **both** Gemini and Claude, side by side, with the archive's own transcription as the answer key. The downloaded facsimile is at [`inputs/zettelkasten/facsimiles/`](../../inputs/zettelkasten/facsimiles/).
- [`outputs/apis-and-vision/sample-board-transcription.md`](../../outputs/apis-and-vision/sample-board-transcription.md) — the transference: the same script reading a CS 1200 **blackboard** frame.

## Files

```
operations/apis-and-vision/
├── README.md            ← you are here
├── requirements.txt     ← just `requests`
└── scripts/
    ├── fetch_zettels.py   open data API — fetch slips (no key)
    └── transcribe.py      vision APIs — image → text via Gemini and/or Claude (key)
```

We call both APIs with plain `requests` (not a provider SDK) on purpose, so the
raw shape of an HTTP API stays visible. Keys are read from `../../.env`
(see [`.env.example`](../../.env.example)); slips are written to
`inputs/zettelkasten/`, transcriptions print to your terminal.

References — Luhmann Archiv: <https://niklas-luhmann-archiv.de/projekt/dokumentation>
