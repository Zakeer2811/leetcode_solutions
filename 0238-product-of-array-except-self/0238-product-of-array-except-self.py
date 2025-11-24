class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left_product=[1]*n
        right_product=[1]*n
        for i in range(1,n):
            left_product[i]=left_product[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            right_product[i]=right_product[i+1]*nums[i+1]
        result=[i*j for i,j in zip(left_product,right_product)]
        return result
        