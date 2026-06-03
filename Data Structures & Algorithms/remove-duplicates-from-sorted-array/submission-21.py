class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 1 # the spot where our next unique element will go
        # everything before w is already processed and correct and unique. no need to worry
        i = 1 # our pointer, we don't consider i = 0, as its the first and its considered
        # to be sorted
        count = 0
        while i < len(nums):
            if nums[i] == nums[w - 1]:
                count += 1
                # w not shift, as we have not yet found unique
            else:
                nums[w] = nums[i]
                w += 1 # everything before w is processed and in correct order and position
            i += 1
            # first element already accepted, now scan remaining elements for unique
        return len(nums) - count 
        # will return num of unique, after substracting num of duplicates
