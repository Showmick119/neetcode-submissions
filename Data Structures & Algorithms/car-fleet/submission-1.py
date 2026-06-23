class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position)):
            curr_time = (target - position[i]) / speed[i]
            position[i] = (position[i], curr_time)
        position.sort(key=lambda x: x[0], reverse=True) # o(nlogn) step
        stack = []
        fleet = 0
        for i in range(len(position)):
            if len(stack) > 0:
                if position[i][1] <= stack[-1]:
                    stack.append(position[i][1])
                else:
                    while len(stack) > 0 and position[i][1] > stack[-1]:
                        stack.pop()
                    stack.append(position[i][1])
                    fleet += 1
            else:
                stack.append(position[i][1])
                fleet += 1
        return fleet