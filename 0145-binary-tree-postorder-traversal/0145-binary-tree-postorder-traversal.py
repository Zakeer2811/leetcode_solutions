# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        if root is not None:
            r += self.postorderTraversal(root.left)
            r += self.postorderTraversal(root.right)
            r.append(root.val)
        return r
