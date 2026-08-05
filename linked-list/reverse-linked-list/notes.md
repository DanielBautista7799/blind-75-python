# Reverse Linked List — Notes

## First Thoughts

My first thought was to go through the linked list one node at a time and make every node point backwards instead of forwards.

The main issue was that once I changed `current.next`, I would lose the rest of the linked list unless I saved the next node first.

## Independent Attempt

- **Attempt time:** 25 minutes

## Brute-Force Approach

A brute-force approach could save every node inside an array and then reconnect them in reverse order.

That would work, but it would use extra space when the list can be reversed directly by changing the pointers.

## Optimized Approach

I used `current`, `prev`, and `next_node`.

`next_node` saves the next node before I change `current.next`. Then I point the current node backwards, move `prev` forward, and move `current` to the saved next node.

Once `current` becomes `None`, `prev` is the new head.

- **Data structure / pattern:** Linked list pointers
- **Time complexity:** O(n)
- **Space complexity:** O(1)

## Mistakes and Debugging

- I had to save `current.next` before changing it or I would lose the rest of the list.
- I originally mixed up when `prev` and `current` should move.
- The order of the pointer changes matters a lot.

## What I Learned

- Save anything you still need before overwriting a pointer.
- A linked list can be reversed in place.
- `prev` becomes the new head at the end.
