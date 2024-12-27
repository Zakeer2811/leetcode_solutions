class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            if n <= 1:  # Fix to handle numbers less than or equal to 1
                return False
            isprime = 1
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    isprime = 0
                    break
            return isprime

        ans = 0
        for i in range(left, right + 1):
            b = bin(i)[2:]
            c = b.count('1')
            if isPrime(c):
                ans += 1
        return ans
