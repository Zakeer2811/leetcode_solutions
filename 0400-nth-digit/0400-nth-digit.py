class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1
        
        # Step 2: Binary search for the correct range (length of the digits)
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        
        # Step 3: Find the actual number where the nth digit is located
        num = start + (n - 1) // length
        
        # Step 4: Find the exact digit in the number
        return int(str(num)[(n - 1) % length])