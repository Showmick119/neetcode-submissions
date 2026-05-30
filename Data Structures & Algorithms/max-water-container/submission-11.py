class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1
        curr = 0

        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            if curr > area:
                area = curr
            if heights[l] > heights[r]: # r is bad and it needs to change
                r -=1
            else: # l is bad and it needs to change
                l += 1
        return area
        # you just have to make the shorter pointer move inwards, and keep checking
        # if it increases and maximizes your area value


""""
- Sliding Window type problem. But all the elements in the window are either equal to
or less than the elements on the 2 edges.
- O(n) time complexity and O(1) space complexity. But this is for optimal solution,
we can do the naive approach first.
- The height is limited by the shorter bar, and width is the distance between the 2
bars.
- We cannot sort it, as that would go against all time-complexity requirements. And
the whole point is to get the max in the current container as it is.
- How about we find the max in the array, as well as it's index. And then find the
other point, which is the furthest from it. But also has a big enough height, ideally
the 2nd biggest height.
"""