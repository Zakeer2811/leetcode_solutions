from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def find_subs(ds, i, arr, ans):
            # Add the current subset (including the empty subset)
            ans.append(ds[:])
            
            for j in range(i, len(arr)):
                # Skip duplicates
                if j > i and arr[j] == arr[j - 1]:
                    continue
                
                # Include arr[j] in the subset
                ds.append(arr[j])
                find_subs(ds, j + 1, arr, ans)
                ds.pop()  # Remove arr[j] from subset
        
        arr = sorted(nums)  # Sort to handle duplicates
        ans = []
        find_subs([], 0, arr, ans)
        return ans
