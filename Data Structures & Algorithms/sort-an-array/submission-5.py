class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def quickSort(self, nums, left, right) -> None:
        if left >= right:
            return
        
        pivot = self.partition(nums, left, right)
        
        # Sorting everything else, other than the pivot, with respect to the 
        # pivot.
        self.quickSort(nums, left, pivot - 1)
        self.quickSort(nums, pivot + 1, right)

    def partition(self, nums, left, right) -> int:
        pivot = nums[right]
        i = left

        for j in range(left, right):
            if nums[j] < pivot:
                self.swap(nums, i, j)
                i += 1
        
        self.swap(nums, i, right)
        return i
    
    def swap(self, nums, left, right) -> None:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp


"""
- Quick Sort and Merge Sort are your only O(nlogn) sorting algorithms.
- Quick Sort has O(logn) space complexity, whereas Merge Sort has O(n), and
O(logn) is preferred over O(n), since they asked for smallest space
complexity possible.
- Selection Sort, Insertion Sort, Bubble Sort are all O(n^2) sorting algos.
"""

"""
- In Quick Sort you keep on picking a random pivot element and sort rest of 
the array relative to it.
- All elements bigger than pivot go to right side. All elements smaller than
pivot go to left side.
- And you keep doing this, and eventually your entire array is sorted.
"""