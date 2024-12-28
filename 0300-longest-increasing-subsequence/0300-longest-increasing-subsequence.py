import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # This list will store the smallest tail for all increasing subsequences of length i+1
        dp = []
        
        for num in nums:
            # Use binary search to find the position to replace or append the current number
            pos = bisect.bisect_left(dp, num)
            
            # If pos is equal to the length of dp, it means num is greater than all elements in dp
            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num
        
        # The length of dp is the length of the longest increasing subsequence
        return len(dp)
