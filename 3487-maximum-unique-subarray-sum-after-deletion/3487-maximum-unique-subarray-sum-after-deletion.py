class Solution:
    def maxSum(self, nums: List[int]) -> int:
        distinct_positives = set()
        for num in nums:
            if num > 0:
                distinct_positives.add(num)
        total = sum(distinct_positives)
        if total > 0:
            return total
        else:
            return max(nums)