class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r=0,len(height)-1
        leftmax,rightmax=height[l],height[r]
        stored_water=0
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax=max(leftmax,height[l])
                stored_water+=(leftmax-height[l])
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                stored_water+=(rightmax-height[r])
        return stored_water

        