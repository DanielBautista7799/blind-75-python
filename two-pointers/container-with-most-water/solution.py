"""Solution for LeetCode 11: Container With Most Water."""

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            width = j - i
            maxA = max(min(heights[j], heights[i]) * width, maxA)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return maxA
