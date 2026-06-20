class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if len(stack) > 0:
                if (stack[-1] > 0 and asteroids[i] > 0) or (stack[-1] < 0 and asteroids[i] < 0):
                    stack.append(asteroids[i])
                else:
                    if abs(stack[-1]) == abs(asteroids[i]):
                        stack.pop()
                    elif abs(stack[-1]) < abs(asteroids[i]):
                        stack.pop()
                        stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])
        if len(stack) == 2:
            if (stack[-1] > 0 and stack[-2] < 0) or (stack[-1] < 0 and stack[-2] > 0):
                if abs(stack[-1]) > abs(stack[-2]):
                    temp = stack.pop()
                    stack.pop()
                    stack.append(temp)
                else:
                    stack.pop()
        return stack

"""
- approach it kind of like valid parentheses, where you push and pop and cancel out as you go.
- you are just doing the 1 v 1 and then forgetting about it. you have to keep propagating and
doing the 1 v 1.
"""