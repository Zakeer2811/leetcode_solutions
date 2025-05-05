class Solution:
    def toHex(self,num):
        # Special case for 0
        if num == 0:
            return "0"
        
        # If the number is negative, convert it to its 32-bit two's complement
        if num < 0:
            num += 2**32
        
        hex_chars = "0123456789abcdef"
        result = ""
        
        # Convert the number to hex by repeatedly dividing by 16
        while num > 0:
            result = hex_chars[num % 16] + result
            num //= 16
        
        return result
# def toBaseN(num, base):
#     # Digits for bases greater than 10
#     digits = "0123456789abcdef"  
    
#     # Handle the special case of zero
#     if num == 0:
#         return "0"
    
#     # Handle negative numbers (convert to two's complement for base n)
#     if num < 0:
#         num += base ** 32  # Assuming 32-bit two's complement
    
#     result = ""
    
#     # Convert number to the desired base
#     while num > 0:
#         result = digits[num % base] + result  # Get the remainder and map to the corresponding digit
#         num //= base  # Integer division by base
    
#     return result
