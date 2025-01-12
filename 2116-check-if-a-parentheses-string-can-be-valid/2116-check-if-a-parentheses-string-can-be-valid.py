class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        
        if n % 2 != 0:
            return False
        
        balance = 0
        
        # First check balance from left to right for opening '(' brackets
        for i in range(n):
            if locked[i] == '0' or s[i] == '(':
                balance += 1
            else:
                balance -= 1
                
            if balance < 0:
                return False
        
        # Reset balance
        balance = 0
        
        # Then check balance from right to left for closing ')' brackets
        for i in range(n - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                balance += 1
            else:
                balance -= 1
            
            if balance < 0:
                return False
        
        return True
