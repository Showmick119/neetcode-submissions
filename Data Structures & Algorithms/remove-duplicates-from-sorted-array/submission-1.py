class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        i = 0
        j = 1
        while j < len(nums) - 1:
            # if nums[i] == None:
            #     nums[i] = nums[j]
            #     if (j + 1) < len(nums):
            #         nums[j] = nums[j + 1]
            #         nums[j + 1] = None
            #     else:
            #         nums[j] = None # final element
            #     continue
            if nums[i] == nums[j]:
                count += 1 ## overcounting
                nums[j] = None
            i += 1
            j += 1
        
        for idx, val in enumerate(nums):
            if val == None:
                for i in range(idx, len(nums)):
                    if (i + 1) < len(nums):
                        nums[i] = nums[i + 1]

        k = len(nums) - count + 1
        return k

"""
- How do we know if it has been seen before?
- Since the array is sorted, what does that signal? Duplicates are always adjacent.
- You only need to compare each element with its predecessor to detect duplicates in
O(1) space.
- Python lists CAN store mixed types. So it can always store None.
- And it's not necessarily a duplicate of just 2, it can be a sequence of multiple of
the same duplicates.
"""