class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        result = []
        current = root

        while current:
            if not current.left:
                # CASE 1: No left child
                # ➤ Visit current and go to right
                result.append(current.val)
                current = current.right
            else:
                # CASE 2: Has left child
                # ➤ Find the inorder predecessor (rightmost node in left subtree)
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    # THREADING
                    # ➤ Visit current before creating thread (Preorder: Root → Left → Right)
                    result.append(current.val)

                    # \U0001f517 Diagram before threading:
                    #        current
                    #        /     \
                    #    left     right
                    #      \
                    #   predecessor -> None
                    #
                    # \U0001f504 Becomes:
                    #   predecessor -> current (thread created)
                    
                    predecessor.right = current  # Create thread to return later
                    current = current.left       # Move to left child
                else:
                    # THREAD ALREADY EXISTS
                    # ➤ Left subtree has been visited, remove thread
                    predecessor.right = None
                    current = current.right      # Move to right child

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

Preorder: [1, 2, 3]

Traversal steps:
1. current = 1
   - No left → visit 1 → move to 2

2. current = 2
   - Has left → find predecessor (3)
   - Visit 2, create thread 3.right → 2
   - Move to 3

3. current = 3
   - No left → visit 3 → move to 2 (via thread)

4. current = 2
   - Thread exists → remove it
   - Move to right (None)

FINAL PREORDER: [1, 2, 3]


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

Preorder: [1,2,4,5,6,7,3,8,9]

Threading happens between:
- 4 → 2
- 6 → 5
- 7 → 2
- 5 → 1
- 9 → 3
- 8 → 1

Each thread is used to return to parent after left traversal is done.
Visit current BEFORE threading (since Preorder = visit before left).

----------------------------------------------------

Why Morris Preorder Traversal?
- Saves space (O(1) vs O(h) in stack/recursive methods)
- Tree is restored
- Visits in Preorder using same threading trick as Inorder
✅ Summary of Preorder Morris Traversal:

What is Preorder Traversal?
➤ Preorder visits nodes in the order:
\U0001f449 Root → Left → Right

What is Morris Preorder Traversal?
➤ It’s similar to Morris Inorder, but we:
   - Visit the node when we first reach it (before going to the left)
   - Still create a thread from the predecessor’s right to the current node
   - But visit current before threading, not after returning via the thread

Comparison:

| Step                  | Morris Inorder          | Morris Preorder             |
|-----------------------|--------------------------|------------------------------|
| When to visit node    | After left subtree       | Before going to left subtree |
| Threading direction   | From predecessor → curr  | Same                         |
| When thread removed   | When returning from left | Same                         |
| Space                 | O(1)                     | O(1)                          |
| Extra Data Structures | None                     | None                          |

----------------------------------------------------

"""
