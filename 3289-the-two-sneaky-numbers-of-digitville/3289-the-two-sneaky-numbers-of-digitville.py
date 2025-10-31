class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        return [e for e in c.keys() if c[e]==2]