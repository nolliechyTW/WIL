import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Initialize a heap to store end times of meetings
        end_times_heap = []

        # Sort the intervals based on start times
        intervals.sort(key=lambda x: x[0])

        # Add the end time of the first meeting
        heapq.heappush(end_times_heap, intervals[0][1])

        # Iterate over the remaining intervals
        for interval in intervals[1:]:
            # If the room is free, remove it from the heap
            if end_times_heap[0] <= interval[0]:
                heapq.heappop(end_times_heap)

            # Add the end time of the current meeting
            heapq.heappush(end_times_heap, interval[1])

        # The size of the heap is the number of rooms required
        return len(end_times_heap)
