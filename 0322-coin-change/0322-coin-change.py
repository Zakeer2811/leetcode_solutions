class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # min_coins[target] = minimum number of coins needed to make 'target'
        min_coins = [float('inf')] * (amount + 1)
        min_coins[0] = 0  # Base case: 0 amount needs 0 coins

        for coin_value in coins:
            # Try to build all targets from coin_value → amount
            for target in range(coin_value, amount + 1):

                # Explanation:
                # We have two choices to form 'target':
                #
                # 1) Do NOT use the current coin:
                #       → existing min_coins[target]
                #
                # 2) USE the current coin:
                #       → 1 coin (coin_value) 
                #       + the best way to form (target - coin_value)
                #
                # So the new candidate is:
                #       min_coins[target - coin_value] + 1
                #
                # We want the **minimum number of coins**, so take the min.
                #
                min_coins[target] = min(
                    min_coins[target],                      # old best solution
                    min_coins[target - coin_value] + 1       # new solution using this coin
                )

        # If amount is unreachable, return -1
        return min_coins[amount] if min_coins[amount] != float('inf') else -1
