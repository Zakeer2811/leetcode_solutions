from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_map = defaultdict(int)
        prefix_sum_map[0] = 1  # To handle subarrays starting from index 0
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num  # Update the current prefix sum
            
            # Check if there is a previous prefix sum that makes a subarray sum = k
            if current_sum - k in prefix_sum_map:
                count += prefix_sum_map[current_sum - k]
            
            # Store the current prefix sum in the map
            prefix_sum_map[current_sum] += 1
        
        return count
