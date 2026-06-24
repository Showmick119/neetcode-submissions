class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position)):
            curr_time = (target - position[i]) / speed[i]
            position[i] = (position[i], curr_time)
        position.sort(key=lambda x: x[0], reverse=True)
        stack = []
        fleet = 0
        for i in range(len(position)):
            if len(stack) > 0:
                if position[i][1] <= stack[-1]:
                    pass ## if its time is less than current leader, it will join the 
                    ## fleet of the current leader and stay there. if we have an arrival
                    ## time which is greater, than we pop the current leader and make a
                    ## new leader for our new fleet
                else:
                    stack.pop() # old leader of old fleet popped
                    stack.append(position[i][1]) # new leader for new fleet appended
                    fleet += 1 # arriving at a different time, hence new fleet
            else:
                stack.append(position[i][1]) # special case of when stack empty at start
                fleet += 1
        return fleet

"""
- there are n cars travelling to the same destination on a one-lane highway.
- you are given two arrays of integers position and speed.
- the destination is at position target miles.
- a car cannot pass another car ahead of it, it can only catch up to another car and then
drive at the same speed as the car ahead of it.
"""