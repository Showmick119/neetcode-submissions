class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        # keep a left pointer to keep track of largest element from left so far
        l = 0
        # keep a right pointer to keep track of largest element from right so far
        r = len(height) - 1
        i = 0
        leftMax = rightMax = 0
        while l < r and i < len(height):
            leftMax = max(height[l], leftMax)
            rightMax = max(height[r], rightMax)
            if leftMax < rightMax:
                l += 1
            else:
                r -=1
            area += max((min(leftMax, rightMax) - height[i]), 0)
            i += 1
        return area

"""
- In Brute force, you can tell and realize that there is a lot of repeated work.
- Identify this repeated work and compress/remove it systematically.
- So you decide to keep a prefix array, which tells you the maximum value up and till
that specific index.
- First brute force, then identify repeated work and then compress/remove that work.
"""