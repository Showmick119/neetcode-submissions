class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0
        max_left, max_right = 0,  0
        l, r = 0, len(height) - 1
        while l < r and l < len(height):
            if l == len(height) - 1 or l == 0:
                l += 1
                continue
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])
            curr_height = height[l]
            area_height = min(max_left, max_right)
            max_area += max(0, area_height - curr_height)
            if max_left > max_right:
                max_area += max(0, area_height - height[r])
                r -=1
            l += 1
        # for i in range(len(height)):
        #     if i == len(height) - 1 or i == 0:
        #         continue
        #     curr = height[i]
        #     maxL = max(height[0:i])
        #     maxR = max(height[i+1:])
        #     print(f'maxL: {maxL} and maxR: {maxR}')
        #     h = min(maxL, maxR)
        #     max_area += max(0, h - curr)
        return max_area
        
"""
- we keep a left and right pointer, and we also keep 2 variables which store the max_left and
max_right pointers. while the left pointer would determine the left boundary.
- in terms of iterating through the array, you would use the left pointer to go through it,
while storing the maxLeft pointer for our left most boundary in between which water would be
stored.
- the naive is to find the MAX RIGHT/LEFT boundary at each index of the array
"""