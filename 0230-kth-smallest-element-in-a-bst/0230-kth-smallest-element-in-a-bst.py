# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val                # Value of the node
#         self.left = left              # Pointer to left child
#         self.right = right            # Pointer to right child

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We use self.count to keep track of how many nodes we've visited in-order so far.
        self.count = 0
        
        # We use self.result to store the kth smallest value when we reach it.
        # This avoids having to return values up through multiple recursive calls.
        self.result = None

        def inorder(node):
            # Base case: If node is None or result is already found, return immediately
            if not node or self.result is not None:
                return

            # Traverse the left subtree first (in-order traversal starts with left)
            inorder(node.left)

            # Process the current node
            self.count += 1  # We've visited one more node
            if self.count == k:
                # If current node is the kth node visited, store its value as the result
                self.result = node.val
                return  # No need to continue traversal

            # Traverse the right subtree after processing current node
            inorder(node.right)

        # Start in-order traversal from the root
        inorder(root)

        # Return the result found during traversal
        return self.result
