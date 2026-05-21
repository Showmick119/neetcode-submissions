class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        self.quicksort(nums, left, right)
        return nums
    
    def quicksort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return
        
        # returns i index, but the right index (pivot) and i already swapped
        # so now, i index actually has the pivot element, and we avoid it
        # in our next parition. as we sort from it's left and right onwards.
        pivot_idx = self.partition(nums, left, right)
        # keep quicksorting from left to pivot - 1, until the value of 
        # pivot - 1 is less than left. this means left side fully sorted.
        self.quicksort(nums, left, pivot_idx - 1)
        # keep quicksorting from pivot + 1 to right, until the value of 
        # pivot + 1 is more than right. this means right side fully sorted.
        self.quicksort(nums, pivot_idx + 1, right)
    
    def partition(self, nums: List[int], left: int, right: int) -> int:
        import random
        pivot_idx = random.randint(left, right)
        self.swap(nums, pivot_idx, right)
        pivot = nums[right]

        i = left

        for j in range(left, right):
            if nums[j] < nums[right]:
                self.swap(nums, i, j)
                i += 1
        
        self.swap(nums, i, right)
        return i
    
    def swap(self, nums: List[int], left: int, right: int) -> None:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp


"""
Very simply explain to me the intuition behind these 2 lines:
1) self.swap(nums, i, right)
2) return i

Before those lines:

all elements before i are smaller than pivot
elements from i onward are bigger/equal

Pivot is currently sitting at right.

self.swap(nums, i, right) puts the pivot into its final correct sorted position.

return i, returns the pivots final index so QuickSort knows:
- left side
- right side
- to recursively sort from where
"""

