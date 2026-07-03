# Minimum Window Substring

## Problem Information

- **Category:** Sliding Window
- **Difficulty:** Hard
- **Status:** Completed
- **Original problem:** [LeetCode 76](https://leetcode.com/problems/minimum-window-substring/)
- **NeetCode reference:** [Minimum Window Substring](https://neetcode.io/problems/minimum-window-with-characters)
- **Started:** 7/2
- **Completed:** 7/2

## Problem Summary

Given two strings `s` and `t`, find the smallest substring in `s` that contains every character from `t`, including repeated characters.

If no valid substring exists, return an empty string.

## Inputs and Expected Output

- Input: a source string `s` and a target string `t`.
- Output: the smallest substring of `s` that contains all characters from `t`.

## Edge Cases to Consider

- No valid window exists.
- `t` is longer than `s`.
- `s` and `t` are the same.
- Repeated characters in `t`.
- The best window appears near the end.
- Single-character strings.
