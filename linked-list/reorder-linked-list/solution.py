class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        first = head
        second = prev

        while (
            first != second
            and first is not None
            and second is not None
            and first.next != second
        ):
            first_next = first.next
            first.next = second
            second_next = second.next
            second.next = first_next
            first = first_next
            second = second_next
