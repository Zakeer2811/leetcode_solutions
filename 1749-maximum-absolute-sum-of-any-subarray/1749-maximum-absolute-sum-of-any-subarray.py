class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(accumulate(nums,initial=0))-min(accumulate(nums,initial=0))
        