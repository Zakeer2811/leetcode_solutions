class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def helper(nums,threshold):
            subarrcnt=1
            sum=0
            for num in nums:
                if num+sum<=threshold:
                    sum+=num
                else:
                    sum=num
                    subarrcnt+=1
            return subarrcnt<=k
        if len(nums)<k:
            return -1
        low=max(nums)
        high=sum(nums) #for k=1
        while low<=high:
            mid=low+(high-low)//2
            if helper(nums,mid):
                high=mid-1
            else:
                low=mid+1
        return low

        