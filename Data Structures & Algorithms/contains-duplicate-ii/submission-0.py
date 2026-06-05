class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False

"""
- given an integer array nums and integer k, return true if there are 2 distinct indices i
and j in the array such that nums[i] == nums[j] and abs(i - j) <= k. Otherwise return false.
- 
"""