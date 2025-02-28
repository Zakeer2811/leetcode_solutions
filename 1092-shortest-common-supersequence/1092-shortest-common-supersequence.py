class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        def longest_common_subsequence(s1, s2):
            m, n = len(s1), len(s2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            # Reconstruct LCS
            i, j = m, n
            lcs = []
            while i > 0 and j > 0:
                if s1[i-1] == s2[j-1]:
                    lcs.append(s1[i-1])
                    i -= 1
                    j -= 1
                else:
                    if dp[i-1][j] > dp[i][j-1]:
                        i -= 1
                    else:
                        j -= 1
            return ''.join(reversed(lcs))
        
        lcs = longest_common_subsequence(str1, str2)
        if not lcs:
            return str1 + str2
        
        # Find positions of LCS characters in str1 and str2
        pos1 = []
        i = 0
        for c in lcs:
            idx = str1.find(c, i)
            pos1.append(idx)
            i = idx + 1
        
        pos2 = []
        j = 0
        for c in lcs:
            idx = str2.find(c, j)
            pos2.append(idx)
            j = idx + 1
        
        # Build the shortest common supersequence
        res = []
        i, j = 0, 0
        for k in range(len(lcs)):
            c = lcs[k]
            x, y = pos1[k], pos2[k]
            res.append(str1[i:x])
            res.append(str2[j:y])
            res.append(c)
            i = x + 1
            j = y + 1
        
        # Add remaining parts of str1 and str2
        res.append(str1[i:])
        res.append(str2[j:])
        
        return ''.join(res)
        # m, n = len(str1), len(str2)
        # # dp[i][j] will hold the LCS of str1[:i] and str2[:j]
        # dp = [["" for _ in range(n+1)] for _ in range(m+1)]
        
        # for i in range(m):
        #     for j in range(n):
        #         if str1[i] == str2[j]:
        #             dp[i+1][j+1] = dp[i][j] + str1[i]
        #         else:
        #             # Choose the longer LCS between dp[i][j+1] and dp[i+1][j]
        #             dp[i+1][j+1] = dp[i][j+1] if len(dp[i][j+1]) > len(dp[i+1][j]) else dp[i+1][j]
        
        # # The LCS of str1 and str2 is now in dp[m][n]
        # lcs = dp[m][n]
        
        # # Build the result by merging str1 and str2 using the LCS
        # res = []
        # i, j = 0, 0
        # for char in lcs:
        #     # Append non-LCS characters from str1
        #     while str1[i] != char:
        #         res.append(str1[i])
        #         i += 1
        #     # Append non-LCS characters from str2
        #     while str2[j] != char:
        #         res.append(str2[j])
        #         j += 1
        #     # Append the LCS character and move both pointers
        #     res.append(char)
        #     i += 1
        #     j += 1
            
        # # Append any remaining characters from both strings
        # res.append(str1[i:])
        # res.append(str2[j:])
        
        # return "".join(res)