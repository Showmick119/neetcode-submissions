class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numset:
            if (num - 1) not in numSet: # not that it is the absolute smallest
            # but that there is no directly smaller element in consecutive series with it
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


"""
- Given an array of integers nums, return the length of the LONGEST consecutive
sequence of elements that can be formed.
- A consecutive sequence is a sequence of elements in which each element is 
EXACTLY 1 greater than the previous element.
- The elements don't have to be together and directly consecutive. Just relatively
consecutive.
- O(n) time and space complexity targeted.
- Sliding Window
"""