class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums), 1):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    if i != j and i != l and i != r and j != l and j != r and l != r:
                        if nums[i] + nums[j] + nums[l] + nums[r] == target:
                            curr = [nums[i], nums[j], nums[l], nums[r]]
                            curr.sort()
                            if curr not in out:
                                out.append(curr)
                            l += 1
                            r -= 1
                        elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                            l += 1
                        elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                            r -=1
                    else:
                        l += 1
                        r -= 1
        return out
                    

"""
- Target time complexity is O(n^3).
- Target space complexity is O(1).
- Space complexity only includes the auxiliary space, meaning the temporary data
structures and variables which are used to solve the problem.
- It excludes the input and output variables and data structures, which are used to
solve the problem.
"""