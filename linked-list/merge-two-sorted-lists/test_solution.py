"""Tests for Merge Two Sorted Lists."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location(
    "merge_two_sorted_lists_solution",
    MODULE_PATH,
)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def build(values: list[int]):
    dummy = solution_module.ListNode()
    current = dummy
    for value in values:
        current.next = solution_module.ListNode(value)
        current = current.next
    return dummy.next


def to_list(head) -> list[int]:
    output = []
    while head:
        output.append(head.val)
        head = head.next
    return output


def test_standard_case() -> None:
    result = solution_module.Solution().mergeTwoLists(
        build([1, 2, 4]),
        build([1, 3, 4]),
    )
    assert to_list(result) == [1, 1, 2, 3, 4, 4]


def test_first_list_empty() -> None:
    result = solution_module.Solution().mergeTwoLists(None, build([0]))
    assert to_list(result) == [0]


def test_second_list_empty() -> None:
    result = solution_module.Solution().mergeTwoLists(build([1, 2, 3]), None)
    assert to_list(result) == [1, 2, 3]


def test_both_lists_empty() -> None:
    assert solution_module.Solution().mergeTwoLists(None, None) is None


def test_duplicate_values() -> None:
    result = solution_module.Solution().mergeTwoLists(
        build([1, 1, 2]),
        build([1, 3]),
    )
    assert to_list(result) == [1, 1, 1, 2, 3]
