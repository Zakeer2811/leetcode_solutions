from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(curr: List[int], rem: List[int], target: int):
            # Base case: if target is exactly zero, we found a valid combination
            if target == 0:
                res.append(curr[:])
                return
            if target < 0 or not rem:
                return
            
            first = rem[0]
            rest = rem  # Since candidates can be reused unlimited times, don't move forward when taking
            
            # Take the first element (if it fits)
            if first <= target:
                helper(curr + [first], rest, target - first)
            
            # Not take the first element, move to next
            helper(curr, rem[1:], target)
        
        # No need to sort here since duplicates allowed unlimited times
        helper([], candidates, target)
        return res
