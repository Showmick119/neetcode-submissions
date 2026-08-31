class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for index, num in enumerate(nums):
            if num not in mp:
                mp[num] = []
            mp[num].append(index)
        out = []
        for index, num in enumerate(nums):
            if target - num in mp:
                tempList = mp[target - num] # array indices which have that value stored
                i = 0
                while i < len(tempList) and index != tempList[i]:
                    i += 1
                if index < tempList[i]:
                    out.append(index)
                    out.append(tempList[i])
                else:
                    out.append(tempList[i])
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