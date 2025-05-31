import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []

        # Push fractions with numerator index 0 and denominator index j (j=1..n-1)
        for j in range(1, n):
            # Why push i=0? Because fractions start with numerator at 0 to get smallest fractions first
            # (arr[0]/arr[j]) is the smallest numerator fraction for denominator arr[j]
            heapq.heappush(heap, (arr[0]/arr[j], 0, j))

        # We pop k-1 times to remove the first k-1 smallest fractions
        # So that the next pop is the kth smallest fraction
        for _ in range(k - 1):
            frac, i, j = heapq.heappop(heap)

            # After popping the fraction (arr[i]/arr[j]), 
            # if possible, push next fraction with numerator i+1 and same denominator j
            # Why? Because arr is sorted, arr[i+1]/arr[j] > arr[i]/arr[j], so this ensures next bigger fraction with same denominator
            if i + 1 < j:
                heapq.heappush(heap, (arr[i+1]/arr[j], i+1, j))

        # Now the top of the heap is the kth smallest fraction
        frac, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]
