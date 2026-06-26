"""Update a problem's status and focused time."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRESS_FILE = ROOT / "progress.json"
VALID_STATUSES = ("not_started", "in_progress", "completed", "review")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Track Blind 75 problem progress.")
    parser.add_argument("slug", help="Problem slug from progress.json")
    parser.add_argument("--status", choices=VALID_STATUSES)
    parser.add_argument("--add-minutes", type=int, default=0)
    parser.add_argument("--note")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.add_minutes < 0:
        raise SystemExit("--add-minutes must be zero or greater.")

    data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    problem = next((item for item in data["problems"] if item["slug"] == args.slug), None)
    if problem is None:
        raise SystemExit(f"Unknown problem slug: {args.slug}")

    if args.status:
        problem["status"] = args.status
        if args.status in {"in_progress", "completed", "review"} and not problem.get("started_on"):
            problem["started_on"] = date.today().isoformat()
        if args.status == "completed":
            problem["completed_on"] = date.today().isoformat()
        elif args.status == "not_started":
            problem["started_on"] = None
            problem["completed_on"] = None

    problem["time_minutes"] = int(problem.get("time_minutes", 0)) + args.add_minutes
    if args.note:
        problem["notes"] = args.note

    PROGRESS_FILE.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "update_progress.py")], check=True)
    print(
        f"{problem['title']}: {problem['status']}, "
        f"{problem['time_minutes']} total minute(s)."
    )


if __name__ == "__main__":
    main()
