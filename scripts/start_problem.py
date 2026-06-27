"""Create a clean Blind 75 problem folder from progress.json."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRESS_FILE = ROOT / "progress.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Start a Blind 75 problem.")
    parser.add_argument("slug", help="Problem slug, such as two-sum")
    return parser.parse_args()


def make_description(problem: dict) -> str:
    today = date.today().strftime("%-m/%-d")

    return f"""# {problem["title"]}

## Problem Information

- **Category:** {problem["category"]}
- **Difficulty:** Add difficulty
- **Status:** In Progress
- **Original problem:** Add LeetCode link
- **NeetCode reference:** Add NeetCode link
- **Started:** {today}
- **Completed:** Not completed

## Problem Summary

Write a short summary in your own words.

## Inputs and Expected Output

- Input:
- Output:

## Edge Cases to Consider

-
"""


def make_notes(problem: dict) -> str:
    return f"""# {problem["title"]} — Notes

## First Thoughts

Write your initial idea before looking at hints.

## Independent Attempt

- **Attempt time:** 0 minutes

## Brute-Force Approach

Describe the brute-force solution.

## Optimized Approach

Explain why the optimized approach works.

- **Data structure / pattern:**
- **Time complexity:**
- **Space complexity:**

## Mistakes and Debugging

-

## What I Learned

-
"""


def make_solution(problem: dict) -> str:
    class_name = "Solution"
    method_name = "solve"

    return f'''"""Solution for {problem["title"]}."""


class {class_name}:
    def {method_name}(self):
        raise NotImplementedError("Complete your {problem["title"]} solution.")
'''


def make_tests(problem: dict) -> str:
    module_name = problem["slug"].replace("-", "_") + "_solution"

    return f'''"""Tests for {problem["title"]}."""

import importlib.util
from pathlib import Path

import pytest

pytestmark = pytest.mark.skip(reason="Enable after implementing {problem["title"]}.")

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "{module_name}",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {{MODULE_PATH}}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_placeholder() -> None:
    solution = solution_module.Solution()

    assert solution is not None
'''


def main() -> None:
    args = parse_args()
    data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))

    problem = next((item for item in data["problems"] if item["slug"] == args.slug), None)

    if problem is None:
        available = ", ".join(item["slug"] for item in data["problems"])
        raise SystemExit(f"Unknown problem slug: {args.slug}\\nAvailable slugs:\\n{available}")

    folder = ROOT / problem["category_slug"] / problem["slug"]
    folder.mkdir(parents=True, exist_ok=True)

    files = {
        "description.md": make_description(problem),
        "notes.md": make_notes(problem),
        "solution.py": make_solution(problem),
        "test_solution.py": make_tests(problem),
    }

    for filename, content in files.items():
        file_path = folder / filename

        if file_path.exists():
            print(f"Skipped existing file: {file_path.relative_to(ROOT)}")
            continue

        file_path.write_text(content, encoding="utf-8")
        print(f"Created: {file_path.relative_to(ROOT)}")

    problem["folder"] = f"{problem['category_slug']}/{problem['slug']}"
    problem["status"] = "in_progress"

    if not problem.get("started_on"):
        problem["started_on"] = date.today().isoformat()

    PROGRESS_FILE.write_text(json.dumps(data, indent=2) + "\\n", encoding="utf-8")

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "update_progress.py")],
        check=True,
    )


if __name__ == "__main__":
    main()