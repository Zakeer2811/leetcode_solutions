class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        # if n < 3:
        #     return 0
        index = {v: i for i, v in enumerate(arr)}
        dp = [[2] * n for _ in range(n)]
        max_len = 0
        for j in range(n):
            for i in range(j):
                target = arr[j] - arr[i]
                if target in index and index[target] < i:
                    k = index[target]
                    dp[i][j] = dp[k][i] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
        return max_len if max_len >= 3 else 0
        