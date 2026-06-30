"""Tests for Best Time to Buy and Sell Stock."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "best_time_to_buy_and_sell_stock_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_standard_case() -> None:
    solution = solution_module.Solution()

    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_prices_only_decrease() -> None:
    solution = solution_module.Solution()

    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0


def test_prices_only_increase() -> None:
    solution = solution_module.Solution()

    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4


def test_repeated_prices() -> None:
    solution = solution_module.Solution()

    assert solution.maxProfit([3, 3, 3, 3]) == 0


def test_best_sell_at_end() -> None:
    solution = solution_module.Solution()

    assert solution.maxProfit([2, 1, 2, 0, 10]) == 10


def test_two_prices() -> None:
    solution = solution_module.Solution()

    assert solution.maxProfit([2, 4]) == 2
