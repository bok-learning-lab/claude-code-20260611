# Sample output — a blackboard frame, read by a vision API

A real run of `operations/apis-and-vision/scripts/transcribe.py`, demonstrating
the transference: the same image-to-text move that reads a Luhmann slip reads a
**blackboard photo**.

- **Source image:** `examples/course-preparation/inputs/lecture-recordings/frames_deduped/t001395s_interval.jpg` (a CS 1200 lecture board)
- **Provider:** Google Gemini (`gemini-2.5-flash`), via `transcribe.py --provider gemini`
- **Prompt:** the default "transcribe the text in this image exactly" prompt

Transcription returned:

```
Searching a keyword on Google
- Pagerank of a url PR(url) ∈ [0,1] ∀ url on WWW
- Keyword Search given w, consider Sw {All urls, where w is found}
- Sorted list: return urls in Sw in decreasing order of PR( )

Sorting Problem

What is an algorithm?
- steps to solve a problem
- procedure given inputs -> outputs
- simplification of "real-world way," to solve problem
- methodology to manage a data set

Unit 1  Storing & Search
Unit 2  Computational models
+ 3.    Graph & Logic
4/5.    Computational complexity & uncomputability

Unit 1  * abstracting a computational problem
        * prove an algorithm solves a problem
        * analysing & comparing efficiency
        * formalize "what is an algorithm"
```

Swap `--provider claude` (with an `ANTHROPIC_API_KEY` in `.env`) to get a second
model's reading of the same board, or `--provider both` to compare them.
