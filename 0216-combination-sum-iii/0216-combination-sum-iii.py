from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(start: int, path: List[int], target: int):
            # If the combination is done and sums to target, add to results
            if len(path) == k and target == 0:
                res.append(path[:])
                return
            
            # If the combination is too long or sum exceeded, stop
            if len(path) > k or target < 0:
                return
            
            # Try numbers from start to 9
            for num in range(start, 10):
                path.append(num)
                backtrack(num + 1, path, target - num)
                path.pop()  # backtrack
        
        backtrack(1, [], n)
        return res
