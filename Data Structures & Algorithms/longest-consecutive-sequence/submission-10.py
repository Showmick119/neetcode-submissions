class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet: # collectively still O(n) as each element only visited once
                length = 1
                # we have found a starting point
                while num + 1 in numSet:
                    length += 1
                    num += 1
                longest = max(length, longest)
        return longest

"""
- They don't care about relative ordering.
"""