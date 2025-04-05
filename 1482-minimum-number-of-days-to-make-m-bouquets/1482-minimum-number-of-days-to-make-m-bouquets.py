class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isPossible(bloomday,mid,m,k):
            cnt=0 
            no_of_boq=0
            for i in range(len(bloomday)):
                if(bloomday[i]<=mid):
                    cnt+=1
                else:
                    no_of_boq+=(cnt//k)
                    cnt=0
            no_of_boq+=(cnt//k)
            return no_of_boq>=m
        if m*k>len(bloomDay):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        while(low<=high):
            mid=(low+high)//2
            if(isPossible(bloomDay,mid,m,k)):
                high=mid-1
            else:
                low=mid+1
        return low
        