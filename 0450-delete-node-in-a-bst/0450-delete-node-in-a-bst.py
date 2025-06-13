from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_max_in_left_subtree(node):
            while node.right is not None:
                node = node.right
            return node
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            successor = find_max_in_left_subtree(root.left)
            root.val = successor.val
            root.left = self.deleteNode(root.left, successor.val)
        return root
