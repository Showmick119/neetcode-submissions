class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1000000000
        nonNeg = False
        for num in nums:
            if num >= 0:
                nonNeg = True
                if num < smallest and (num + 1) not in nums:
                    smallest = num
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