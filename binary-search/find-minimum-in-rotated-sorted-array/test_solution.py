"""Tests for Find Minimum in Rotated Sorted Array."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "find_minimum_in_rotated_sorted_array_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_standard_rotation() -> None:
    assert solution_module.Solution().findMin([3, 4, 5, 1, 2]) == 1


def test_larger_rotation() -> None:
    assert solution_module.Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0


def test_not_rotated() -> None:
    assert solution_module.Solution().findMin([1, 2, 3, 4, 5]) == 1


def test_single_value() -> None:
    assert solution_module.Solution().findMin([7]) == 7


def test_two_values_rotated() -> None:
    assert solution_module.Solution().findMin([2, 1]) == 1


def test_minimum_at_end() -> None:
    assert solution_module.Solution().findMin([2, 3, 4, 5, 1]) == 1
