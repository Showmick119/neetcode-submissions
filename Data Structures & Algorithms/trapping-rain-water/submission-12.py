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
            area += max((min(maxLeft, maxRight) - height[l]), 0) # we don't want negatives
            if maxLeft > maxRight:
                r -= 1
                # move the bad one such that we can progress towards a higher overall score
            l += 1 # has to always move. it acts as our pointer for scanning through
            # the array
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