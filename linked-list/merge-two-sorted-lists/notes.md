# Merge Two Sorted Lists — Notes

## First Thoughts

My first thought was to make a new linked list and compare the current node from both lists. Whichever one was smaller would get added next and then I would move that list forward.

## Independent Attempt

- **Attempt time:** 30 minutes

## Brute-Force Approach

A brute force way would probably be putting every value from both linked lists into an array, sorting it, and then making a new linked list from that.

That would work but it would be doing extra work since both lists are already sorted.

## Optimized Approach

I made a dummy node first so I did not have to worry about setting the head separately.

I kept one pointer for each linked list and compared their current values. Whichever value was smaller got connected to the new list and then that pointer moved forward.

Once one of the linked lists ran out, I could just connect the rest of the other list since everything left in it was already sorted.

At the end I return `head.next` because `head` itself is just the dummy node I used to make building the list easier.

- **Data structure / pattern:** Linked List
- **Time complexity:** O(n + m)
- **Space complexity:** O(1)

## Mistakes and Debugging

- The main thing I had to figure out was how to keep the beginning of the new linked list while still moving through it.
- Using a dummy node made this way easier.
- I also had to remember that once one list finishes I can just attach the rest of the other list instead of continuing comparisons.

## What I Learned

- Dummy nodes make linked list problems a lot easier to manage.
- Since both lists are already sorted I only need to move through them once.
- I can reuse the original nodes instead of creating a completely new node for every value.
