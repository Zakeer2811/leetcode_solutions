from typing import List
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        
        # Initialize heap with fractions where numerator index = 0
        for j in range(1, n):
            heapq.heappush(heap, (arr[0]/arr[j], 0, j))
        
        # Pop k-1 fractions and push next fraction with numerator index + 1
        for _ in range(k-1):
            val, i, j = heapq.heappop(heap)
            if i + 1 < j:
                heapq.heappush(heap, (arr[i+1]/arr[j], i+1, j))
        
        # The kth smallest fraction
        val, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]
