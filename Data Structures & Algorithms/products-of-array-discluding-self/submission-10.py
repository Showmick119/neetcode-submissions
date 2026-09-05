class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [0] * len(nums)
        curr_product = 1
        for idx, num in enumerate(nums):
            prefix_product[idx] = curr_product
            curr_product *= num
        
        suffix_product = [0] * len(nums)
        curr_product = 1
        for idx in range(len(nums) - 1, -1, -1):
            suffix_product[idx] = curr_product
            curr_product *= nums[idx]
        
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix_product[i] * suffix_product[i]
        return output

"""
- need prefix and suffix products/sums, which means the product of everything to the left
of the current index, and the product of everything to the right of the current index.
"""