# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:
    def serialize(self, root):
        """
        Encodes a binary tree to a single string using level-order traversal.

        :param root: TreeNode, root of the binary tree
        :return: str, serialized tree representation
        """
        if not root:
            # If tree is empty, represent with '#'
            return "#"

        result = []  # To store serialized node values or '#' for None nodes
        queue = deque([root])  # Queue for BFS traversal starting from root

        while queue:
            node = queue.popleft()

            if node:
                # Add current node's value as string
                result.append(str(node.val))
                # Enqueue left and right children (even if None)
                queue.append(node.left)
                queue.append(node.right)
            else:
                # Use '#' to represent None (missing node)
                result.append("#")

        # Join all parts with space to form final string
        return ' '.join(result)


    def deserialize(self, data):
        """
        Decodes your encoded data to binary tree using array indexing.
        
        :param data: str, serialized tree string
        :return: TreeNode, root of the reconstructed binary tree
        """
        if data == "#":
            # If data is just '#', tree is empty
            return None

        nodes = data.split()  # Split serialized string by spaces
        n = len(nodes)  # Total number of entries (nodes + '#')

        # Create an array to hold TreeNode objects or None
        tree_nodes = [None] * n

        # Step 1: Instantiate TreeNode objects for non-# entries
        for i in range(n):
            if nodes[i] != "#":
                tree_nodes[i] = TreeNode(int(nodes[i]))

        # Step 2: Link children using the formula for a binary heap:
        # Left child index = 2*i + 1
        # Right child index = 2*i + 2
        for i in range(n):
            if tree_nodes[i] is not None:
                left_index = 2 * i + 1
                right_index = 2 * i + 2

                # Link left child if within bounds
                if left_index < n:
                    tree_nodes[i].left = tree_nodes[left_index]

                # Link right child if within bounds
                if right_index < n:
                    tree_nodes[i].right = tree_nodes[right_index]

        # The root of the tree is at index 0
        return tree_nodes[0]

