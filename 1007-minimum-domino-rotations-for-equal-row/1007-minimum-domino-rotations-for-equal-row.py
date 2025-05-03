from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Helper function to check if it's possible to make all values equal to target
        def check(target: int) -> int:
            top_rotations = bottom_rotations = 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return -1  # Impossible to make both sides the same
                if tops[i] != target:
                    top_rotations += 1
                if bottoms[i] != target:
                    bottom_rotations += 1
            return min(top_rotations, bottom_rotations)
        
        # Try making all values equal to tops[0] or bottoms[0]
        rotations = check(tops[0])
        if rotations != -1:
            return rotations
        
        rotations = check(bottoms[0])
        return rotations
