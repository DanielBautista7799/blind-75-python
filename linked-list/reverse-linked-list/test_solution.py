"""Tests for Reverse Linked List."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location("reverse_linked_list_solution", MODULE_PATH)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)


def build_linked_list(values: list[int]):
    dummy = solution_module.ListNode()
    current = dummy

    for value in values:
        current.next = solution_module.ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head) -> list[int]:
    values = []

    while head is not None:
        values.append(head.val)
        head = head.next

    return values


def test_standard_case() -> None:
    head = build_linked_list([0, 1, 2, 3])
    result = solution_module.Solution().reverseList(head)
    assert linked_list_to_list(result) == [3, 2, 1, 0]


def test_empty_list() -> None:
    assert solution_module.Solution().reverseList(None) is None


def test_single_node() -> None:
    head = build_linked_list([5])
    result = solution_module.Solution().reverseList(head)
    assert linked_list_to_list(result) == [5]


def test_two_nodes() -> None:
    head = build_linked_list([1, 2])
    result = solution_module.Solution().reverseList(head)
    assert linked_list_to_list(result) == [2, 1]


def test_old_head_becomes_tail() -> None:
    head = build_linked_list([1, 2, 3])
    old_head = head
    solution_module.Solution().reverseList(head)
    assert old_head.next is None
