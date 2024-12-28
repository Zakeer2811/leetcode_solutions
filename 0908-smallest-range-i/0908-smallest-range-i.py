class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        
        min_possible = min_val + k
        max_possible = max_val - k
        
        return max(0, max_possible - min_possible)
