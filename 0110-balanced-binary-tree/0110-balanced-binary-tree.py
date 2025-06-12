# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Definition of a Balanced Binary Tree:
        - A binary tree is height-balanced if:
          For every node, the height difference between the left and right subtrees is at most 1.

        Process to check if a tree is balanced:
        - Perform post-order traversal (check left → right → node)
        - At each node:
            1. Compute the height of left and right subtrees.
            2. If either subtree is unbalanced, propagate -1.
            3. If height difference > 1, return -1.
            4. Otherwise, return 1 + max(left_height, right_height)
        """

        def check_balance(node):
            if not node:
                return 0  # Base case: height of empty tree is 0

            left_height = check_balance(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced

            right_height = check_balance(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced

            if abs(left_height - right_height) > 1:
                return -1  # Current node is not balanced

            return 1 + max(left_height, right_height)  # Return height if balanced

        return check_balance(root) != -1


# Example Tree:
#         1
#        / \
#       2   2
#      / \
#     3   3
#    / \
#   4   4

# Represented as: [1,2,2,3,3,null,null,4,4]

# Recursion Trace (post-order traversal):

# check_balance(4) → returns 1
# check_balance(4) → returns 1
# check_balance(3) → left=1, right=1 → balanced → returns 2
# check_balance(3) → returns 1 (leaf)
# check_balance(2) → left=2, right=1 → balanced → returns 3
# check_balance(2) (right child of root) → returns 1 (leaf)
# check_balance(1) → left=3, right=1 → abs(3-1) = 2 → Not balanced → returns -1

# Final output → False (tree is not balanced)
