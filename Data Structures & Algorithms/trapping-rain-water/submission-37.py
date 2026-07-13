class Solution:
    def trap(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[r]
        while l <= r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if maxL < maxR:
                maxArea += max(0, min(maxL, maxR) - height[l])
                l += 1
            else:
                maxArea += max(0, min(maxL, maxR) - height[r])
                r -= 1
        return maxArea
        
"""
- having smaller side maximum is good thing, and means we are done processing for that side
and can move on, as we have that side's best value
"""