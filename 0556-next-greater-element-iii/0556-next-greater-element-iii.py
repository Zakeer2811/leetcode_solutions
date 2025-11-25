class Solution:
    def nextGreaterElement(self,n: int) -> int:
        # Convert the integer n to a list of digits
        digits = list(map(int, str(n)))
        
        # Step 1: Find the first pair from the right where digits[i] < digits[i+1]
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
            
        # If no such pair exists, the digits are sorted in non-increasing order
        if i == -1:
            return -1
        
        # Step 2: Find the smallest digit larger than digits[i] to the right of i
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        
        # Step 3: Swap digits[i] and digits[j]
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 4: Reverse the part of the list to the right of index i to get the smallest possible number
        digits = digits[:i + 1] + sorted(digits[i + 1:])
        
        # Convert the list of digits back to an integer
        result = int(''.join(map(str, digits)))
        
        # Check if the result is within the 32-bit signed integer range
        if result > 2**31 - 1:
            return -1
        return result
