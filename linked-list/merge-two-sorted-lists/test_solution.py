import importlib.util
from pathlib import Path
import pytest

pytestmark = pytest.mark.skip(reason="Enable after implementing Merge Two Sorted Lists.")

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location("merge_two_sorted_lists_solution", MODULE_PATH)

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)

def test_placeholder():
    assert solution_module.Solution() is not None
