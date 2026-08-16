class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: ListNode | None, n: int
    ) -> ListNode | None:
        raise NotImplementedError
