class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first build a hashmap mapping every value to it's index
        numMap = {}
        for index, num in enumerate(nums):
            if num not in numMap:
                numMap[num] = index
            else:
                continue
            # we only want the smallest index containing the number
            # no need to store later iterations
        for index, num in enumerate(nums):
            remaining = target - num
            if remaining in numMap:
                remainingIndex = numMap[remaining]
                if remainingIndex < index:
                    return [remainingIndex, index]
                else:
                    return [index, remainingIndex]
        return []

"""
- Main thing you need to remember is that we need to complete it
in O(n) time complexity.
- So we cannot do a double for-loop. That is the initial easy way,
but it won't work too well.
"""