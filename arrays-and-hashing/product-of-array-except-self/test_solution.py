"""Tests for Product of Array Except Self."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "product_of_array_except_self_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_standard_case() -> None:
    solution = solution_module.Solution()

    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_contains_one_zero() -> None:
    solution = solution_module.Solution()

    assert solution.productExceptSelf([1, 2, 0, 4]) == [0, 0, 8, 0]


def test_contains_two_zeroes() -> None:
    solution = solution_module.Solution()

    assert solution.productExceptSelf([0, 2, 0, 4]) == [0, 0, 0, 0]


def test_negative_numbers() -> None:
    solution = solution_module.Solution()

    assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_two_numbers() -> None:
    solution = solution_module.Solution()

    assert solution.productExceptSelf([5, 10]) == [10, 5]
