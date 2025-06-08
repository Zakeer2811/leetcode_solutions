from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        merged = []
        i = 0
        n = len(intervals)
        new_start, new_end = new_interval

        # 1️⃣ Add intervals that come entirely before new_interval
        # Example: intervals = [[1, 7], [8, 21]], new_interval = [25, 30]
        # The first two intervals end before 25, so just add them as is.
        while i < n:
            curr_start, curr_end = intervals[i]
            if curr_end < new_start:
                merged.append([curr_start, curr_end])
                i += 1
            else:
                break

        # 2️⃣ Merge overlapping intervals with new_interval
        # Example: intervals = [[3, 7], [5, 12]], new_interval = [6, 10]
        # These intervals overlap with new_interval, so we update new_start and new_end.
        while i < n:
            curr_start, curr_end = intervals[i]
            if curr_start <= new_end:
                new_start = min(new_start, curr_start)
                new_end = max(new_end, curr_end)
                i += 1
            else:
                break
        # Add the merged interval
        merged.append([new_start, new_end])

        # 3️⃣ Add the rest of the intervals that come after new_interval
        # Example: intervals = [[3, 7], [5, 12], [15, 20]], new_interval = [6, 10]
        # After merging [3, 7], [5, 12], and [6, 10], add remaining [15, 20]
        while i < n:
            curr_start, curr_end = intervals[i]
            merged.append([curr_start, curr_end])
            i += 1

        return merged
