class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        l = 0
        r = 0
        while r < len(temperatures) and l < len(temperatures):
            if r == len(temperatures) - 1 and temperatures[r] <= temperatures[l]:
                results[l] = 0
                l += 1
                r = 1
            if temperatures[r] > temperatures[l]:
                results[l] = r - l
                l += 1
                r = l
            else:
                r += 1
        return results

"""
- you are given array of integers where temp[i] represents the daily temperatures on the
ith day.
- return an array result, where results[i] is the number of days after the ith day before a
warmer temperature appears on a future day.
- if there is no day in the future where a warmer temperature appears, set result[i] to 0.
- length of results will be the same as the length of temperatures.
- time and space comp of o(n). forget about stack for a moment.
"""