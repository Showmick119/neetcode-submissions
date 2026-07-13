class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        done = False
        for a in asteroids:
            if len(stack) > 0 and stack[-1] > 0 and a < 0 and not done:
                while len(stack) > 0 and stack[-1] > 0 and a < 0 and not done:
                    if abs(a) == abs(stack[-1]):
                        stack.pop()
                        done = True
                    elif abs(a) > abs(stack[-1]):
                        stack.pop()
                        stack.append(a)
                        done = True
                    else:
                        continue
                        done = False
                        # keep what's already in the stack
                        # don't add the new element
                done = False
            else:
                stack.append(a)
        return stack