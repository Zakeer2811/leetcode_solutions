class Solution:
    
    def countOfSubstrings(self,word, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        
        # Precompute the consonant prefix sum array
        consonant_prefix = [0] * (n + 1)
        for i in range(n):
            consonant_prefix[i + 1] = consonant_prefix[i] + (0 if word[i] in vowels else 1)
        
        # Sliding window to find minimal end for each left
        min_r = [n + 1] * n  # Initialize to an invalid value
        from collections import defaultdict
        counts = defaultdict(int)
        formed = 0
        left = 0
        for right in range(n):
            c = word[right]
            if c in vowels:
                counts[c] += 1
                if counts[c] == 1:
                    formed += 1
            # Shrink the window as long as all vowels are present
            while formed == 5:
                current_min = right + 1  # The end is exclusive, so window is [left, current_min)
                min_r[left] = current_min
                # Remove the left character from the window
                c_left = word[left]
                if c_left in vowels:
                    counts[c_left] -= 1
                    if counts[c_left] == 0:
                        formed -= 1
                left += 1
        
        result = 0
        # For each left, find valid end indices
        for left in range(n):
            r_l = min_r[left]
            if r_l > n:
                continue
            target = consonant_prefix[left] + k
            # Find the first occurrence of target >= r_l
            left_idx = bisect.bisect_left(consonant_prefix, target, r_l, n + 1)
            if left_idx > n:
                continue
            if consonant_prefix[left_idx] != target:
                continue
            # Find the last occurrence of target in the prefix array
            right_idx = bisect.bisect_right(consonant_prefix, target, left_idx, n + 1) - 1
            if right_idx < left_idx:
                continue
            result += right_idx - left_idx + 1
        return result