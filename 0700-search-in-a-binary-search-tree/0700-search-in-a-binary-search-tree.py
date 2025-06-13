class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Function to search for a value in a Binary Search Tree (BST).
        
        The algorithm leverages the BST property:
        - If val is greater than the current node's value, we search the right subtree.
        - If val is smaller, we search the left subtree.
        - If val equals the current node's value, we return the current node.
        
        Parameters:
        root (TreeNode): The root of the BST.
        val (int): The value to search for in the BST.
        
        Returns:
        TreeNode: The node where the value is found, or None if the value is not present.
        """
        
        # Base case: If the root is None, we return None (value is not found)
        if not root:
            return None
        
        # If the value is greater than the current node's value, search in the right subtree
        if val > root.val:
            return self.searchBST(root.right, val)
        
        # If the value is smaller than the current node's value, search in the left subtree
        elif val < root.val:
            return self.searchBST(root.left, val)
        
        # If the value equals the current node's value, we've found the node
        else:
            return root
