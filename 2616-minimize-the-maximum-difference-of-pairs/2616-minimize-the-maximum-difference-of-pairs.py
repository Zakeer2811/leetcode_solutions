class Solution:
    def minimizeMax(self,nums, p):
        # Step 1: Sort the array to bring closer elements together
        nums.sort()
        
        # Helper function to check if we can form at least p pairs with max difference <= maxDiff
        def canFormPairs(maxDiff):
            count = 0  # Number of pairs formed
            i = 0
            # Iterate through nums to greedily form pairs
            while i < len(nums) - 1:
                # Check if the difference between adjacent elements is within maxDiff
                if nums[i+1] - nums[i] <= maxDiff:
                    count += 1      # Form a pair
                    i += 2          # Skip the next index as it's paired
                else:
                    i += 1          # Otherwise move one step forward and try again
                if count >= p:      # If we already formed p pairs, no need to continue
                    return True
            return False             # Couldn't form p pairs with maxDiff difference
        
        # Binary search boundaries: minimum possible difference is 0, max possible difference is max - min
        left, right = 0, nums[-1] - nums[0]
        
        # Binary search to find the smallest maxDiff for which canFormPairs is True
        while left < right:
            mid = (left + right) // 2
            if canFormPairs(mid):
                right = mid      # Try to find a smaller maxDiff on the left side
            else:
                left = mid + 1   # Increase maxDiff since mid was too small
        
        # When left == right, we have the minimum max difference possible
        return left

    """
    Dry run example:
    nums = [10,1,2,7,1,3], p = 2

    Step 1: Sort nums:
    nums = [1, 1, 2, 3, 7, 10]

    Initial binary search range:
    left = 0
    right = 10 - 1 = 9

    Iteration 1:
    mid = (0 + 9) // 2 = 4
    canFormPairs(4):
    - i=0: nums[1] - nums[0] = 1 - 1 = 0 <= 4 -> pair (1,1), count=1, i=2
    - i=2: nums[3] - nums[2] = 3 - 2 = 1 <= 4 -> pair (2,3), count=2, i=4
    count >= p (2), return True
    => right = 4

    Iteration 2:
    left=0, right=4
    mid = (0+4)//2 = 2
    canFormPairs(2):
    - i=0: nums[1] - nums[0] = 0 <= 2 -> pair (1,1), count=1, i=2
    - i=2: nums[3] - nums[2] = 1 <= 2 -> pair (2,3), count=2, i=4
    count >= p, return True
    => right = 2

    Iteration 3:
    left=0, right=2
    mid = (0+2)//2 = 1
    canFormPairs(1):
    - i=0: nums[1] - nums[0] = 0 <= 1 -> pair (1,1), count=1, i=2
    - i=2: nums[3] - nums[2] = 1 <= 1 -> pair (2,3), count=2, i=4
    count >= p, return True
    => right = 1

    Iteration 4:
    left=0, right=1
    mid = (0+1)//2 = 0
    canFormPairs(0):
    - i=0: nums[1] - nums[0] = 0 <= 0 -> pair (1,1), count=1, i=2
    - i=2: nums[3] - nums[2] = 1 > 0 -> no pair, i=3
    - i=3: nums[4] - nums[3] = 7 - 3 = 4 > 0 -> no pair, i=4
    - i=4: nums[5] - nums[4] = 10 - 7 = 3 > 0 -> no pair, i=5
    count = 1 < p(2) -> return False
    => left = mid + 1 = 1

    Now left == right == 1, so return 1

    This matches the expected output.
    """
