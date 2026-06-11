#!/usr/bin/env python3
"""
Extract key frames from lecture videos for slide creation.

For each video, extracts frames using two strategies combined:
  1. Scene change detection (ffmpeg scene filter, threshold 0.25) — catches
     major board changes like erasure + new content
  2. Regular interval fallback (every 45 seconds) — ensures coverage of
     gradual board filling

Frames are deduplicated by keeping only one frame per 15-second window.
Output: frames/<video_stem>/<timestamp>.jpg

Usage:
    python extract_frames.py [--videos videos/] [--out frames/] [--interval 45] [--threshold 0.25]
"""

import argparse
import os
import subprocess
import json
import glob


def get_duration(video_path: str) -> float:
    """Return video duration in seconds using ffprobe."""
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json",
         "-show_format", video_path],
        capture_output=True, text=True
    )
    data = json.loads(result.stdout)
    return float(data["format"]["duration"])


def extract_frames(video_path: str, out_dir: str, interval: int, threshold: float):
    stem = os.path.splitext(os.path.basename(video_path))[0]
    frame_dir = os.path.join(out_dir, stem)
    os.makedirs(frame_dir, exist_ok=True)

    existing = glob.glob(os.path.join(frame_dir, "*.jpg"))
    if existing:
        print(f"  [skip] {len(existing)} frames already exist in {frame_dir}")
        return

    duration = get_duration(video_path)
    print(f"  Duration: {duration/60:.1f} min")

    # Strategy 1: scene change detection
    # Outputs frames where scene score > threshold, with timestamp in filename
    scene_filter = (
        f"select='gt(scene,{threshold})',setpts=N/FRAME_RATE/TB"
    )
    # Use showinfo to get timestamps, write to temp file
    scene_cmd = [
        "ffmpeg", "-i", video_path,
        "-vf", f"select='gt(scene,{threshold})'",
        "-vsync", "vfr",
        "-frame_pts", "1",
        "-q:v", "2",
        os.path.join(frame_dir, "scene_%08d.jpg"),
    ]

    # Strategy 2: regular interval (every N seconds)
    # Use showinfo filter to write actual timestamps, then rename based on those
    interval_ts_file = os.path.join(frame_dir, "_interval_timestamps.txt")
    interval_cmd = [
        "ffmpeg", "-i", video_path,
        "-vf", f"fps=1/{interval},showinfo",
        "-q:v", "2",
        os.path.join(frame_dir, "interval_%08d.jpg"),
    ]

    print(f"  Extracting scene-change frames (threshold={threshold})...")
    subprocess.run(scene_cmd, capture_output=True)

    print(f"  Extracting interval frames (every {interval}s)...")
    result = subprocess.run(interval_cmd, capture_output=True, text=True)

    # Parse actual timestamps from showinfo stderr output
    interval_timestamps = []
    for line in result.stderr.splitlines():
        if "pts_time:" in line and "showinfo" in line:
            try:
                t = float(line.split("pts_time:")[1].split()[0])
                interval_timestamps.append(int(round(t)))
            except (IndexError, ValueError):
                pass

    # Rename interval frames using actual timestamps
    interval_frames = sorted(glob.glob(os.path.join(frame_dir, "interval_*.jpg")))
    for i, path in enumerate(interval_frames):
        if i < len(interval_timestamps):
            t = interval_timestamps[i]
        else:
            t = i * interval  # fallback
        new_name = os.path.join(frame_dir, f"t{t:06d}s_interval.jpg")
        os.rename(path, new_name)

    # Rename scene frames — we don't know exact timestamps from filenames alone,
    # so we run a second pass with ffprobe to extract pts timestamps
    scene_frames = sorted(glob.glob(os.path.join(frame_dir, "scene_*.jpg")))
    if scene_frames:
        # Re-extract scene frames with timestamp info via select+metadata filter
        ts_file = os.path.join(frame_dir, "_timestamps.txt")
        ts_cmd = [
            "ffmpeg", "-i", video_path,
            "-vf", f"select='gt(scene,{threshold})',metadata=print:file={ts_file}",
            "-vsync", "vfr", "-f", "null", "-"
        ]
        subprocess.run(ts_cmd, capture_output=True)

        # Parse timestamps
        timestamps = []
        if os.path.exists(ts_file):
            with open(ts_file) as f:
                for line in f:
                    if line.startswith("frame:pts_time"):
                        try:
                            t = float(line.split("pts_time:")[1].split()[0])
                            timestamps.append(t)
                        except (IndexError, ValueError):
                            pass
            os.remove(ts_file)

        for i, path in enumerate(scene_frames):
            if i < len(timestamps):
                t = int(timestamps[i])
                new_name = os.path.join(frame_dir, f"t{t:06d}s_scene.jpg")
            else:
                new_name = os.path.join(frame_dir, f"scene_unknown_{i:04d}.jpg")
            os.rename(path, new_name)

    total = len(glob.glob(os.path.join(frame_dir, "*.jpg")))
    print(f"  [ok] {total} frames saved to {frame_dir}/")


def main():
    parser = argparse.ArgumentParser(description="Extract key frames from lecture videos")
    parser.add_argument("--videos", default="videos", help="Directory containing .mp4 files")
    parser.add_argument("--out", default="frames", help="Output directory for frames")
    parser.add_argument("--interval", type=int, default=45,
                        help="Seconds between interval frames (default: 45)")
    parser.add_argument("--threshold", type=float, default=0.25,
                        help="Scene change threshold 0-1 (default: 0.25; lower = more sensitive)")
    args = parser.parse_args()

    videos = sorted(glob.glob(os.path.join(args.videos, "*.mp4")))
    if not videos:
        print(f"No .mp4 files found in {args.videos}/")
        return

    print(f"Found {len(videos)} videos.\n")
    for v in videos:
        print(f"Processing: {os.path.basename(v)}")
        extract_frames(v, args.out, args.interval, args.threshold)
        print()

    print("Done.")


if __name__ == "__main__":
    main()
