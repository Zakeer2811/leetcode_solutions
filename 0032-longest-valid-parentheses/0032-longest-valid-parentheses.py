class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
       
        max_length = 0
        
        # Left to Right Pass
        left_count = right_count = 0
        for char in s:
            if char == '(':
                left_count += 1
            else:  # char == ')'
                right_count += 1
            
            if left_count == right_count:
                len1=left_count+right_count
                max_length = max(max_length, len1)
            elif right_count > left_count:
                left_count = right_count = 0
        
        # Right to Left Pass
        left_count = right_count = 0
        for char in reversed(s):
            if char == '(':
                left_count += 1
            else:  # char == ')'
                right_count += 1
            
            if left_count == right_count:
                len1=left_count+right_count
                max_length = max(max_length, len1)
            elif left_count > right_count:
                left_count = right_count = 0
        
        return max_length
