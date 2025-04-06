from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = 0
        max_row_index = 0
        for i, row in enumerate(mat):
            ones_in_row = sum(row)
            if ones_in_row > max_ones:
                max_ones = ones_in_row
                max_row_index = i
        return [max_row_index, max_ones]
