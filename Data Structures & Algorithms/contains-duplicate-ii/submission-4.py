class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import deque
        w = deque() # our window which should not contain more than k elements
        for num in nums:
            if len(w) >= k + 1:
                w.popleft() # if its at max window length of k + 1, pop an element from the front
                # such that we have room for the next element which we are adding to the back, in this loop. 
                # upon adding that next element, we still maintain that max window length of k + 1.
                # we cannot exceed it, as that break the conditiion for what distance is needed for an element
                # match to be considered correct.
            if num in w:
                return True
            w.append(num)
        return False

"""
- abs(i - j) <= k, means its in a window of (k + 1) elements, and the elements can be at most
k distance apart.
- [0, 1, 2, 3] is a valid window of k + 1 elements, as the farthest pair, at idx = 0 and
idx = 3 are k distance apart.
"""