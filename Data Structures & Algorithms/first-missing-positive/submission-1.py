class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 10000000
        for i in range(len(nums)):
            idx, val = min(enumerate(nums), key=lambda x: x[1])
            if val + 1 not in nums:
                if val >= 0:
                    smallest = val
                else:
                    smallest = 0
            else:
                nums[idx] = 10000000000
        return smallest + 1

"""
- You are given an unsorted integer array nums. Return the smallest POS int,
that is NOT present in nums.
- O(n) time and O(1) AUXILIARY SPACE, meaning it's not counting the return
data structure. But then we have to return an int anyways, so it don't matter.
- nums[i] can be ANY negative or positive integer.
- Find the smallest positive integer present, and then do 1+ that, make sure
there is a slot for the 1+ tho, and that the 1+ DOES not exist in the nums.
"""

"""
- Keep iterating and find the smallest possible and then return an element
greater than that by 1.
"""