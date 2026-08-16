# Remove Nth Node From End of List — Notes

## First Thoughts

My first thought was to use two pointers so I would not have to count the whole linked list first. I moved `end` ahead by `n` nodes and then moved `end` and `point` together so that `point` would end up on the node that needs to be removed.

## Independent Attempt

- **Attempt time:** 15 minutes

## Brute-Force Approach

A brute force way would be going through the linked list once to get its length, then figuring out which position from the front needs to be removed and going through the list again. That would work but it needs two passes through the list.

## Optimized Approach

I start `end` and `point` at `head`, then move `end` forward `n` times. If `end` is already `None`, that means the node I need to remove is the head, so I can return `head.next`.

Otherwise I move `end` and `point` forward together. I keep `prev` one node behind `point`, and I save `point.next` in `next_node`. Once `end` reaches `None`, `point` is on the node that needs to be removed and `prev` is right before it. I then connect `prev.next` to `next_node`.

- **Data structure / pattern:** Two pointers
- **Time complexity:** O(n)
- **Space complexity:** O(1)

## Mistakes and Debugging

- The main special case was when the node being removed is the head. In that case `end` becomes `None` after moving it forward `n` times.
- I had to keep `prev` so I could reconnect the list after finding the node to remove.

## What I Learned

- Keeping one pointer `n` nodes ahead makes it possible to find the nth node from the end in one pass.
- Linked list removal usually comes down to keeping track of the node before the one being deleted.
