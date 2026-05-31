class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        seq = set(nums)
        for num in nums:
            if ((num - 1) in seq):
                seq.add(num)
                count += 1
        return count

"""
- They don't care about relative ordering.
"""