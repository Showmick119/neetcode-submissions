class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        w = 1
        count = 0
        while i < len(nums):
            if nums[i] == nums[w - 1]:
                count += 1
            elif nums[i] != nums[w - 1]:
                nums[w] = nums[i]
                w += 1
            i += 1
        return len(nums) - count