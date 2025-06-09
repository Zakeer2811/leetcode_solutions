class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def b2d(bi, ind, res=0):
            if ind == len(bi):
                return res
            res += int(bi[ind]) * (2 ** (len(bi) - (ind + 1)))
            return b2d(bi, ind + 1, res)

        def d2b(n):
            if n == 0:
                return ''
            return d2b(n // 2) + str(n % 2)
        if a=='0' and b=='0':
            return '0'
        return d2b(b2d(a,0)+b2d(b,0))

        