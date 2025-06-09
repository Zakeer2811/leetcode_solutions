class Solution:
    def numberOfSteps(self, num: int) -> int:
        def helper(n,c):
            if n==0:
                return c
            if n%2==0:
                return helper(n//2,c+1)
            else:
                return helper(n-1,c+1)
        return helper(num,c=0)
        