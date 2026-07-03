# Longest Repeating Character Replacement — Notes

## First Thoughts

I knew this was a sliding window problem because I needed the longest continuous substring. The hard part was figuring out when a window was valid.

## Independent Attempt

- **Attempt time:** 60 minutes

## Brute-Force Approach

A brute-force approach would check every possible substring and count how many replacements are needed for each one.

That would be too slow because it would keep recounting characters for many overlapping substrings.

## Optimized Approach

The optimized approach uses a sliding window and a hashmap for character counts.

For each window, the most frequent character is the one I would keep. Every other character in the window would need to be replaced.

The number of replacements needed is the window length minus the count of the most frequent character. If that number is greater than `k`, the window is too expensive, so I move the left pointer forward until the window becomes valid again.

- **Data structure / pattern:**
Sliding window and hashmap

- **Time complexity:**
O(n)

- **Space complexity:**
O(1), because the alphabet size is limited

## Mistakes and Debugging

- I had to understand that I do not need to replace characters directly.
- The key formula is window length minus max frequency.
- I learned that the most frequent character count tells me how many characters can stay unchanged.

## What I Learned

- Sliding window problems often depend on knowing when the current window becomes invalid.
- For this problem, replacements needed equals the current window size minus the most frequent character count.
- A hashmap can track the character counts inside the current window.
