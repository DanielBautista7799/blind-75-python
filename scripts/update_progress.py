"""Generate README progress metrics and the full PROGRESS.md table."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRESS_FILE = ROOT / "progress.json"
README_FILE = ROOT / "README.md"
DETAIL_FILE = ROOT / "PROGRESS.md"

STATUS_LABELS = {
    "not_started": "Not started",
    "in_progress": "In progress",
    "completed": "Completed",
    "review": "Review",
}


def format_minutes(minutes: int) -> str:
    if minutes < 60:
        return f"{minutes} min"
    hours, remainder = divmod(minutes, 60)
    if remainder == 0:
        return f"{hours}h"
    return f"{hours}h {remainder}m"


def load_data() -> dict:
    return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))


def problem_display(problem: dict) -> str:
    folder = problem.get("folder")
    title = problem["title"]
    if folder:
        return f"[{title}]({folder}/)"
    return title


def build_progress_document(data: dict) -> str:
    problems = data["problems"]
    completed = sum(problem["status"] == "completed" for problem in problems)
    total_minutes = sum(int(problem.get("time_minutes", 0)) for problem in problems)

    lines = [
        "# Blind 75 Progress",
        "",
        f"- **Started:** {data['started_on']}",
        f"- **Completed:** {completed} / {len(problems)}",
        f"- **Total focused time:** {format_minutes(total_minutes)}",
        "",
        (
            "Time includes independent attempts, study, implementation, testing, "
            "documentation, and review."
        ),
        "",
    ]

    categories: list[str] = []
    for problem in problems:
        if problem["category"] not in categories:
            categories.append(problem["category"])

    for category in categories:
        category_problems = [p for p in problems if p["category"] == category]
        category_completed = sum(p["status"] == "completed" for p in category_problems)
        lines.extend([
            f"## {category} — {category_completed}/{len(category_problems)}",
            "",
            "| Problem | Status | Focused time | Started | Completed |",
            "|---|---|---:|---|---|",
        ])
        for problem in category_problems:
            lines.append(
                "| "
                + " | ".join([
                    problem_display(problem),
                    STATUS_LABELS[problem["status"]],
                    format_minutes(int(problem.get("time_minutes", 0))),
                    problem.get("started_on") or "—",
                    problem.get("completed_on") or "—",
                ])
                + " |"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def update_readme(data: dict) -> None:
    problems = data["problems"]
    completed = sum(problem["status"] == "completed" for problem in problems)
    in_progress = sum(problem["status"] == "in_progress" for problem in problems)
    total_minutes = sum(int(problem.get("time_minutes", 0)) for problem in problems)
    completion = (completed / len(problems)) * 100

    block = "\n".join([
        "<!-- PROGRESS_START -->",
        "| Metric | Current value |",
        "|---|---:|",
        f"| Completed | {completed} / {len(problems)} |",
        f"| In progress | {in_progress} |",
        f"| Total focused time | {format_minutes(total_minutes)} |",
        f"| Completion | {completion:.1f}% |",
        "<!-- PROGRESS_END -->",
    ])

    readme = README_FILE.read_text(encoding="utf-8")
    start_marker = "<!-- PROGRESS_START -->"
    end_marker = "<!-- PROGRESS_END -->"
    start = readme.index(start_marker)
    end = readme.index(end_marker) + len(end_marker)
    README_FILE.write_text(readme[:start] + block + readme[end:], encoding="utf-8")


def main() -> None:
    data = load_data()
    DETAIL_FILE.write_text(build_progress_document(data), encoding="utf-8")
    update_readme(data)
    print("Updated README.md and PROGRESS.md.")


if __name__ == "__main__":
    main()
