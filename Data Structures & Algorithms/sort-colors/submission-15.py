class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redPointer = 0
        bluePointer = len(nums) - 1
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                temp = nums[redPointer]
                nums[redPointer] = nums[i]
                nums[i] = temp
                redPointer += 1
            elif nums[i] == 2:
                temp = nums[bluePointer]
                nums[bluePointer] = nums[i]
                nums[i] = temp
                bluePointer -= 1
                continue
            i += 1

"""
- there's 2 extreme sides which you have to sort, and the rest will sort on its own
- you have to sort the left and right side, and then the middle values will automatically
sort
"""