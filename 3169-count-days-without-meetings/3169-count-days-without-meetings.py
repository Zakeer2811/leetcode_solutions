class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days

        # Sort the meetings by start time
        meetings.sort(key=lambda x: x[0])
        
        merged = []
        # Merge intervals
        for meeting in meetings:
            if not merged or meeting[0] > merged[-1][1]:
                merged.append(meeting.copy())
            else:
                merged[-1][1] = max(merged[-1][1], meeting[1])
        
        # Calculate total meeting days
        total_meeting_days = sum(end - start + 1 for start, end in merged)
        
        # Ensure available days is not negative
        return max(0, days - total_meeting_days)
            