class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # biggest in nums1
        j = n - 1 # biggest in nums2
        last = m + n - 1 # final spot in nums1 that we are currently trying to fill

        ## just try and place all the nums2 in the correct place, and then nums1 is autosorted
        while i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                nums1[last] = nums2[j]
                last -= 1
                j -= 1
            else:
                nums1[last] = nums1[i]
                last -= 1
                i -= 1
        
        if j >= 0:
            while j >= 0 and last >= 0:
                nums1[last] = nums2[j]
                last -= 1
                j -= 1

"""
- We add from the back, such that we don't overwrite any of the existing elements.
- nums1 and its pointer i is larger than nums2 and its pointer j. So if j is done, and its
value is < 0, that means there's no more comparisons to be done, and that all the j elemenets
have been placed correctly, and the remaining i elements are in their correct position
already.
- But if i < 0, that means all i elements have been placed corretly, but that doesn't mean
all the j elements are placed correctly. Because j elements are coming from a different
array. So j value has to be < 0, for us to be sure that all the j elements from nums2 have
been bought over and placed correctly in nums1.
- Even if i value not < 0, i values are already placed in nums1. And if all j comparisons are
complete, that it means that those i values are not only already in nums1, but also in their
correct relative position, as all their comparions with j elements have completed.
"""