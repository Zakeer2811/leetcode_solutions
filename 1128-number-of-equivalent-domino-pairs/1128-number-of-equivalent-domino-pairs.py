class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        from collections import defaultdict


        # Dictionary to store frequency of each canonical domino pair
        freq = defaultdict(int)
        count = 0
        
        for a, b in dominoes:
            # Normalize the domino pair by making sure the smaller number is first
            domino = (min(a, b), max(a, b))
            
            # For the current domino, add how many times it's been seen before
            count += freq[domino]
            
            # Increment the frequency of the current domino
            freq[domino] += 1
        
        return count
