class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        from collections import deque
        window = deque()
        shortest = 1000000000
        l = 0
        runningSum = 0 # because using the sum() method would make it O(n^2) time complexity
        for num in nums:
            window.append(num)
            runningSum += num
            while runningSum >= target:
                shortest = min(shortest, len(window))
                window.popleft()
                runningSum -= nums[l]
                l += 1
        if shortest == 1000000000:
            return 0
        else:
            return shortest