class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # \U0001f50d Intuition:
        # We treat each node (subtree) as a "mini-tree".
        # If one target is found in the left subtree and the other in the right,
        # then the current root is where their paths split — the Lowest Common Ancestor.
        # If both are in one side, we keep searching down that side.

        # \U0001f6d1 Base case 1: If root is None, return None (end of path)
        if not root:
            return None

        # \U0001f6d1 Base case 2: If root is either p or q, we found one of the nodes
        # This could be a potential LCA if the other node is found below.
        if root == p or root == q:
            return root

        # \U0001f501 Recursive calls: Search for p and q in left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # ✅ If both left and right return non-null, that means:
        # One node is found in the left subtree and the other in the right
        # So, current node is their Lowest Common Ancestor
        if left_lca and right_lca:
            return root

        # ↩️ If only one side is non-null, return that one.
        # It means both p and q are in that subtree, or we've only found one so far.
        return left_lca if left_lca else right_lca
'''
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
Call: LCA(3, 5, 1)
- root = 3
- Not equal to p or q → go left and right

  Call: LCA(5, 5, 1)
  - root == p → return 5          ← [Case 2]

  Call: LCA(1, 5, 1)
  - root == q → return 1          ← [Case 2]

← Now back at LCA(3):
- left_lca = 5
- right_lca = 1
- both are non-null → return 3    ← [Case 3]

Answer: 3 (Lowest Common Ancestor)

'''