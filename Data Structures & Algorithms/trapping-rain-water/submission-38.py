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
- the side with the smaller maximum is "resolved" because its water level is already
determined

The amount of water above an index is:

water = min(highest wall on left, highest wall on right height)

The problem is: you don't know the future highest wall on the opposite side.

But if:
maxL = 4
maxR = 7

then the right side is already tall enough. Even if it gets taller later, the minimum is still:
min(4, 7+) = 4

So the water at the left index is fully determined right now. You can compute it and move on.

If instead you tried to compute the right index, you don't know whether a taller left wall 
might appear later, so its water level isn't guaranteed yet.

That's why you always process the side with the smaller maximum.
"""