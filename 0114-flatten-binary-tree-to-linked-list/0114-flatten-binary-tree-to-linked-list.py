# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
"""
        Do not return anything, modify root in-place instead.
"""
"""
        Flatten the binary tree to a linked list in place using reverse preorder traversal.
        We process the tree in the reverse preorder order (Right -> Left -> Root),
        which ensures that we flatten the tree into a right-skewed linked list.
        
        This method mutates the tree by setting each node's left pointer to None
        and the right pointer to the next node in the preorder traversal.
        
        Intuition behind Reverse Preorder Traversal:
        
        - **Preorder Traversal (Root -> Left -> Right)**: The goal is to flatten the binary tree into a 
          linked list where the nodes follow the preorder sequence.
          
        - **Reverse Preorder Traversal (Right -> Left -> Root)**:
          - By visiting the **right subtree first**, we can link the right pointer of the current node to 
            the next node in the preorder sequence.
          - By visiting the **left subtree next**, we ensure that the left child of each node is set to `None`,
            effectively flattening the tree into a right-skewed linked list.
          - Finally, the **root** is processed after its children are linked, maintaining the correct order in 
            the linked list.
        
        Why Reverse Preorder?
        - **Preorder**: We visit the root first, then its left subtree, and then the right subtree.
        - **Reverse Preorder**: We first visit the **right subtree**, then the **left subtree**, and finally the **root**.
        - By using reverse preorder, we ensure that the `right` pointer is set correctly to the next node in the preorder sequence.
        
        Dry Run Example:
        
        Given a tree:
        
            1
           / \
          2   5
         / \   \
        3   4   6
        
        We want to flatten it to:
        
        1 -> 2 -> 3 -> 4 -> 5 -> 6
        
        Steps:
        1. Start with the root node 1.
        2. Process right subtree of 1 (node 5):
            - Visit 5 → Traverse right (6) → Visit 6 → Link 5's right to 6.
            - Set 5's left to None.
        3. Process left subtree of 1 (node 2):
            - Visit 2 → Traverse right (4) → Visit 4 → Link 2's right to 4.
            - Set 2's left to None.
        4. Process left subtree of 2 (node 3): Visit 3 → Link 2's right to 3.
        
        Final tree after flattening:
        1 -> 2 -> 3 -> 4 -> 5 -> 6
        
        Time Complexity:
        - O(n), where n is the number of nodes. We visit each node exactly once.
        
        Space Complexity:
        - O(h), where h is the height of the tree. In the worst case (skewed tree), the space complexity is O(n),
          but for a balanced tree, it is O(log n).
        """
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        TreeNode constructor that initializes a tree node with a given value,
        and optional left and right child pointers (default is None).
        """
        self.val = val  # Value of the node
        self.left = left  # Left child pointer
        self.right = right  # Right child pointer


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Flattens the binary tree into a right-skewed tree (like a linked list)
        following preorder traversal order. The tree is modified in-place with
        O(1) extra space (i.e., no additional data structures are used).
        
        Intuition Behind the Algorithm:
        --------------------------------
        Preorder Traversal (Root → Left → Right):
        - In preorder traversal, we visit nodes in the order: Root → Left → Right.
        - To flatten the binary tree into a linked list in preorder, we need to visit each node before its children,
          and link the nodes in a **right-skewed manner**. The `right` child of each node should point to the next node in the preorder traversal.

        Using Recursion:
        ----------------
        - We use **reverse preorder** (right → left → root) to ensure that the right pointer of each node gets linked to the correct node in the preorder order.
        - By visiting the right subtree first, we ensure that the nodes are linked in the correct order.

        Tracking the Last Flattened Node (`prev`):
        -----------------------------------------
        - As we traverse the tree, we need to track the last node we flattened (i.e., the node we visited and linked to the current node's `right` child).
        - This is done by passing the `prev` node through each recursive call, ensuring that the current node's `right` pointer is linked to the `prev` node.

        In-place Flattening:
        -------------------
        - We mutate the tree **in-place**, adjusting the pointers such that:
          - The **left pointer** of each node becomes `None`.
          - The **right pointer** of each node is linked to the next node in the preorder sequence.
        - No additional data structures are used, and no extra space is required, except for the recursion stack.

        Time Complexity:
        ----------------
        - **O(n)**, where `n` is the number of nodes in the binary tree. We visit each node exactly once during the recursion.

        Space Complexity:
        -----------------
        - **O(h)**, where `h` is the height of the tree due to the recursion stack. In the worst case (a skewed tree), the space complexity could be **O(n)**, but for a balanced tree, it would be **O(log n)**.
        """

        def reverse_preorder(node, prev):
            """
            This helper function performs a reverse preorder traversal (right → left → root) and flattens
            the binary tree into a linked list. The `prev` variable is passed around to keep track of the last
            flattened node that needs to be linked to the current node's right pointer.

            Args:
                node (TreeNode): Current node in the binary tree.
                prev (TreeNode or None): The last flattened node (initially None).
            
            Returns:
                TreeNode: The current node, which is the "previous" node for the next recursive call.
            """

            if not node:
                # Base case: if the current node is None, return the prev node (this indicates the end of a branch)
                return prev

            # Reverse Preorder Traversal: Right → Left → Root

            # Recursively flatten the right subtree
            prev = reverse_preorder(node.right, prev)

            # Recursively flatten the left subtree
            prev = reverse_preorder(node.left, prev)

            # Flatten the current node
            node.right = prev  # Link the current node's right child to the previous flattened node
            node.left = None   # Set the current node's left child to None (flattened list has no left children)

            # Move the "prev" pointer to the current node, so it can be linked to the next node in the next recursive call
            prev = node

            # Return the current node (now it becomes the "prev" for the parent node or higher levels)
            return prev

        # Start the flattening process from the root, with the initial "prev" as None
        reverse_preorder(root, None)

# Dry Run Example:
# Input: 
#        1
#       / \
#      2   5
#     / \   \
#    3   4   6
#
# Step 1: Start with root 1 and call reverse_preorder(1, None)
#
# Step 2: Process the tree in reverse preorder:
# - Traverse the right subtree of 1 (starting at node 5):
#   - Visit right subtree (6), flatten it: 6.right = None, 6.left = None.
#   - Link 5.right = 6, 5.left = None.
# - Traverse the left subtree of 1 (starting at node 2):
#   - Visit right subtree (4), flatten it: 4.right = None, 4.left = None.
#   - Link 2.right = 4, 2.left = None.
#   - Traverse the left subtree of 2 (starting at node 3), flatten it: 3.right = None, 3.left = None.
#   - Link 2.right = 3.
# Step 3: Flattened Tree: 1 -> 2 -> 3 -> 4 -> 5 -> 6
#
# Final flattened tree will look like this:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#
# Time Complexity: O(n), where n is the number of nodes in the binary tree. We visit each node exactly once.
#
# Space Complexity: O(h), where h is the height of the tree due to the recursion stack. In the worst case (a skewed tree), space complexity could be O(n). For a balanced tree, space complexity is O(log n).
