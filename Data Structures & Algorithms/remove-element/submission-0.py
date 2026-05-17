class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        count = 0
        while (i < len(nums) and k <= i):
            if nums[i] != val:
                nums[k] = nums[i]
                count += 1
                i += 1
                k += 1
            else:
                i += 1
        return count

"""
- Target Space Complexity: O(1)
- Target Time Complexity: O(n)
- Cannot create a new array, all changes should be in place.
- Also, for the elements equal to val, trying to take it to the end
of the list, and then shifting every element back by 1 index, would
make the process O(n^2).
- Two Pointers has been suggested.
- Overwrite the front of the array with the elements not equal to val.
And ignore the elements equal to val. This will implicitly remove them.
- We cannot shrink the array.
- count variable stores the number of elements not equal to val.
- We want all those elements to come to the front of the array. The order
does not matter.
"""