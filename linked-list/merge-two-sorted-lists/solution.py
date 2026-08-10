"""Solution for LeetCode 21: Merge Two Sorted Lists."""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: ListNode | None,
        list2: ListNode | None,
    ) -> ListNode | None:
        new = ListNode()
        head = new
        currentlist1 = list1
        currentlist2 = list2

        while currentlist1 is not None and currentlist2 is not None:
            if currentlist1.val >= currentlist2.val:
                new.next = currentlist2
                new = new.next
                currentlist2 = currentlist2.next
            else:
                new.next = currentlist1
                new = new.next
                currentlist1 = currentlist1.next

        if currentlist1:
            new.next = currentlist1
        else:
            new.next = currentlist2

        return head.next
