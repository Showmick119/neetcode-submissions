class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1
        curr = 0
        idx, biggest = max(enumerate(heights), key=lambda x: x[1])
        
        for i in range(len(heights)):
            curr = min(heights[i], biggest) * abs(i - idx)
            if curr > area:
                area = curr

        # while l < r:
        #     curr = min(heights[l], heights[r]) * (r - l)
        #     if curr > area:
        #         area = curr
        #     l += 1
        #     r -= 1
        return area


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