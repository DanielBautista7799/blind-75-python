"""Tests for 3Sum."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "three_sum_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def normalize(triplets: list[list[int]]) -> list[list[int]]:
    return sorted(sorted(triplet) for triplet in triplets)


def test_standard_case() -> None:
    solution = solution_module.Solution()

    result = solution.threeSum([-1, 0, 1, 2, -1, -4])

    assert normalize(result) == normalize([[-1, -1, 2], [-1, 0, 1]])


def test_no_valid_triplets() -> None:
    solution = solution_module.Solution()

    assert solution.threeSum([1, 2, 3, 4]) == []


def test_all_zeroes() -> None:
    solution = solution_module.Solution()

    assert solution.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]


def test_less_than_three_numbers() -> None:
    solution = solution_module.Solution()

    assert solution.threeSum([0, 1]) == []


def test_duplicate_heavy_case() -> None:
    solution = solution_module.Solution()

    result = solution.threeSum([-2, 0, 0, 0, 2, 2])

    assert normalize(result) == normalize([[-2, 0, 2]])


def test_multiple_triplets() -> None:
    solution = solution_module.Solution()

    result = solution.threeSum([-2, -1, 0, 1, 2, 3])

    assert normalize(result) == normalize([[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])
