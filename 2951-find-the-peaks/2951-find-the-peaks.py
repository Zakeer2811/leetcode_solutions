from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        def binary_search(left, right):
            # Base condition: if left index exceeds right, return an empty list
            if left > right:
                return []
            
            mid = (left + right) // 2
            peaks = []
            
            # Check if the middle element is a peak
            if (mid > 0 and mountain[mid] > mountain[mid - 1]) and (mid < len(mountain) - 1 and mountain[mid] > mountain[mid + 1]):
                peaks.append(mid)
            
            # Recursively search left and right halves
            peaks += binary_search(left, mid - 1)
            peaks += binary_search(mid + 1, right)
            
            return peaks

        # Binary search starts from index 1 to n-2 to avoid first and last elements
        return binary_search(1, len(mountain) - 2)
