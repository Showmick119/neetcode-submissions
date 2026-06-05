class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0
        for r in range(1, len(prices)):
            curr = prices[r] - prices[l]
            if curr > best:
                best = curr
                if l > 0:
                    l -= 1
            else:
                l += 1
                curr = prices[r] - prices[l]
                best = max(curr, best)
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