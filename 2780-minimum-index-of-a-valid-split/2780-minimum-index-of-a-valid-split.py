class Solution:
    def minimumIndex(self, nums):
        # Step 1: Find the majority element using the Boyer-Moore Voting Algorithm
        majority = nums[0]
        count = 0
        for n in nums:
            if n == majority:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority = n
                count = 1
        
        # Step 2: Count the occurrences of the majority element
        majCount = nums.count(majority)
        
        # Step 3: Check if a valid split is possible
        count = 0
        for i in range(len(nums)):
            if nums[i] == majority:
                count += 1
            if count * 2 > (i + 1) and (majCount - count) * 2 > (len(nums) - i - 1):
                return i
        
        return -1
