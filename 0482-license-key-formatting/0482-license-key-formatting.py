class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s1=""
        for i in s:
            if i!='-':
                s1+=i.upper()
        n1=len(s1)
        res=""
        if n1%k==0:
            j=0
            for i in range(int(n1/k)):
                res+=s1[j:j+k]+"-"
                j+=k
        else:
            first=n1%k
            res=s1[:first]+"-"
            j=first
            for i in range(int(n1/k)):
                res+=s1[j:j+k]+"-"
                j+=k
        return res[:-1]

            