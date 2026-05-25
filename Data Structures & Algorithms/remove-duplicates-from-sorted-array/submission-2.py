class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 # where to place the next unique element
        r = 0 # scans through the array and finds a new value, diff from what's at l
        # copy value at r into position l and advance both pointers
        while r < len(nums):
            nums[l] = nums[r]
            while r < len(nums) and nums[r] == nums[l]:
                r += 1 # such that it is no longer equal to l, and there's a new val
            l += 1
        return l

"""
- Remember that duplicates are always adjacent in a sorted array.
- O(n) time comp and O(1) space comp.
"""