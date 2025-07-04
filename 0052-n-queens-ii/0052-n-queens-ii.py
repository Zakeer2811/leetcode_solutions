from typing import List

class Solution:
    def totalNQueens(self, n: int) -> int:
        # Initialize the chessboard as an n x n grid with all cells empty (False)
        chessboard = [[False] * n for _ in range(n)]
        solution_count = 0  # This will store the total number of valid arrangements

        def is_position_safe(chessboard, current_row, current_col):
            """
            Check if it's safe to place a queen at (current_row, current_col).
            A queen can attack in 3 directions: 
            - vertically upward (↑)
            - upper-left diagonal (↖)
            - upper-right diagonal (↗)

            Diagonal movement explanations:

            ↖ Upper-left diagonal (row - i, col - i):
                - We move up and to the left from (row, col)
                - We must stop if:
                    row - i < 0  or  col - i < 0  → out of bounds
                - So the maximum number of safe diagonal steps is:
                    max_steps = min(row, col)

            ↗ Upper-right diagonal (row - i, col + i):
                - We move up and to the right from (row, col)
                - We must stop if:
                    row - i < 0  or  col + i >= n  → out of bounds
                - So the maximum number of safe diagonal steps is:
                    max_steps = min(row, n - col - 1)
            """

            # Check vertically upward (same column)
            for r in range(current_row):
                if chessboard[r][current_col]:
                    return False

            # ↖ Check upper-left diagonal
            max_steps_left = min(current_row, current_col)
            for step in range(1, max_steps_left + 1):
                if chessboard[current_row - step][current_col - step]:
                    return False

            # ↗ Check upper-right diagonal
            max_steps_right = min(current_row, len(chessboard) - current_col - 1)
            for step in range(1, max_steps_right + 1):
                if chessboard[current_row - step][current_col + step]:
                    return False

            return True


        def place_queens(chessboard, row):
            """
            Try to place queens from the current row to the end using backtracking.
            Instead of storing valid boards, we just count them.
            """
            nonlocal solution_count

            if row == n:
                # All queens are placed successfully; increment the count
                solution_count += 1
                return

            # Try placing a queen in each column of the current row
            for col in range(n):
                if is_position_safe(chessboard, row, col):
                    # Place queen
                    chessboard[row][col] = True
                    # Move to the next row
                    place_queens(chessboard, row + 1)
                    # Backtrack: remove the queen
                    chessboard[row][col] = False

        # Start the backtracking from the first row
        place_queens(chessboard, 0)

        return solution_count
