class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet: # collectively still O(n) as each element only visited once
                length = 1
                # we have found a starting point
                while num + 1 in numSet:
                    length += 1
                    num += 1
                longest = max(length, longest)
        return longest

"""
- They don't care about relative ordering.
- Visiting an element twice is not the same as O(n^2).
- O(n^2) happens when each element causes a full scan of all the other elements.
- Checking elements twice means O(2n), not O(n^2).
- Outer-loop at most n checks, while loops combined at most n checks: O(n + n) = O(2n).
- The inner while loop DOES NOT RUN for EVERY OUTER ITERATION. Hence IT IS NOT O(n^2) time
complexity.
- Due to the if-condition, the total work for the while-loop across the entire program is
still O(n). As it simply won't run majority of the times, due to the sequence already existing.
- O(n^2) is when for each element i, you SCAN and LOOP THROUGH all n elements of the array.
"""