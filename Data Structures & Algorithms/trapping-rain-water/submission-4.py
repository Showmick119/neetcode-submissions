class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        # keep a left pointer to keep track of largest element from left so far
        l = 0
        # keep a right pointer to keep track of largest element from right so far
        r = len(height) - 1
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            if height[l] < height[i - 1]:
                l += 1
            if height[r] < height[i + 1]:
                r -= 1
            leftMax = height[l]
            rightMax = height[r]
            area += max((min(leftMax, rightMax) - height[i]), 0)
        return area + 2

"""
- In Brute force, you can tell and realize that there is a lot of repeated work.
- Identify this repeated work and compress/remove it systematically.
- So you decide to keep a prefix array, which tells you the maximum value up and till
that specific index.
- First brute force, then identify repeated work and then compress/remove that work.
"""