from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        n = len(s)
        l = r = maxlen = 0  # Initialize left pointer, right pointer, and maxlen
        
        while r < n:
            # Update the count of the current character
            d[s[r]] += 1
            
            # Calculate the maximum frequency of any character in the window
            maxfreq = max(d.values())
            
            # If the current window size minus the max frequency is greater than k
            if r - l + 1 - maxfreq > k:
                # Shrink the window from the left
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
            
            # Update maxlen with the largest window size where the condition holds
            maxlen = max(maxlen, r - l + 1)
            
            # Move the right pointer to expand the window
            r += 1
        
        return maxlen
