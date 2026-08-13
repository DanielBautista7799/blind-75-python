import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location("reorder_linked_list_solution", MODULE_PATH)

if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Could not load solution module from {MODULE_PATH}")

solution_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(solution_module)

ListNode = solution_module.ListNode
Solution = solution_module.Solution


def build(values: list[int]) -> ListNode | None:
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def to_list(head: ListNode | None) -> list[int]:
    values = []
    current = head
    seen = set()

    while current is not None:
        node_id = id(current)
        if node_id in seen:
            raise AssertionError("Cycle detected in reordered list")
        seen.add(node_id)
        values.append(current.val)
        current = current.next

    return values


def test_even_length():
    head = build([1, 2, 3, 4])
    Solution().reorderList(head)
    assert to_list(head) == [1, 4, 2, 3]


def test_odd_length():
    head = build([1, 2, 3, 4, 5])
    Solution().reorderList(head)
    assert to_list(head) == [1, 5, 2, 4, 3]


def test_six_nodes():
    head = build([1, 2, 3, 4, 5, 6])
    Solution().reorderList(head)
    assert to_list(head) == [1, 6, 2, 5, 3, 4]


def test_single_node():
    head = build([1])
    Solution().reorderList(head)
    assert to_list(head) == [1]


def test_two_nodes():
    head = build([1, 2])
    Solution().reorderList(head)
    assert to_list(head) == [1, 2]


def test_three_nodes():
    head = build([1, 2, 3])
    Solution().reorderList(head)
    assert to_list(head) == [1, 3, 2]
