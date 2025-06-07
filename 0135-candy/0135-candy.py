from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        # Step 1: Assign each child at least 1 candy initially
        # Reason: Problem states that every child must have at least one candy
        candies = [1] * n

        # ---------------------------- FIRST PASS (Left to Right) ---------------------------- #
        # We process from left to right to ensure that if a child has a higher rating than
        # their previous (left) neighbor, then they get more candies than them.
        # At this stage, we are only considering the left neighbor constraint.
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                # Child at index i has higher rating than left neighbor → get more candies
                candies[i] = candies[i - 1] + 1

        # ---------------------------- SECOND PASS (Right to Left) ---------------------------- #
        # Now we go from right to left to make sure:
        # If a child has a higher rating than their next (right) neighbor,
        # then they must have more candies than them as well.
        #
        # Important: We must not reduce any already-assigned candies from the first pass.
        # So we only update if needed, and preserve higher previous values.
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                if candies[i] > candies[i + 1]:
                    # No need to update; left child already has more candies
                    continue
                else:
                    # Right neighbor has more or equal candies; not valid
                    # So we increase current child's candies to 1 more than the right
                    candies[i] = candies[i + 1] + 1

        # Final step: Return total number of candies distributed
        return sum(candies)
