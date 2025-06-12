# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            levels = len(q)
            temp = []

            for i in range(levels):
                node = q.popleft()
                temp.append(node.val)

                # First add right child, then left child (to prioritize rightmost)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

            # Add the first value from temp, which is the rightmost node of this level
            ans.append(temp[0])  # FIX: was using *temp which is invalid here

        return ans
