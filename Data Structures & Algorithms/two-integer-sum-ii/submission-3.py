class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = []
        for idx1 in range(len(numbers)):
            for idx2 in range(len(numbers)):
                if idx2 <= idx1:
                    continue
                if numbers[idx1] + numbers[idx2] == target:
                    out.append(idx1 + 1)
                    out.append(idx2 + 1)
                    return out
        return []
                

"""
- The final output data structure doesn't count in 
"""