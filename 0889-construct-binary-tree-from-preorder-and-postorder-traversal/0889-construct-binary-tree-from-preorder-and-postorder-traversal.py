# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        if len(preorder) == 1:
            return root
        # Find the left root in postorder to determine the split
        left_root_val = preorder[1]
        left_size = postorder.index(left_root_val) + 1  # Size of the left subtree
        # Split preorder and postorder for left and right subtrees
        root.left = self.constructFromPrePost(preorder[1:1 + left_size], postorder[:left_size])
        root.right = self.constructFromPrePost(preorder[1 + left_size:], postorder[left_size:-1])
        return root