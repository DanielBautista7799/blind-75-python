# Longest Consecutive Sequence — Notes

## First Thoughts

I needed a way to check whether numbers existed quickly without sorting the array. A set made sense because it lets me check if a number exists fast.

## Independent Attempt

- **Attempt time:** 35 minutes

## Brute-Force Approach

A brute-force approach would check each number and keep searching for the next consecutive number by scanning the whole list again.

That would be slow because the same searches would be repeated many times.

## Optimized Approach

I converted the list into a set. Then for each number, I only started counting if it was the beginning of a sequence.

A number is the start of a sequence when the number before it is not in the set. From that starting point, I count upward until the sequence ends.

- **Data structure / pattern:**
Hashset

- **Time complexity:**
O(n)

- **Space complexity:**
O(n)

## Mistakes and Debugging

- I had to understand why checking `item - 1 not in numset` prevents recounting the same sequence.
- I needed to count only from the start of a sequence instead of from every number.
- Using a set removes duplicate values and makes lookup fast.

## What I Learned

- A hashset is useful when I only care whether a value exists.
- Finding the start of a sequence avoids repeated work.
- An unsorted array can still be solved efficiently without sorting.
