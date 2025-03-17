from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                d[i] = d.get(i) + 1
            else:
                d[i] = 1
        l = []
        for v in d.values():
            if v % 2 != 0:  
                l.append(False)
        return len(l) == 0 
