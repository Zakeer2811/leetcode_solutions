from collections import deque
class Solution:
    def orangesRotting(self,grid):
        rows, cols = len(grid), len(grid[0])  # Dimensions of the grid
        queue = deque()  # Queue to perform BFS (holds rotten oranges with their timestamp)
        fresh = 0  # Counter for fresh oranges

        # Step 1: Initialize the queue with positions of all rotten oranges
        # and count the total number of fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time=0) for initially rotten orange
                elif grid[r][c] == 1:
                    fresh += 1  # Count fresh oranges

        # Directions for 4-directional movement: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        time_elapsed = 0  # To track total time taken for rotting all fresh oranges

        # Step 2: Perform BFS to spread rot from rotten oranges
        while queue:
            r, c, time = queue.popleft()  # Get current rotten orange and the minute it rotted
            time_elapsed = max(time_elapsed, time)  # Update the latest time

            # Try to rot adjacent fresh oranges
            for dr, dc in directions:
                nr, nc = r + dr, c + dc  # New row and column
                # Check if the new position is within bounds and has a fresh orange
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Rot the fresh orange
                    fresh -= 1  # One less fresh orange
                    queue.append((nr, nc, time + 1))  # Add new rotten orange to queue with incremented time

        # Step 3: If there are any fresh oranges left, return -1 (not all oranges can be rotten)
        # Otherwise, return the total time elapsed
        return time_elapsed if fresh == 0 else -1
# -------------------------------------------------------------
# Dry Run Example: grid = [[2,1,1],[1,1,0],[0,1,1]]
#
# Initial grid:
#  2 1 1
#  1 1 0
#  0 1 1
#
# Step 1:
# Initial rotten = [(0, 0, 0)]
# Fresh count = 7
#
# Step 2 (BFS Rotting Process):
#
# Minute 0:
# - Rotten at (0, 0) rots (0, 1) and (1, 0)
#   → New rotten = [(0, 1, 1), (1, 0, 1)], fresh = 5
#
# Minute 1:
# - (0, 1) rots (0, 2) and (1, 1)
#   → New rotten = [(1, 0, 1), (0, 2, 2), (1, 1, 2)], fresh = 3
# - (1, 0) rots nothing new (0,0 already rotten, 2,0 is 0)
#
# Minute 2:
# - (0, 2) rots nothing
# - (1, 1) rots (2, 1)
#   → New rotten = [(2, 1, 3)], fresh = 2
#
# Minute 3:
# - (2, 1) rots (2, 2)
#   → New rotten = [(2, 2, 4)], fresh = 1
#
# Minute 4:
# - (2, 2) has no adjacent fresh oranges
#
# All fresh oranges are now rotten → Return 4
#
# Final grid after 4 minutes:
#  2 2 2
#  2 2 0
#  0 2 2
# -------------------------------------------------------------