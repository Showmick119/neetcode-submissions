class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for currIdx, currVal in enumerate(nums):
            complement = target - currVal
            if complement in seen:
                return [seen[complement], currIdx]
            else:
                seen[currVal] = currIdx
        return []