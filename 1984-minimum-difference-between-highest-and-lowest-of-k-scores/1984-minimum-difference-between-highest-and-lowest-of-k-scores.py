from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float('inf')
        
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            ans = min(ans, diff)
        
        return ans
