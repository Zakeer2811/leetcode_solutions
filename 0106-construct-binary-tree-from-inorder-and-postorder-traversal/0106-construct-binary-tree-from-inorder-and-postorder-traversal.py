from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        # Pop the last element from postorder to get the root
        root_val = postorder.pop()
        root = TreeNode(root_val)

        # Find the index of the root value in inorder
        ind = inorder.index(root_val)

        # Build the right subtree first (since we are popping from the end of postorder)
        root.right = self.buildTree(inorder[ind + 1:], postorder)
        # Build the left subtree
        root.left = self.buildTree(inorder[:ind], postorder)

        return root
