class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        write = None
        idx = 0
        for i in range(len(nums)):
            if write:
                nums[idx] = nums[i]
                write = False
            if i + 1 < len(nums):
                if nums[i] == nums[i + 1] and not write:
                    count += 1
                    write = True
                    idx = i + 1
        return len(nums) - count


"""
- Remember that the array is sorted. So all the duplicates would be right next to
each other.
- Remove all the duplicates in-place. After removing the duplicates, return the
number of unique elements, denoted as k. Such that the first k elements of nums
contain the unique elements.
- First k elements must contain all the unique elements.
- Have a write index which stores the index to which you can write. But write what?
- Write the next available element.
- So if we recently get an index to which we can write, we introduce some sort of
boolean flag which would tell us, that we are ready to write.
"""