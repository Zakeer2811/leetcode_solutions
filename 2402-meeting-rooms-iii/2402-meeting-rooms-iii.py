from heapq import heappush, heappop
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        Function to determine the meeting room that was used the most.
        
        Args:
        n (int): The number of meeting rooms available.
        meetings (List[List[int]]): List of meetings, where each meeting is a list of two integers [start, end].
        
        Returns:
        int: Index of the room that was used the most.
        """

        # Priority queue to keep track of the next available time for each room.
        free_rooms = []
        
        # Initialize the free_rooms heap with all meeting rooms, their initial availability is 0 (all rooms are available from the start).
        for i in range(n):
            heappush(free_rooms, (0, i))  # (time the room becomes free, room index)

        # A list to track the number of meetings booked in each room.
        booked_rooms = [0] * n

        # Sort meetings by their start time for sequential processing.
        meetings.sort()

        # Go through each meeting and allocate it to an available room.
        for start, end in meetings:
            # Get the first room that's available (minimum free time).
            free_time, room = heappop(free_rooms)

            # If the room is available before the meeting starts, it can be used.
            if free_time <= start:
                # If the room was free before the meeting started, it will be booked from `end` time.
                booked_rooms[room] += 1
                heappush(free_rooms, (end, room))  # Push the updated free time of the room back into the heap.
            else:
                # Otherwise, this room is still occupied until `free_time`.
                booked_rooms[room] += 1
                heappush(free_rooms, (free_time + (end - start), room))  # Book the room for this meeting.

        # Find the room that was booked the most.
        max_booked = max(booked_rooms)
        
        # Return the index of the room that was used the most.
        return booked_rooms.index(max_booked)
        
