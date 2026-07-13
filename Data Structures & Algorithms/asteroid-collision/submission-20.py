class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        add = False # this rating will be based on the most recent collision it does
        # considering all fall throughs
        for a in asteroids:
            if len(stack) > 0 and stack[-1] > 0 and a < 0:
                while len(stack) > 0 and stack[-1] > 0 and a < 0:
                    if abs(a) == abs(stack[-1]):
                        stack.pop()
                        add = False
                        break
                    elif abs(a) > abs(stack[-1]):
                        stack.pop()
                        add = True
                    else:
                        add = False
                        break
                if add:
                    stack.append(a)
                    add = False
            else:
                stack.append(a)
        return stack