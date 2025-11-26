class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            # Out of bounds or water → stop
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            
            # Mark current cell as visited (sink the island)
            grid[r][c] = "0"
            
            # DFS in four directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # Loop through all cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1        # Found a new island
                    dfs(r, c)        # Sink the entire island
        
        return count
