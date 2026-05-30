class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        write = 0 # last unique spot which needs to be updated
        ## first element is ALWAYS UNIQUE
        i = 1 # scan through array
        while i < len(nums):
            if nums[write] != nums[i]:
                if write == 0:
                    write = i
                    i += 1
                    continue
                nums[write] = nums[i]
                write = i # latest unique
            elif nums[write] == nums[i]:
                count += 1
                write += 1
            i += 1
        return len(nums) - count