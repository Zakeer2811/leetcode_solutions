class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Out-of-bounds or water
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0  # mark visited
            area = 1
            
            # Explore 4 directions
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)
            
            return area
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
