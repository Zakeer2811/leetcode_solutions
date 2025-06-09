class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        rev = 0
        n = x  # Store the original value of x
        
        if n < 0:
            return False
        else:
            while n != 0:
                r = n % 10
                rev = (rev * 10) + r
                n = n // 10  # Use integer division to update n
            if rev == x:  # Compare with the original value, not n
                return True
            else:
                return False



        

        
        
            
        
         
            
            
         
        
            


