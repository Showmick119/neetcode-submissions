class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # last element of nums1
        j = n - 1 # last element of nums2
        num1Ex = False
        num2Ex = False
        last = m + n - 1
        while j >= 0 and i >= 0: # all num2 elements have been placed, so stop
            if nums1[i] > nums2[j]: # finding the greatest between the 2 lists and placing it at the back
                nums1[last] = nums1[i]
                i -= 1
                last -= 1
                if i < 0:
                    num1Ex = True
            else:
                nums1[last] = nums2[j]
                j -= 1
                last -= 1
                if j < 0:
                    num2Ex = True
        
        if num1Ex:
            while last >= 0 and j >= 0:
                nums1[last] = nums2[j]
                j -= 1
                last -= 1
        elif num2Ex:
            while last >= 0 and i >= 0:
                nums1[last] = nums1[i]
                i -= 1
                last -= 1

"""
- Remember that they are both sorted. How can we use this fact to our advantage?
- 3 Pointers needed.
- Filling from the back ensures we never overwrite a valid element that hasn't
been placed yet.
- Since both input arrays are sorted, the largest remaining element among nums1[i]
and nums2[j] belongs at nums1[last].
- Keep comparing the largest of nums1 and nums2, and place it at the last available
index of nums1. Fill from the back, such that we can take advantage of both of these
lists sorted property.
- Keep decrementing the last spot of nums1, and this way you keep progressively
filling it from the back.
"""