class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        result = []
        current = root  # Start from the root

        while current:
            if not current.left:
                # CASE 1: No left child
                # ➤ Visit this node and move to right
                result.append(current.val)
                current = current.right
            else:
                # CASE 2: Has left child
                # ➤ Find the rightmost node in left subtree (predecessor)
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    # THREADING:
                    # ➤ Create a thread from predecessor back to current
                    #    so we can return after left subtree is done
                    predecessor.right = current
                    
                    # \U0001f517 Diagram before threading:
                    #        current
                    #        /     \
                    #    left     right
                    #      \
                    #   predecessor -> None
                    #
                    # \U0001f504 Becomes:
                    #   predecessor -> current (thread created)
                    
                    current = current.left  # Move to left subtree
                else:
                    # THREAD ALREADY EXISTS:
                    # ➤ Time to break the thread (left is already visited)
                    predecessor.right = None  # Remove the thread
                    result.append(current.val)  # Visit current
                    current = current.right     # Move to right subtree

        return result


"""
VISUALIZATION OF THREADING:

Example Input:
    1
     \
      2
     /
    3

Tree structure:

      1
       \
        2
       /
      3

Inorder: [1, 3, 2]

Traversal steps:
1. current = 1
   - No left → visit 1 → move to 2

2. current = 2
   - Has left → find predecessor (3)
   - Thread 3.right → 2
   - Move to 3

3. current = 3
   - No left → visit 3 → move to 2 (via thread)

4. current = 2
   - Thread exists → remove it
   - Visit 2 → move to right (None)

FINAL INORDER: [1, 3, 2]


----------------------------------------------------

Edge Case Example:
Input: []  (empty tree)
Output: []

Input: [1]
     1
Output: [1]

Input: [1,2,3,4,5,null,8,null,null,6,7,9]

            1
           / \
          2   3
         / \     \
        4   5     8
           / \     \
          6   7     9

Inorder: [4,2,6,5,7,1,3,9,8]
Threading happens between:
- 4 → 2
- 6 → 5
- 7 → 2
- 5 → 1
- 9 → 3
- 8 → 1

At each node, thread is created before going left, and removed when returning to the node after left subtree is done.

This creates a space-efficient traversal.

----------------------------------------------------

Why Morris Traversal?
- Saves space (O(1) vs O(h) in stack/recursive methods)
- Restores tree to original after traversal
- Elegant handling of tree navigation via temporary threading

"""
