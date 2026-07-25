class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        smallest = 10**3
        while l <= r:
            if nums[l] <= nums[r]: # in a sorted portion from the start (edge case)
                smallest = min(nums[l], smallest)
            mid = (l + r) // 2
            if nums[mid] >= nums[l]: # you are in left sorted array, you want to go right
                smallest = min(nums[l], smallest)
                l = mid + 1
            else:
                smallest = min(nums[mid], smallest)
                r = mid - 1
        return smallest