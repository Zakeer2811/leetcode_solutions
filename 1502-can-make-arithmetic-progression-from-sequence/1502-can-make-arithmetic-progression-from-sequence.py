class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff=abs(arr[0]-arr[1])
        for i in range(2,len(arr)):
            d=abs(arr[i]-arr[i-1])
            print(d)
            if d!=diff:
                return False
        return True