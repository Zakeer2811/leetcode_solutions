class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        for i in range(1,n):
            n1=bin(nums[i-1])[2:].count('1')
            n2=bin(nums[i])[2:].count('1')
            if n1!=n2:
                return False
        return True