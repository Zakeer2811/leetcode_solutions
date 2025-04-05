class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(weights,mid):
            days1=1
            w=0
            for i in range(len(weights)):
                if(w+weights[i]>mid):
                    days1+=1
                    w=weights[i]
                else:
                    w+=weights[i]
            return days1
        low=max(weights)
        high=sum(weights)
        while(low<=high):
            mid=(low+high)//2
            dayscount=helper(weights,mid)
            if dayscount<=days:
                high=mid-1
            else:
                low=mid+1
        return low
        