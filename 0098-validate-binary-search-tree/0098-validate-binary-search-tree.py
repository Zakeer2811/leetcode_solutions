class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Intuition:
        A binary search tree (BST) must follow this rule:
        - All nodes in the left subtree must be strictly less than the current node's value
        - All nodes in the right subtree must be strictly greater than the current node's value

        We can use a recursive helper function that checks:
        - if each node lies within a valid range (min_val, max_val)
        - and updates this range as we go down the tree
        """

        # Helper function that recursively validates BST with bounds
        def isBST(node, min_val, max_val):
            if not node:
                # An empty subtree is always a valid BST
                return True

            # The current node's value must lie strictly between min_val and max_val
            if not (min_val < node.val < max_val):
                return False  # BST property violated

            # Recur on the left child:
            # All values in the left subtree must be < node.val,
            # so we update the max_val to node.val
            is_left_valid = isBST(node.left, min_val, node.val)

            # Recur on the right child:
            # All values in the right subtree must be > node.val,
            # so we update the min_val to node.val
            is_right_valid = isBST(node.right, node.val, max_val)

            # Both left and right subtrees must be valid BSTs
            return is_left_valid and is_right_valid

        # Initially, the entire range is (-∞, ∞) since there's no restriction on root
        return isBST(root, float('-inf'), float('inf'))
