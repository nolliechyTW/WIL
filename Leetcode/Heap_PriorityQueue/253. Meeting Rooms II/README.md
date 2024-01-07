## 253. Meeting Rooms II
🔗  Link: [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Heap<br>

=======================================================================================<br>
Given an array of meeting time intervals intervals where `intervals[i] = [starti, endi]`, return the *minimum number* of conference rooms required.
 

Example 1:<br>
Input: intervals = [[0,30],[5,10],[15,20]]<br>
Output: 2<br>

Example 2:<br>
Input: intervals = [[7,10],[2,4]]<br>
Output: 1<br>


Constraints:<br>
- 1 <= intervals.length <= 10^4
- 0 <= starti < endi <= 10^6

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can we confirm that a conference room is needed for each set of overlapping meetings? For example, if one meeting ends at the same time another begins, do they require separate rooms?
    - Yes
<!-- 2. Any requirement on time/space complexity? 
    - You must write a solution in O(n) time complexity and O(n) space complexity -->
3. Should we assume the intervals are not sorted by their start or end times?
    - Yes
4. Are the intervals guaranteed to be valid, with the start time always less than or equal to the end time?
    - Yes


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Heap <br>
- Priority Queue for Dynamic Minimum:
A heap, particularly a min-heap, is an excellent tool for keeping track of the meeting with the earliest end time. This is crucial in deciding whether a new meeting can be accommodated in the same room or if a new room is needed.<br>
- Efficient Overlap Detection:
The problem requires you to check for overlaps between meetings. By keeping meetings in a min-heap sorted by their end times, you can efficiently compare the start time of a new meeting with the earliest ending meeting, which is always at the top of the heap.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

- General Idea: by using a min heap to efficiently manage and update the end times of meetings, we can dynamically allocate and deallocate rooms as needed, ensuring the minimum number of rooms are used at any given time

1) Check for Empty Intervals List:
    - If `intervals` is empty, it returns `0`, as no meeting rooms are needed

2) Sort the Intervals:
    - The intervals are sorted based on their start times. This helps in processing the meetings in the order they begin.

3) Use a Min Heap for End Times:
    -  A min heap (`end_times_heap`) is used to track the end times of meetings currently occupying the rooms

4) Process Each Meeting:
    - Initially, the end time of the first meeting is added to the heap
    - For each subsequent meeting, it checks if the meeting can use an existing room (if its start time is equal to or later than the earliest ending meeting in the heap).
        - If an existing room can be reused (the top of the heap), its end time is removed from the heap (as the room becomes free), and the new meeting's end time is added.
        - If no room is free, the new meeting's end time is simply added to the heap, representing the allocation of a new room.

5) Determine the Number of Rooms:  
    - The size of the heap at the end of the process gives the minimum number of rooms required. This is because the heap only contains meetings that are simultaneously occurring, and its size represents the peak number of concurrent meetings.


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of intervals

- Time Complexity: O(N log N)
- Space Complexity: O(N), in the worst case, when all intervals overlap, the heap can contain all N intervals simultaneously

<!-- 
Time Complexity:
- Sorting the Intervals:
    - The intervals.sort() method sorts the intervals based on their start times. The time complexity of sorting is O(N log N), where N is the number of intervals.
- Heap Operations:
    - The code iterates through each interval and performs heap operations (either heappush or heappop or both).
    - The heapq.heappush() and heapq.heappop() operations have a time complexity of O(log K) each, where K is the number of elements in the heap.
    - In the worst case, the heap can contain all N intervals (if all meetings overlap), so the time complexity for heap operations across all intervals is O(N log N).
 
Combining these, the overall time complexity is dominated by the sorting and the heap operations, resulting in O(N log N).
 -->