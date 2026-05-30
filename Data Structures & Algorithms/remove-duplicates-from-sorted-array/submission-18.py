class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        write = 1 # write is empty index for our next unique value
        # first element is ALWAYS UNIQUE
        i = 1 # scan through array
        # (write - 1) is already written and established
        # we scan with i and find unique values to place at index write
        # then progress write index, as it can store next unique value only at
        # the next index, as this current index has been filled with a unique value
        while i < len(nums):
            if nums[i] == nums[write - 1]:
                count += 1
            else:
                nums[write] = nums[i]
                write += 1
            i += 1
        return len(nums) - count