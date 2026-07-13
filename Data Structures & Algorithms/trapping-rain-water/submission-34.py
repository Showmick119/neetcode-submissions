class Solution:
    def trap(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[r]
        while l <= r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if maxL > maxR:
                maxArea += max(0, min(maxL, maxR) - height[l])
                l += 1
            else:
                maxArea += max(0, min(maxL, maxR) - height[r])
                r -= 1
        return maxArea

        # for i in range(len(height)):
        #     if i == len(height) - 1 or i == 0:
        #         continue
        #     curr = height[i]
        #     maxL = max(height[0:i])
        #     maxR = max(height[i+1:])
        #     print(f'maxL: {maxL} and maxR: {maxR}')
        #     h = min(maxL, maxR)
        #     max_area += max(0, h - curr)

        
"""
- we keep a left and right pointer, and we also keep 2 variables which store the max_left and
max_right pointers. while the left pointer would determine the left boundary.
- in terms of iterating through the array, you would use the left pointer to go through it,
while storing the maxLeft pointer for our left most boundary in between which water would be
stored.
- the naive is to find the MAX RIGHT/LEFT boundary at each index of the array
"""