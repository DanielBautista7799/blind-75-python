# Blind 75 — Python Solutions

A recruiter-facing record of my progress through the **Blind 75** interview problem set.

This repository is not only a collection of accepted answers. Each completed problem documents
how I approached it, the tradeoffs I considered, the final Python solution, its time and space
complexity, the mistakes I made, and the amount of focused time I spent learning it.

> **Status:** Active learning project  
> **Language:** Python 3.11+  
> **Started:** June 25, 2026  
> **Problem set:** [NeetCode Blind 75](https://neetcode.io/practice/practice/blind75)

## Progress

<!-- PROGRESS_START -->
| Metric | Current value |
|---|---:|
| Completed | 0 / 75 |
| In progress | 0 |
| Total focused time | 0 min |
| Completion | 0.0% |
<!-- PROGRESS_END -->

Detailed tracking is available in [PROGRESS.md](PROGRESS.md).

## What This Repository Demonstrates

- Pattern recognition across common interview problem families.
- Clean and readable Python with type hints.
- The ability to compare brute-force and optimized approaches.
- Accurate time and space complexity analysis.
- Testing against normal cases, edge cases, and failure cases.
- Written technical communication instead of code-only submissions.
- Consistent reflection on mistakes, tradeoffs, and reusable lessons.

## Topics Covered

| Topic | Problems |
|---|---:|
| Arrays & Hashing | 8 |
| Two Pointers | 3 |
| Sliding Window | 4 |
| Stack | 1 |
| Binary Search | 2 |
| Linked List | 6 |
| Trees | 11 |
| Heap / Priority Queue | 1 |
| Backtracking | 2 |
| Tries | 3 |
| Graphs | 6 |
| Advanced Graphs | 1 |
| 1-D Dynamic Programming | 10 |
| 2-D Dynamic Programming | 2 |
| Greedy | 2 |
| Intervals | 5 |
| Math & Geometry | 3 |
| Bit Manipulation | 5 |
| **Total** | **75** |

## Repository Structure

```text
blind-75-python/
├── README.md
├── PROGRESS.md
├── LEARNING_LOG.md
├── progress.json
├── arrays-and-hashing/
│   ├── README.md
│   └── contains-duplicate/
│       ├── description.md
│       ├── notes.md
│       ├── solution.py
│       └── test_solution.py
├── two-pointers/
├── sliding-window/
├── ...
├── templates/
│   ├── description.md
│   ├── notes.md
│   ├── solution.py
│   └── test_solution.py
├── scripts/
│   ├── start_problem.py
│   ├── track_problem.py
│   └── update_progress.py
└── .github/workflows/python-tests.yml
```

Every problem folder uses the same format:

| File | Purpose |
|---|---|
| `description.md` | Original summary, links, examples, constraints, and completion checklist |
| `notes.md` | First thoughts, brute force, optimized reasoning, mistakes, and lessons |
| `solution.py` | Final clean Python solution |
| `test_solution.py` | Focused tests for normal and edge cases |

Problem statements are summarized in my own words. Full copyrighted statements are not copied
into this repository; each folder links back to the original problem.

## My Process for Every Problem

1. Read the problem and restate it in my own words.
2. Attempt it without looking at a solution.
3. Record the first approach, including why it may be inefficient.
4. Identify the core data structure or algorithmic pattern.
5. Implement and test the optimized solution.
6. Write the time and space complexity.
7. Record mistakes and the general lesson that transfers to future problems.
8. Revisit the problem later without notes to verify retention.

## Time Tracking

Focused time includes:

- Independent attempt time.
- Studying hints or explanations.
- Implementing and debugging.
- Writing tests and documentation.
- Reviewing the problem later.

The root progress summary is generated from `progress.json`.

Start a problem:

```bash
python scripts/start_problem.py valid-anagram
```

Add time and update its status:

```bash
python scripts/track_problem.py valid-anagram --status in_progress --add-minutes 35
```

Mark it complete:

```bash
python scripts/track_problem.py valid-anagram --status completed --add-minutes 20
```

Regenerate the progress files:

```bash
python scripts/update_progress.py
```

## Running the Project

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install development tools:

```bash
python -m pip install -r requirements-dev.txt
```

Run all tests:

```bash
pytest
```

Run code-quality checks:

```bash
ruff check .
```

## Completion Standard

A problem counts as complete only when:

- The final implementation works.
- The solution is written cleanly in Python.
- Tests cover important edge cases.
- Time and space complexity are documented.
- The reasoning is explained in my own words.
- The time spent is recorded.
- At least one reusable lesson is documented.

## Learning Goals

By the end of the project, I expect to be able to:

- Recognize common patterns before writing code.
- Explain why an approach works, not only reproduce it.
- Choose appropriate data structures based on constraints.
- Analyze algorithmic complexity accurately.
- Write interview-ready Python under time pressure.
- Communicate technical decisions clearly to engineers and recruiters.

## Attribution

The study list is based on the
[NeetCode Blind 75](https://neetcode.io/practice/practice/blind75), and individual problem folders
link to their original practice pages. All explanations, notes, tests, and implementations in this
repository are my own unless explicitly attributed.

## License

Code in this repository is available under the [MIT License](LICENSE).
