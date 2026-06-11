#!/usr/bin/env bash
# build.sh -- rebuild the worked example outputs from the .tex sources.
#
# Requires: tectonic (https://tectonic-typesetting.github.io) on PATH.
# Optional: pdftotext (poppler) for the extract step shown in the prompts.
#
# What it does:
#   1. Copies the canonical style packages from operations/ into outputs/ so the
#      example course tree compiles standalone (the outputs/ copies are
#      generated; the sources of truth live in operations/).
#        - handout.sty    the provided environment package (problem/solution/...)
#        - coursestyle.sty the visual layer (colors, banners, title macros)
#   2. Compiles every .tex under outputs/Worksheets and outputs/Homework.
#
# Run from anywhere; paths are resolved relative to this script.
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
recipe="$(cd "$here/../.." && pwd)"

echo "Refreshing outputs/ style packages from operations/"
cp "$recipe/operations/handout.sty"     "$recipe/outputs/handout.sty"
cp "$recipe/operations/coursestyle.sty" "$recipe/outputs/coursestyle.sty"

for dir in "$recipe/outputs/Worksheets" "$recipe/outputs/Homework"; do
    [ -d "$dir" ] || continue
    for tex in "$dir"/*.tex; do
        [ -e "$tex" ] || continue
        echo "Compiling $(basename "$tex")"
        ( cd "$dir" && tectonic "$(basename "$tex")" )
    done
done

echo "Done. PDFs are written next to their .tex sources."
