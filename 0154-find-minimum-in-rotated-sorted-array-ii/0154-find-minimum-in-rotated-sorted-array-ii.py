class Solution(object):
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1  # Initialize two pointers: lo (start) and hi (end)
        
        while lo <= hi:  # Continue the search as long as the range is valid
            mid = lo + (hi - lo) // 2  # Calculate the middle index
            
            # If the middle element is greater than the last element,
            # the minimum must be in the right half
            if nums[mid] > nums[hi]:
                lo = mid + 1  # Move the lower bound to the right of mid
            else:
                # If nums[mid] <= nums[hi], the minimum could be at mid or in the left half
                # Handle duplicates:
                # If nums[mid] == nums[hi], we can't determine which side has the minimum
                # So, reduce the search space by moving the high pointer leftward
                hi = mid  if nums[hi] != nums[mid] else hi - 1
        
        return nums[lo]  # Return the minimum element found
