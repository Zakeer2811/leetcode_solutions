class Solution:
    def numberOfSteps(self, n: int) -> int:
        c=0
        while n>0:
            if n&1:
                n-=1
                c+=1
            else:
                n>>=1
                c+=1
        return c