from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = [item for sublist in grid for item in sublist]
        c = Counter(l)
        l1 = []
        
        repeated_value = None
        for k, v in c.items():
            if v == 2:
                repeated_value = k
                break
                
        n = len(l)
        total_sum = sum(sum(row) for row in grid)
        expected_sum = n * (n + 1) // 2
        missing_value = expected_sum - total_sum + repeated_value
        
        
        l1.append(repeated_value)
        l1.append(missing_value)
        return l1
