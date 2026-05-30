class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        # keep a left pointer to keep track of largest element from left so far
        l = 0
        # keep a right pointer to keep track of largest element from right so far
        r = len(height) - 1
        leftMax = rightMax = 0
        while l < r: ## accounting for each water index from both sides!!!
            leftMax = max(height[l], leftMax) ## checking if its the greatest left
            # boundary so far
            rightMax = max(height[r], rightMax) ## checking if its the greatest right
            ## boundary so far
            if leftMax < rightMax:
                area += max((min(leftMax, rightMax) - height[l]), 0)
                l += 1
                # compute water on the side you move, this way you make sure you
                # cover each and every valid index
            else:
                area += max((min(leftMax, rightMax) - height[r]), 0)
                r -=1
        return area

"""
- In Brute force, you can tell and realize that there is a lot of repeated work.
- Identify this repeated work and compress/remove it systematically.
- So you decide to keep a prefix array, which tells you the maximum value up and till
that specific index.
- First brute force, then identify repeated work and then compress/remove that work.
"""