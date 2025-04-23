class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        max_count = 0
        for i in range(1, n + 1):
            s = sum(int(digit) for digit in str(i))
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
            
            max_count = max(max_count, d[s])
                
        ans = sum(1 for count in d.values() if count == max_count)
        
        return ans