class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        leader = nums[0]
        count = 0
        for i in range(len(nums)):
            if nums[i] == leader:
                count += 1
            else:
                count -=1
            if count < 0:
                leader = nums[i]
                count = 0
        return leader

"""
- Easy to solve it naively. But challenge comes when doing it optimally.
"""