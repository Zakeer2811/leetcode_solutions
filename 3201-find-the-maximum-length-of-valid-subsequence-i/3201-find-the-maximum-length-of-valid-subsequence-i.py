from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # 1) even-sum subsequence: take all evens or all odds
        count_even = sum(1 for x in nums if x % 2 == 0)
        count_odd  = len(nums) - count_even
        even_sum_max = max(count_even, count_odd)

        # 2) odd-sum subsequence: longest parity-alternating subsequence
        dp_even = 0  # best length ending in an even
        dp_odd  = 0  # best length ending in an odd
        for x in nums:
            if x % 2 == 0:
                # we can either start a new subsequence of length 1 (dp_even stays ≥1),
                # or append this even to one ending in odd
                dp_even = max(dp_even, dp_odd + 1)
            else:
                dp_odd  = max(dp_odd, dp_even + 1)

        odd_sum_max = max(dp_even, dp_odd)

        # 3) best of both strategies
        return max(even_sum_max, odd_sum_max)
