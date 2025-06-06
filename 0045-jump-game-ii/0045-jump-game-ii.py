class Solution:
    def jump(self, nums: List[int]) -> int:
        # If the list is empty or has only one element, no jumps are needed
        if len(nums) <= 1:
            return 0
        
        # Initialize jumps counter, current range (end of the current jump), and furthest position that can be reached
        jumps = 0
        current_end = 0
        furthest = 0
        
        # Traverse through the list except the last element
        for i in range(len(nums) - 1):
            # Update the furthest position that can be reached
            furthest = max(furthest, i + nums[i])
            
            # If we reach the end of the current jump range
            if i == current_end:
                # Increment the jump count
                jumps += 1
                # Update the end of the current jump range to the furthest position reached
                current_end = furthest
                
                # If the current end is beyond or at the last index, we can stop
                if current_end >= len(nums) - 1:
                    break
        
        return jumps
