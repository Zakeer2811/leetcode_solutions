class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 1
        minEnd = float('inf')  # Representing INT_MAX as infinity
        
        # Sorting the intervals in ascending order of the starting point
        points.sort()
        
        for p in points:
            if p[0] > minEnd:  # If the current interval starts after the previous interval's end
                count += 1
                minEnd = p[1]  # Start a new active set with the current interval's end
            else:
                minEnd = min(minEnd, p[1])  # Renew the key parameters of the active set
        
        return count
        