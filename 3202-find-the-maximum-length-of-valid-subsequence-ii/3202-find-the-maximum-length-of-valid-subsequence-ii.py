from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        
        for num in nums:
            r = num % k
            # Instead of copying the whole matrix, just compute updates in a list and apply them
            updates = [0] * k
            for a in range(k):
                updates[a] = dp[r][a] + 1
            for a in range(k):
                dp[a][r] = max(dp[a][r], updates[a])
        
        return max(max(row) for row in dp)
