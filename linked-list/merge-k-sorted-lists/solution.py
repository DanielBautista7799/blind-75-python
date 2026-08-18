class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(
        self, lists: list[ListNode | None]
    ) -> ListNode | None:
        raise NotImplementedError
