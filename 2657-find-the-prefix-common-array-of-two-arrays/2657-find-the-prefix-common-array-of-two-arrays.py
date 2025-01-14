from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        common_count = 0
        res = [0] * n
        count_a = [0] * (n + 1)
        count_b = [0] * (n + 1)
        
        for i in range(n):
            j = A[i]
            k = B[i]
            
            # Update frequency counts
            count_a[j] += 1
            count_b[k] += 1
            
            # Check if j is common
            if count_a[j] == 1 and count_b[j] == 1:
                common_count += 1
            
            # Check if k is common and different from j
            if j != k and count_a[k] == 1 and count_b[k] == 1:
                common_count += 1
            
            res[i] = common_count
        
        return res
