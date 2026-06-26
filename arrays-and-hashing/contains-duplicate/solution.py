"""Solution for LeetCode 217: Contains Duplicate."""


class Solution:
    """LeetCode-compatible wrapper."""
    def hasDuplicate(self, nums: list[int]) -> bool:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return True
            else:
                hash_map[nums[i]] = nums[i]
        return False        
        


