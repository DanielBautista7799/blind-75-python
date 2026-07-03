"""Tests for Minimum Window Substring."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "minimum_window_substring_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_standard_case() -> None:
    solution = solution_module.Solution()

    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"


def test_single_character_match() -> None:
    solution = solution_module.Solution()

    assert solution.minWindow("a", "a") == "a"


def test_single_character_no_match() -> None:
    solution = solution_module.Solution()

    assert solution.minWindow("a", "aa") == ""


def test_repeated_characters_in_t() -> None:
    solution = solution_module.Solution()

    assert solution.minWindow("aaab", "aab") == "aab"


def test_no_valid_window() -> None:
    solution = solution_module.Solution()

    assert solution.minWindow("abc", "z") == ""


def test_best_window_near_end() -> None:
    solution = solution_module.Solution()

    assert solution.minWindow("abdecfab", "cf") == "cf"


def test_same_strings() -> None:
    solution = solution_module.Solution()

    assert solution.minWindow("abc", "abc") == "abc"
