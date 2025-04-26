class Solution:
    def diStringMatch(self,S: str) -> list[int]:
        res = [0] * (len(S) + 1)
        l, r = 0, len(S)
        
        for i in range(len(S)):
            if S[i] == 'I':
                res[i] = l
                l += 1
            else:
                res[i] = r
                r -= 1
        
        res[len(S)] = l
        return res
