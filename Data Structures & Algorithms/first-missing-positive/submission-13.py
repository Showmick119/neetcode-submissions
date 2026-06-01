class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        biggest = max(nums)

        for i in range(1, len(nums) + 1, 1):
            if i not in nums:
                return i
        return biggest + 1

"""
- We are given an unsorted integer array called nums. We have to return the smallest POSTIVE
integer which is NOT present in nums.
- The array itself can have all negative values. But we need to return the SMALLEST postive
integer which IS NOT INSIDE THE ARRRAY.
- Can only use O(1) extra space, not considering the input and output data structures.
- Need to do it in O(n) time comp (this does not mean you can only pass the array one time
it just means you can't pass the array once for every element you process). 
"""