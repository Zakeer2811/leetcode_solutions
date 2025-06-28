class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Pair each number with its index to keep track of original positions
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Step 2: Sort the pairs by number in descending order to get the largest values first
        indexed_nums.sort(key=lambda x: -x[0])
        
        # Step 3: Select the top k elements with the largest values
        top_k = indexed_nums[:k]
        
        # Step 4: Sort the selected top k elements based on their original index
        # This ensures we return a valid subsequence (order preserved from original list)
        top_k.sort(key=lambda x: x[1])
        
        # Step 5: Extract the numbers from the top_k elements to form the final result
        return [num for num, i in top_k]

        # --- Dry Run Example ---
        # Input: nums = [2, 1, 3, 3], k = 2
        #
        # Step 1: Pair with indices
        #   indexed_nums = [(2, 0), (1, 1), (3, 2), (3, 3)]
        #
        # Step 2: Sort by value descending
        #   indexed_nums = [(3, 2), (3, 3), (2, 0), (1, 1)]
        #
        # Step 3: Take top 2 elements
        #   top_k = [(3, 2), (3, 3)]
        #
        # Step 4: Sort by index to preserve original order
        #   top_k = [(3, 2), (3, 3)]
        #
        # Step 5: Extract values
        #   result = [3, 3]
        #
        # Output: [3, 3]
