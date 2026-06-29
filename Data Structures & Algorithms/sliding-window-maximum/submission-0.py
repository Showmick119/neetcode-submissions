class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        l = 0
        r = k
        while r < len(nums) + 1:
            out.append(max(nums[l:r]))
            r += 1
            l += 1
        return out

"""
- You are given an array of integers nums and an integer k. there is a sliding window of
size k that starts at the left edge of the array
- the window slides one position to the right until it reaches the edge of the array
- return a list that contains the maximum element in the window at each step
"""