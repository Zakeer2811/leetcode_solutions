class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if there's only one row, return the string as it is
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize rows for the zigzag pattern
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Loop through the string and fill the rows in the zigzag pattern
        for char in s:
            rows[current_row] += char
            
            # If we reach the top or bottom, we need to reverse direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row depending on the direction
            current_row += 1 if going_down else -1
        
        # Concatenate all rows to form the final result
        return ''.join(rows)
