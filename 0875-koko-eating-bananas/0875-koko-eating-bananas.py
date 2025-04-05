class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cal_hours(arr,n):
            h1=0
            for i in arr:
                h1+=ceil(i/n)
            return h1
                
        low=1
        high=max(piles)
        while(low<=high):
            mid=(low+high)//2
            total_hours=cal_hours(piles,mid)
            if(total_hours<=h):
                high=mid-1
            else:
                low=mid+1
        return low