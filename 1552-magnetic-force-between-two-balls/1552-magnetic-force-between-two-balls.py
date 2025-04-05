from typing import List

class Solution:
    def maxDistance(self, positions: List[int], m: int) -> int:
        # Step 1: Sort the positions of the balls on the line
        positions.sort()

        # Step 2: Helper function to check if it's possible to place `m` balls
        # with at least `min_distance` distance between them
        def canPlaceBalls(positions, min_distance):
            # Initialize the first ball at the first position
            ball_count = 1
            last_ball_position = positions[0]

            # Try placing the remaining balls
            for i in range(1, len(positions)):
                # If the current position is far enough from the last placed ball
                if positions[i] - last_ball_position >= min_distance:
                    # Place a new ball here
                    ball_count += 1
                    # Update the position of the last placed ball
                    last_ball_position = positions[i]

            # If we were able to place at least `m` balls, return True
            return ball_count >= m

        # Step 3: Binary search to find the maximum minimum distance
        low = 1  # Minimum possible distance between balls
        high = positions[-1] - positions[0]  # Maximum possible distance (max position - min position)

        # Step 4: Perform binary search on the possible minimum distance
        while low <= high:
            mid = low + (high - low) // 2  # Find the middle point

            # Step 5: Check if it's possible to place balls with at least `mid` distance between them
            if canPlaceBalls(positions, mid):
                # If we can place the balls, it means we can try a larger distance
                low = mid + 1
            else:
                # If we cannot place the balls, try a smaller distance
                high = mid - 1

        # Step 6: Return the maximum possible minimum distance found
        return high
