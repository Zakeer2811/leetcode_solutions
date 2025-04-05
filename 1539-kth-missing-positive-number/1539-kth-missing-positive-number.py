class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l=[i for i in range(max(arr)+k+1) if i not in arr]
        return l[k]
        
        