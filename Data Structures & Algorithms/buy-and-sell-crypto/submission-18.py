class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0
        for r in range(1, len(prices)):
            curr1 = prices[r] - prices[l]
            best = max(best, curr1)
            
            if l > 0:
                l -= 1
                curr2 = prices[r] - prices[l]
                best = max(best, curr2)

            if l < len(prices) - 1:
                l += 1
                curr3 = prices[r] - prices[l]
                best = max(best, curr3)
            
            l += 1
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