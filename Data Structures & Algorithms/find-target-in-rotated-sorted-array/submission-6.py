class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # elif nums[m] > target:
            #     r = m - 1
            # else:
            #     l = m + 1
            elif nums[m] >= nums[l]: # in left sorted half, but is it the correct half
                if nums[l] <= target and nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[r] >= target and nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1 
        return -1