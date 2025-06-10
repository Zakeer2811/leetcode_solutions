from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        c = list(Counter(s).values())
        print(c)
        even_freqs = [x for x in c if x % 2 == 0]
        odd_freqs = [x for x in c if x % 2 == 1]
        print(even_freqs)
        print(odd_freqs)
        if not even_freqs or not odd_freqs:
            return -1  # or raise an Exception, or handle edge case as needed

        return max(odd_freqs) - min(even_freqs)
