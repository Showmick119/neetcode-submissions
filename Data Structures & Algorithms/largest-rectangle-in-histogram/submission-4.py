class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        area = 0
        for index, height in enumerate(heights):
            starting_index = index
            while len(stack) > 0 and stack[-1][1] > height:
                starting_index, popped_height = stack.pop()
                area = max(area, popped_height * (index - starting_index))
            stack.append((starting_index, height))
        while len(stack) > 0:
            index, height = stack.pop()
            area = max(area, height * (len(heights) - index))
        return area

"""
- find all the potential rectangles, and then keep the max. we want to keep an ascending
order at all times, if that breaks, we pop from the stack.
- in the stack we only keep elements which can have their rectangle extended forward, and we
pop when it can no longer extend due to being too large of a value
"""