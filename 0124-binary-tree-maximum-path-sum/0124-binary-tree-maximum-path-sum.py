# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node, maxi):
            if not node:
                return 0  # Base case: null node contributes 0

            # Recurse on left child
            leftpathsum = max(helper(node.left, maxi), 0)

            # Recurse on right child
            rightpathsum = max(helper(node.right, maxi), 0)

            # -------- Recursion Explanation --------
            # Example: For node = 20
            # leftpathsum = 15 (from node 15)
            # rightpathsum = 7 (from node 7)
            # current_max = 20 + 15 + 7 = 42
            # Update maxi[0] if 42 > previous value

            # Compute current path sum through this node
            current_max = node.val + leftpathsum + rightpathsum

            # Update global max path sum if current is greater
            maxi[0] = max(maxi[0], current_max)

            # -------- Return Path to Parent --------
            # We can only take one side (left or right) upward in the path
            # Example: For node = 20, return 20 + max(15, 7) = 35
            return node.val + max(leftpathsum, rightpathsum)

        # Global maximum (mutable list so it can be updated in recursion)
        maxi = [float('-inf')]

        # Start DFS traversal
        helper(root, maxi)

        # Final answer
        return maxi[0]
