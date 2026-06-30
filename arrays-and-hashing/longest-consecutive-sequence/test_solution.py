"""Tests for Longest Consecutive Sequence."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "longest_consecutive_sequence_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_standard_case() -> None:
    solution = solution_module.Solution()

    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4


def test_sequence_out_of_order() -> None:
    solution = solution_module.Solution()

    assert solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_empty_list() -> None:
    solution = solution_module.Solution()

    assert solution.longestConsecutive([]) == 0


def test_single_number() -> None:
    solution = solution_module.Solution()

    assert solution.longestConsecutive([10]) == 1


def test_duplicates() -> None:
    solution = solution_module.Solution()

    assert solution.longestConsecutive([1, 2, 2, 3]) == 3


def test_negative_numbers() -> None:
    solution = solution_module.Solution()

    assert solution.longestConsecutive([-3, -2, -1, 5, 6]) == 3
