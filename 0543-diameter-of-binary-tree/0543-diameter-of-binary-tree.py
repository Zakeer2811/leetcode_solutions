# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Definition:
        - The diameter of a binary tree is the length of the longest path 
          between any two nodes. The path may or may not pass through the root.
        - The length is measured as the number of edges between nodes.

        Strategy:
        - Use post-order traversal to compute the height of left and right subtrees.
        - At each node, compute the path length as left_height + right_height.
        - Update the maximum diameter found so far.
        """

        self.max_diameter = 0  # This will hold the final maximum diameter

        def depth(node):
            if not node:
                return 0  # Base case: depth of empty subtree is 0

            # Recursively get depths of left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Diameter passing through this node = left + right
            current_diameter = left_depth + right_depth

            # Update global max diameter if current is larger
            self.max_diameter = max(self.max_diameter, current_diameter)

            # Return height of this node = 1 + max depth of its subtrees
            return 1 + max(left_depth, right_depth)

        # Start depth-first traversal
        depth(root)

        return self.max_diameter


# Example Tree:
#         1
#        / \
#       2   3
#      / \
#     4   5

# Input: [1,2,3,4,5]
# Path: [4,2,1,3] or [5,2,1,3]
# Edges in the longest path = 3 → Output: 3

# Recursion Trace (depth function):
# depth(4) → returns 1
# depth(5) → returns 1
# depth(2) → left=1, right=1 → update diameter to 2 → returns 2
# depth(3) → returns 1
# depth(1) → left=2, right=1 → update diameter to 3 → returns 3

# Final max_diameter = 3

# Why we return height:
# - To let parent nodes compute their own max path
# - height = 1 + max(left, right)
# - diameter at each node = left_height + right_height

# Time Complexity: O(n), where n is number of nodes
# Space Complexity: O(h), where h is height of the tree (stack space)
