from collections import Counter, defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        l = have = 0
        c = Counter(p)
        need = len(c)
        d = defaultdict(int)

        for r in range(len(s)):
            ch = s[r]
            d[ch] += 1
            if ch in c and d[ch] == c[ch]:
                have += 1
            while have == need:
                if r - l + 1 == len(p):  # only add if window size matches p
                    ans.append(l)
                d[s[l]] -= 1
                if s[l] in c and d[s[l]] < c[s[l]]:
                    have -= 1
                l += 1
        return ans
