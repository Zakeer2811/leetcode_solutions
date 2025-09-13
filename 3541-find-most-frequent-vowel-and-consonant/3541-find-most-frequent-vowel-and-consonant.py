class Solution:
    def maxFreqSum(self, s: str) -> int:
        c=Counter(s)
        va=0
        vc=0
        for k,v in c.items():
            if k.lower() in 'aeiou':
                va=max(va,v)
            else:
                vc=max(vc,v)
        return va+vc

        