from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index: int):
            # Base case: when we've processed all elements
            if index == len(nums):
                result.append(nums[:])  # Store the current permutation
                return

            seen = set()  # Set to track numbers used at this level
            for i in range(index, len(nums)):
                # Skip duplicates: if nums[i] is the same as nums[i-1] and i > index, skip
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                # Swap to place nums[i] at the current position `index`
                nums[i], nums[index] = nums[index], nums[i]
                # Recurse for the rest of the elements
                backtrack(index + 1)
                # Backtrack: Swap back to the original state
                nums[i], nums[index] = nums[index], nums[i]

        # Sort nums first to make sure duplicates are adjacent
        nums.sort()
        result = []  # To store all the valid permutations
        backtrack(0)  # Start backtracking from the first index
        return result


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