class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 # first element always unique
        write = 1
        count = 0
        for i in range(1, len(nums), 1):
            if nums[i] == nums[k]:
                count += 1
            else:
                nums[write] = nums[i]
                write += 1
                
        return len(nums) - count

"""
- Think about it this way. You don't actually remove any elements. You just need the
first k elements to be the unique ones.
- The first element is always unique.
- When you find a new unique element, where should you place it?
"""