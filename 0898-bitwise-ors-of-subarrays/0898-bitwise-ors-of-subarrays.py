class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # Set to store unique results
        unique_results = set()
        # Set to store ORs for the current subarrays ending at current index
        current_or = set()
        
        for num in arr:
            # For each num, create new ORs by combining num with previous subarrays
            current_or = {num} | {x | num for x in current_or}
            # Add the current ORs to the global set of unique results
            unique_results |= current_or
        
        return len(unique_results)
