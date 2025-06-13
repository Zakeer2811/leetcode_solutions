from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Pair:
    def __init__(self, node, index):
        self.node = node          # TreeNode object
        self.index = index        # Position in the level (like a full binary tree)

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_width = 0  # Holds the maximum width found across all levels
        queue = deque([Pair(root, 0)])  # Queue stores Pair(node, index)

        while queue:
            level_size = len(queue)
            level_min_index = queue[0].index  # Used to normalize indices for this level
            level_first_index = 0             # Normalized index of the first node
            level_last_index = 0              # Normalized index of the last node

            for i in range(level_size):
                current_pair = queue.popleft()
                # Normalize index to avoid large numbers or overflow
                normalized_index = current_pair.index - level_min_index
                current_node = current_pair.node

                # Capture the first and last index at this level
                if i == 0:
                    level_first_index = normalized_index
                if i == level_size - 1:
                    level_last_index = normalized_index

                # Enqueue left child with calculated position
                if current_node.left:
                    queue.append(Pair(current_node.left, 2 * normalized_index + 1))
                # Enqueue right child with calculated position
                if current_node.right:
                    queue.append(Pair(current_node.right, 2 * normalized_index + 2))

            # Calculate width of current level
            level_width = level_last_index - level_first_index + 1
            max_width = max(max_width, level_width)

        return max_width


"""
\U0001f9ea Dry Run Example:

Tree:
        1
       / \
      3   2
     /     \
    5       9
   /         \
  6           7

Structure as full binary tree:
Level 0:         [1]                           → indices: [0]
Level 1:       [3,   2]                        → indices: [0, 1]
Level 2:     [5,  x, x,   9]                   → indices: [0, 3]
Level 3:   [6, x, x, x, x, x, x,   7]          → indices: [0, 7]

Step-by-step:

Level 0:
- queue: [(1, 0)]
- level_min_index = 0
- first_index = 0, last_index = 0
- width = 0 - 0 + 1 = 1
- max_width = 1

Level 1:
- queue: [(3, 1), (2, 2)]
- level_min_index = 1
- normalized indices: 0, 1
- first_index = 0, last_index = 1
- width = 1 - 0 + 1 = 2
- max_width = 2

Level 2:
- queue: [(5, 1), (9, 6)]  ← positions in full binary tree
- level_min_index = 1
- normalized indices: 0, 5
- first_index = 0, last_index = 5
- width = 5 - 0 + 1 = 6
- max_width = 6

Level 3:
- queue: [(6, 1), (7, 14)]
- level_min_index = 1
- normalized indices: 0, 13
- first_index = 0, last_index = 13
- width = 13 - 0 + 1 = 14
- max_width = 14

✅ Final Answer: 14
"""
