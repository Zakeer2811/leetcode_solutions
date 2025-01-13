class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0] * 26  # Frequency array for each letter in the alphabet
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        result = 0
        for f in freq:
            if f > 0:
                result += 2 if f % 2 == 0 else 1  # Add 2 for even frequencies, 1 for odd frequencies
        
        return result
