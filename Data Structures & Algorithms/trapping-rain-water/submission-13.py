class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        maxLeft = height[l]
        r = len(height) - 1
        maxRight = height[r]
        area = 0
        while l < r:
            maxLeft = max(height[l], maxLeft)
            maxRight = max(height[r], maxRight)
            if maxLeft < maxRight:
                l += 1 # we found minimum here, so we have its contribution to the answer
                area += max(maxLeft - height[l], 0)
            else:
                r -= 1
                area += max(maxRight - height[r], 0)
        return area

"""
- each value represents the height of the bar and each bar has a width of 1
- area of water that can be trapped BETWEEN the bars
- target time and space comp is O(n)
- we treat each i as an individaul water count
- this water count solely depends on the minimum between the left and right
- but not minimum between direct left and right, rather minimum between maxLeft and maxRight
- you don't iterate with an i pointer, as that would make the problem into quadratic time
- you iterate with the l pointer, you treat it like an 
"""