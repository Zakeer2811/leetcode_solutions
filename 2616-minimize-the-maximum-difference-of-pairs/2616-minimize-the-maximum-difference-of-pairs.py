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
                # Because mid could still be the answer so we don't exclude it from search space
            else:
                left = mid + 1   # Increase maxDiff since mid was too small
        
        # When left == right, we have the minimum max difference possible
        return left
"""
Key binary search logic:
- left = smallest possible difference (0).
- right = largest possible difference (max(nums) - min(nums)).
- For a mid value, check if forming pairs is possible.
- If yes, try smaller differences.
- If no, try larger differences.

Your original (buggy) update step in binary search:
if canFormPairs(mid):
    right = mid - 1
else:
    left = mid + 1

Why is this wrong?
If canFormPairs(mid) is True, it means mid is a valid answer (you can form pairs with max difference ≤ mid).
But by doing right = mid - 1, you exclude mid from the next search space.
This can cause skipping the correct minimum max difference.

Correct update step:
if canFormPairs(mid):
    right = mid     # keep mid in the search space because mid might be the answer
else:
    left = mid + 1

Dry Run Example with nums = [10,1,2,7,1,3], p = 2

Step 1: Sort the array
nums = [1, 1, 2, 3, 7, 10]

Step 2: Define search boundaries
left = 0                      # min possible difference
right = 10 - 1 = 9            # max possible difference

Step 3: First iteration
mid = (0 + 9) // 2 = 4

Check canFormPairs(4):
  - Pair (1,1) difference = 0 <= 4 -> count = 1, i = 2
  - Pair (2,3) difference = 1 <= 4 -> count = 2, i = 4
Count = 2 >= p (2) -> True

=> can form pairs with maxDiff = 4
=> right = mid = 4   # Correct update (not 3)

Step 4: Second iteration
left = 0, right = 4
mid = (0 + 4) // 2 = 2

Check canFormPairs(2):
  - Pair (1,1) difference = 0 <= 2 -> count = 1, i = 2
  - Pair (2,3) difference = 1 <= 2 -> count = 2, i = 4
Count = 2 >= p -> True

=> right = mid = 2

Step 5: Third iteration
left = 0, right = 2
mid = (0 + 2) // 2 = 1

Check canFormPairs(1):
  - Pair (1,1) difference = 0 <= 1 -> count = 1, i = 2
  - Pair (2,3) difference = 1 <= 1 -> count = 2, i = 4
Count = 2 >= p -> True

=> right = mid = 1

Step 6: Fourth iteration
left = 0, right = 1
mid = (0 + 1) // 2 = 0

Check canFormPairs(0):
  - Pair (1,1) difference = 0 <= 0 -> count = 1, i = 2
  - (2,3) difference = 1 > 0 -> no pair, i = 3
  - (3,7) difference = 4 > 0 -> no pair, i = 4
  - (7,10) difference = 3 > 0 -> no pair, i = 5
Count = 1 < p (2) -> False

=> left = mid + 1 = 1

Step 7: End condition
left = 1, right = 1
Loop ends since left == right

Return left = 1 as the minimum maximum difference.

What happens if you use right = mid - 1?
When mid = 1 and canFormPairs(1) returns True,
You set right = 0,
Next iteration tries mid = 0,
canFormPairs(0) returns False,
So left moves to 1,
But the binary search overshoots the range and might miss 1 as a valid answer,
Leading to incorrect answers like 0.

Summary:
- When mid is valid, keep it in your search space: right = mid.
- When mid is invalid, discard the left side: left = mid + 1.
- This ensures you never skip valid answers and find the smallest max difference correctly.
"""
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
