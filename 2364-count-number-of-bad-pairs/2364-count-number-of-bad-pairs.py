class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        c=Counter(i-n for i,n in enumerate(nums))
        res=len(nums)*(len(nums)-1)
        
        for v in c.values():
            if v>1:
                res-=v*(v-1)
        return res//2
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        tot = len(nums) * (len(nums) - 1) // 2
        good = 0
        dp = {}
        
        for i,num in enumerate(nums):
            v = i - num
            good += dp.get(v, 0)
            dp[v] = dp.get(v, 0) + 1
        
        return tot - good
