class StockSpanner:

    def __init__(self):
        self.stack = []
        self.curr_count = 0

    def next(self, price: int) -> int:
        # reset the curr counter
        self.stack.append(price)
        self.curr_count = 0
        temp = []
        while len(self.stack) > 0 and self.stack[-1] <= price:
            temp.append(self.stack.pop())
            self.curr_count += 1
        while len(temp) > 0:
            self.stack.append(temp.pop())
        return self.curr_count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

"""
- for each new price, count how many consecutive previous days, including today's, had price
<= today's price
- receive today's price and return today's span immediately
"""