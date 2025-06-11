class Solution:
    def myPow(self,x: float, n: int) -> float:
        # Helper function to perform fast exponentiation using recursion
        def helper(x: float, n: int) -> float:
            # Base case: anything raised to the power 0 is 1
            if n == 0:
                return 1
            
            # If n is even, we can reduce the problem by squaring x and halving n
            # This reduces the number of multiplications: x^n = (x*x)^(n/2)
            if n % 2 == 0:
                return helper(x * x, n // 2)
            else:
                # If n is odd, we reduce it to an even problem:
                # x^n = x * x^(n-1), and now (n-1) is even
                return x * helper(x * x, n // 2)
        
        # Handle negative powers: x^(-n) = 1 / (x^n)
        if n < 0:
            # Convert x to 1/x and n to -n to make the exponent positive
            return 1 / helper(x, -n)
        else:
            # For non-negative n, just compute directly
            return helper(x, n)
