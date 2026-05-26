class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx1 in range(len(numbers)):
            for idx2 in range(len(numbers)):
                if idx2 <= idx1:
                    continue
                if numbers[idx1] + numbers[idx2] == target:
                    return [idx1 + 1, idx2 + 1]
        return []
                

"""
- Given an array of integers called numbers that is sorted in non-decreasing order.
Return the indices (NOT ZERO INDEXED) of 2 numbers [index1, index2], such that they
add up to a given target number target.
- index1 and index2 cannot be equal.
- Can only use O(1) additional space, return .
- Can only pass through the array once, as we need an O(n) time complexity.
- First do the basic solution
"""