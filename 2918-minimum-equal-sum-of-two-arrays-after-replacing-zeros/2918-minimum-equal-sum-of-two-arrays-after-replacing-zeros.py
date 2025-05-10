class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize variables to count zeros and sum of non-zero elements
        nums1Zeroes = 0
        nums2Zeroes = 0
        sum1 = 0
        sum2 = 0
        # Calculate sum and count zeros for nums1
        for num in nums1:
            if num == 0:
                nums1Zeroes += 1
            sum1 += num
        
        # Calculate sum and count zeros for nums2
        for num in nums2:
            if num == 0:
                nums2Zeroes += 1
            sum2 += num
        
        # Minimum achievable sums for both arrays after replacing zeros with 1's
        min1 = sum1 + nums1Zeroes
        min2 = sum2 + nums2Zeroes
        
        # Case 1: If both arrays have no zeros
        if nums1Zeroes == 0 and nums2Zeroes == 0:
            return sum1 if sum1 == sum2 else -1
        
        # Case 2: If nums1 has no zeros, check if we can reach min2
        elif nums1Zeroes == 0:
            return sum1 if min2 <= sum1 else -1
        
        # Case 3: If nums2 has no zeros, check if we can reach min1
        elif nums2Zeroes == 0:
            return sum2 if min1 <= sum2 else -1
        
        # Case 4: Both arrays have zeros, return the max of min1 and min2
        return max(min1, min2)
