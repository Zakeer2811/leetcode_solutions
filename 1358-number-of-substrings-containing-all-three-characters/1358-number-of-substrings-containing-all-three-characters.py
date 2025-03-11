class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        count = 0
        char_count = defaultdict(int)
        i = 0
        
        for j in range(n):
            # Add the current character to the window
            char_count[s[j]] += 1
            
            # Shrink the window from the left if it contains all three characters
            while len(char_count) == 3:  # the window contains 'a', 'b', 'c'
                # All substrings starting from i to j are valid
                count += (n - j)
                # Try to shrink the window from the left
                char_count[s[i]] -= 1
                if char_count[s[i]] == 0:
                    del char_count[s[i]]
                i += 1
        
        return count
