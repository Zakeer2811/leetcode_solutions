# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def order(root):
            if not root:
                return 0
            left_count = order(root.left)
            right_count = order(root.right)
            return 1 + left_count + right_count
        return order(root)

        
        