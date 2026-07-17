class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        maxArea = 0
        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            areaHeight = min(maxL, maxR)
            if maxL <= maxR: # it has experienced what its like to be the boundary height,
            # hence it can move forward
                maxArea += max(0, areaHeight - height[l])
                l += 1
            else:
                maxArea += max(0, areaHeight - height[r])
                r -= 1
        return maxArea