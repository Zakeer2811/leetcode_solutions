class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(nums,k):
            if k<0:
                return 0
            cnt=0
            ans=0
            l=r=0
            n=len(nums)
            while r<n:
                cnt+=(nums[r]&1)
                while cnt>k:
                    cnt-=(nums[l]&1)
                    l+=1
                ans+=(r-l+1)
                r+=1
            return ans
        return helper(nums,k)-helper(nums,k-1)
                
                
