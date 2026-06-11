class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0
        for r in range(1, len(prices)):
            if prices[r] < smallest:
                smallest = prices[r]
            curr = prices[r] - smallest
            profit = max(curr, profit)
        return profit

"""
- You are given an integer array prices where prices[i] is the price of the NeetCoin on the
ith day.
- keep track of the smallest value you have seen so far, and store it. and then constantly
compare with other values and 
"""