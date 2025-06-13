class BSTIterator:
    def __init__(self, root):
        """
        Initializes an iterator over the BST with the root node.
        The stack stores the path to the next smallest node.
        """
        self.stack = []
        self._pushLeftPath(root)  # Simulate in-order left traversal

    def hasNext(self):
        """
        Returns True if there's a next smallest node (i.e., stack is not empty).
        This checks whether more nodes remain to be visited.
        """
        return len(self.stack) > 0

    def next(self):
        """
        Returns the next smallest element in the BST.
        In-order means: Left → Node → Right.
        So:
        - Pop the top node (which is the current smallest)
        - If it has a right child, push all its left descendants (next smallest path)
        """
        # Node step: get the top element (leftmost unvisited node)
        current_node = self.stack.pop()

        # Right step: if there's a right subtree, push its leftmost path
        if current_node.right:
            self._pushLeftPath(current_node.right)

        return current_node.val

    def _pushLeftPath(self, node):
        """
        Helper function to push all nodes on the path from 'node'
        down to its leftmost child. This simulates the in-order traversal's
        'go left' part.

        Why? So that the top of the stack is always the next smallest element.
        """
        while node:
            self.stack.append(node)
            node = node.left  # Go left to find smaller nodes
# def inorderTraversal(root):
#     stack = []
#     result = []
#     current = root

#     while current or stack:
#         # Step 1: Go as left as possible
#         while current:
#             stack.append(current)  # Push current node to stack
#             current = current.left  # Move to left child

#         # Step 2: Process node
#         current = stack.pop()  # Left is done, process node
#         result.append(current.val)  # Visit the node

#         # Step 3: Move to right subtree
#         current = current.right  # Now process right subtree

#     return result
