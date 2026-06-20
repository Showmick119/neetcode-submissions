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
        return stack

"""
- approach it kind of like valid parentheses, where you push and pop and cancel out as you go
"""