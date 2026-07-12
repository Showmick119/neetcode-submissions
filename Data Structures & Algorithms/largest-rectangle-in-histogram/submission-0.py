class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (index, height)
        for curr_index, curr_height in enumerate(heights):
            start_index = curr_index
            while len(stack) > 0 and stack[-1][1] > h:
                popped_index, popped_height = stack.pop()
                maxArea = max(maxArea, curr_height * (popped_index - curr_index))
                start_index = curr_index
        
        for curr_index, curr_height in stack:
            maxArea = max(maxArea, curr_height * (len(stack) - curr_index))
        
        return maxArea
        
"""
- the challenge is determining the width of the rectangle for the current bar which we are
processing
- visualize how many rectangles are formed in the given input
"""