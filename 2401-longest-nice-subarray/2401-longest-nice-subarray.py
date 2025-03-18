class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        lo, mask, ans = -1, 0, 1
        for hi, n in enumerate(nums):
            while (mask & n): # n has duplicate set bits for current sliding window.
                lo += 1 # shrink left bound of current sliding window.
                mask ^= nums[lo] # remove the corresponding element out of the window.
            mask |= n # Expand right bound and put n into window.
            ans = max(ans, hi - lo) # update the max window size.
        return ans