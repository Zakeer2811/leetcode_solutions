class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        
        # There are 2^n possible subsets
        total_subsets = 1 << n  # 2^n
        
        for i in range(total_subsets):
            subset = []
            for j in range(n):
                # Check if the jth bit in the integer i is set. If set, include nums[j]
                if i & (1 << j):
                    subset.append(nums[j])
            subsets.append(subset)
        
        return subsets