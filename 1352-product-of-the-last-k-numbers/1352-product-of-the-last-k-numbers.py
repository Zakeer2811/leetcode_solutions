class ProductOfNumbers:
    def __init__(self):
        self.A = [1]  # Initialize the list with 1 to handle the first product multiplication.

    def add(self, a):
        if a == 0:
            self.A = [1]  # Reset the list if we encounter a 0.
        else:
            self.A.append(self.A[-1] * a)  # Store the cumulative product.

    def getProduct(self, k):
        if len(self.A) <= k:  # If there are fewer than k elements, return 0 (because of a 0 in the product sequence).
            return 0
        return self.A[-1] // self.A[-k - 1]  # Integer division to get the product of the last k elements.
