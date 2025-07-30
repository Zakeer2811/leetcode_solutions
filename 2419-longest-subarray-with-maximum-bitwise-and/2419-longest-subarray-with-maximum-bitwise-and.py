class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == max_num:
                current_count += 1
            else:
                current_count = 0
            max_count = max(max_count, current_count)
        
        return max_count
        