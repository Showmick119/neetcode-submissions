class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        w = 0
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] != val:
                nums[w] = nums[i]
                w += 1
                i += 1
            else:
                count += 1
                i += 1
        return len(nums) - count

"""
- Everything before write is already correct and in the write position.
- w pointer builds the answer, i pointer explores the candidates.
- Write all good stuff to w, and skip the bad stuff!! Just skip the elements equal to val,
you don't have to set to null and everything. Just skip it!
- The order of elements may be changed.
"""