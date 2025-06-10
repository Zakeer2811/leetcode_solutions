class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7  # For modulo as required by the problem
        
        # Memoization dictionary to store intermediate results
        memo = {}

        # Recursive function to calculate number of ways
        def noofways(dice_left, target_left):
            # Base case: No dice left
            if dice_left == 0:
                # If target is also 0, it's a valid combination
                return 1 if target_left == 0 else 0
            
            # If this state has already been computed, return it
            if (dice_left, target_left) in memo:
                return memo[(dice_left, target_left)]

            # Initialize number of ways
            ways = 0

            # Try every face value from 1 to k
            for face in range(1, k + 1):
                if target_left - face >= 0:
                    # Recurse with one less die and reduced target
                    ways = (ways + noofways(dice_left - 1, target_left - face)) % MOD

            # Memoize and return result
            memo[(dice_left, target_left)] = ways
            return ways

        # Start recursion with n dice and the target sum
        return noofways(n, target)
