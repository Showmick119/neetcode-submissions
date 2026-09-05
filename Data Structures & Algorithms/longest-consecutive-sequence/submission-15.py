class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in seen:
                curr = 1 # starting a new sequence
                while num + 1 in seen: # since we are checking in a hashset, it's O(1) time-comp
                    curr += 1
                    num += 1
                longest = max(longest, curr)
        return longest

"""
- given an array of integers nums, return the length of the longest consecutive sequence of
elements that can be formed.
- a consecutive sequence is a sequence of elements in which each element is exactly 1 greater
than the previous element. the elements do not have to be consecutive in the original array, they just have to be present in the original array.
"""