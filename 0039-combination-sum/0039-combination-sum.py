from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def recursion(ind, ds, target):
            if ind == len(candidates):
                if target == 0:
                    ans.append(ds[:])  # Use ds[:] to append a copy of ds
                return
            
            if candidates[ind] <= target:
                # Pick condition
                ds.append(candidates[ind])
                recursion(ind, ds, target - candidates[ind])
                ds.pop()
            
            # Not pick condition
            recursion(ind + 1, ds, target)
        
        recursion(0, [], target)
        return ans
