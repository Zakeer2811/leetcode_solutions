from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array to facilitate two-pointer approach
        n = len(nums)
        closest_sum = float('inf')  # Initialize closest sum to infinity
        min_diff = float('inf')  # Initialize minimum difference to infinity
        
        for i in range(n - 2):  # Iterate through the array until the third last element
            # Skip duplicates to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1  # Left pointer
            right = n - 1  # Right pointer
            
            while left < right:  # Two-pointer approach
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(current_sum - target)  # Calculate the difference
                
                if current_diff < min_diff:  # Update closest sum if the current difference is smaller
                    min_diff = current_diff
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1  # Move left pointer to the right
                elif current_sum > target:
                    right -= 1  # Move right pointer to the left
                else:
                    return target  # If the sum is exactly equal to the target, return it
        
        return closest_sum  # Return the closest sum found
