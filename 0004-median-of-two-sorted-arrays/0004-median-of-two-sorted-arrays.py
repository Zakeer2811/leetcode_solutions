class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=sorted(nums1+nums2)
        l=len(m)
        if l%2==1:
            return m[l//2]
        else:
            return (m[l//2]+m[l//2-1])/2