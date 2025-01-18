from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        # Initialize the write pointer
        write_index = 0
        read_index = 0
        n = len(chars)

        while read_index < n:
            char = chars[read_index]
            count = 0
            
            # Count consecutive characters
            while read_index < n and chars[read_index] == char:
                read_index += 1
                count += 1
            
            # Write the character to the result
            chars[write_index] = char
            write_index += 1
            
            # If the count is greater than 1, write the count as well
            if count > 1:
                for c in str(count):
                    chars[write_index] = c
                    write_index += 1
        
        return write_index
