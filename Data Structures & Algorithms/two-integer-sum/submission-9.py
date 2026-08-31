class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for index, num in enumerate(nums):
            if num in mp:
                if index < mp[num]:
                    mp[num] = index
            else:
                mp[num] = index
        out = []
        for index, num in enumerate(nums):
            if target - num in mp:
                if mp[target - num] > index:
                    out.append(index)
                    out.append(mp[target - num])
                else:
                    out.append(mp[target - num])
                    out.append(index)
                return out
        return []

"""
- given an array of integers nums and an integer target, return the indices i and j such that
the values at those indices add up to equal target and the indices are not equal.
- you may assume that every input has exactly one pair of indices i and j that satisfy the
condition.
- return the answer with the smaller index first.
- put every number's smallest index in the hashmap.
"""