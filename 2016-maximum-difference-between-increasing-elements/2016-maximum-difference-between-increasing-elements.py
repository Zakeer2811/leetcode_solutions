class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        ans=-1
        while i<j:
            if nums[i]<nums[j]:
                ans=max(ans,nums[j]-nums[i])
            i+=1
            j-=1
        return ans
        