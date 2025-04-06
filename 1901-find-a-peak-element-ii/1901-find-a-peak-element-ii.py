from typing import List

class Solution:
    def find_max_in_column(self, matrix: List[List[int]], column_index: int) -> int:
        """
        Finds the row index of the maximum element in a specific column.
        """
        num_rows = len(matrix)
        max_row_index = 0
        for row_index in range(num_rows):
            if matrix[row_index][column_index] > matrix[max_row_index][column_index]:
                max_row_index = row_index
        return max_row_index

    def findPeakGrid(self, matrix: List[List[int]]) -> List[int]:
        """
        Uses binary search on columns to find a peak element.
        A peak is an element that is greater than its immediate left and right neighbors.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        left_col = 0
        right_col = num_cols - 1

        while left_col <= right_col:
            mid_col = left_col + (right_col - left_col) // 2

            # Find the row with the max element in the mid column
            max_row = self.find_max_in_column(matrix, mid_col)
            current_val = matrix[max_row][mid_col]

            # Get values of the left and right neighbors
            left_neighbor = matrix[max_row][mid_col - 1] if mid_col > 0 else -1
            right_neighbor = matrix[max_row][mid_col + 1] if mid_col < num_cols - 1 else -1

            # Check if the current value is a peak
            if current_val > left_neighbor and current_val > right_neighbor:
                return [max_row, mid_col]
            elif current_val < left_neighbor:
                right_col = mid_col - 1  # Move search to the left half
            else:
                left_col = mid_col + 1   # Move search to the right half

        return [-1, -1]  # No peak found (shouldn't happen with valid input)
