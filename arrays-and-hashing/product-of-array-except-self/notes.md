# Product of Array Except Self — Notes

## First Thoughts

My first idea was to split the array into everything on the left and everything on the right of the current index. Then I combined those two parts and multiplied every value together.

## Independent Attempt

- **Attempt time:** 50 minutes

## Brute-Force Approach

My first solution used slicing. For each index, I made a left array and a right array, combined them, and multiplied everything in that combined array.

This worked logically, but it repeated too much work. For every index, I was rebuilding arrays and multiplying almost the whole list again.

## Optimized Approach

The optimized solution uses a left product and a right product.

First, I move left to right and store the product of everything before the current index. Then I move right to left and multiply each position by the product of everything after the current index.

This avoids division and avoids rebuilding arrays for every index.

- **Data structure / pattern:**
Prefix and postfix product

- **Time complexity:**
O(n)

- **Space complexity:**
O(1) extra space, not counting the output array

## Mistakes and Debugging

- My first solution used slicing, which made extra arrays.
- I had to understand that the output array can store the left products first.
- I learned that the right side does not need its own array because one variable can track the running product.

## What I Learned

- Prefix and postfix passes can replace repeated slicing.
- Sometimes the output array can hold intermediate work.
- A solution can be correct but still too slow if it repeats the same work many times.
