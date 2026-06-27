"""Tests for Top K Frequent Elements."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "top_k_frequent_elements_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_standard_case() -> None:
    solution = solution_module.Solution()

    result = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)

    assert set(result) == {1, 2}


def test_single_value() -> None:
    solution = solution_module.Solution()

    assert solution.topKFrequent([1], 1) == [1]


def test_negative_numbers() -> None:
    solution = solution_module.Solution()

    result = solution.topKFrequent([-1, -1, -2, -2, -2, 3], 2)

    assert set(result) == {-1, -2}


def test_k_equals_unique_values() -> None:
    solution = solution_module.Solution()

    result = solution.topKFrequent([4, 4, 5, 6], 3)

    assert set(result) == {4, 5, 6}


def test_clear_top_one() -> None:
    solution = solution_module.Solution()

    assert solution.topKFrequent([7, 7, 7, 8, 8, 9], 1) == [7]
