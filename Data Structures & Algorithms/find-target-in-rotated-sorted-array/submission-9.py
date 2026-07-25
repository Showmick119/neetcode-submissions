class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                # on the left side
                if nums[l] <= target and nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1 # move to right side
            else:
                # on the right side
                if nums[r] >= target and nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1 # move to left side
        return -1

"""
- there is a left and right sorted portion. first find out which portion you are in, and then
continue your search to the other side.
"""