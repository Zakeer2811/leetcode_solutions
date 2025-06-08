from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Edge case: no intervals given
        if not intervals:
            return 0

        # Step 1: Sort intervals based on their end time
        intervals.sort(key=lambda x: x[1])

        # Step 2: Initialize count of non-overlapping intervals
        non_overlapping_count = 1  # First interval is always picked
        prev_end = intervals[0][1]  # End time of the last added interval

        # Step 3: Iterate through the remaining intervals
        for start, end in intervals[1:]:
            if start >= prev_end:
                # No overlap: include this interval
                non_overlapping_count += 1
                prev_end = end
            # Else: overlap → skip this interval (implicitly removed)

        # Step 4: Total intervals - non-overlapping = intervals to remove
        return len(intervals) - non_overlapping_count
