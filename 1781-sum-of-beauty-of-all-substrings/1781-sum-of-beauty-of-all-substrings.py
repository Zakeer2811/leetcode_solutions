class Solution:
    def beautySum(self, s: str) -> int:
        def helper(s1):
            freq = Counter(s1)
            return max(freq.values()) - min(freq.values()) if freq else 0
        ans=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                ans+=helper(s[i:j])
        return ans
        