class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for idx, num in enumerate(nums2):
            nums1[m + idx] = num
        nums1.sort()

"""
- Both arrays sorted in non-decreasing order.
- m tells us number of valid elements in num1.
- n tells us the number of elements in num2.
- Merge such that the final merged array is also sorted in non-decreasing order
and stored entirely within nums1. All changes must have been in-place.
"""