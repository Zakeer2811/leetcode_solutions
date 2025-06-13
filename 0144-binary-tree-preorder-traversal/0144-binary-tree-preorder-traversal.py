# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        st = [root]
        preorder = []

        while st:
            node = st.pop()
            preorder.append(node.val)

            # Push right first so left is processed first
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)

        return preorder
