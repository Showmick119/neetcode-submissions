class Solution:
    def trap(self, height: List[int]) -> int:
        # precompute left maxes
        leftMax = [0] * len(height)
        m = 0
        for i in range(len(height)):
            if height[i] > m:
                m = height[i]
            leftMax[i] = m

        # precompute right maxes
        rightMax = [0] * len(height)
        m = 0
        for i in range(len(height) - 1, -1, -1): # will stop one substraction before -1
            if height[i] > m:
                m = height[i]
            rightMax[i] = m

        area = 0
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            l = leftMax[i]
            r = rightMax[i]
            area += max((min(l, r) - height[i]), 0)
        return area

"""
- In Brute force, you can tell and realize that there is a lot of repeated work.
- Identify this repeated work and compress/remove it systematically.
- So you decide to keep a prefix array, which tells you the maximum value up and till
that specific index.
- First brute force, then identify repeated work and then compress/remove that work.
"""