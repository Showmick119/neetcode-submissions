class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][1]:
                idx = stack[-1][0]
                result[idx] = index - idx
                stack.pop()
            stack.append((index, temp))
        return result

"""
- you are given an array of integers temperatures where tempe
"""