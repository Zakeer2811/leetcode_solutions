class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
       Intuition:
        In a Binary Search Tree (BST), for any node:
            - All values in the left subtree are less than node.val
            - All values in the right subtree are greater than node.val

        So, to find the Lowest Common Ancestor (LCA) of nodes p and q:
            - If both p and q are smaller than root → LCA lies in left subtree
            - If both p and q are greater than root → LCA lies in right subtree
            - If one is on the left and one is on the right (or root == p or root == q) →
              the current root is the **split point** and hence the LCA

        This works because the first node where the path to p and q diverge is the
        lowest (i.e., deepest) common ancestor in a BST.

        So, to find the LCA of nodes p and q:

        ➤ If both p and q are smaller than root → LCA must lie in the left subtree
        ➤ If both p and q are greater than root → LCA must lie in the right subtree
        ➤ If we cannot decide (i.e., one is on the left and the other on the right), OR
          one of them is equal to the current node → then the current node is the **split point**
          where their paths diverge → hence, it is the **Lowest Common Ancestor**
        Why This Works:
            The moment we can’t confidently go entirely left or right, we’ve reached the lowest node that connects both paths.

            That node is the LCA because it's the first point from the root where the paths to p and q split.
        ✅ Example of the split point:
            root = 8, p = 5, q = 9
            → p is on the left, q is on the right → root 8 is the LCA
        """

        while root:
            if p.val < root.val and q.val < root.val:
                # Both nodes are smaller → go to the left subtree
                root = root.left
            elif p.val > root.val and q.val > root.val:
                # Both nodes are greater → go to the right subtree
                root = root.right
            else:
                # Split point: either nodes are on different sides,
                # or one of them is the current node → this is the LCA
                return root
