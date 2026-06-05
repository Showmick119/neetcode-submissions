class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0
        idx, s = min(enumerate(prices), key=lambda x: x[1])
        if idx == len(prices) - 1:
            prices[idx] = 10000000000
        idx, s = min(enumerate(prices), key=lambda x: x[1])
        for r in range(idx + 1, len(prices)):
            curr = prices[r] - prices[idx]
            if curr > best:
                best = curr
        return best

"""
- we have to create a window nonetheless, but start off with the smallest possible l value,
and then find the largest possible r value.

HOW TO USE LAMBDA FUNCTION:
lambda parameter: value_to_return

lambda x: x[1]
lambda x: abs(x)
lambda x: x.name


With min, max, sort, sorted:
max(items, key=lambda x: x[1])

For each item x, use x[1] as the comparison value. The lambda doesn't do the
sorting/min/max itself. It just tells Python what value to compare by.
"""