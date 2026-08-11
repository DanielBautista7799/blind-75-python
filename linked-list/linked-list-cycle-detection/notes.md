# Linked List Cycle Detection — Notes

## First Thoughts

My first thought was to use two pointers going through the linked list at different speeds. If there is a cycle the fast pointer should eventually catch up to the slow pointer because it keeps moving two nodes at a time.

## Independent Attempt

- **Attempt time:** 15 minutes

## Brute-Force Approach

A brute force way would be keeping every node I have already visited in a set. Before moving to the next node I could check if that node was already in the set. That would work but it would use extra memory for every node in the list.

## Optimized Approach

I used `slow` and `fast` starting at `head`. `slow` moves one node at a time while `fast` moves two. If there is no cycle then `fast` or `fast.next` eventually becomes `None` and I return `False`. If there is a cycle then the fast pointer eventually catches the slow pointer and `fast == slow`, so I return `True`.

- **Data structure / pattern:** Fast and slow pointers
- **Time complexity:** O(n)
- **Space complexity:** O(1)

## Mistakes and Debugging

- The main thing was making sure I checked both `fast` and `fast.next` before doing `fast.next.next`.
- I also had to compare the pointers themselves instead of comparing the node values.

## What I Learned

- Moving two pointers at different speeds can detect a linked list cycle without using extra memory.
- A cycle guarantees that the fast pointer eventually catches the slow pointer.
