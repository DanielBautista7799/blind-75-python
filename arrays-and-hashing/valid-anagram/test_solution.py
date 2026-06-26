"""Tests for Valid Anagram."""

import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "valid_anagram_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_valid_anagram() -> None:
    solution = solution_module.Solution()

    assert solution.isAnagram("racecar", "carrace") is True


def test_invalid_anagram() -> None:
    solution = solution_module.Solution()

    assert solution.isAnagram("jar", "jam") is False


def test_different_lengths() -> None:
    solution = solution_module.Solution()

    assert solution.isAnagram("cat", "cats") is False


def test_empty_strings() -> None:
    solution = solution_module.Solution()

    assert solution.isAnagram("", "") is True


def test_repeated_character_count_differs() -> None:
    solution = solution_module.Solution()

    assert solution.isAnagram("aacc", "ccac") is False


def test_identical_strings() -> None:
    solution = solution_module.Solution()

    assert solution.isAnagram("python", "python") is True
