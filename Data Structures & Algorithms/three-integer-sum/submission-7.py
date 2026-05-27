class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if i != j and j!= k and i!= k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            curr = (nums[i], nums[j], nums[k])
                            seen.add(curr)
        return [list(i) for i in seen]

"""
- Let's do the naive solution first.
"""