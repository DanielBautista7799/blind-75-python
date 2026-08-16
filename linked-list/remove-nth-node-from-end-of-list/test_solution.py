import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("solution.py")
SPEC = importlib.util.spec_from_file_location("solution_module", MODULE_PATH)

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

    while head is not None:
        values.append(head.val)
        head = head.next

    return values


def test_remove_second_from_end():
    result = Solution().removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)
    assert to_list(result) == [1, 2, 3, 5]


def test_remove_head():
    result = Solution().removeNthFromEnd(build([1, 2]), 2)
    assert to_list(result) == [2]


def test_remove_last_node():
    result = Solution().removeNthFromEnd(build([1, 2, 3]), 1)
    assert to_list(result) == [1, 2]


def test_single_node():
    result = Solution().removeNthFromEnd(build([1]), 1)
    assert result is None


def test_remove_middle():
    result = Solution().removeNthFromEnd(build([1, 2, 3, 4, 5]), 3)
    assert to_list(result) == [1, 2, 4, 5]
