"""Tests for Valid Palindrome."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "valid_palindrome_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def test_standard_palindrome_phrase() -> None:
    solution = solution_module.Solution()

    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True


def test_not_palindrome() -> None:
    solution = solution_module.Solution()

    assert solution.isPalindrome("race a car") is False


def test_empty_string() -> None:
    solution = solution_module.Solution()

    assert solution.isPalindrome("") is True


def test_only_punctuation() -> None:
    solution = solution_module.Solution()

    assert solution.isPalindrome(".,:;!") is True


def test_numbers_and_letters_palindrome() -> None:
    solution = solution_module.Solution()

    assert solution.isPalindrome("0P0") is True


def test_case_insensitive() -> None:
    solution = solution_module.Solution()

    assert solution.isPalindrome("RaceCar") is True
