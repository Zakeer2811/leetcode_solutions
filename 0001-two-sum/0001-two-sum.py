class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i, v in enumerate(nums):
            map1[v] = i
        
        for i, v in enumerate(nums):
            complement = target - v
            if complement in map1 and map1[complement] != i:
                return [i, map1[complement]]