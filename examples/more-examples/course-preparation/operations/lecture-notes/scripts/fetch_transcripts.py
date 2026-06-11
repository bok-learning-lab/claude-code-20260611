#!/usr/bin/env python3
"""
Download all Panopto transcripts from a folder.

Usage:
    python fetch_transcripts.py --cookie "your_session_cookie" [--out transcripts/]

To get your session cookie:
    1. Log into https://harvard.hosted.panopto.com in your browser
    2. Open DevTools (F12) -> Application -> Cookies -> harvard.hosted.panopto.com
    3. Copy the value of the cookie named ".ASPXAUTH" (or run in the Console:
         document.cookie
       and paste the full string here)
"""

import argparse
import json
import os
import re
import sys
import time
import requests

BASE_URL = "https://harvard.hosted.panopto.com"
FOLDER_ID = "8077e062-6574-4e03-8148-b383013ba98b"


def get_sessions(session: requests.Session, folder_id: str) -> list[dict]:
    """Fetch all sessions in the folder, handling pagination."""
    sessions = []
    page = 0
    page_size = 50
    while True:
        resp = session.get(
            f"{BASE_URL}/Panopto/api/v1/folders/{folder_id}/sessions",
            params={"pageNumber": page, "pageSize": page_size},
        )
        resp.raise_for_status()
        data = resp.json()
        results = data.get("Results", [])
        sessions.extend(results)
        if len(sessions) >= data.get("TotalNumberOfResults", 0):
            break
        page += 1
    return sessions


def download_transcript(session: requests.Session, session_data: dict, out_dir: str):
    """Download the transcript for a single Panopto session."""
    title = session_data.get("Name", session_data.get("Id"))
    caption_url = session_data.get("Urls", {}).get("CaptionDownloadUrl")

    if not caption_url:
        print(f"  [skip] No caption URL for: {title}")
        return

    resp = session.get(caption_url)
    if resp.status_code != 200:
        print(f"  [fail] HTTP {resp.status_code} for: {title}")
        return

    safe_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
    filename = os.path.join(out_dir, f"{safe_title}.srt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(resp.text)
    print(f"  [ok] {filename}")


def main():
    parser = argparse.ArgumentParser(description="Download Panopto transcripts")
    parser.add_argument("--cookie", required=True,
                        help="Full cookie string from browser (copy from DevTools)")
    parser.add_argument("--out", default="transcripts",
                        help="Output directory (default: transcripts/)")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    session = requests.Session()
    session.headers.update({
        "Cookie": args.cookie,
        "User-Agent": "Mozilla/5.0",
        "Referer": BASE_URL,
    })

    print(f"Fetching sessions from folder {FOLDER_ID}...")
    try:
        sessions = get_sessions(session, FOLDER_ID)
    except requests.HTTPError as e:
        print(f"Error fetching sessions: {e}")
        print("Check that your cookie is valid and not expired.")
        sys.exit(1)

    print(f"Found {len(sessions)} sessions.\n")

    for s in sessions:
        # Fetch full session data (includes Urls field with CaptionDownloadUrl)
        session_id = s.get("Id")
        title = s.get("Name", session_id)
        print(f"Processing: {title}")
        full = session.get(f"{BASE_URL}/Panopto/api/v1/sessions/{session_id}")
        if full.status_code != 200:
            print(f"  [fail] Could not fetch session details (HTTP {full.status_code})")
            continue
        download_transcript(session, full.json(), args.out)
        time.sleep(0.3)  # be polite to the server

    print("\nDone.")


if __name__ == "__main__":
    main()
