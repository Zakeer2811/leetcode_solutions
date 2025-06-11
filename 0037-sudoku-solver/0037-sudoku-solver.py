class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Modify board in-place to solve the Sudoku puzzle.
        The board is a 9x9 grid filled with digits '1' to '9' and '.' for empty cells.
        """

        def isSafe(row: int, col: int, num: str) -> bool:
            """
            Checks if placing 'num' at board[row][col] is valid
            according to Sudoku rules:
            - 'num' must not appear in the same row
            - 'num' must not appear in the same column
            - 'num' must not appear in the same 3x3 sub-grid
            """
            # ✅ Check the current row
            for c in range(9):
                if board[row][c] == num:
                    return False

            # ✅ Check the current column
            for r in range(9):
                if board[r][col] == num:
                    return False

            # ✅ Check the 3x3 sub-grid that contains (row, col)
            # We compute the starting row and column of the box
            # For example: if row = 5, col = 7 → box starts at (3, 6)
            # Calculate the starting indices (top-left corner) of the 3x3 box
            # Every cell (row, col) belongs to one of the 9 sub-boxes.
            # For any given cell, to find its 3x3 sub-grid:
            #   - The rows in that box start from: row - (row % 3)
            #   - The cols in that box start from: col - (col % 3)
            #
            # Example:
            # If row = 5, col = 7:
            #   - row_start = 5 - (5 % 3) = 3
            #   - col_start = 7 - (7 % 3) = 6
            # So the 3x3 box spans from (3,6) to (5,8)

            box_start_row = row - row % 3
            box_start_col = col - col % 3

            # Now we check each of the 9 cells in the 3x3 box.
            # Each 3x3 box has 3 rows and 3 columns, so we use range(start, start + 3)
            # This gives us exactly 3 values: start, start+1, and start+2
            #
            # For example:
            #     range(3, 6) gives [3, 4, 5]
            # This ensures we only scan the cells within the 3x3 grid.
            #
            # Why +3?
            # Because each box is 3 rows x 3 cols,
            # and Python's range is exclusive at the end (range(a, b) includes a, excludes b).
            # So range(start, start + 3) covers 3 rows and 3 columns as required.
           

            # We need to check all 9 cells in this 3x3 box
            # So we go from (box_start_row, box_start_col) to (box_start_row+2, box_start_col+2)
            # That's why we use range(start, start + 3)
            for r in range(box_start_row, box_start_row + 3):
                for c in range(box_start_col, box_start_col + 3):
                    if board[r][c] == num:
                        return False

            # If the number is not found in row, column, or 3x3 box, it's safe to place
            return True

        def solve() -> bool:
            """
            Recursive backtracking function to fill the board.
            Tries to place a valid digit in each empty cell ('.') one by one.
            If a dead end is reached, it backtracks and tries the next possibility.
            Returns True if the board is successfully filled.
            """
            # Traverse each cell of the board
            for row in range(9):
                for col in range(9):
                    # Look for an empty cell
                    if board[row][col] == '.':
                        # Try all digits from '1' to '9'
                        for digit in map(str, range(1, 10)):
                            if isSafe(row, col, digit):
                                # Place the digit if it's safe
                                board[row][col] = digit
                                # Recursively try to solve the rest of the board
                                if solve():
                                    return True
                                # If the current choice doesn't lead to a solution, backtrack
                                board[row][col] = '.'
                        # If no digit can be placed in this cell, return False (trigger backtracking)
                        return False
            # If the loop completes, all cells are filled correctly
            return True

        # Start the recursive solver
        solve()
