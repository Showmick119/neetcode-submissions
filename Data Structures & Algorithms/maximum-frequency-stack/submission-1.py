class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = {}

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        self.stack.append((val, self.freq[val]))
        self.stack.sort(key=lambda x: x[1])

    def pop(self) -> int:
        curr = self.stack.pop()
        return curr[0]


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

"""
- naive solution is easy, solve it naively first, and then worry about optimality
"""