from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index: int):
            # Base case: when we've processed all elements
            if index == len(nums):
                return [nums[:]]  # Return the current permutation as a list of lists

            all_permutations = []  # Store all permutations generated in this call
            for i in range(index, len(nums)):
                # Skip duplicates: if nums[i] is the same as nums[i-1], skip this iteration
                if i > index and nums[i] == nums[i - 1]:
                    continue
                # Swap to place nums[i] at the current position `index`
                nums[i], nums[index] = nums[index], nums[i]
                # Recurse for the rest of the elements
                all_permutations += backtrack(index + 1)  # Collect all permutations from recursion
                # Backtrack: Swap back to the original state
                nums[i], nums[index] = nums[index], nums[i]

            return all_permutations  # Return the list of permutations

        # Sort nums first to make sure duplicates are adjacentSorting and Unique Permutations:
# When you sort the array [1, 2, 2], it becomes [1, 2, 2]. This sorted order ensures that identical numbers (2 in this case) are adjacent to each other.Thus, permutations like [1, 2, 2], [2, 1, 2], and [2, 2, 1] will not be repeated, and only unique permutations are generated.
        nums.sort()
        # Start recursion from the first index
        return backtrack(0)
'''
                              permuteUnique([1, 2, 2])
                              /           |         \
                      swap(0,0)    swap(1,1)    swap(2,2)
                        |             |            |
                permute([1, 2, 2]) permute([1, 2, 2]) permute([1, 2, 2])
                      /           \                 /    \
              swap(1,1)       swap(2,2)         swap(0,1) swap(1,2)
                    |             |               |        |
         permute([1, 2, 2])   permute([1, 2, 2])    [result]   [result]  
             /    |    \            /     |     \           /    |   \
    swap(1,2) swap(1,1) swap(2,2)  swap(1,2) swap(1,2) swap(1,1) [1, 2, 2]  [2, 1, 2]  [2, 2, 1]
        |             |                |           |         /    |  \
  permute([1, 2, 2]) permute([1, 2, 2])  [skip]  [skip]     [1,2,2] [2,1,2]
'''