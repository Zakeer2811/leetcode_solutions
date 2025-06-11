class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def find_comb(ind,target,ds,arr,ans):
            if target==0:
                ans.append(ds[:])
            for i in range(ind,len(arr)):
                if i>ind and arr[i]==arr[i-1]:continue
                if arr[i]>target:break
                ds.append(arr[i])
                find_comb(i+1,target-arr[i],ds,arr,ans)
                ds.pop()
        candidates.sort()
        ans=[]
        find_comb(0,target,[],candidates,ans)
        return ans
        