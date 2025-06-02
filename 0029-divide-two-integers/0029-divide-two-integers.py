class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Edge case: Overflow case
        # If the dividend is the minimum 32-bit integer and the divisor is -1,
        # the result would overflow (it would exceed 2^31), so we return the max 32-bit value.
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # 2^31 - 1 is the maximum value for a 32-bit signed integer
        
        # Determine the sign of the result
        # The XOR operator `^` is used to determine if the signs of the dividend and divisor are opposite
        # If the signs are different, the result will be negative (sign=True).
        sign = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values to simplify the logic, as dividing negative values directly can be tricky
        # We take the absolute value of both the dividend and divisor to avoid negative number handling.
        numerator = abs(dividend)
        denominator = abs(divisor)
        
        # Initialize the result
        ans = 0
        
        # The main loop that performs the division
        # While the numerator (dividend) is larger than or equal to the denominator (divisor),
        # we keep subtracting multiples of the denominator from the numerator.
        while numerator >= denominator:
            # We initialize a counter to track how many times we can double the denominator (power of 2).
            cnt = 0
            
            # This inner loop finds the largest multiple of the denominator that fits into the numerator.
            # Instead of dividing by the denominator repeatedly, we shift the denominator left
            # (which is equivalent to multiplying by powers of 2) and check if it fits in the numerator.
            # We use `denominator << (cnt + 1)` to check the next power of two, where `<<` is a left shift operator.
            # It’s equivalent to `denominator * 2^(cnt + 1)`.
            while denominator << (cnt + 1) <= numerator:
                cnt += 1
            
            # Once the largest power of 2 multiple is found, subtract that multiple from the numerator.
            # `denominator << cnt` gives us `denominator * 2^cnt`, which is the largest multiple of 
            # the denominator that fits in the numerator.
            numerator -= denominator << cnt  # Equivalent to: numerator -= denominator * 2^cnt
            
            # Add the corresponding power of 2 to the result.
            # `1 << cnt` is equivalent to `2^cnt`. We add it to `ans` because we know that the largest multiple
            # of the denominator that we just found contributes `2^cnt` to the quotient.
            ans += 1 << cnt  # Equivalent to: ans += 2^cnt
        
        # Apply the sign: if the result should be negative, we negate the answer.
        if sign:
            ans = -ans
        
        # Overflow check: 
        # Ensure that the result fits within the 32-bit integer range.
        # The minimum 32-bit signed integer is -2^31 and the maximum is 2^31 - 1.
        if ans < -2**31:
            return -2**31  # Return the minimum 32-bit value
        if ans > 2**31 - 1:
            return 2**31 - 1  # Return the maximum 32-bit value
        
        return ans
