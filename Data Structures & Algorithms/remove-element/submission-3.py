class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0 # number of elements equal to val
        w = 0
        for num in nums:
            if num != val:
                nums[w] = num
                w += 1
            else:
                count += 1
        return len(nums) - count # number of elements not equal to val