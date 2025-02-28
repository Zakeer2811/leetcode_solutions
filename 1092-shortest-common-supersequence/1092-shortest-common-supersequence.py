class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        # dp[i][j] will hold the LCS of str1[:i] and str2[:j]
        dp = [["" for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = dp[i][j] + str1[i]
                else:
                    # Choose the longer LCS between dp[i][j+1] and dp[i+1][j]
                    dp[i+1][j+1] = dp[i][j+1] if len(dp[i][j+1]) > len(dp[i+1][j]) else dp[i+1][j]
        
        # The LCS of str1 and str2 is now in dp[m][n]
        lcs = dp[m][n]
        
        # Build the result by merging str1 and str2 using the LCS
        res = []
        i, j = 0, 0
        for char in lcs:
            # Append non-LCS characters from str1
            while str1[i] != char:
                res.append(str1[i])
                i += 1
            # Append non-LCS characters from str2
            while str2[j] != char:
                res.append(str2[j])
                j += 1
            # Append the LCS character and move both pointers
            res.append(char)
            i += 1
            j += 1
            
        # Append any remaining characters from both strings
        res.append(str1[i:])
        res.append(str2[j:])
        
        return "".join(res)