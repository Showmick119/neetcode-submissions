class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        stack.append(asteroids[0])
        i = 1
        # WHILE COLLISION HAPPENS
        while i < len(asteroids):
            append = True # if no collision happens, append stays true and asteroid added
            while len(stack) > 0 and (stack[-1] > 0 and asteroids[i] < 0):
                if abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    append = False
                    break
                elif abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                    append = True
                else:
                    append = False
                    # no current asteroid left to collide with anything else inside, stop
                    break
            if append:
                stack.append(asteroids[i])
            i += 1
        return stack

"""
- you are given an array representing asteroids in a row. the indicies of the asteroids
represent their relative position in space.
- for each asteroid, the absolute value represents its size, and the sign represents its
direction (positive meaning right side and negative meaning left side).
- each asteroid moves at the same speed.
- find the state of the asteroids after all collisions. if two asteroids meet, the smaller
one will explode. if both are the same size, both will explode. two asteroids moving in the
same direction or opposite direction, will never meet.
- keep going till current asteroid can keep breaking the asteroids in the stack. when it can
no longer break the asteroids in the stack, and itself gets broken. then u stop, as the
colisions are done and over for this specific current asteroid, as it can no longer collide
with and break the asteroids in the stack. so move to the next asteroid and see if it can
break the asteroids in the stack.
"""