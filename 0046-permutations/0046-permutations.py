from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def generate_permutations(current_permutation: List[int], remaining_elements: List[int]):
            # Base case: when no elements are left to insert
            if not remaining_elements:
                result.append(current_permutation[:])  # Add a copy of the complete permutation
                return

            # Take the first element from the remaining list
            element_to_insert = remaining_elements[0]

            # Insert it into every possible position in current_permutation
            for position in range(len(current_permutation) + 1):
                left = current_permutation[:position]
                right = current_permutation[position:]
                new_permutation = left + [element_to_insert] + right
                # Recurse with the new permutation and the remaining elements (excluding current)
                generate_permutations(new_permutation, remaining_elements[1:])

        generate_permutations([], nums)
        return result


"""
RECURSION TREE FOR nums = [1, 2, 3]

Initial Call:
generate_permutations([], [1, 2, 3])

Step 1: Insert 1 into all positions of []
    → [1]
    Call: generate_permutations([1], [2, 3])

Step 2: Insert 2 into all positions of [1]
    → [2, 1]
        Call: generate_permutations([2, 1], [3])
            → Insert 3:
                [3, 2, 1]
                [2, 3, 1]
                [2, 1, 3]
    → [1, 2]
        Call: generate_permutations([1, 2], [3])
            → Insert 3:
                [3, 1, 2]
                [1, 3, 2]
                [1, 2, 3]

Step 3: Insert 3 into all positions of all previous results:
    From [2, 1]:
        → [3, 2, 1]
        → [2, 3, 1]
        → [2, 1, 3]
    From [1, 2]:
        → [3, 1, 2]
        → [1, 3, 2]
        → [1, 2, 3]

Final Result:
[
 [3, 2, 1],
 [2, 3, 1],
 [2, 1, 3],
 [3, 1, 2],
 [1, 3, 2],
 [1, 2, 3]
]

Key idea:
- At each level, take the next number (`element_to_insert`) from `remaining_elements`
- Insert it into all positions of the `current_permutation`
- Recursively build up until `remaining_elements` is empty
"""

#         res = []

#         def helper(ind: int):
#             # Base case: If we've fixed all positions, store a copy of the permutation
#             if ind == len(nums):
#                 res.append(nums[:])
#                 return

#             # Try placing each number at the current index `ind`
#             for i in range(ind, len(nums)):
#                 # Swap current index with i to fix nums[i] at index ind
#                 nums[ind], nums[i] = nums[i], nums[ind]
#                 helper(ind + 1)  # Recurse for the rest of the list
#                 nums[ind], nums[i] = nums[i], nums[ind]  # Backtrack to restore original state

#         helper(0)
#         return res


# """
# RECURSION TREE for nums = [1, 2, 3]

# Start: ind=0, nums=[1, 2, 3]

# Level 0:
#     Fix nums[0] with index 0 → [1, 2, 3]
#         |
#         V
#         Level 1:
#             Fix nums[1] with index 1 → [1, 2, 3]
#                 |
#                 V
#                 Level 2:
#                     Fix nums[2] with index 2 → [1, 2, 3]  ✅ valid
#             Backtrack → [1, 2, 3]

#             Fix nums[1] with index 2 → [1, 3, 2]
#                 |
#                 V
#                 Level 2:
#                     Fix nums[2] with index 2 → [1, 3, 2]  ✅ valid
#             Backtrack → [1, 2, 3]

#     Fix nums[0] with index 1 → [2, 1, 3]
#         |
#         V
#         Level 1:
#             Fix nums[1] with index 1 → [2, 1, 3]
#                 |
#                 V
#                 Level 2:
#                     Fix nums[2] with index 2 → [2, 1, 3] ✅ valid
#             Backtrack → [2, 1, 3]

#             Fix nums[1] with index 2 → [2, 3, 1]
#                 |
#                 V
#                 Level 2:
#                     Fix nums[2] with index 2 → [2, 3, 1] ✅ valid
#             Backtrack → [2, 1, 3]

#     Fix nums[0] with index 2 → [3, 2, 1]
#         |
#         V
#         Level 1:
#             Fix nums[1] with index 1 → [3, 2, 1]
#                 |
#                 V
#                 Level 2:
#                     Fix nums[2] with index 2 → [3, 2, 1] ✅ valid
#             Backtrack → [3, 2, 1]

#             Fix nums[1] with index 2 → [3, 1, 2]
#                 |
#                 V
#                 Level 2:
#                     Fix nums[2] with index 2 → [3, 1, 2] ✅ valid
#             Backtrack → [3, 2, 1]

# Final result:
# [
#  [1, 2, 3],
#  [1, 3, 2],
#  [2, 1, 3],
#  [2, 3, 1],
#  [3, 2, 1],
#  [3, 1, 2]
# ]

# """
