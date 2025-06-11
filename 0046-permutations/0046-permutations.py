from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(ind: int):
            # Base case: If we've fixed all positions, store a copy of the permutation
            if ind == len(nums):
                res.append(nums[:])
                return

            # Try placing each number at the current index `ind`
            for i in range(ind, len(nums)):
                # Swap current index with i to fix nums[i] at index ind
                nums[ind], nums[i] = nums[i], nums[ind]
                helper(ind + 1)  # Recurse for the rest of the list
                nums[ind], nums[i] = nums[i], nums[ind]  # Backtrack to restore original state

        helper(0)
        return res


"""
RECURSION TREE for nums = [1, 2, 3]

Start: ind=0, nums=[1, 2, 3]

Level 0:
    Fix nums[0] with index 0 → [1, 2, 3]
        |
        V
        Level 1:
            Fix nums[1] with index 1 → [1, 2, 3]
                |
                V
                Level 2:
                    Fix nums[2] with index 2 → [1, 2, 3]  ✅ valid
            Backtrack → [1, 2, 3]

            Fix nums[1] with index 2 → [1, 3, 2]
                |
                V
                Level 2:
                    Fix nums[2] with index 2 → [1, 3, 2]  ✅ valid
            Backtrack → [1, 2, 3]

    Fix nums[0] with index 1 → [2, 1, 3]
        |
        V
        Level 1:
            Fix nums[1] with index 1 → [2, 1, 3]
                |
                V
                Level 2:
                    Fix nums[2] with index 2 → [2, 1, 3] ✅ valid
            Backtrack → [2, 1, 3]

            Fix nums[1] with index 2 → [2, 3, 1]
                |
                V
                Level 2:
                    Fix nums[2] with index 2 → [2, 3, 1] ✅ valid
            Backtrack → [2, 1, 3]

    Fix nums[0] with index 2 → [3, 2, 1]
        |
        V
        Level 1:
            Fix nums[1] with index 1 → [3, 2, 1]
                |
                V
                Level 2:
                    Fix nums[2] with index 2 → [3, 2, 1] ✅ valid
            Backtrack → [3, 2, 1]

            Fix nums[1] with index 2 → [3, 1, 2]
                |
                V
                Level 2:
                    Fix nums[2] with index 2 → [3, 1, 2] ✅ valid
            Backtrack → [3, 2, 1]

Final result:
[
 [1, 2, 3],
 [1, 3, 2],
 [2, 1, 3],
 [2, 3, 1],
 [3, 2, 1],
 [3, 1, 2]
]

"""
