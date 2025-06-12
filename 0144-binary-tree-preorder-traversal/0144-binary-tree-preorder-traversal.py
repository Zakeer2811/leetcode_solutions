# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        if root is not None:
            r.append(root.val)
            r+=self.preorderTraversal(root.left)
            r+=self.preorderTraversal(root.right)
        return r
        