from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        n = len(s)
        i = 0
        
        while i < n:
            # Take substring from i to i+k
            chunk = s[i:i+k]
            
            # If chunk is shorter than k, fill it
            if len(chunk) < k:
                chunk += fill * (k - len(chunk))
            
            ans.append(chunk)
            i += k
        
        return ans
