class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span = 1

    def next(self, price: int) -> int:
        self.span = 1
        if len(self.stack) < 1:
            self.stack.append((price, 1))
            return 1
        while len(self.stack) > 0 and self.stack[-1][0] <= price:
            self.span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, self.span))
        return self.span
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

"""
- for each new price, count how many consecutive previous days, including today's, had price
<= today's price
- receive today's price and return today's span immediately
- each pair gets pushed once and popped once, hence o(1) ammortized per call
"""