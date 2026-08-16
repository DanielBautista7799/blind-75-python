class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: ListNode | None, n: int
    ) -> ListNode | None:
        end = head
        point = head
        prev = None

        for _ in range(n):
            end = end.next

        if end is None:
            return head.next

        while end is not None:
            prev = point
            point = point.next
            next_node = point.next
            end = end.next

        prev.next = next_node
        return head
