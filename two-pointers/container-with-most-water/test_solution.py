"""Tests for Container With Most Water."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "container_with_most_water_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_standard_case() -> None:
    solution = solution_module.Solution()

    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_two_heights() -> None:
    solution = solution_module.Solution()

    assert solution.maxArea([1, 1]) == 1


def test_increasing_heights() -> None:
    solution = solution_module.Solution()

    assert solution.maxArea([1, 2, 3, 4, 5]) == 6


def test_decreasing_heights() -> None:
    solution = solution_module.Solution()

    assert solution.maxArea([5, 4, 3, 2, 1]) == 6


def test_equal_heights() -> None:
    solution = solution_module.Solution()

    assert solution.maxArea([5, 5, 5, 5]) == 15


def test_tallest_lines_not_answer() -> None:
    solution = solution_module.Solution()

    assert solution.maxArea([1, 3, 2, 5, 25, 24, 5]) == 24
