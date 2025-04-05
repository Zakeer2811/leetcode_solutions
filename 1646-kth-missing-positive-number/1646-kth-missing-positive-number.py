from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Step 1: Determine the length of the input array `arr`
        n = len(arr)
        
        # Step 2: Initialize binary search boundaries
        low = 0   # Starting point of the search (left side of the array)
        high = n - 1   # Ending point of the search (right side of the array)
        
        # Step 3: Perform binary search
        while low <= high:  # Continue searching while the range is valid
            mid = low + (high - low) // 2  # Find the middle index of the current range
            
            # Step 4: Calculate how many numbers are missing up to index `mid`
            no_of_missing_numbers = arr[mid] - (mid + 1)  # Missing numbers before arr[mid]
            
            # Step 5: Check if the missing numbers are less than `k`
            if no_of_missing_numbers < k:
                # If there are fewer missing numbers than `k`, search in the right half
                low = mid + 1
            else:
                # If there are more or equal missing numbers than `k`, search in the left half
                high = mid - 1
        
        # Step 6: The missing number at position `k` is at index `low + k`
        return low + k  # After binary search, the position `low` is the answer

