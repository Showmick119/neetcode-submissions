class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        stack.append(asteroids[0])
        i = 1
        while i < len(asteroids):
            while ((stack[-1] > 0 and asteroids[i] < 0) or (stack[-1] < 0 and asteroids[i] > 0)):
                # WHILE A COLLISION IS STILL POSSIBLE
                # IF NOT POSSIBLE, YOU HAVE YOUR ANSWER
                if abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                elif abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                    stack.append(asteroids[i])
                else:
                    pass
            i += 1
        return stack

"""
- approach it kind of like valid parentheses, where you push and pop and cancel out as you go.
- you are just doing the 1 v 1 and then forgetting about it. you have to keep propagating and
doing the 1 v 1.
- don't think if collision possible. think WHILE collision possible;
"""