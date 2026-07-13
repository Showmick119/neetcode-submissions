class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        temp = []
        count = 0
        self.stack.append(price)
        while len(self.stack) > 0 and self.stack[-1] <= price:
            count += 1
            temp.append(self.stack.pop())
        while len(temp) > 0:
            self.stack.append(temp.pop())
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