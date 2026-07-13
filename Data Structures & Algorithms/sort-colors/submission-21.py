class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redPointer = 0
        bluePointer = len(nums) - 1
        i = 0
        while i < len(nums):
            if i == len(nums) - 1 and nums[i] == 2:
                break
            elif i == 0 and nums[i] == 0:
                i += 1
                redPointer += 1
                continue
            elif nums[i] == 0 and redPointer < len(nums):
                temp = nums[redPointer]
                nums[redPointer] = nums[i]
                nums[i] = temp
                redPointer += 1
                i += 1
            elif nums[i] == 2 and bluePointer > 0:
                temp = nums[bluePointer]
                nums[bluePointer] = nums[i]
                nums[i] = temp
                bluePointer -= 1
            else:
                i += 1

"""
- it's a two pointers question, we have one at the front and another at the back. one for the
red group and the other for the blue group
"""