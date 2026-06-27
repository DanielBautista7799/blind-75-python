"""Tests for Two Sum."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location("two_sum_solution", MODULE_PATH)
solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)

def test_example_one():
    assert solution_module.Solution().twoSum([2,7,11,15],9)==[0,1]

def test_example_two():
    assert solution_module.Solution().twoSum([3,2,4],6)==[1,2]

def test_duplicates():
    assert solution_module.Solution().twoSum([3,3],6)==[0,1]
