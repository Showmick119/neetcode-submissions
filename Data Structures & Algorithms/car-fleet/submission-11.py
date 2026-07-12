class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        work = [(0, 0)] * len(position)
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            work[i] = (position[i], time)
        work.sort(key = lambda x : x[0], reverse = True)
        stack = []
        stack.append(work[0][1])
        leader = work[0][1]
        i = 1
        fleet = 1
        while i < len(position) and len(stack) > 0:
            if work[i][1] <= leader:
                stack.append(work[i][1])
            else:
                leader = work[i][1]
                while len(stack) > 0:
                    stack.pop()
                stack.append(leader)
                fleet += 1
            i += 1
        return fleet