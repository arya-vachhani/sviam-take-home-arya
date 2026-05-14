"""
Session data loader.
Reads session JSON files from /data/sessions/.
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "sessions"
LABELS_PATH = Path(__file__).resolve().parent.parent / "data" / "labels.json"


def load_session(session_id: str) -> dict:
    """Load a single session by ID (e.g., 'session_01')."""
    path = DATA_DIR / f"{session_id}.json"
    with open(path) as f:
        return json.load(f)


def load_all_sessions() -> list[dict]:
    """Load all 18 sessions, sorted by session_id."""
    sessions = []
    for path in sorted(DATA_DIR.glob("session_*.json")):
        with open(path) as f:
            sessions.append(json.load(f))
    return sessions


def load_labels() -> dict:
    """Load the ground-truth labels (only 5 of 18 are labeled)."""
    with open(LABELS_PATH) as f:
        return json.load(f)


if __name__ == "__main__":
    sessions = load_all_sessions()
    labels = load_labels()
    print(f"Loaded {len(sessions)} sessions, {len(labels)} labels")
    for s in sessions:
        label = labels.get(s["session_id"], "unlabeled")
        print(f"  {s['session_id']}: {s['problem_id']} ({s['language']}) — {label}")
