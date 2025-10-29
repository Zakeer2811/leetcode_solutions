class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while (1 << x) - 1 < n:
            x += 1
        return (1 << x) - 1
