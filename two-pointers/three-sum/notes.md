# 3Sum — Notes

## First Thoughts

My first idea was to use three indexes and check every possible triple. That made sense logically because the problem asks for three numbers, but it would be too slow.

## Independent Attempt

- **Attempt time:** 60 minutes

## Brute-Force Approach

The brute-force approach would use three loops. The first loop picks the first number, the second loop picks the second number, and the third loop picks the third number. Then it checks whether the sum is zero.

This works logically, but it repeats too much work and becomes too slow for larger inputs.

## Optimized Approach

The optimized approach sorts the array first. Then I fix one number with index `i` and use two pointers for the remaining part of the array.

If the sum is too large, I move the right pointer left. If the sum is too small, I move the left pointer right. If the sum equals zero, I add the triplet and then move both pointers.

Duplicates are handled by skipping repeated `i` values and skipping repeated left and right pointer values after a valid triplet is found.

- **Data structure / pattern:**
Sorting and two pointers

- **Time complexity:**
O(n²)

- **Space complexity:**
O(1) extra space, not counting the output array

## Mistakes and Debugging

- I first thought about using three loops.
- I had to understand that `j` should start at `i + 1` so the same index is not reused.
- I originally used `if j < k`, but it needed to be `while j < k` so the two pointers keep moving.
- I had to use `while` when skipping duplicates because there can be more than one repeated value.

## What I Learned

- Sorting makes the two-pointer strategy possible.
- 3Sum can be reduced to fixing one number and solving a two-pointer search for the other two.
- Duplicate handling is a major part of this problem.
