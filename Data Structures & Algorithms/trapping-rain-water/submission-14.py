class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        while l < r: # standard 2 pointers template
            maxR = max(height[r], maxR)
            maxL = max(height[l], maxL)
            print((maxL, maxR))
            max_area += min(maxL, maxR) - l
            l += 1
            r -= 1
        return max_area
        
"""
- we keep a left and right pointer, and we also keep 2 variables which store the max_left and
max_right pointers. while the left pointer would determine the left boundary.
- in terms of iterating through the array, you would use the left pointer to go through it,
while storing the maxLeft pointer for our left most boundary in between which water would be
stored.
- the naive is to find the MAX RIGHT/LEFT boundary at each index of the array
"""