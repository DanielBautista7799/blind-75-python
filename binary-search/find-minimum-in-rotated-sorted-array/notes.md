# Find Minimum in Rotated Sorted Array — Notes

## First Thoughts

My first thought was to use binary search since the array was originally sorted. The difficult part was figuring out which side the minimum had to be on after looking at the middle value.

## Independent Attempt

- **Attempt time:** 14 minutes

## Brute-Force Approach

The brute-force approach would just go through every number and keep track of the smallest one. That would work, but it would ignore the fact that the array is sorted and would take O(n).

## Optimized Approach

This approach uses binary search and compares the middle value to the value at the right pointer.

If `nums[mid]` is smaller than `nums[j]`, then the middle value could be the minimum, or the minimum could be somewhere to its left. Because of that, I move `j` to `mid` instead of `mid - 1`.

If `nums[mid]` is larger than `nums[j]`, then the minimum has to be to the right of `mid`, so I move `i` to `mid + 1`.

Eventually both pointers meet at the minimum value, so I return `nums[i]`.

- **Data structure / pattern:** Binary search
- **Time complexity:** O(log n)
- **Space complexity:** O(1)

## Mistakes and Debugging

- I initially had to figure out whether to compare the middle value against the left or right pointer.
- I also had to remember that when the middle value is smaller than the right value, `mid` could still be the minimum, so I use `j = mid`.
- When the middle value is larger, I can safely skip it by using `i = mid + 1`.

## What I Learned

- Binary search can still be used on an array that is not fully sorted as long as there is still enough order to remove half of the search area.
- Comparing the middle value to the right side tells me which half contains the rotation point.
