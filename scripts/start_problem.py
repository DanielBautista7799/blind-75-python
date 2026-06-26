"""Create a standard folder for a problem listed in progress.json."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRESS_FILE = ROOT / "progress.json"
TEMPLATES = ROOT / "templates"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Start a Blind 75 problem.")
    parser.add_argument("slug", help="Problem slug from progress.json, such as valid-anagram")
    return parser.parse_args()


def render(template_name: str, title: str, category: str) -> str:
    template = (TEMPLATES / template_name).read_text(encoding="utf-8")
    return (
        template.replace("{{TITLE}}", title)
        .replace("{{CATEGORY}}", category)
        .replace("{{DATE}}", date.today().isoformat())
    )


def main() -> None:
    args = parse_args()
    data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))

    problem = next((item for item in data["problems"] if item["slug"] == args.slug), None)
    if problem is None:
        available = ", ".join(item["slug"] for item in data["problems"])
        raise SystemExit(f"Unknown problem slug: {args.slug}\nAvailable slugs:\n{available}")

    folder = ROOT / problem["category_slug"] / problem["slug"]
    if folder.exists():
        print(f"Problem folder already exists: {folder.relative_to(ROOT)}")
    else:
        folder.mkdir(parents=True)
        for filename in ("description.md", "notes.md", "solution.py", "test_solution.py"):
            (folder / filename).write_text(
                render(filename, problem["title"], problem["category"]),
                encoding="utf-8",
            )
        print(f"Created {folder.relative_to(ROOT)}")

    problem["folder"] = f"{problem['category_slug']}/{problem['slug']}"
    if problem["status"] == "not_started":
        problem["status"] = "in_progress"
    if not problem.get("started_on"):
        problem["started_on"] = date.today().isoformat()

    PROGRESS_FILE.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "update_progress.py")], check=True)


if __name__ == "__main__":
    main()
