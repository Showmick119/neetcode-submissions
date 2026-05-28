class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if i != j and j != k and i != k:
                    if nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    else:
                        curr = [nums[i], nums[j], nums[k]]
                        out.add(tuple(curr))
        final = [list(i) for i in out]
        return final

"""
- Sort it such that, we know that when sum is less than our target, we have to move
the left pointer up (as that would increase our cumulative value).
- And when our sum is more than the target, we move the right pointer down, as the
right side generally has the bigger values. And we want to reduce the value, such
that we get closer to the target.
- A HashSet works better, as trying to sort the current array each time would lead
to inefficiency.
"""