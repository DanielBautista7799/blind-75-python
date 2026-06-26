"""Tests for Contains Duplicate."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "contains_duplicate_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_detects_duplicate() -> None:
    solution = solution_module.Solution()

    assert solution.hasDuplicate([1, 2, 3, 1]) is True


def test_all_values_are_unique() -> None:
    solution = solution_module.Solution()

    assert solution.hasDuplicate([1, 2, 3, 4]) is False


def test_empty_list() -> None:
    solution = solution_module.Solution()

    assert solution.hasDuplicate([]) is False


def test_single_value() -> None:
    solution = solution_module.Solution()

    assert solution.hasDuplicate([1]) is False


def test_repeated_zero() -> None:
    solution = solution_module.Solution()

    assert solution.hasDuplicate([0, 0]) is True


def test_negative_duplicate() -> None:
    solution = solution_module.Solution()

    assert solution.hasDuplicate([-1, -2, -1]) is True