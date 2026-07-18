class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        out = 10**3
        while l <= r:
            if nums[l] < nums[r]:
                out = min(out, nums[l])
                return out
            mid = (l + r) // 2
            out = min(out, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return out

"""
- its still binary search, but now the indexes will wrap around using the remainder function
- so there's a breaking point inside the rotated array, which breaks the sorted property,
we need to find this breaking point and then just do +1 on its index to get the minimum value
"""