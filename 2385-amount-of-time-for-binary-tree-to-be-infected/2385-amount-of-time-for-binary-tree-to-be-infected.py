from collections import deque, defaultdict
from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        # Step 1: Convert the binary tree into an undirected graph
        # We'll use an adjacency list to represent the graph
        graph = defaultdict(list)

        def build_graph(node, parent):
            if not node:
                return  # Base case: nothing to do for null nodes

            if parent:
                # Create bi-directional edges: node <-> parent
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)

            # Recurse for left and right children, passing current node as parent
            build_graph(node.left, node)
            build_graph(node.right, node)

        # Start building the graph from the root node
        build_graph(root, None)

        # Step 2: Do BFS from the `start` node to simulate infection spreading
        visited = set()           # To keep track of which nodes are already infected
        queue = deque([start])    # BFS queue starting from the infection source
        minutes = -1              # Start time is -1 since minute 0 will be the first loop

        while queue:
            level_size = len(queue)  # Number of infected nodes at the current minute

            for _ in range(level_size):
                node_val = queue.popleft()  # Process the current infected node
                visited.add(node_val)       # Mark it as visited (infected)

                # Infect all its unvisited neighbors (adjacent nodes in the graph)
                for neighbor in graph[node_val]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

            # After processing all nodes at this level (minute), increment the time
            minutes += 1

        return minutes  # Total minutes it took to infect all nodes


# ----------------------------- DRY RUN EXAMPLE -----------------------------
"""
Input:
    Tree: [1,5,3,null,4,10,6,9,2]
    start = 3

Tree structure (visualized):

        1
       / \
      5   3
       \  / \
        4 10 6
       / \
      9   2

Step 1: Build the graph from the tree

Adjacency list after build_graph():
    1: [5, 3]
    3: [1, 10, 6]
    5: [1, 4]
    4: [5, 9, 2]
    10: [3]
    6: [3]
    9: [4]
    2: [4]

Step 2: BFS from start node = 3

Minute 0: [3]
    → Infect neighbors: 1, 10, 6

Minute 1: [1, 10, 6]
    → Infect neighbor of 1 → 5
    → 10 and 6 have no unvisited neighbors

Minute 2: [5]
    → Infect neighbor: 4

Minute 3: [4]
    → Infect neighbors: 9, 2

Minute 4: [9, 2]
    → No unvisited neighbors left

Answer = 4 (It takes 4 minutes to infect the whole tree)

"""
