class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        write = 1 # last unique spot which needs to be updated
        ## first element is ALWAYS UNIQUE
        i = 1 # scan through array
        # (write - 1) is already written and established
        # write is empty spot for our next unique value
        while i < len(nums):
            if nums[i] == nums[write - 1]:
                count += 1
            else:
                nums[write] = nums[i]
                write += 1
            i += 1
        return len(nums) - count