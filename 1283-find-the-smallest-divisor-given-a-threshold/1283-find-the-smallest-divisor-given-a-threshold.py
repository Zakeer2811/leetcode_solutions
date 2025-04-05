from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def cal_div(arr, n):
            d1 = 0
            for i in arr:
                d1 += ceil(i / n)
            return d1
        
        low = 1
        high = max(nums)
        
        while low <= high:
            mid = (low + high) // 2
            divi = cal_div(nums, mid)
            
            if divi > threshold:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
