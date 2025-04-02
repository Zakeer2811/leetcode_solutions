class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0  # No transactions can be made
    
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)  # Track lowest price seen so far
            max_profit = max(max_profit, price - min_price)  # Maximize profit

        return max_profit
