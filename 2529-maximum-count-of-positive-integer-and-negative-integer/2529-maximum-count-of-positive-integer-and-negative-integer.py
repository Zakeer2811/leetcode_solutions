
class Solution:
    def maximumCount(self, nums):
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1
        positive_count = n - left

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
        negative_count = right + 1

        return max(positive_count, negative_count)
import bisect

# class Solution:
#     def maximumCount(self, nums):
#         # Find the index of the first positive number using bisect_right
#         positive_count = len(nums) - bisect.bisect_right(nums, 0)
        
#         # Find the index of the last negative number using bisect_left
#         negative_count = bisect.bisect_left(nums, 0)
        
#         # Return the maximum count of positive and negative integers
#         return max(positive_count, negative_count)