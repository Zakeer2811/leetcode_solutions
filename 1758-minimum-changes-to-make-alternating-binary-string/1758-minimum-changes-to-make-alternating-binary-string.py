class Solution:
    def minOperations(self, s: str) -> int:
        c1=s.count('1')
        n=len(s)
        c2=n-c1
        if c1==c2:
            return 0
        elif c1==n:
            return c1//2
        elif c2==n:
            return c2//2
        else:
            return min(abs(c1-c2),c1,c2)
                
        