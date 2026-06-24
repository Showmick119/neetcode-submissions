class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(positions)):
            curr_time = (target - position[i]) / speed[i]
            position[i] = (position[i], curr_time)
        positions.sort(lambda x: x[0], reverse=True)
        stack = []
        fleet = 0
        for i in range(len(position)):
            if len(stack) > 0:
                if position[i][1] <= stack[-1]:
                    pass
                else:
                    stack.pop() # new leader
                    stack.append(position[i][1])
                    fleet += 1 # arriving at a different time
            else:
                stack.append(position[i][1])
                fleet += 1

"""
- there are n cars travelling to the same destination on a one-lane highway.
- you are given two arrays of integers position and speed.
- the destination is at position target miles.
- a car cannot pass another car ahead of it, it can only catch up to another car and then
drive at the same speed as the car ahead of it.
"""