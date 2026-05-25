class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 10000000
        changed = False
        
        for i in range(len(nums) + 1):
            if i == 0:
                continue
            if i not in nums and not changed:
                smallest = i
                changed = True
                return i
        if changed:
            return smallest
        else:
            return biggest + 1
            
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

"""
- First missing positive is always in 1 to len(nums) + 1
"""