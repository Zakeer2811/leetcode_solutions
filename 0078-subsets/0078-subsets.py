from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Get the total number of elements in the input list.
        num_elements = len(nums)
        
        # Step 2: Calculate the total number of subsets.
        # For a set of size n, the total number of subsets is 2^n.
        # We use bit shifting: (1 << n) is equivalent to 2^n.
        total_subsets = 1 << num_elements  # same as 2 ** num_elements
        
        # This will store all the generated subsets
        all_subsets = []

        # Step 3: Iterate over the range from 0 to 2^n - 1 (each value represents a bitmask for a subset)
        for subset_mask in range(total_subsets):
            current_subset = []

            # Step 4: For each bit in the bitmask, determine whether to include nums[j]
            # If the j-th bit in subset_mask is 1, include nums[j] in the current subset
            for element_index in range(num_elements):
                # (1 << element_index) creates a bitmask where only the element_index-th bit is 1.
                # Performing bitwise AND with subset_mask checks if that bit is set.
                # If it is set, it means nums[element_index] should be included in this subset.
                if subset_mask & (1 << element_index):
                    current_subset.append(nums[element_index])
            
            # Add the current subset to the list of all subsets
            all_subsets.append(current_subset)
        
        # Return the complete list of subsets
        return all_subsets
