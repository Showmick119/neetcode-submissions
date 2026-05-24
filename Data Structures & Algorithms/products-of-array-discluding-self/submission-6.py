class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        curr = 0
        scan = 0
        while scan < len(nums) and curr < len(nums):
            if scan != curr:
                output[curr] *= nums[scan]
            if scan == len(nums) - 1: ## reached final index of nums
                curr += 1
                scan = 0
            else:
                scan += 1

"""
- Given an integer array nunms, return an array output, where output[i] is
the product of all the elements of nums except nums[i].
- Target time complexity is O(n). Space too.
- Challenge: Don't use division operation.
- Do your fist shot, then do follow-up. It's a follow-up, not an entirely
different question.
- Said O(n) time, not one-pass.
- Calculate a prefix matrix and a suffix matrix. The multiply them element
by element.
"""