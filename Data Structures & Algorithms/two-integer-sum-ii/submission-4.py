class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = 0
        while idx2 < len(numbers):
            if idx2 <= idx1:
                idx2 += 1
                continue
            if numbers[idx1] + numbers[idx2] == target:
                return [idx1 + 1, idx2 + 1]
            if idx2 == len(nums) - 1:
                idx1 += 1
                idx2 = 0
            else:
                idx2 += 1
        return []


        # for idx1 in range(len(numbers)):
        #     for idx2 in range(len(numbers)):
        #         if idx2 <= idx1:
        #             continue
        #         if numbers[idx1] + numbers[idx2] == target:
        #             return [idx1 + 1, idx2 + 1]
        # return []

"""
- The final output data structure doesn't count in 
"""