"""Solution for LeetCode 238: Product of Array Except Self."""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left = 1
        for index in range(len(nums)):
            output[index] = left
            left = nums[index] * left

        right = 1
        for index in range(len(nums) - 1, -1, -1):
            output[index] = output[index] * right
            right = right * nums[index]

        return output
