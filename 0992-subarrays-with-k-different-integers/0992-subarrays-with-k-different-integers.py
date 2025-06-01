class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(k,nums):
            if k<0:
                return 0
            d=defaultdict(int)
            l=r=cnt=0
            while r<len(nums):
                n1=nums[r]
                d[n1]+=1
                while len(d)>k:
                    d[nums[l]]-=1
                    if d[nums[l]]==0:
                        del d[nums[l]]
                    l+=1
# Add the number of valid subarrays that end at 'r'
# The subarrays that end at 'r' and start from any index between 'l' and 'r' are valid.
# This is because the sliding window contains at most 'k' distinct elements,
# so all subarrays starting from the left pointer (l) to the right pointer (r) are valid subarrays
# with at most 'k' distinct elements.
# 
# The number of valid subarrays ending at 'r' is simply the number of subarrays that start at 
# index 'l', 'l+1', ..., 'r'. This can be calculated as (r - l + 1), because:
# - When 'r' is at position 3 and 'l' is at position 1, the subarrays ending at 3 are:
#   [nums[1], nums[3]], [nums[2], nums[3]], [nums[3]]
#   This gives 3 subarrays in total: [nums[l], nums[r]], [nums[l+1], nums[r]], ..., [nums[r]]
# 
# As we move 'r' and expand the window to include more elements, we keep track of the valid subarrays
# by adding (r - l + 1) to the count. This ensures that every valid subarray is counted exactly once.


                cnt+=(r-l+1)
                r+=1
            return cnt
        return helper(k,nums)-helper(k-1,nums)
            