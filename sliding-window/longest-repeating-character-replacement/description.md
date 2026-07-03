# Longest Repeating Character Replacement

## Problem Information

- **Category:** Sliding Window
- **Difficulty:** Medium
- **Status:** Completed
- **Original problem:** [LeetCode 424](https://leetcode.com/problems/longest-repeating-character-replacement/)
- **NeetCode reference:** [Longest Repeating Character Replacement](https://neetcode.io/problems/longest-repeating-substring-with-replacement)
- **Started:** 7/2
- **Completed:** 7/2

## Problem Summary

Given a string and an integer `k`, find the length of the longest substring that can be turned into the same repeating character by replacing at most `k` characters.

## Inputs and Expected Output

- Input: a string `s` and an integer `k`.
- Output: the length of the longest valid substring.

## Edge Cases to Consider

- `k` is zero.
- The whole string is already the same character.
- The whole string can be changed into one character.
- Multiple characters have similar frequencies.
- The best window appears near the end.
- Single-character string.
