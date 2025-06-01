from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        # Helper function to count subarrays whose sum is <= k
        def count_subarrays_with_sum_at_most(k):
            count = 0  # To store the number of valid subarrays
            left = 0  # Left pointer of the sliding window
            current_sum = 0  # Running sum of the current window
            
            # Iterate through the array with the right pointer
            for right in range(len(nums)):
                current_sum += nums[right]  # Add the current element to the running sum
                
                # If the current sum exceeds k, move the left pointer to shrink the window
                while current_sum > k and left<=right:
                    current_sum -= nums[left]  # Subtract the element at the left pointer
                    left += 1  # Move the left pointer to the right
                # # Problem: Here you're adding subarrays from left to right
                # # Every subarray from 'l' to 'r' is counted, but the sum of those subarrays
                # # is not guaranteed to be exactly 'goal', they could be less than or equal to 'k'.
                # # This causes the count to be incorrect for exactly 'goal' sums.
                # if s <= k:
                #     cnt += (r - l + 1)  # Adding all subarrays from 'l' to 'r'
                # The number of valid subarrays ending at 'right' is (right - left + 1)
                # because all subarrays from index 'left' to 'right' are valid
                count += (right - left + 1)
            
            return count
        
        # We use the difference of counts:
        # Subarrays with sum exactly 'goal' = Subarrays with sum <= 'goal' - Subarrays with sum <= 'goal - 1'
        return count_subarrays_with_sum_at_most(goal) - count_subarrays_with_sum_at_most(goal - 1)
