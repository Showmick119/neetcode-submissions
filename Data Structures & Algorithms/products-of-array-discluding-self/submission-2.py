class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        for index1, num1 in enumerate(nums):
            curr = 0
            for index2, num2 in enumerate(nums):
                if index1 != index2:
                    output[index1] += num2
        return output

"""
- Given an integer array nunms, return an array output, where output[i] is
the product of all the elements of nums except nums[i].
- Target time complexity is O(n). Space too.
- Challenge: Don't use division operation.
- Do your fist shot, then do follow-up. It's a follow-up, not an entirely
different question.
"""