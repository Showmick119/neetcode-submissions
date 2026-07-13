class StockSpanner:

    def __init__(self):
        self.stack1 = []
        self.stack2 = [] # WE WILL NOT POP FROM THIS! IT WILL ALWAYS HOLD EVERYTHING

    def next(self, price: int) -> int:
        count = 0 # reset to zero each time the method is called
        self.stack2.append(price)

        self.stack1 = self.stack2
        while len(self.stack1) > 0 and self.stack1[-1] <= price:
            count += 1
            self.stack1.pop()
        self.stack1 = self.stack2
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

"""
- the span of the stock's price in one day is the maximum number of consecutive days,
starting from that day and going backward, for which the stock price was less than or equal
to the price of that day.
- target time and space complexity is o(n).
"""