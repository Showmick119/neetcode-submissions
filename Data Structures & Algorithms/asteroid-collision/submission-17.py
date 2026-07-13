class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while len(stack) > 0 and stack[-1] > 0 and a < 0:
                if abs(a) == abs(stack[-1]):
                    stack.pop()
                elif abs(a) > abs(stack[-1]):
                    stack.pop()
                    stack.append(a)
                else:
                    continue
                    '''
                    - keep what's already in the stack
                    - don't add the new element
                    '''
            else:
                stack.append(a)
        return stack