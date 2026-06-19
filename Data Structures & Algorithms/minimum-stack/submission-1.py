class MinStack:
    smallest = 100000000

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if val < smallest:
            smallest = val
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return smallest

"""
- it has to be designed in a way, such that the minimum element is always at the top of the
stack, so getMin() is really just a call to top().
"""