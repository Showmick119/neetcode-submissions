class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n <= 1:
            return nums

        pivot = nums[n // 2]
        left = [x for x in nums if x < pivot]
        right = [x for x in nums if x > pivot]

        return self.sortArray(left) + [pivot] + self.sortArray(right)

"""
- Smallest space complexity possible.
- Needs an O(nlogn) average time-complexity
- So one thing becomes very obvious, NO MERGE SORT, as it is recursive and
needs O(n) space complexity.
- Quick sort will give us O(nlogn) time complexity and O(logn) space comp.
"""