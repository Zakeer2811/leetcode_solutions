from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        all_even = 0
        all_odd = 0
        alt_even = 0  # starts with even, next odd
        alt_odd = 0   # starts with odd, next even
        
        for num in nums:
            if num % 2 == 0:
                all_even += 1
                alt_even = alt_odd + 1
                # alt_odd remains as is
            else:
                all_odd += 1
                alt_odd = alt_even + 1
                # alt_even remains as is
        
        return max(all_even, all_odd, alt_even, alt_odd)