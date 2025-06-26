from typing import List

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # Step 1: Calculate the total sum of the array
        total_sum = sum(A)
        
        # Step 2: If the total sum is not divisible by 3, we can't split it into three equal parts
        if total_sum % 3 != 0:
            return False
        
        # Step 3: Calculate the target sum for each part (sum of each partition)
        target_sum = total_sum // 3
        
        # Initialize variables:
        # - left_sum starts at the first element (left side)
        # - right_sum starts at the last element (right side)
        left_sum = A[0]
        right_sum = A[-1]
        
        # Pointers: `l` moves from left to right, `r` moves from right to left
        left_pointer = 1
        right_pointer = len(A) - 2
        
        # Step 4: Iterate until the pointers meet in the middle
        while left_pointer <= right_pointer:
            # Expand the left partition by adding the current left element
            if left_pointer < right_pointer and left_sum != target_sum:
                left_sum += A[left_pointer]
                left_pointer += 1
            
            # Expand the right partition by adding the current right element
            if left_pointer < right_pointer and right_sum != target_sum:
                right_sum += A[right_pointer]
                right_pointer -= 1
            
            # Step 5: Check if both the left and right sums have reached the target sum
            if left_sum == target_sum == right_sum:
                return True
            
            # Step 6: If the pointers meet, we can't find valid partitions
            if left_pointer == right_pointer:
                return False
        
        # If no solution was found, return False
        return False
