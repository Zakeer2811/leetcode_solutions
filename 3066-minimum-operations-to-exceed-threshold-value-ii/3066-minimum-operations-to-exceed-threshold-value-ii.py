class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        # Step 2: Initialize counter
        c = 0
        # Step 3: Process the heap until all elements are >= k
        while nums[0] < k:  # Check if the smallest element is >= k
            # Pop the two smallest elements from the heap
            if nums:
                x = heapq.heappop(nums)
            if nums:
                y = heapq.heappop(nums)
            # Calculate the new element and push it back into the heap
            s = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, s)
            # Increment the operation count
            c += 1
        return c