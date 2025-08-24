class Solution:
    def isUgly(self, n: int) -> bool:
        def is_divisible_by_2(n):
            return str(n)[-1] in '02468'

        def is_divisible_by_3(n):
            return sum(int(d) for d in str(n)) % 3 == 0

        def is_divisible_by_5(n):
            return str(n)[-1] in '05'

       
        if n <= 0:
            return False

        while is_divisible_by_2(n):
            n //= 2
        while is_divisible_by_3(n):
            n //= 3
        while is_divisible_by_5(n):
            n //= 5

        return n == 1
