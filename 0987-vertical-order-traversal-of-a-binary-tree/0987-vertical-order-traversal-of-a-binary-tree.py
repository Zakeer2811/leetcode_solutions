# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict, deque

        # node_map will hold column index x -> list of (y, val) pairs
        node_map = defaultdict(list)
        # BFS queue stores tuples: (node, x, y)
        queue = deque([(root, 0, 0)])

        while queue:
            node, x, y = queue.popleft()
            if node:
                # Append current node's (y, val) into the corresponding column
                node_map[x].append((y, node.val))
                # Traverse left and right children
                queue.append((node.left, x - 1, y + 1))
                queue.append((node.right, x + 1, y + 1))

        result = []
        # Sort the x keys (left to right columns)
        for x in sorted(node_map.keys()):
            # Sort by y first (top to bottom), then by val (ascending)
            level = sorted(node_map[x], key=lambda pair: (pair[0], pair[1]))
            # Extract only values from sorted pairs
            result.append([val for y, val in level])

        return result

"""
\U0001f9ea Dry Run on this Tree:
        3
       / \
      9  20
         / \
        15  7

Step 1: BFS Traversal
Queue Processing Order:
1. (3, 0, 0)     → node_map[0].append((0, 3))
2. (9, -1, 1)    → node_map[-1].append((1, 9))
3. (20, 1, 1)    → node_map[1].append((1, 20))
4. (15, 0, 2)    → node_map[0].append((2, 15))
5. (7, 2, 2)     → node_map[2].append((2, 7))

node_map becomes:
{
    -1: [(1, 9)],
     0: [(0, 3), (2, 15)],
     1: [(1, 20)],
     2: [(2, 7)]
}

Step 2: Build Result
1. x = -1 → sorted = [(1, 9)]        → values = [9]
2. x = 0  → sorted = [(0, 3), (2, 15)] → values = [3, 15]
3. x = 1  → sorted = [(1, 20)]       → values = [20]
4. x = 2  → sorted = [(2, 7)]        → values = [7]

✅ Final Output: [[9], [3, 15], [20], [7]]
"""
