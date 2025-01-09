class Solution:
    def prefixCount(self, words, pref):
        count = 0
        preflen = len(pref)  # Step 1: calculate the length of "pref"
        
        for word in words:  # Iterate through each word in "words"
            if word[:preflen] == pref:  # Step 2: check if the substring matches "pref"
                count += 1  # Increment count if there's a match
        
        return count  # Return the total count
