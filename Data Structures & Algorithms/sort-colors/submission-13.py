class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 2 and nums[r] == 2:
                break
            if nums[i] == 0:
                self.swap(nums, i, l)
                l += 1 ## there can't possibly be a new 1 which we have to handle, as we 
                ## would have handled it by now. so the new element that comes to index i
                # is a 0
            elif nums[i] == 2:
                self.swap(nums, i, r)
                r -= 1
                i -= 1
                # could have another 2 in the position of i. so we need to handle it and
                # put it to the back
            i += 1

    def swap(self, nums: List[int], l: int, r: int) -> None:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp

"""
- Each element is an integer representing a color. O represents red, 1 represents white and
2 represents blue.
- 0s should come first, then 1s and then 2s. Elements of the same color should be grouped
together and arranged in the above order.
- Super each naively, but need to do it in one-pass.
- Sort both ends, and the middle one is going to be sorted on its own.
"""