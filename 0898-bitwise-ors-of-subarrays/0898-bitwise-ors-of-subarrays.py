class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        def helper(i,j):
            res=0
            for k in range(i,j+1):
                res|=arr[k]
            return res
        d={}
        n=len(arr)
        if n==1:
            return 1
        for i in range(n):
            for j in range(i,n):
                res=helper(i,j)
                if res in d:
                    d[res]+=1
                else:
                    d[res]=1
        return len(d)
        