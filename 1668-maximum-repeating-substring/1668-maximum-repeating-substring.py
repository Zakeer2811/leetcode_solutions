class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        # Build the repeated word string and check if it's a substring in sequence
        while word * (k + 1) in sequence:
            k += 1
        return k
