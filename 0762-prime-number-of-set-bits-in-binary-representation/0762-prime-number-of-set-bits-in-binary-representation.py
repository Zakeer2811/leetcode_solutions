class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
            def isPrime(n):
                if n < 2:  # Numbers less than 2 are not prime
                    return False
                if n == 2:  # 2 is the only even prime
                    return True
                if n % 2 == 0:  # Eliminate other even numbers
                    return False
            # Check divisors from 3 to √n, skipping even numbers
                for i in range(3, int(n**0.5) + 1, 2):
                    if n % i == 0:
                        return False
                return True
            ans = 0
            for i in range(left, right + 1):
                b = bin(i)[2:]
                c = b.count('1')
                if isPrime(c):
                    ans += 1
            return ans
