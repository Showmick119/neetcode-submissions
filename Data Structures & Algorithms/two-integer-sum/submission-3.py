class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen: # checks the keys of the dict
                return [seen[complement], i]
            seen[num] = i