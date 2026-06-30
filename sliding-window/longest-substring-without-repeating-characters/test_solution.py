"""Tests for Longest Substring Without Repeating Characters."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "longest_substring_without_repeating_characters_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_standard_case() -> None:
    solution = solution_module.Solution()

    assert solution.lengthOfLongestSubstring("abcabcbb") == 3


def test_all_same_character() -> None:
    solution = solution_module.Solution()

    assert solution.lengthOfLongestSubstring("bbbbb") == 1


def test_mixed_repeats() -> None:
    solution = solution_module.Solution()

    assert solution.lengthOfLongestSubstring("pwwkew") == 3


def test_empty_string() -> None:
    solution = solution_module.Solution()

    assert solution.lengthOfLongestSubstring("") == 0


def test_single_character() -> None:
    solution = solution_module.Solution()

    assert solution.lengthOfLongestSubstring("a") == 1


def test_space_character() -> None:
    solution = solution_module.Solution()

    assert solution.lengthOfLongestSubstring("a b c a") == 3


def test_no_repeats() -> None:
    solution = solution_module.Solution()

    assert solution.lengthOfLongestSubstring("abcdef") == 6
