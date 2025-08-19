from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        current_zero_segment_length = 0
        
        for num in nums:
            if num == 0:
                current_zero_segment_length += 1
                total += current_zero_segment_length
            else:
                current_zero_segment_length = 0
        
        return total