class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            # find max wall on left
            leftMax = max(height[0:i]) # O(n) space complexity due to creating lists
            # find max wall on right
            rightMax = max(height[i:]) # O(n) space complexity due to creating lists

            area += max((min(leftMax, rightMax) - height[i]), 0)
            # add 0 when your particular index can't store water, since one of its
            # walls are smaller than it
        return area

"""
- You are calculating the water at each index individually.
- You are not trying to find multiple good windows per say. You are just trying to
find the water value at each particular inxex. Given that the bar value at index i
is less than both the maxLeft and maxRight.
- We are not finding basins or windows, stop thinking like that. We are individually
adding water at each index.
- For each index i, find the max wall on left and right.
"""