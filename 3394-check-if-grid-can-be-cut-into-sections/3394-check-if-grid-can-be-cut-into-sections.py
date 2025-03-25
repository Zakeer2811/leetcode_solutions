from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        return self.can_cut(rectangles, 0) or self.can_cut(rectangles, 1)

    def can_cut(self, rectangles: List[List[int]], axis: int) -> bool:
        rectangles.sort(key=lambda x: x[axis])
        cuts, previous_end = 0, -1

        for rect in rectangles:
            start, end = rect[axis], rect[axis + 2]

            if start >= previous_end:
                cuts += 1
            previous_end = max(previous_end, end)
            
            if cuts >= 3:
                return True

        return False