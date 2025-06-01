from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = r = maxlen = 0
        d = defaultdict(int)
        
        while r < len(fruits):
            d[fruits[r]] += 1
            
            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
            
            maxlen = max(maxlen, r - l + 1)
            r += 1
        
        return maxlen
