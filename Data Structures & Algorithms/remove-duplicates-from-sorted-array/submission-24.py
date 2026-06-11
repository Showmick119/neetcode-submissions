class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 1 # everything before current w is processed and in correct order and state
        i = 1
        count = 0
        while i < len(nums):
            if nums[i] == nums[w - 1]:
                count += 1
            else:
                nums[w] = nums[i]
                w += 1
            i += 1
        return len(nums) - count

"""
- Given an integer array nums which is sorted. That means all duplicates will be right next
to each other. Your task is to remove duplicates in-place such that each element appears
only once.
- After removing the duplicates, return the number of unique elements, denoted as k. And the
first k elements of nums should contain the unique elements. The elements after that don't
matter.
- If (w - 1) is not a duplicate with i, that means its clear and good to.
"""