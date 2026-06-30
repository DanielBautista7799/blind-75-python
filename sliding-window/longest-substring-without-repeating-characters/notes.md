# Longest Substring Without Repeating Characters — Notes

## First Thoughts

I knew I needed to track which characters were currently inside the substring. A set made sense because I only needed to know whether a character was already in the current window.

## Independent Attempt

- **Attempt time:** 20 minutes

## Brute-Force Approach

A brute-force approach would check every possible substring and then test whether each substring has duplicate characters.

This would be too slow because it repeats a lot of work.

## Optimized Approach

The optimized approach uses a sliding window with a set.

The right side of the window moves through the string one character at a time. If the character is not already in the set, I add it and update the longest length. If the character is already in the set, I move the left side of the window forward and remove characters until the duplicate is gone.

- **Data structure / pattern:**
Sliding window and hashset

- **Time complexity:**
O(n)

- **Space complexity:**
O(n)

## Mistakes and Debugging

- I had to understand that the set only represents the current window, not the entire string.
- When a duplicate appears, I need to remove from the left until that duplicate is gone.
- The left pointer tracks where the current valid substring begins.

## What I Learned

- Sliding window is useful when the problem asks for the longest continuous section.
- A set can track whether a character already exists in the current window.
- Moving the left pointer only when needed avoids checking every substring.
