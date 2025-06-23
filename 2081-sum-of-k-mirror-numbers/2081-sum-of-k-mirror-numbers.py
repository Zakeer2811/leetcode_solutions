class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def decimal_to_base_k(n: int, k: int) -> str:
            if n == 0:
                return "0"
            result = ""
            while n > 0:
                result = str(n % k) + result
                n //= k
            return result

        count = 0
        num = 1
        total = 0

        while count < n:
            if is_palindrome(str(num)):
                base_k = decimal_to_base_k(num, k)
                if is_palindrome(base_k):
                    total += num
                    count += 1
            num += 1

        return total
