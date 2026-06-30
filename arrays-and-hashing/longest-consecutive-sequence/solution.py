"""Solution for LeetCode 128: Longest Consecutive Sequence."""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for item in numset:
            if item - 1 not in numset:
                count = 1

                while item + count in numset:
                    count += 1

                longest = max(longest, count)

        return longest
