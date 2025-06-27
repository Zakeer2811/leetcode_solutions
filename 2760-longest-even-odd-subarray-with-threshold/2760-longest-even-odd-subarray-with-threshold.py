from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_len = 0
        n = len(nums)

        for i in range(n):
            # Only start at even number <= threshold
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                length = 1
                for j in range(i + 1, n):
                    # Break if exceeds threshold or parity not alternating
                    if nums[j] > threshold or nums[j] % 2 == nums[j - 1] % 2:
                        break
                    length += 1
                max_len = max(max_len, length)

        return max_len
