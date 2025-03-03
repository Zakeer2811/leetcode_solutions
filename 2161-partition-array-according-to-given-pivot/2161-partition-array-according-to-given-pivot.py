class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l1=[]
        l2=[]
        l3=[]
        for i in nums:
            if i<pivot:
                l1.append(i)
        for i in nums:
            if i==pivot:
                l2.append(i)
        for i in nums:
            if i>pivot:
                l3.append(i)
        l1+=l2+l3
        return l1
        