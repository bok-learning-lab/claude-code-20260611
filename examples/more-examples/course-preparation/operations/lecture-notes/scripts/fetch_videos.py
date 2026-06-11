#!/usr/bin/env python3
"""
Download the camera (dv) stream from all Panopto lecture sessions in a folder.

The camera stream shows the instructor + blackboard, which is what we want
for frame extraction. The composite MP4 (which includes the laptop screen
as the dominant element) is not used.

Usage:
    python3 fetch_videos.py --cookie ".ASPXAUTH=..." [--out videos/]

Videos are saved as <title>.mp4. Skips files that already exist.
"""

import argparse
import os
import re
import subprocess
import sys
import time
import requests

BASE_URL = "https://harvard.hosted.panopto.com"
FOLDER_ID = "8077e062-6574-4e03-8148-b383013ba98b"


def get_sessions(session: requests.Session) -> list[dict]:
    sessions = []
    page = 0
    while True:
        resp = session.get(
            f"{BASE_URL}/Panopto/api/v1/folders/{FOLDER_ID}/sessions",
            params={"pageNumber": page, "pageSize": 50},
        )
        resp.raise_for_status()
        data = resp.json()
        sessions.extend(data.get("Results", []))
        if len(sessions) >= data.get("TotalNumberOfResults", 0):
            break
        page += 1
    return sessions


def get_camera_stream_url(session: requests.Session, session_id: str) -> str | None:
    """Fetch the HLS URL for the camera (dv) stream via the DeliveryInfo endpoint."""
    resp = session.get(
        f"{BASE_URL}/Panopto/Pages/Viewer/DeliveryInfo.aspx",
        params={
            "deliveryId": session_id,
            "invocationId": "",
            "isLiveNotes": "false",
            "refreshAuthCookie": "true",
            "isActiveBroadcast": "false",
            "isEditing": "false",
            "isKollectiveAgentInstalled": "false",
            "isEmbed": "false",
            "responseType": "json",
        },
    )
    if resp.status_code != 200:
        return None
    streams = resp.json().get("Delivery", {}).get("Streams", [])
    for stream in streams:
        if stream.get("Tag") == "dv":
            return stream.get("StreamHttpUrl") or stream.get("StreamUrl")
    return None


def safe_filename(title: str) -> str:
    return re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')


def download_video(session: requests.Session, session_id: str, title: str, out_dir: str):
    filename = os.path.join(out_dir, f"{safe_filename(title)}.mp4")
    if os.path.exists(filename):
        print(f"  [exists] {filename}")
        return

    stream_url = get_camera_stream_url(session, session_id)
    if not stream_url:
        print(f"  [skip] No camera stream found for: {title}")
        return

    print(f"  Downloading camera stream: {title}")
    # ffmpeg handles HLS natively; -c copy avoids re-encoding
    result = subprocess.run([
        "ffmpeg", "-i", stream_url,
        "-c", "copy",
        "-stats", "-loglevel", "warning",
        "-y", filename,
    ])

    if result.returncode == 0:
        size_mb = os.path.getsize(filename) / 1024 / 1024
        print(f"  [ok] {filename} ({size_mb:.0f} MB)")
    else:
        print(f"  [fail] ffmpeg error for: {title}")


def main():
    parser = argparse.ArgumentParser(description="Download Panopto camera streams")
    parser.add_argument("--cookie", required=True, help="Browser cookie string")
    parser.add_argument("--out", default="videos", help="Output directory (default: videos/)")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    session = requests.Session()
    session.headers.update({
        "Cookie": args.cookie,
        "User-Agent": "Mozilla/5.0",
        "Referer": BASE_URL,
    })

    print("Fetching session list...")
    try:
        sessions = get_sessions(session)
    except requests.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Found {len(sessions)} sessions.\n")

    for s in sessions:
        session_id = s.get("Id")
        title = s.get("Name", session_id)
        print(f"Processing: {title}")
        download_video(session, session_id, title, args.out)
        time.sleep(0.5)

    print("\nDone.")


if __name__ == "__main__":
    main()
