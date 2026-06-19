class MinStack:

    def __init__(self):
        self.stack = []
        from collections import deque
        self.small = deque()
        self.smallest = 100000000

    def push(self, val: int) -> None:
        if val <= self.smallest:
            self.smallest = val
            self.small.appendleft(val)
        else:
            self.small.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.top() == self.small[0]:
            self.small.popleft()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.small[0]

"""
- it has to be designed in a way, such that the minimum element is always at the top of the
stack, so getMin() is really just a call to top().
"""