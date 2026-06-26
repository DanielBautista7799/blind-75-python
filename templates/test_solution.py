"""Tests for {{TITLE}}."""

import importlib.util
from pathlib import Path

import pytest

pytestmark = pytest.mark.skip(reason="Remove this marker after implementing the solution.")

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location("problem_solution", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution)


def test_solution_placeholder() -> None:
    """Replace this test with problem-specific cases."""
    assert callable(solution.solve)
