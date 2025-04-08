class Solution:
    def minimumOperations(self, nums):
        # Create a frequency map to count occurrences of each element in nums
        frequency_map = [0] * 101  # We assume the elements of nums are between 0 and 100
        
        # Traverse the list from the end to the beginning
        for i in range(len(nums) - 1, -1, -1):
            # Increment the count for the current element in the frequency map
            frequency_map[nums[i]] += 1
            
            # If the element appears more than once, we need to remove it
            if frequency_map[nums[i]] == 2:
                # Return the minimum number of operations (removing 3 elements at a time)
                # (i + 3) // 3 calculates the number of operations required
                return (i + 3) // 3
        
        # If no duplicates are found, return 0 since no operation is needed
        return 0
