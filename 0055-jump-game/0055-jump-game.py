class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the final position we need to reach, starting from the last index of the array
        finalposition = len(nums) - 1
        
        # Iterate through the list from the second to last element to the first element (right to left)
        for i in range(len(nums) - 2, -1, -1):
            # Check if the current index plus the maximum jump length from this index reaches or surpasses the final position
            if i + nums[i] >= finalposition:
                # If it does, update the final position to be the current index
                finalposition = i
        
        # If we have moved the final position back to the start (index 0), it means we can reach the last index from the first
        return finalposition == 0
