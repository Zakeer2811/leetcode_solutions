from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []

        # Initialize a queue (double-ended) with the root node
        q = deque([root])

        # Final result list to store the zigzag level order traversal
        ans = []

        # Flag to control the direction of traversal; False = left to right, True = right to left
        zigzag = False

        # Process the tree level by level
        while q:
            # Number of nodes at the current level
            level_size = len(q)

            # List to hold values of nodes at the current level
            level_nodes = []

            # Process all nodes at the current level
            for _ in range(level_size):
                if not zigzag:
                    # Pop node from the left for left-to-right traversal
                    node = q.popleft()

                    # Append its value to the current level list
                    level_nodes.append(node.val)

                    # Add child nodes to the queue from left to right
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    # Pop node from the right for right-to-left traversal
                    node = q.pop()

                    # Append its value to the current level list
                    level_nodes.append(node.val)

                    # Add child nodes to the queue from right to left (reverse order)
                    # So that they are processed correctly on the next level
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)

            # Append the completed level to the result list
            ans.append(level_nodes)

            # Toggle the traversal direction for the next level
            zigzag = not zigzag

        # Return the final zigzag level order traversal
        return ans
