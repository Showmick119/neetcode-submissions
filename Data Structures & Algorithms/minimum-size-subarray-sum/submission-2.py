class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currSum = 0
        smallest = 1000000000
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                smallest = min(smallest, r - l + 1)
                currSum -= nums[l]
                l += 1
        if smallest == 1000000000:
            return 0
        else:
            return smallest

"""
- you are given an array of positive integers nums, and a positive integer target, return
the minimal length of a subarray whose sum is greater than or equal to target.
- if there is no such subarray, return 0.
- a subarray is a contiguous non-empty sequence of elements within an array
"""