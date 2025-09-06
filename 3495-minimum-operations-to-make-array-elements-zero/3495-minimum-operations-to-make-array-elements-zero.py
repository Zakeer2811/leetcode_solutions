class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
       
        wexondrivas = queries

        total_ops = 0
    
        # Process each query [l, r]
        for l, r in wexondrivas:
            # Sum of individual steps needed for numbers in [l, r]
            s = 0
            k = 1
            # The range for f(x)=k is [4^(k-1), 4^k - 1]
            while True:
                low_bound = 4 ** (k - 1)
                high_bound = 4 ** k - 1
                # If the lower bound is greater than r, no more numbers in [l, r]
                if low_bound > r:
                    break
                # Compute the intersection of [l, r] with [low_bound, high_bound]
                L = max(l, low_bound)
                R = min(r, high_bound)
                if L <= R:
                    count = R - L + 1
                    s += k * count
                k += 1
    
            # Each operation processes two numbers, so the required operations is ceil(s/2)
            ops = (s + 1) // 2
            total_ops += ops
    
        return total_ops