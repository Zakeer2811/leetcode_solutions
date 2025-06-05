from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c = 0
        i = j = 0  # Index for greed factors and cookie sizes

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                c += 1
                i += 1
            j += 1

        return c
