class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from collections import deque
        w = deque()
        for r in range(len(arr)):
            if len(w) == k:
                if abs(arr[r] - x) == abs(w[0] - x):
                    if arr[r] < w[0]:
                        w.popleft()
                        w.append(arr[r])
                elif abs(arr[r] - x) < abs(w[0] - x):
                    w.popleft()
                    w.append(arr[r])
            else:
                w.append(arr[r])
        return list(w)

"""
- given a SORTED integer array and two integers k and x, return the k closest integers to
x in the array. the result should also be sorted in ascending order.
- the integer x doesn't necessarily have to be in the array, but the k elements must be
from the array, even though x doesn't have to be in the array itself.
"""