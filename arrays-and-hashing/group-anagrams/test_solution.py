"""Tests for Group Anagrams."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "group_anagrams_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def normalize(groups: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(group) for group in groups)


def test_standard_case() -> None:
    solution = solution_module.Solution()

    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

    assert normalize(result) == normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])


def test_empty_input() -> None:
    solution = solution_module.Solution()

    assert solution.groupAnagrams([]) == []


def test_empty_string() -> None:
    solution = solution_module.Solution()

    assert solution.groupAnagrams([""]) == [[""]]


def test_single_character_strings() -> None:
    solution = solution_module.Solution()

    result = solution.groupAnagrams(["a", "b", "a"])

    assert normalize(result) == normalize([["a", "a"], ["b"]])


def test_no_matching_anagrams() -> None:
    solution = solution_module.Solution()

    result = solution.groupAnagrams(["abc", "def", "ghi"])

    assert normalize(result) == normalize([["abc"], ["def"], ["ghi"]])