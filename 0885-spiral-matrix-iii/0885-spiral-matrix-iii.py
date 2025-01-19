from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # Directions in order: east, south, west, north
        dirt = [[0, 1], [1, 0], [0, -1], [-1, 0]]  
        res = []
        len_move = 0  # Counter to increase the number of steps in a row/column
        d = 0  # Start with moving east (direction index: 0 - east, 1 - south, 2 - west, 3 - north)
        res.append([rStart, cStart])  # Start point
        
        while len(res) < rows * cols:
            if d == 0 or d == 2:  # When moving east or west, increase the length of the path
                len_move += 1
            
            # Move in the current direction for 'len_move' steps
            for _ in range(len_move):
                rStart += dirt[d][0]
                cStart += dirt[d][1]
                # Check if the new position is within the bounds of the matrix
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
            
            # Turn to the next direction (east -> south -> west -> north -> east...)
            d = (d + 1) % 4

        return res
