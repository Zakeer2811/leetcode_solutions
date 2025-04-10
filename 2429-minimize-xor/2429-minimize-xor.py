class Solution:
    def minimizeXor(self, num1, num2):
        a, b = bin(num1).count('1'), bin(num2).count('1')
        res = num1
        for i in range(32):
            if ((a > b) - (a < b)) == ((1 << i) & num1 > 0.5) - ((1 << i) & num1 < 0.5):
                res ^= 1 << i
                a -= (a > b) - (a < b)
        return res
