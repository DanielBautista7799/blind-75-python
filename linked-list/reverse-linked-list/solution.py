"""Solution for LeetCode 206: Reverse Linked List."""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        current = head
        prev = None

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
