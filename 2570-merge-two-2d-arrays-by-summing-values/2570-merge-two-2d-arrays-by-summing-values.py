from collections import defaultdict
from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # Create a dictionary to store sums by key
        d = defaultdict(int)
        
        # Iterate through nums1 and sum the values for the same key
        for i in nums1:
            d[i[0]] += i[1]
        
        # Iterate through nums2 and sum the values for the same key
        for i in nums2:
            d[i[0]] += i[1]
        
        # Sort the dictionary by keys and prepare the result list
        result = []
        for k in sorted(d.keys()):
            result.append([k, d[k]])

        return result
