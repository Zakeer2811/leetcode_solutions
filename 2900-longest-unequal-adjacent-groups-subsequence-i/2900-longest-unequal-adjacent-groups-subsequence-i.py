class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        ans = []
        flag = -1
        n=len(words)
        for i in range(n):
            if groups[i] != flag:
                flag = groups[i]
                ans.append(words[i])
        return ans
