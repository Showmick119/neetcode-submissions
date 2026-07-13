class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = float('inf')
        l = 0
        runningSum = 0
        for r in range(len(nums)):
            runningSum += nums[r]
            while runningSum >= target:
                shortest = min(shortest, r - l + 1)
                runningSum -= nums[l]
                l += 1
        return 0 if shortest == float('inf') else shortest