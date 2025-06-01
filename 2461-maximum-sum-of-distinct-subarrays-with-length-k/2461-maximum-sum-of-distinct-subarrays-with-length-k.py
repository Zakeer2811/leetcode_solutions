from collections import deque
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = deque()
        window_set = set()
        current_sum = 0
        max_sum = 0

        for num in nums:
            # Remove from left if duplicate or window is too large
            while num in window_set or len(window) >= k:
                removed = window.popleft()
                window_set.remove(removed)
                current_sum -= removed

            window.append(num)
            window_set.add(num)
            current_sum += num

            if len(window) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
