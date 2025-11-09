class Solution:
    def countOperations(self, n1: int, n2: int) -> int:
        #def helper(n1,n2,c):
            
        c=0
        while n1>0 and n2>0:
            if n1>=n2:
                n1-=n2
                c+=1
            else:
                n2-=n1
                c+=1
        return c
