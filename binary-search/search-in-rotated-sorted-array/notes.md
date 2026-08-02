# Search in Rotated Sorted Array — Notes

## First Thoughts

My first thought was to use binary search since the original array was sorted, but the rotation made it harder to know which side to search.

The main thing I had to figure out was how to tell which half was still sorted after finding the middle index.

## Independent Attempt

- **Attempt time:** 30 minutes

## Brute-Force Approach

The brute-force approach would just loop through the entire array until the target was found.

That would work, but it would take O(n) and ignore the fact that part of the array is still sorted.

## Optimized Approach

The optimized approach uses binary search.

After finding `mid`, I first check if the target is already at that index.

Then I check whether the left side is sorted by comparing `nums[i]` to `nums[mid]`. If the left side is sorted, I check whether the target falls inside that range. If it does, I move the right pointer left. Otherwise, I search the other side.

If the left side is not sorted, then the right side has to be sorted. I do the same range check on that side and remove the half that cannot contain the target.

- **Data structure / pattern:** Binary search
- **Time complexity:** O(log n)
- **Space complexity:** O(1)

## Mistakes and Debugging

- I first tried treating the array like a normal sorted array, which failed after the rotation point.
- I had to understand that one side of the array will always still be sorted.
- I also had to use `mid - 1` and `mid + 1` so the search area actually gets smaller.

## What I Learned

- Binary search can still work on a rotated array because at least one half is always sorted.
- Once I know which half is sorted, I can check if the target falls inside its range.
- The important part is deciding which half can safely be removed.
