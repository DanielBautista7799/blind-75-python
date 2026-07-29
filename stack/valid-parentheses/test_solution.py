import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location("valid_parentheses_solution", MODULE_PATH)
solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)

def test_simple():
    assert solution_module.Solution().isValid("()")

def test_nested():
    assert solution_module.Solution().isValid("({[]})")

def test_wrong():
    assert solution_module.Solution().isValid("(]") is False

def test_extra_open():
    assert solution_module.Solution().isValid("(()") is False

def test_extra_close():
    assert solution_module.Solution().isValid("())") is False

def test_empty():
    assert solution_module.Solution().isValid("")
