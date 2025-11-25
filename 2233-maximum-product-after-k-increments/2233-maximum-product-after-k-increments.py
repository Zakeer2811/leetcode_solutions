class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
    
        # Step 1: Convert nums into a min-heap
        heapq.heapify(nums)
        
        # Step 2: Perform at most k increment operations
        for _ in range(k):
            # Pop the smallest element, increment it, and push it back to the heap
            smallest = heapq.heappop(nums)
            heapq.heappush(nums, smallest + 1)
        
        # Step 3: Calculate the product of the elements in the heap
        product = 1
        for num in nums:
            product = (product * num) % MOD
        
        return product
