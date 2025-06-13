class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Helper function that performs the actual insertion
        def helper(root, val):
            # Base Case: If we reach an empty spot (None), it means we can insert the new value here
            if not root:
                return TreeNode(val)  # Create a new node with the value 'val' and return it as the new root of the subtree
            
            # Recursive Case: We are in the correct spot, but we need to decide whether to go left or right
            if val < root.val:  # If val is smaller than the root's value, insert it in the left subtree
                root.left = helper(root.left, val)  # Recurse to the left child and update root.left
            else:  # If val is greater or equal to the root's value, insert it in the right subtree
                root.right = helper(root.right, val)  # Recurse to the right child and update root.right
            
            # Return the root at the end of recursion to maintain the structure of the tree
            return root  # We return 'root' because, after the insertion, the entire tree structure should stay intact

        # Main function starts here:
        # `return helper(root, val)` is the correct approach, because we need the recursive function to properly
        # propagate the updates back to the root. Simply returning `root` would break the recursive propagation
        return helper(root, val)  # This will return the updated root of the tree after insertion
        
        
# --------------------------------------------------------------
# Dry Run Example

# Let's dry run the function with the following initial tree:
#      4
#     / \
#    2   7
#   / \
#  1   3
#
# And we will insert the value `5`.

# Initial function call:
# insertIntoBST(root, 5)

# The current tree looks like this:
#      4
#     / \
#    2   7
#   / \
#  1   3
#
# The root is 4, and we are trying to insert 5.

# 1. Call helper(root = 4, val = 5):
#    - root.val (4) is less than 5, so we go to the right subtree.
#    - Now we call helper(root = 7, val = 5).
#
# 2. Call helper(root = 7, val = 5):
#    - root.val (7) is greater than 5, so we go to the left subtree.
#    - Now we call helper(root = None, val = 5) because the left child of 7 is None.
#
# 3. Call helper(root = None, val = 5):
#    - root is None, so we create a new node with value 5.
#    - Return the newly created node (TreeNode(val = 5)).
#
# 4. Returning to helper(root = 7, val = 5):
#    - We update the left child of 7 to be the newly created node (TreeNode(val = 5)).
#    - Now we return root (TreeNode(val = 7)) with its updated left child.
#
# 5. Returning to helper(root = 4, val = 5):
#    - We update the right child of 4 to be the updated root (TreeNode(val = 7)).
#    - Now we return root (TreeNode(val = 4)) with its updated right child.
#
# The final tree structure is:
#
#      4
#     / \
#    2   7
#   / \  /
#  1   3 5
#
# Now, we have successfully inserted the value 5 into the Binary Search Tree.

# --------------------------------------------------------------

# Difference between `return helper(...)` and `return root`:

# 1. **Using `return helper(root, val)`**:
#    - The `helper(root, val)` call is necessary because it performs the recursion.
#    - **Recursion** ensures that the entire tree structure gets updated properly.
#    - The recursive call updates the tree by modifying the parent-child relationships (like `root.left` or `root.right`).
#    - When `helper` finishes its work, it returns the updated root node, ensuring the tree structure is correct.
#    - **Example**: In the case of the value `5`, the recursion updates the left child of `7` and the right child of `4`.
#    - This ensures that all parent-child relationships in the tree are updated correctly.

# 2. **Using `return root` directly** (Incorrect Approach):
#    - Returning just `root` without `helper(...)` would break the recursion.
#    - When you return `root` directly after modifying `root.left` or `root.right`, you do not properly **propagate** the updates made to the left and right subtrees.
#    - The recursive calls would still insert the new node correctly, but the **parent-child relationships** may not be properly set, leading to an incomplete tree structure.
#    - **Problem**: You might end up with the wrong tree structure because the child pointers (`root.left` or `root.right`) are not being updated properly when `root` is returned.
#    - The main issue with `return root` is that it **does not propagate the changes** made in the recursive calls to the parent node.
#    - **Example**: If you return `root` at the start, the recursive call that updates `root.left` or `root.right` may not propagate correctly, and the insertion might not be reflected in the parent node.

# Conclusion:
# - **`return helper(root, val)`** is the correct approach because it allows the recursion to propagate the updated tree structure back to the root.
# - **`return root`** would be incorrect because it would not ensure that the child pointers are correctly updated, which could lead to an incomplete or incorrect tree structure.
