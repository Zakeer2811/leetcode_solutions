
'''
You iterate over every city (node).

If a city hasn't been visited, it's the start of a new province.

You perform a DFS from this city, visiting all cities connected directly or indirectly.

Each DFS call marks one full province.

Count how many times you have to start a new DFS — that’s your answer.
'''
class Solution:
    def findCircleNum(self, isConnected):
        # Helper function: performs DFS to visit all nodes in the current connected component
        def dfs(node):
            # Traverse all possible neighbors of the current node
            for neighbor in range(len(isConnected)):
                # If there is a connection and the neighbor hasn't been visited yet
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)  # Mark neighbor as visited
                    dfs(neighbor)          # Recursively visit its neighbors

        visited = set()  # To track visited nodes (cities) But in connected components / provinces counting, we should not pre-mark any node. Why?Because we don't know in advance which nodes belong to which component.Instead, we need to explore all nodes:
        provinces = 0     # Count of connected components / provinces

        # Iterate through all nodes (cities)
        for i in range(len(isConnected)):
            # If the current city hasn't been visited yet, it's a new province
            if i not in visited:
                provinces += 1        # Start of a new connected component
                visited.add(i)        # Mark current city as visited
                dfs(i)                # Visit all cities in this province using DFS

        return provinces  # Return total number of provinces



        