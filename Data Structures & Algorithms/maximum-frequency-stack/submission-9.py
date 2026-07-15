class FreqStack:

    def __init__(self):
        self.freqMap = {}
        self.stackMap = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        if val in self.freqMap:
            self.freqMap[val] += 1
        else:
            self.freqMap[val] = 1
        if self.freqMap[val] in self.stackMap:
            self.stackMap[self.freqMap[val]].append(val)
        else:
            self.stackMap[self.freqMap[val]] = []
            self.stackMap[self.freqMap[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.freqMap[val])

    def pop(self) -> int:
        out = 0
        if self.maxFreq in self.stackMap and len(self.stackMap[self.maxFreq]) > 0:
            out = self.stackMap[self.maxFreq].pop()
            self.freqMap[out] -= 1
            if len(self.stackMap[self.maxFreq]) == 0:
                del self.stackMap[self.maxFreq]
                self.maxFreq -= 1
        return out 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

"""
- it doesn't necessarily have to be a stack of stacks. get used to using 2 data structures.
- we can have two hashmaps, one to store frequencies and another to store the stacks!
- we can't create stacks of stacks since we don't know exactly how many elements will be
pushed in. it can be a maximum of 20,000.
"""