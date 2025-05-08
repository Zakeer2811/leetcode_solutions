import heapq
from typing import List

class Solution:
    @staticmethod
    def is_outside(i: int, j: int, n: int, m: int) -> bool:
        return i < 0 or i >= n or j < 0 or j >= m

    @staticmethod
    def minTimeToReach(moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        time = [[float('inf')] * m for _ in range(n)]
        pq = []

        # Start at (0, 0) with time=0 and adjust=True
        heapq.heappush(pq, (0, 0, 0, True))
        time[0][0] = 0

        d = [0, 1, 0, -1, 0]

        while pq:
            t, i, j, adjust = heapq.heappop(pq)

            if i == n - 1 and j == m - 1:
                return t

            for a in range(4):
                r, s = i + d[a], j + d[a + 1]
                if Solution.is_outside(r, s, n, m):
                    continue

                # Compute the next time
                next_time = max(t, moveTime[r][s]) + 1 + (not adjust)

                if next_time < time[r][s]:
                    time[r][s] = next_time
                    heapq.heappush(pq, (next_time, r, s, not adjust))

        return -1  # Cannot reach destination
