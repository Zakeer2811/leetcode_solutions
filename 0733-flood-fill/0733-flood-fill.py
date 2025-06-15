from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Step 1: Get the original color of the starting pixel.
        original_color = image[sr][sc]

        # Mistake originally: Not needed to proceed if the target color is same as original.
        # Reason: This avoids infinite recursion or unnecessary work.
        if original_color == color:
            return image

        # Define DFS function to recursively fill adjacent pixels.
        def dfs(r, c, visited, m, n, original_color, color):
            # Mistake: Incorrect boundary condition used in your original code.
            # r > m or c > n should be r >= m or c >= n
            # Reason: Indexing in Python is 0-based. r == m is out of bounds (since last valid index is m - 1)
            if r < 0 or c < 0 or r >= m or c >= n:
                return

            # Skip visited or different-color pixels
            if (r, c) in visited or image[r][c] != original_color:
                return

            # Mark current pixel as visited
            visited.add((r, c))

            # Change the color of the current pixel
            image[r][c] = color

            # Mistake: You did r, c = r + dr, c + dc in your earlier version.
            # Reason: This modifies r and c for all future iterations, which leads to incorrect recursion paths.
            # Fix: Use new variables r + dr, c + dc when calling dfs.
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, m, n, original_color, color)

        # Initialize visited set to avoid reprocessing the same pixel
        visited = set()

        # Get dimensions of the image
        m, n = len(image), len(image[0])

        # Start the DFS traversal from the initial pixel
        dfs(sr, sc, visited, m, n, original_color, color)

        # Return the modified image
        return image
# --------------------------------------------------------------------
# Dry Run Example: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
#
# Initial image:
# [1, 1, 1]
# [1, 1, 0]
# [1, 0, 1]
#
# Start at (1, 1). Original color = 1, target color = 2
#
# Step 1: Change (1,1) to 2 → visited = {(1,1)}
# Step 2: DFS to (0,1) → 1 → change to 2 → visited = {(1,1), (0,1)}
# Step 3: DFS to (0,0) → 1 → change to 2 → visited = {(1,1), (0,1), (0,0)}
# Step 4: DFS to (0,2) → 1 → change to 2 → visited = {(1,1), (0,1), (0,0), (0,2)}
# Step 5: DFS to (1,2) → 0 → stop
# Step 6: DFS to (1,0) → 1 → change to 2 → visited = {(1,1), (0,1), (0,0), (0,2), (1,0)}
# Step 7: DFS to (2,0) → 1 → change to 2 → visited = {(1,1), (0,1), (0,0), (0,2), (1,0), (2,0)}
# Step 8: DFS to (2,1) → 0 → stop
# Step 9: DFS to (2,2) → 1 → color match, but not connected to component → stop
#
# Final image:
# [2, 2, 2]
# [2, 2, 0]
# [2, 0, 1]
# --------------------------------------------------------------------
'''
dfs(1,1)
├── dfs(0,1)
│   ├── dfs(-1,1) → out of bounds
│   ├── dfs(1,1) → already visited
│   ├── dfs(0,0)
│   │   ├── dfs(-1,0) → out of bounds
│   │   ├── dfs(1,0)
│   │   │   ├── dfs(2,0)
│   │   │   │   ├── dfs(3,0) → out of bounds
│   │   │   │   ├── dfs(2,1) → 0 → stop
│   │   │   │   ├── dfs(2,-1) → out of bounds
│   │   │   │   ├── dfs(2,1) → already checked
│   │   │   ├── dfs(0,0) → already visited
│   │   │   ├── dfs(1,-1) → out of bounds
│   │   │   ├── dfs(1,1) → already visited
│   │   ├── dfs(0,-1) → out of bounds
│   │   ├── dfs(0,1) → already visited
│   ├── dfs(0,2)
│   │   ├── dfs(-1,2) → out of bounds
│   │   ├── dfs(1,2) → 0 → stop
│   │   ├── dfs(0,1) → already visited
│   │   ├── dfs(0,3) → out of bounds
├── dfs(2,1) → 0 → stop
├── dfs(1,0) → already visited
├── dfs(1,2) → 0 → stop

'''