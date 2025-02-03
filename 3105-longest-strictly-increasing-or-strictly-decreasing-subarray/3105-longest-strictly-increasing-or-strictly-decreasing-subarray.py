class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans=0
        l1,l2=1,1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                l1+=1
                ans=max(l1,l2,ans)
            elif nums[i-1]>nums[i]:
                l2+=1
                ans=max(l1,l2,ans)
            else:
                l1=l2=0
            ans=max(l1,l2,ans)
        return ans if ans>0 else 1
            

        