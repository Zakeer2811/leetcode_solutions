class Solution:
    MOD = 10**9 + 7  # Modulo constant
    
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # Initialize the frequency array for characters 'a' to 'z'
        freq = [0] * 26  # There are 26 lowercase English letters
        
        # Count the frequency of each character in the initial string s
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        # Apply t transformations
        for _ in range(t):
            # Create a new frequency array for the next transformation
            new_freq = [0] * 26
            
            for i in range(26):
                if freq[i] > 0:
                    if i == 25:  # If it's 'z', it turns into 'ab' (i.e., new 'a' and 'b')
                        new_freq[0] = (new_freq[0] + freq[i]) % self.MOD  # 'a' increases
                        new_freq[1] = (new_freq[1] + freq[i]) % self.MOD  # 'b' increases
                    else:
                        new_freq[i + 1] = (new_freq[i + 1] + freq[i]) % self.MOD  # Next character in the alphabet
            
            # Move to the next transformation with the updated frequency array
            freq = new_freq
        
        # Calculate the total length of the string after t transformations
        length = sum(freq) % self.MOD
        
        return length
