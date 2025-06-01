from collections import defaultdict
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        current_sum = 0
        max_sum = 0
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1
            current_sum += nums[right]

            # Shrink window if it exceeds size k
            if right - left + 1 > k:
                freq[nums[left]] -= 1
                current_sum -= nums[left]
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            # Check for valid window
            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
