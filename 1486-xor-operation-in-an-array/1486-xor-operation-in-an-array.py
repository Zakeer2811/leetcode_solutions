class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i=n
        j=start
        l=[]
        while(i>=0):
            l.append(j)
            j+=2
            i-=1
        result=l[0]
        for k in range(1,n):
            result^=l[k]
        return result
            
            
            
            
            
            
        