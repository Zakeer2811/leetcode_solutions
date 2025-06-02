class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        subsets_count=1<<n
        ans=[]
        for i in range(subsets_count):
            temp=[]
            for j in range(n):
                if i&(1<<j):
                    temp.append(nums[j])
            ans.append(temp)
        return ans
        