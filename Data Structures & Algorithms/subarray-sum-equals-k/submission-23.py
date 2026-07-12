class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        runningSum = 0
        sumMap = {}
        sumMap[0] = 1
        for num in nums:
            runningSum += num
            if runningSum - k in sumMap:
                count += sumMap[runningSum - k]
            if runningSum not in sumMap:
                sumMap[runningSum] = 1
            else:
                sumMap[runningSum] += 1
        return count