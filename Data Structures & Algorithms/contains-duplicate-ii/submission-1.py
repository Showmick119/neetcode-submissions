class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import deque
        window = deque()
        for i in range(len(nums)): # keep expanding the window from the front
            if len(window) > k:
                window.popleft()
            if nums[i] in window:
                return True
            window.append(nums[i])
        return False

"""
- given an integer array nums and integer k, return true if there are 2 distinct indices i
and j in the array such that nums[i] == nums[j] and abs(i - j) <= k. Otherwise return false.
- you need 2 pointers even in sliding window. one to expand the window, another to shrink
the window.
"""