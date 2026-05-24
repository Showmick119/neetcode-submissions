class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        i = 0
        
        while i <= r:
            if nums[i] == 0:
                self.swap(nums, l, i)
                l += 1
            elif nums[i] == 2:
                self.swap(nums, r, i)
                r -= 1
                i -= 1
            i += 1
    
    def swap(self, nums: List[int], l: int, r: int) -> None:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp

"""
- Pointers methods always help when you have to do a one-pass algorithm and
need constant space.
- This is a 3-pointers problem. Whenever you are dealing with 3 pointers,
there's a left pointer (0th index), a right pointer (last index), and a
pointer for iterating through the list.
- Sort both sides, the 0s and the 2s, and the 1 will subconciously be sorted
in the middle.
"""