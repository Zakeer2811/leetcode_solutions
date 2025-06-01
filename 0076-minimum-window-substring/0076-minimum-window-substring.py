from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=='':return ""
        # Frequency maps for characters in t and the current window in s
        tmap = defaultdict(int)  # Target character frequencies from t
        smap = defaultdict(int)  # Current window character frequencies in s
        
        # Initialize target frequency map (tmap) from string t
        for char in t:
            tmap[char] += 1
        
        # Variables to track the current window and the minimum window
        minlen = float('inf')  # Start with an infinitely large window
        ind = [-1, -1]  # To store the start and end index of the minimum window
        have = 0  # Number of characters from t that we have matched in the window
        needed = len(tmap)  # Number of unique characters in t
        
        l = 0  # Left pointer of the window

        # Iterate through the string s with right pointer (r)
        for r in range(len(s)):
            ch = s[r]
            smap[ch] += 1  # Increase the count of the current character in the window
            
            # If the current character matches the count in t, increment the 'have' counter
            if ch in tmap and smap[ch] == tmap[ch]:
                have += 1
            
            # Once the window contains all the characters from t, try to shrink it
            while have == needed:
                # Check if the current window is the smallest we've found so far
                len1 = r - l + 1
                if minlen > len1:
                    minlen = len1
                    ind = [l, r]  # Store the indices of the current valid window
                
                # Move the left pointer (l) to shrink the window
                smap[s[l]] -= 1  # Remove the character at position l from the window
                if smap[s[l]] == 0:
                    del smap[s[l]]  # Remove the character from the map if its count is zero
                
                # If we removed a character that was in t and its count dropped below what's needed
                if s[l] in tmap and smap[s[l]] < tmap[s[l]]:
                    have -= 1  # Decrease the 'have' counter because we no longer have enough of that character
                
                # Move the left pointer forward to shrink the window
                l += 1
        
        # If a valid window was found, return the substring, otherwise return an empty string
        if minlen == float('inf'):
            return ""
        return s[ind[0]: ind[1] + 1]
