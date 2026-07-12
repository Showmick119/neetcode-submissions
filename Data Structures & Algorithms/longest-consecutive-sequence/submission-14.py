class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in seen:
                curr = 1
                while num + 1 in seen:
                    curr += 1
                    num += 1
                longest = max(longest, curr)
        return longest

"""
- use hashset such that the 'in nums' line of code is o(1) time complexity
- the longest consecutive sequence doesn't have to be in perfect order relative to the rest
of the array
"""