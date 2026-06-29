class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x) # popping this would return the final element which was added

    def pop(self) -> int:
        # need to pop the element at the absolute front (one which was appended first)
        if len(self.outStack) > 0:
            out = self.outStack.pop()
            return out
        else:
            while len(self.inStack) > 0:
                self.outStack.append(self.inStack.pop())
            out = self.outStack.pop()
            return out

    def peek(self) -> int:
        if len(self.outStack) > 0:
            return self.outStack[-1]
        else:
            out = self.pop()
            self.outStack.append(out)
            return out

    def empty(self) -> bool:
        return len(self.inStack) == 0 and len(self.outStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
- implement a FIFO queue using only 2 stacks
- the implemented queue should support all the functions of a normal queue
- one of the stack deal with all the out elements, and the other stack deals with all the
in elements
"""