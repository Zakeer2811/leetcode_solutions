from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            left = nums[m - 1] if m - 1 >= 0 else float('-inf')
            right = nums[m + 1] if m + 1 < len(nums) else float('-inf')

            if left <= nums[m] >= right:
                return m
            elif nums[m] < right:
                l = m + 1
            else:
                h = m - 1


