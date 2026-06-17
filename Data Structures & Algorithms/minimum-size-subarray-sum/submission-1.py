class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        from collections import deque
        w = deque()
        l = 0
        smallest = 1000000000
        for r in range(len(nums)):
            w.append(nums[r])
            while sum(w) >= target:
                smallest = min(smallest, len(w))
                w.popleft()
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