"""Tests for Contains Duplicate."""

import importlib.util
from pathlib import Path

import pytest

pytestmark = pytest.mark.skip(reason="Enable after implementing Contains Duplicate.")

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location("contains_duplicate_solution", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution)


def test_detects_duplicate() -> None:
    assert solution.contains_duplicate([1, 2, 3, 1]) is True


def test_all_values_unique() -> None:
    assert solution.contains_duplicate([1, 2, 3, 4]) is False


def test_empty_input() -> None:
    assert solution.contains_duplicate([]) is False


def test_repeated_zero() -> None:
    assert solution.contains_duplicate([0, 0]) is True
