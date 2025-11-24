
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Build events: (location, change_in_passengers)
        events = []
        for num, start, end in trips:
            events.append((start, num))   # pickup -> increase passengers
            events.append((end, -num))    # dropoff -> decrease passengers

        # Sort events by location.
        # Important: when pickups and dropoffs occur at same location,
        # process dropoffs before pickups to free seats first.
        events.sort(key=lambda x: (x[0], x[1]))

        current = 0
        for loc, change in events:
            current += change
            if current > capacity:
                return False
        return True
