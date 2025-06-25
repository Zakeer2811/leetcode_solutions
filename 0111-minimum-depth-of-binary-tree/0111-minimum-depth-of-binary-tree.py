class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # If one of the subtrees is None, we return the depth of the other subtree + 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        # If both children exist, return the min depth of the two
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
