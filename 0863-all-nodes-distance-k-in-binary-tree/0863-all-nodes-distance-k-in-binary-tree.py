from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []                     # Final list of nodes at distance K
        parent_map = {}                 # Map to store parent references
        bfs_queue = deque([root])      # Queue to build parent references using BFS

        # Step 1: Build the parent reference map for all nodes
        while bfs_queue:
            current_node = bfs_queue.popleft()

            if current_node.left:
                parent_map[current_node.left.val] = current_node
                bfs_queue.append(current_node.left)

            if current_node.right:
                parent_map[current_node.right.val] = current_node
                bfs_queue.append(current_node.right)

        # Step 2: BFS starting from target node to find nodes at distance K
        visited = set()                # To keep track of visited nodes
        bfs_queue = deque([target])   # Start from the target node

        while k > 0 and bfs_queue:
            level_size = len(bfs_queue)

            for _ in range(level_size):
                current_node = bfs_queue.popleft()
                visited.add(current_node.val)

                # Visit left child
                if current_node.left and current_node.left.val not in visited:
                    bfs_queue.append(current_node.left)

                # Visit right child
                if current_node.right and current_node.right.val not in visited:
                    bfs_queue.append(current_node.right)

                # Visit parent
                if current_node.val in parent_map and parent_map[current_node.val].val not in visited:
                    bfs_queue.append(parent_map[current_node.val])

            k -= 1  # Move one level away

        # Step 3: Collect all nodes in queue (these are exactly k distance from target)
        while bfs_queue:
            result.append(bfs_queue.popleft().val)

        return result


# ------------------- DRY RUN EXAMPLE -------------------
"""
Given Binary Tree:

        3
       / \
      5   1
     / \  / \
    6  2 0  8
      / \
     7   4

Input:
    root = TreeNode(3)
    target = TreeNode with value 5
    k = 2

Execution Flow:

Step 1: Build parent map
    parent_map = {
        6: 5,
        2: 5,
        0: 1,
        8: 1,
        5: 3,
        1: 3,
        7: 2,
        4: 2
    }

Step 2: BFS from target node (5) with distance k = 2

Level 0 (k=2): [5]           → Visit node 5
    Add children 6, 2
    Add parent 3

Level 1 (k=1): [6, 2, 3]     → Visit nodes 6, 2, 3
    - Node 6: no new nodes
    - Node 2: add 7, 4
    - Node 3: add 1

Level 2 (k=0): [7, 4, 1]     → These are the answer nodes

Output:
    [7, 4, 1]
"""
