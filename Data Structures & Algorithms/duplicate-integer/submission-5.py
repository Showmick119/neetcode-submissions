class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for num in nums:
            if num in mp:
                return True
            else:
                mp[num] = 1
        return False

"""
- given an array nums, return true if any value appears more than once in the array. otherwise
return false.
"""