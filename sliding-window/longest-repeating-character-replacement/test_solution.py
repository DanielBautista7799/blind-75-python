"""Tests for Longest Repeating Character Replacement."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "longest_repeating_character_replacement_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_standard_case() -> None:
    solution = solution_module.Solution()

    assert solution.characterReplacement("ABAB", 2) == 4


def test_replacement_needed() -> None:
    solution = solution_module.Solution()

    assert solution.characterReplacement("AABABBA", 1) == 4


def test_k_zero() -> None:
    solution = solution_module.Solution()

    assert solution.characterReplacement("AABBB", 0) == 3


def test_all_same_character() -> None:
    solution = solution_module.Solution()

    assert solution.characterReplacement("AAAA", 2) == 4


def test_single_character() -> None:
    solution = solution_module.Solution()

    assert solution.characterReplacement("A", 0) == 1


def test_best_window_near_end() -> None:
    solution = solution_module.Solution()

    assert solution.characterReplacement("BAAAB", 1) == 4
