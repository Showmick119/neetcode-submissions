class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] > prices[left]:
                total += prices[right] - prices[left]
                left = right
            else:
                left += 1
            right += 1
        return total

            

"""
- Sliding Window Approach, keep left pointer and start it at 0, and then use
right pointer to iterate through all elements.
"""