# Reorder Linked List — Notes

## First Thoughts

My first thought was that I needed access to both the front and back of the linked list, but since a singly linked list only moves forward I could not just grab the last node and move backwards. The main thing I had to figure out was how to turn the second half around so I could merge from both sides.

## Independent Attempt

- **Attempt time:** 40 minutes

## Brute-Force Approach

A brute force way would be putting all the nodes into an array first. Then I could use one pointer at the beginning and one at the end of the array and rebuild the links in the right order. That would work but it would use O(n) extra space.

## Optimized Approach

I first use `slow` and `fast` to get to the middle of the linked list. Then I start at `slow` and reverse the second half using `current`, `prev`, and `next_node`.

After that `first` starts at the original head and `second` starts at `prev`, which is now the beginning of the reversed second half. I alternate the pointers by connecting `first` to `second`, then `second` back to the next node from the first half. The loop stops once the two sides meet so I do not reconnect nodes that are already in their final position.

- **Data structure / pattern:** Fast and slow pointers, linked list reversal, two-pointer merge
- **Time complexity:** O(n)
- **Space complexity:** O(1)

## Mistakes and Debugging

- The part I had to think through the most was when the merge should stop. I was checking whether `first` and `second` had met or were directly beside each other.
- I had to save `first.next` and `second.next` before changing either pointer or I would lose the rest of the list.
- This problem is in place, so there is nothing to return after the pointers are changed.

## What I Learned

- Reversing the second half turns this into a much easier two-pointer merge.
- Saving the next pointers before rewiring a linked list is important because otherwise the rest of the list can get lost.
