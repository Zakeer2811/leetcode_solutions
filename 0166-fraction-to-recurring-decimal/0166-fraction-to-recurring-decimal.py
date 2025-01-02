class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        # Result string
        res = []
        
        # Handle the sign
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        
        # Use absolute values to simplify calculation
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Add the integral part
        res.append(str(numerator // denominator))
        
        # Get the remainder
        remainder = numerator % denominator
        
        # If there's no remainder, we're done
        if remainder == 0:
            return ''.join(res)
        
        res.append('.')
        
        # Dictionary to detect cycles
        seen_remainders = {}
        
        # Process the fractional part
        while remainder != 0:
            if remainder in seen_remainders:
                # Insert the repeating part in parentheses
                res.insert(seen_remainders[remainder], '(')
                res.append(')')
                break
            
            # Record the position of this remainder
            seen_remainders[remainder] = len(res)
            
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        
        return ''.join(res)
