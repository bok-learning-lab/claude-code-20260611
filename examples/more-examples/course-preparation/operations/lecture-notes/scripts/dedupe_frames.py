#!/usr/bin/env python3
"""
Deduplicate lecture frames by removing near-identical consecutive images.

For each lecture folder in --frames, compares consecutive frames using
a perceptual image hash. Frames that are too similar to the last kept
frame are skipped. The kept frames are copied to --out with the same
subfolder structure.

Usage:
    python3 dedupe_frames.py [--frames frames_camera/] [--out frames_deduped/] [--sensitivity 10]

--sensitivity: hash distance threshold (0-64). Higher = keep more frames
               (less aggressive deduplication). Default 10 is a good start.
               Try 5 for aggressive dedup, 15 for light dedup.
"""

import argparse
import glob
import os
import shutil
from PIL import Image


def ahash(img: Image.Image, size: int = 16) -> int:
    """Compute average hash of an image as an integer."""
    grey = img.convert("L").resize((size, size), Image.LANCZOS)
    pixels = list(grey.getdata()) if hasattr(grey, 'getdata') else list(grey.tobytes())
    pixels = list(grey.tobytes())
    avg = sum(pixels) / len(pixels)
    bits = [1 if p >= avg else 0 for p in pixels]
    h = 0
    for b in bits:
        h = (h << 1) | b
    return h


def hamming(a: int, b: int) -> int:
    """Hamming distance between two hashes."""
    return bin(a ^ b).count("1")


def dedupe_lecture(frame_dir: str, out_dir: str, sensitivity: int) -> tuple[int, int]:
    """
    Deduplicate frames in frame_dir, copying unique ones to out_dir.
    Returns (total, kept) counts.
    """
    frames = sorted(glob.glob(os.path.join(frame_dir, "*.jpg")))
    if not frames:
        return 0, 0

    os.makedirs(out_dir, exist_ok=True)

    last_hash = None
    kept = 0

    for path in frames:
        img = Image.open(path)
        h = ahash(img)

        if last_hash is None or hamming(h, last_hash) >= sensitivity:
            shutil.copy2(path, os.path.join(out_dir, os.path.basename(path)))
            last_hash = h
            kept += 1

    return len(frames), kept


def main():
    parser = argparse.ArgumentParser(description="Deduplicate lecture frames")
    parser.add_argument("--frames", default="frames_camera",
                        help="Input frames directory (default: frames_camera/)")
    parser.add_argument("--out", default="frames_deduped",
                        help="Output directory (default: frames_deduped/)")
    parser.add_argument("--sensitivity", type=int, default=10,
                        help="Hash distance threshold 0-64 (default: 10)")
    args = parser.parse_args()

    lecture_dirs = sorted(glob.glob(os.path.join(args.frames, "*")))
    lecture_dirs = [d for d in lecture_dirs if os.path.isdir(d)]

    if not lecture_dirs:
        print(f"No subdirectories found in {args.frames}/")
        return

    print(f"Found {len(lecture_dirs)} lecture(s). Sensitivity={args.sensitivity}\n")
    total_in = total_out = 0

    for lecture_dir in lecture_dirs:
        name = os.path.basename(lecture_dir)
        out_dir = os.path.join(args.out, name)
        n_in, n_out = dedupe_lecture(lecture_dir, out_dir, args.sensitivity)
        pct = (1 - n_out / n_in) * 100 if n_in else 0
        print(f"{name}")
        print(f"  {n_in} frames → {n_out} kept ({pct:.0f}% removed)\n")
        total_in += n_in
        total_out += n_out

    print(f"Total: {total_in} → {total_out} frames ({(1-total_out/total_in)*100:.0f}% removed)")


if __name__ == "__main__":
    main()
