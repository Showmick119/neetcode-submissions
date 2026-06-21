class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # stores all the indices
        stack.append(0)
        result = [0] * len(temperatures)
        for curr_idx in range(1, len(temperatures), 1):
            while len(stack) > 0 and temperatures[curr_idx] > temperatures[stack[-1]]:
                result[stack[-1]] = curr_idx - stack[-1]
                stack.pop()
            stack.append(curr_idx)
        return result

"""
- store indices, not temperatures
- stack stores the days/indices which are still waiting for a future warmer day
- keep CONTINUOUSLY POPPING while current temp CAN solve previous colder days
- when current temp is warmer than current stack top, result[old_idx] = curr_idx - old_idx
- old_idx would come from the stack itself. the stack stores the indices of the days that are
still waiting for a warmer day
- old_index = stack[-1]
"""