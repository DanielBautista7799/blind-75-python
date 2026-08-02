"""Tests for Search in Rotated Sorted Array."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "search_in_rotated_sorted_array_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_target_in_right_half() -> None:
    assert solution_module.Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_target_not_found() -> None:
    assert solution_module.Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_single_value_found() -> None:
    assert solution_module.Solution().search([1], 1) == 0


def test_single_value_not_found() -> None:
    assert solution_module.Solution().search([1], 0) == -1


def test_target_in_left_half() -> None:
    assert solution_module.Solution().search([6, 7, 1, 2, 3, 4, 5], 7) == 1


def test_not_rotated() -> None:
    assert solution_module.Solution().search([1, 2, 3, 4, 5], 4) == 3


def test_target_at_last_index() -> None:
    assert solution_module.Solution().search([3, 4, 5, 6, 1, 2], 2) == 5
