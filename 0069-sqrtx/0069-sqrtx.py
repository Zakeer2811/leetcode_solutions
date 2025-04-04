class Solution:
    def mySqrt(self, x: int) -> int:
        n=x
        c=0
        if n==0:
            return 0
        if n>0:
            for i in range(1,2**31,2):
                n=n-i
                if n>0 or n==0:
                    c=c+1
                if n<0:
                    return c
                    break
                
        