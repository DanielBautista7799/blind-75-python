"""Solution for LeetCode 1: Two Sum."""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
            seen = {}
            i = 0
            j = len(nums)
            while i < j:
                needed = target - nums[i]
                if needed in seen:
                    return [seen[needed], i]
                else:
                    seen[nums[i]] = i
                    i +=1