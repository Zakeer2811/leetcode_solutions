from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        temp = deque()  # Temporary deque for the next level
        q = deque([root])  # Initialize queue with root
        ans = []
        
        while q:
            max_val = float('-inf')  # Track max value for the current level
            
            for _ in range(len(q)):
                n = q.popleft()
                max_val = max(max_val, n.val)  # Update max value
                
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            
            ans.append(max_val)  # Store max value of the current level
            q = temp  # Move to the next level
            temp = deque()  # Reset temp for the next level
        
        return ans
