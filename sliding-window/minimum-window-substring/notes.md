# Minimum Window Substring — Notes

## First Thoughts

I knew this was a sliding window problem, but it was harder because the window needed to contain all characters from `t`, including duplicate counts.

## Independent Attempt

- **Attempt time:** 50 minutes

## Brute-Force Approach

A brute-force approach would check every possible substring of `s` and test whether it contains all the characters from `t`.

This would be too slow because there are many possible substrings, and each one would need character counting.

## Optimized Approach

The optimized approach uses two hashmaps and a sliding window.

First, I count the characters needed from `t`. Then I expand the right side of the window through `s`. When the current window has all required characters, I try to shrink the window from the left while it is still valid.

The `have` variable tracks how many required character counts are currently satisfied. The `need` variable tracks how many unique character requirements must be satisfied.

- **Data structure / pattern:**
Sliding window and hashmap

- **Time complexity:**
O(n)

- **Space complexity:**
O(m), where `m` is the number of unique characters stored in the maps

## Mistakes and Debugging

- I originally put the shrinking loop outside the main loop.
- I had to move `best` and `bestlen` before the main loop so they update while scanning.
- I learned that `left += 1` must happen every time after removing the left character.
- I used `right - left + 1` instead of creating a substring just to measure its length.

## What I Learned

- Minimum window problems expand until valid, then shrink while still valid.
- `have == need` means the current window satisfies all required character counts.
- The window can be valid even if it contains extra characters.
