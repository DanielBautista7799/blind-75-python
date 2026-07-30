"""Solution for LeetCode 153: Find Minimum in Rotated Sorted Array."""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            mid = (i + j) // 2

            if nums[mid] < nums[j]:
                j = mid
            elif nums[mid] > nums[j]:
                i = mid + 1

        return nums[i]
