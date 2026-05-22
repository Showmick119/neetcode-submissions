class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(r, i)
                r -= 1
                i -= 1
            i += 1
            


"""
- Target Time Complexity: O(n)
- Target Space Complexity: O(1)
- Given an array nums consisting of n elements where each element is an
integer representing a color.
- O: red
- 1: white
- 2: blue
- elements of the same color are grouped together and arranged in order
- 0s should come first, then 1s, then 2s
- Come up with a one-pass algo, so O(n) and only constant extra space like
naming variables, etc.
"""

"""
As you pass through it, you keep track of incorrect indicies and then replace
it with the correct element when you run into it.
"""


