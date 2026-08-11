import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location("linked_list_cycle_solution", MODULE_PATH)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)

ListNode = solution_module.ListNode
Solution = solution_module.Solution


def test_cycle_in_middle():
    nodes = [ListNode(value) for value in [1, 2, 3, 4]]
    for current, nxt in zip(nodes, nodes[1:]):
        current.next = nxt
    nodes[-1].next = nodes[1]

    assert Solution().hasCycle(nodes[0]) is True


def test_no_cycle():
    nodes = [ListNode(value) for value in [1, 2, 3, 4]]
    for current, nxt in zip(nodes, nodes[1:]):
        current.next = nxt

    assert Solution().hasCycle(nodes[0]) is False


def test_empty_list():
    assert Solution().hasCycle(None) is False


def test_single_node_no_cycle():
    head = ListNode(1)

    assert Solution().hasCycle(head) is False


def test_single_node_self_cycle():
    head = ListNode(1)
    head.next = head

    assert Solution().hasCycle(head) is True


def test_cycle_starts_at_head():
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)

    first.next = second
    second.next = third
    third.next = first

    assert Solution().hasCycle(first) is True
