from collections import deque

class Codec:
    def serialize(self, root):
        """
        Encodes a binary tree to a single string using level-order traversal.
        
        :param root: TreeNode, root of the binary tree
        :return: str, serialized tree representation
        """
        if not root:
            # If the tree is empty, represent it as a single '#'
            return "#"
        
        result = []  # List to store serialized node values or '#' for None
        queue = deque([root])  # Queue for BFS traversal, start with root
        
        while queue:
            node = queue.popleft()
            
            if node:
                # Append current node value as a string
                result.append(str(node.val))
                # Enqueue left and right children (even if they are None)
                queue.append(node.left)
                queue.append(node.right)
            else:
                # Use '#' to represent None (no node)
                result.append("#")
        
        # Join all values by spaces to form the final serialized string
        return ' '.join(result)

    def deserialize(self, data):
        """
        Decodes the serialized string back to the binary tree.
        
        :param data: str, serialized tree string
        :return: TreeNode, root of the reconstructed binary tree
        """
        if data == "#":
            # If the data is just '#', it means the tree is empty
            return None
        
        nodes = data.split()  # Split the string by spaces to get node values
        root = TreeNode(int(nodes[0]))  # The first value is the root node's value
        queue = deque([root])  # Queue to rebuild tree level-by-level
        index = 1  # Pointer to traverse the 'nodes' list
        
        while queue and index < len(nodes):
            current = queue.popleft()
            
            # Process left child
            if nodes[index] != "#":
                # If not '#', create a new node and assign as left child
                left_node = TreeNode(int(nodes[index]))
                current.left = left_node
                queue.append(left_node)  # Add left child to queue to process its children later
            index += 1
            
            # Process right child (make sure we don't go out of range)
            if index < len(nodes) and nodes[index] != "#":
                # If not '#', create a new node and assign as right child
                right_node = TreeNode(int(nodes[index]))
                current.right = right_node
                queue.append(right_node)  # Add right child to queue
            index += 1
        
        # Return the root of the reconstructed tree
        return root
