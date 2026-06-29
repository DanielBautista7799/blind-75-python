"""Tests for Encode and Decode Strings."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "encode_and_decode_strings_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def round_trip(words: list[str]) -> list[str]:
    solution = solution_module.Solution()
    encoded = solution.encode(words)

    return solution.decode(encoded)


def test_standard_case() -> None:
    assert round_trip(["neet", "code", "love", "you"]) == ["neet", "code", "love", "you"]


def test_empty_list() -> None:
    assert round_trip([]) == []


def test_empty_string_inside_list() -> None:
    assert round_trip(["", "abc", ""]) == ["", "abc", ""]


def test_strings_with_hash_character() -> None:
    assert round_trip(["a#b", "##", "hello"]) == ["a#b", "##", "hello"]


def test_strings_with_numbers() -> None:
    assert round_trip(["123", "4#5", "000"]) == ["123", "4#5", "000"]


def test_strings_with_spaces() -> None:
    assert round_trip(["hello world", "  ", "end"]) == ["hello world", "  ", "end"]


def test_longer_mixed_case() -> None:
    words = ["", "abc", "#", "12#34", "spaces are fine", "final"]

    assert round_trip(words) == words
