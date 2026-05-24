class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        left = 0
        for right in range(len(prices)):
            if prices[right] > prices[left]:
                total += prices[right] - prices[left]
                left += 1
        return total
            

"""
- Sliding Window Approach, keep left pointer and start it at 0, and then use
right pointer to iterate through all elements.
"""