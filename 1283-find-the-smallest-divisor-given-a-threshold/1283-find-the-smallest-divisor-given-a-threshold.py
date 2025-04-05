class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def helper(div,nums):
            total=0
            for i in nums:
                total+=ceil(i/div)#ceil
            return total<=threshold
        low=min(nums)
        high=max(nums)
        while(low<=high):
            mid=low+(high-low)//2
            if helper(mid,nums):
                high=mid-1
            else:
                low=mid+1
        return low 
            
        