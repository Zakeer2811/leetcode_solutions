class StockSpanner:

    def __init__(self):
        # Stack will store pairs of (price, index)
        self.stack = []
        self.ind = -1  # Keeps track of the current day/index

    def next(self, price: int) -> int:
        self.ind += 1  # Move to next day/index

        # Remove all prices from the stack that are less than or equal to current price
        # These prices cannot act as barriers to the span
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        # If stack is empty, it means this price is greater than all previous -> span = ind + 1
        # Else, span = difference between current index and last higher price's index
        if not self.stack:
            span = self.ind + 1
        else:
            span = self.ind - self.stack[-1][1]

        # Push current price and index onto the stack
        self.stack.append([price, self.ind])

        return span
