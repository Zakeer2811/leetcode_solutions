class Solution:
    def minOperations(self, grid, x):
        arr = []
        m = len(grid)
        n = len(grid[0])
        
        # Flatten the grid into a single list
        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])
        
        # Sort the array
        arr.sort()
        
        # Find the median element
        median = arr[len(arr) // 2]
        
        # Initialize the count of operations
        count = 0
        
        # Calculate the number of operations
        for val in arr:
            diff = abs(val - median)
            if diff % x != 0:
                return -1
            count += diff // x
        
        return count
