# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val                # Value of the node
#         self.left = left              # Pointer to the left child
#         self.right = right            # Pointer to the right child

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We use self.count to track how many nodes we have visited in in-order traversal
        self.count = 0

        # ❓ Why use self.result as a separate variable?
        # - To avoid complex return chaining through recursive calls.
        # - To allow early exit once the kth smallest is found.
        # - Makes the code easier to read and maintain.
        self.result = None

        # Define the helper function for in-order traversal
        def inorder(node):
            # If node is None or kth element already found, stop recursion
            if not node or self.result is not None:
                return

            # Traverse the left subtree (smaller values)
            inorder(node.left)

            # Visit the current node
            self.count += 1  # Count this node
            if self.count == k:
                self.result = node.val  # Found kth smallest value
                return  # Stop further traversal

            # Traverse the right subtree (larger values)
            inorder(node.right)

        # Start in-order traversal from the root
        inorder(root)

        # Return the stored result
        return self.result


# \U0001f9ea Dry Run Example
# Input BST:
#       3
#      / \
#     1   4
#      \
#       2
#
# In-order Traversal: 1 → 2 → 3 → 4
# Goal: Find the 1st smallest element (k = 1)
#
# Step-by-step Execution:
# 1. Start at root (3), go left → node = 1
# 2. At node 1, go left → None → return
# 3. Visit node 1 → count = 1 → count == k → result = 1 → return
# 4. Since result is found, all remaining recursive calls return early
#
# ✅ Final Output: 1
